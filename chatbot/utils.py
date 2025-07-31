# utils.py
import os
import sys
import shutil
from colorama import Fore, Style, init

# --- CHANGE: Initialize colorama ---
# This makes the Fore and Style commands work on all platforms, including Windows.
init(autoreset=True)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def stream_and_collect_answer(stream):
    """
    Streams the response from the LLM to the console character by character
    and collects the full response.
    """
    full_response = ""
    for chunk in stream:
        # We print the LLM's answer in the default text color.
        print(chunk, end="", flush=True)
        full_response += chunk
    return full_response

# --- CHANGE 1: Made status_update more flexible and colorful ---
def status_update(message: str):
    """
    Displays a temporary status message on a single line in yellow.
    The caller provides the entire message.
    """
    # We use Fore.YELLOW to make the status message stand out.
    sys.stdout.write(f"\r{Fore.YELLOW}{Style.BRIGHT}{message}{Style.RESET_ALL}")
    sys.stdout.flush()

# --- CHANGE 3: Made clear_status_line more robust ---
def clear_status_line():
    """Clears the current terminal line to remove a status message."""
    # Get the actual width of the terminal.
    width = shutil.get_terminal_size().columns
    # Overwrite the line with spaces.
    sys.stdout.write("\r" + " " * width + "\r")
    sys.stdout.flush()

# --- NEW FUNCTION: Added a dedicated, colorful printer for sources ---
def print_sources(sources: list):
    """
    Prints the list of source documents in a clean, readable format with color.
    """
    if not sources:
        return

    print(f"\n\n{Style.BRIGHT}SOURCES:{Style.RESET_ALL}")
    for i, doc in enumerate(sources, start=1):
        source_name = doc.metadata.get('source_file', 'Unknown')
        page_number = doc.metadata.get('page_number', None)
        
        # Use green for the source file name to make it clear.
        display_name = f"{Fore.GREEN}{source_name}{Style.RESET_ALL}"
        
        if page_number:
            print(f"  [{i}] {display_name} (Page: {page_number})")
        else:
            print(f"  [{i}] {display_name}")