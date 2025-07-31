# judge_answers.py
import os
import asyncio
import json
import logging
import yaml 
from tqdm import tqdm
from datasets import Dataset
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from config import CONFIG 

# --- Professional-Grade Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration from CONFIG object ---
GENERATED_ANSWERS_PATH = CONFIG.GENERATED_ANSWERS_CHECKPOINT
JUDGED_RESULTS_CHECKPOINT = CONFIG.JUDGED_RESULTS_CHECKPOINT
FINAL_RESULTS_PATH = CONFIG.FINAL_RESULTS_PATH
JUDGE_LLM_MODEL = CONFIG.JUDGE_LLM_MODEL
API_SLEEP_INTERVAL = CONFIG.API_SLEEP_INTERVAL
MAX_CONTEXT_CHARS = CONFIG.MAX_CONTEXT_CHARS
MAX_ANSWER_CHARS = CONFIG.MAX_ANSWER_CHARS
MAX_GT_CHARS = CONFIG.MAX_GT_CHARS

# --- The brilliant Unified Evaluation Prompt from your friend's script ---
EVALUATION_PROMPT_TEMPLATE = """
SYSTEM: You are a meticulous and fair evaluator for a RAG (Retrieval-Augmented Generation) system.
Your task is to evaluate a response against three criteria on a scale of 0 to 10.
Your final output MUST be a single, valid JSON object. Do not include any text, formatting, or explanations before or after the JSON object.
The JSON object must have these three keys: "faithfulness", "context_recall", "answer_correctness".
For each key, the value should be another JSON object with two keys: "score" (an integer from 0 to 10) and "reasoning" (a concise, one-sentence explanation for your score).

[EVALUATION CRITERIA]
1.  **Faithfulness (Score 0-10)**: How well does the "Submission" align with the provided "Context"?
    - Score 10 if all claims in the Submission are directly and explicitly supported by the Context.
    - Score 0 if the Submission makes claims that directly contradict the Context.
    - Give partial scores for answers that make claims not mentioned in the context (minor hallucinations).
2.  **Context Recall (Score 0-10)**: Does the "Context" contain all the necessary information from the "Reference Context" to answer the "Question"?
    - Score 10 if all key pieces of information from the Reference Context are present in the retrieved Context.
    - Score 0 if the retrieved Context is completely irrelevant.
3.  **Answer Correctness (Score 0-10)**: How factually and substantively similar is the "Submission" to the "Reference Answer"?
    - Score 10 if the Submission is a perfect or near-perfect match to the Reference Answer.
    - Score 0 if the Submission is completely wrong.

[DATA]
- Question: {question}
- Context: {context}
- Submission: {prediction}
- Reference Context: {reference_context}
- Reference Answer: {reference_answer}

[YOUR JSON RESPONSE]
"""

async def main():
    """
    PHASE 2: Judges answers using a unified, single-call evaluation prompt.
    """
    print("--- Phase 2: Answer Judging (Unified Prompt) ---")

    # --- Initialize Judge LLM ---
    try:
        api_key = CONFIG.GROQ_API_KEY
        judge_llm = ChatGroq(model_name=JUDGE_LLM_MODEL, groq_api_key=api_key, temperature=0)
    except Exception as e:
        print(f"FATAL: Could not initialize Groq. Is your GROQ_API_KEY correct? Error: {e}")
        return
        
    # --- Create the Unified Evaluation Chain ---
    evaluation_prompt = ChatPromptTemplate.from_template(EVALUATION_PROMPT_TEMPLATE)
    evaluation_chain = evaluation_prompt | judge_llm | JsonOutputParser()
    
    # --- FIX: Define the list of metric names at the top level of the function ---
    all_metric_names = ["faithfulness", "context_recall", "answer_correctness"]

    # --- Main Loop with Resumable Checkpointing ---
    while True:
        try:
            with open(GENERATED_ANSWERS_PATH, 'r', encoding='utf-8') as f:
                answers_to_judge = [json.loads(line) for line in f]
        except FileNotFoundError:
            print(f"ERROR: File not found at '{GENERATED_ANSWERS_PATH}'.")
            return

        judged_results = []
        if os.path.exists(JUDGED_RESULTS_CHECKPOINT):
            with open(JUDGED_RESULTS_CHECKPOINT, 'r', encoding='utf-8') as f:
                judged_results = [json.loads(line) for line in f]
        
        processed_questions = {res['question'] for res in judged_results}
        rows_to_process = [row for row in answers_to_judge if row['question'] not in processed_questions]
        
        if not rows_to_process:
            print("\nAll answers have been judged. Finishing.")
            break

        print(f"\nFound {len(rows_to_process)} remaining answers to judge...")
        
        rate_limit_hit = False
        with open(JUDGED_RESULTS_CHECKPOINT, 'a', encoding='utf-8') as f_out:
            for row in tqdm(rows_to_process, desc="Judging Answers"):
                try:
                    contexts_str = "\n---\n".join(row["contexts"])
                    
                    prepared_payload = {
                        "question": row["question"],
                        "context": contexts_str[:MAX_CONTEXT_CHARS],
                        "prediction": row["answer"][:MAX_ANSWER_CHARS],
                        "reference_context": "\n---\n".join(row["ground_truth_context"])[:MAX_GT_CHARS],
                        "reference_answer": row.get("ground_truth_answer", "")[:MAX_ANSWER_CHARS]
                    }

                    evaluation_prompt = ChatPromptTemplate.from_template(EVALUATION_PROMPT_TEMPLATE)
                    evaluation_chain = evaluation_prompt | judge_llm | JsonOutputParser()
                    
                    response = await evaluation_chain.ainvoke(prepared_payload)

                    scores_dict = {}
                    reasoning_dict = {}
                    for name in all_metric_names:
                        # Safely get the score, default to 0 if missing or invalid
                        score_value = response.get(name, {}).get('score', 0)
                        try:
                            scores_dict[name] = int(score_value)
                        except (ValueError, TypeError):
                            scores_dict[name] = 0 # Default to 0 on parsing error
                        
                        # Get the reasoning
                        reasoning_dict[f"{name}_reasoning"] = response.get(name, {}).get("reasoning", "")
                    
                    final_result = {**row, **scores_dict, **reasoning_dict}
                    f_out.write(json.dumps(final_result) + '\n')
                    
                except Exception as e:
                    err_str = str(e).lower()
                    if "rate limit" in err_str or "429" in err_str:
                        tqdm.write(f"\n--- RATE LIMIT HIT. Pausing for 60 seconds. ---")
                        await asyncio.sleep(60)
                        rate_limit_hit = True
                        break
                    else:
                        tqdm.write(f"\n--- ERROR (skipping): '{row['question'][:50]}...' ---")
                        tqdm.write(f"  {e}")
                        null_scores = {name: None for name in all_metric_names}
                        final_result = {**row, **null_scores}
                        f_out.write(json.dumps(final_result) + '\n')
                        continue
                
                await asyncio.sleep(API_SLEEP_INTERVAL)
        
        if rate_limit_hit:
            continue
        else:
            break

    # --- Final Report Generation ---
    final_judged_results = []
    if os.path.exists(JUDGED_RESULTS_CHECKPOINT):
        with open(JUDGED_RESULTS_CHECKPOINT, 'r', encoding='utf-8') as f:
            final_judged_results = [json.loads(line) for line in f]
    if not final_judged_results:
        print("No judged results found.")
        return
        
    print("\nAll judging complete. Generating final CSV report...")
    results_df = Dataset.from_list(final_judged_results).to_pandas()
    
    cols_to_drop = ['ground_truth_context', 'ground_truth_answer']
    for col in cols_to_drop:
        if col in results_df.columns:
            results_df = results_df.drop(columns=[col])
    
    print("\n--- Evaluation Results (First 10 Rows) ---")
    print(results_df.head(10))
    
    if not set(all_metric_names).issubset(results_df.columns):
        print("\nWarning: Not all metric columns are present in the final results. Averages may be inaccurate.")
    
    # Calculate averages only for the columns that actually exist
    existing_metrics = [name for name in all_metric_names if name in results_df.columns]
    average_scores = results_df[existing_metrics].mean(numeric_only=True)   
    print("\n--- Average Scores ---")
    print(average_scores)
    
    print(f"\nSaving detailed results to {FINAL_RESULTS_PATH}...")
    results_df.to_csv(FINAL_RESULTS_PATH, index=False)
    
    print("\nEvaluation finished successfully.")


if __name__ == "__main__":
    asyncio.run(main())