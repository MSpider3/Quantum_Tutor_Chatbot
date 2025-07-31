**1. What is a qubit and how is it different from a classical bit?**

A classical bit, the fundamental unit of classical computers, is like a light switch: it can only be in one of two definite states, either **0** (off) or **1** (on).

A qubit (or quantum bit) is the fundamental unit of quantum computers. It is much more powerful because, thanks to the principle of **superposition**, it can be in a state of **0**, **1**, or a combination of *both at the same time*.

**The key differences are:**
*   **State Space:** A bit is either 0 or 1. A qubit's state is a vector representing a linear combination of the 0 and 1 states.
*   **Superposition:** Qubits can represent multiple values simultaneously. A great analogy is a spinning coin: while it's in the air, it's both heads and tails at once. Only when it lands (is measured) does it pick one definite state.
*   **Entanglement:** Qubits can be linked together in a special way called entanglement, where the state of one qubit is instantly correlated with the state of another, no matter how far apart they are. Classical bits do not have this property.

---

**2. What does it mean for two qubits to be entangled?**

Entanglement is a unique quantum phenomenon where two or more qubits become linked in such a way that their fates are intertwined. They form a single, unified quantum state.

The defining characteristic is **perfect correlation**. If you have two entangled qubits, A and B, and you measure the state of qubit A, you will instantly know the state of qubit B, and vice-versa. This is true no matter how far apart they are—even light-years. Albert Einstein famously called this "spooky action at a distance."

A common analogy is having two "magic coins." You flip them and send them to opposite ends of the universe. The moment you look at your coin and see it's "heads," you know with 100% certainty that the other coin is "tails," without ever looking at it. This powerful, shared state is what allows quantum computers to perform complex parallel computations.

---

**3. What is superposition in quantum computing?**

Superposition is the core principle that allows a qubit to be in a combination of both its `|0⟩` and `|1⟩` basis states simultaneously.

Mathematically, a qubit's state `|ψ⟩` is described as `α|0⟩ + β|1⟩`, where:
*   `α` and `β` are complex numbers called amplitudes.
*   The probability of measuring the qubit and finding it in the **0** state is `|α|²`.
*   The probability of measuring the qubit and finding it in the **1** state is `|β|²`.
*   The sum of these probabilities must equal 1: `|α|² + |β|² = 1`.

Crucially, **superposition is destroyed by measurement**. When you measure a qubit in a superposition, it "collapses" into one of the definite classical states, either `|0⟩` or `|1⟩`, based on the probabilities defined by its amplitudes.

---

**4. What is the role of the Hadamard gate in a quantum circuit?**

The Hadamard gate (H-gate) is one of the most fundamental single-qubit gates. Its primary role is to **create superposition**.

Specifically, it performs the following transformations:
*   When applied to a qubit in the `|0⟩` state, it transforms it into an equal superposition: `(|0⟩ + |1⟩) / √2`. This state has a 50% chance of being measured as 0 and a 50% chance of being measured as 1.
*   When applied to a qubit in the `|1⟩` state, it transforms it into a different superposition: `(|0⟩ - |1⟩) / √2`.

Because it's the simplest and most common way to put a qubit into a superposition, the Hadamard gate is the essential first step in a vast number of quantum algorithms, including Grover's search and the Quantum Fourier Transform.

---

**5. What is quantum measurement and how does it affect a qubit state?**

Quantum measurement is the process of probing a quantum system to extract classical information from it. In the context of a qubit, it is the act of "looking" to see if it is a 0 or a 1.

Measurement has a profound and irreversible effect on the qubit's state:
1.  **Collapse of the Wavefunction:** The act of measurement forces the qubit to exit its superposition state and "collapse" into one of its definite classical basis states, either `|0⟩` or `|1⟩`.
2.  **Probabilistic Outcome:** The outcome of the measurement is not deterministic. It is governed by the qubit's amplitudes. For a state `α|0⟩ + β|1⟩`, the outcome will be 0 with probability `|α|²` and 1 with probability `|β|²`.
3.  **Destructive Nature:** Once a measurement is made and the state collapses, the original superposition is destroyed. The qubit is now in a classical state, and the quantum information held in its amplitudes is lost.

---

**6. How can you create a Bell state using Qiskit?**

A Bell state is the simplest example of a two-qubit entangled state. It is created by applying a Hadamard gate to one qubit and then using that qubit as the control for a CNOT gate on the second qubit.

Here is the correct, standard Qiskit code to create the `|Φ⁺⟩` Bell state:
```python
from qiskit import QuantumCircuit

# Create a circuit with 2 qubits and 2 classical bits for measurement
qc = QuantumCircuit(2, 2)

# 1. Apply a Hadamard gate to the first qubit (qubit 0)
# This puts it into an equal superposition.
qc.h(0)

# 2. Apply a CNOT gate.
# Qubit 0 is the control, Qubit 1 is the target.
# This entangles the two qubits.
qc.cx(0, 1)

# (Optional) Measure the qubits to see the result
qc.measure([0, 1], [0, 1])

# Print the circuit
print(qc)
```
When this circuit is run, the only possible measurement outcomes will be `00` or `11`, each with approximately 50% probability, proving the qubits are entangled.

---

**7. What is the difference between the Pauli-X and Pauli-Z gates?**

Both are fundamental single-qubit gates, but they perform different rotations on the Bloch sphere.

*   **Pauli-X Gate (`X`):** This is the quantum equivalent of the classical **NOT gate**. It performs a 180-degree rotation around the X-axis of the Bloch sphere. This has the effect of flipping the basis states:
    *   It flips `|0⟩` to `|1⟩`.
    *   It flips `|1⟩` to `|0⟩`.
    *   It is a **bit-flip** operation.

*   **Pauli-Z Gate (`Z`):** This is a **phase-flip** gate. It performs a 180-degree rotation around the Z-axis of the Bloch sphere. It leaves the basis states `|0⟩` and `|1⟩` on the poles of the sphere but changes the relative phase of the superposition.
    *   It leaves `|0⟩` unchanged.
    *   It flips the phase of `|1⟩`, turning `|1⟩` into `-|1⟩`.

---

**8. What does the Bloch sphere represent in quantum computing?**

The Bloch sphere is a geometric visualization tool that represents the state space of a **single qubit**.

It is a unit sphere in 3D space where:
*   The **North Pole** represents the definite state `|0⟩`.
*   The **South Pole** represents the definite state `|1⟩`.
*   Any other point on the **surface** of the sphere represents a pure superposition state, a linear combination of `|0⟩` and `|1⟩`.

Single-qubit gate operations can be visualized as rotations of the state vector on the surface of the sphere. For example, an X-gate is a 180-degree rotation around the x-axis.

Its most important limitation is that it can **only represent the state of one qubit**. There is no simple Bloch sphere generalization for multiple entangled qubits.

---

**9. How is a controlled-NOT (CNOT) gate used in quantum circuits?**

The Controlled-NOT (CNOT) gate is a fundamental two-qubit gate and is arguably the most important one for building complex algorithms.

**How it works:**
It has two input qubits: a **control qubit** and a **target qubit**.
*   If the control qubit is in the `|0⟩` state, it does nothing to the target qubit.
*   If the control qubit is in the `|1⟩` state, it applies a Pauli-X (NOT) gate to the target qubit, flipping its state.

**Its primary use is to create entanglement.** By first placing the control qubit in a superposition (using a Hadamard gate) and then applying a CNOT, the two qubits become linked in an entangled Bell state. This ability to create and manipulate entanglement is essential for nearly all quantum algorithms that offer a speedup over classical computers.

---

**10. What is the purpose of a quantum register in Qiskit?**

In Qiskit, a `QuantumRegister` is an organizational object that acts as a container or an array for a group of qubits.

Its main purposes are:
1.  **Organization:** It allows you to group qubits that belong to a single logical unit, making the circuit easier to design and read.
2.  **Addressing:** It provides a convenient way to apply gates to specific qubits within the register using their index (e.g., `qc.h(qreg[0])`).
3.  **Circuit Construction:** It is a required component for creating a `QuantumCircuit`, which also takes a `ClassicalRegister` to store the results of measurements.

In essence, it's a software abstraction that helps manage the collection of qubits you are working with in your quantum circuit.

---

**11. Explain how Grover’s algorithm achieves quadratic speedup.**

Grover's algorithm solves the problem of searching an unstructured database of N items in `O(√N)` time, a quadratic speedup over the classical `O(N)` requirement. It achieves this not by checking items faster, but by using quantum interference to amplify the probability of the correct answer.

The algorithm iterates through two key steps:
1.  **The Oracle:** This quantum "black box" recognizes the solution. When it finds the item being searched for (the "marked" item), it applies a phase shift, effectively "tagging" it by flipping its phase (`|ψ⟩ → -|ψ⟩`). All other items are left unchanged.
2.  **The Diffusion Operator (Amplitude Amplification):** This is the clever part. The diffusion operator takes the state of all qubits and performs an "inversion about the mean." It reflects every qubit's amplitude across the average amplitude of all qubits. Because the marked item has a negative amplitude while all others are positive, this reflection dramatically increases the amplitude of the marked item while decreasing the amplitudes of all others.

By repeating these two steps `~√N` times, the amplitude of the correct answer grows closer and closer to 1, while all others shrink. When you finally measure the qubits, you are highly likely to get the correct result.

---

**12. What is the role of the ancilla qubit in quantum error correction?**

An ancilla qubit is a "helper" or "auxiliary" qubit used in quantum circuits. In quantum error correction (QEC), its role is absolutely critical: **to detect errors without destroying the quantum information in the data qubits.**

Directly measuring the data qubits to check for errors would collapse their superposition, ruining the computation. The ancilla qubit provides a way around this. The process is called **syndrome measurement**:
1.  One or more ancilla qubits are entangled with a block of data qubits in a carefully designed way.
2.  The ancilla qubits are then measured. The state of the data qubits is not measured.
3.  The outcome of the ancilla measurement (e.g., `010`) is the "error syndrome." This syndrome reveals *if* an error occurred and *what kind* of error it was (e.g., a bit-flip on the third data qubit), but it reveals **nothing** about the logical state of the data itself.
4.  Based on the syndrome, a classical computer applies the appropriate correction (e.g., an X-gate to the third qubit) to fix the error. The ancilla is then reset and can be used again.

---

**13. How does the Quantum Fourier Transform differ from the classical one?**

While mathematically related, the Quantum Fourier Transform (QFT) and the classical Discrete Fourier Transform (DFT) are fundamentally different in their operation and output.

1.  **Complexity:** This is the most significant difference. The best classical DFT algorithms have a complexity of `O(N log N)`. The QFT can be implemented on a quantum computer with `O(log² N)` or `O(n²)` gates (where `n = log N`), which is an **exponential speedup**.
2.  **Input/Output:** A classical DFT takes a list of numbers as input and outputs a new list of numbers representing the frequency spectrum. A QFT takes a quantum state (a vector of amplitudes) as input and transforms it into a *new quantum state* where the frequency information is encoded in the new amplitudes.
3.  **Accessibility of Output:** With a classical DFT, you can read the entire output vector. With QFT, you cannot directly read all the output amplitudes. The act of measurement collapses the state to a single value. Therefore, QFT is not used for general signal processing but as a crucial subroutine inside other algorithms (like Shor's algorithm) to find the periodicity of a state.

---

**14. What is the stabilizer formalism and why is it useful in error correction?**

The stabilizer formalism is a powerful mathematical framework for describing and manipulating a specific but very important class of quantum states, called "stabilizer states," which includes the states used in most quantum error-correcting codes.

**The Core Idea:** Instead of describing a complex N-qubit state with its 2^N complex amplitudes, we describe it more efficiently by identifying a set of operators (the "stabilizers") that leave the state unchanged. A quantum state is uniquely defined as the `+1` eigenvector of all operators in its stabilizer group.

**Usefulness in Error Correction:**
1.  **Efficient Description:** Error-correcting codes can be described compactly by their stabilizer generators instead of a giant state vector.
2.  **Error Detection:** Errors (represented by Pauli X, Y, Z operators) either commute or anti-commute with the stabilizer operators. By measuring the stabilizers (using ancilla qubits), we can determine which stabilizers anti-commute with the error that occurred. This measurement outcome is the "error syndrome," which tells us what the error was and where it happened, allowing for correction.
3.  **Simplified Analysis:** It makes the analysis of gate operations and error propagation in quantum circuits much more tractable.

---

**15. How does phase kickback play a role in the Quantum Phase Estimation algorithm?**

Phase kickback is the central mechanism that makes the Quantum Phase Estimation (QPE) algorithm work. QPE is designed to estimate the eigenvalue of an eigenvector of a unitary operator `U`.

**The Process:**
1.  We have a target register in an eigenstate `|ψ⟩` of `U`, such that `U|ψ⟩ = e^(i2πφ)|ψ⟩`, where `φ` is the phase we want to estimate.
2.  We have a counting register of ancilla qubits, all prepared in a superposition using Hadamard gates.
3.  A series of **controlled-U** operations are performed, where the ancilla qubits act as the controls and the target register is the target.
4.  **Phase Kickback Occurs:** Because the target register is an eigenvector of `U`, the phase `e^(i2πφ)` is "kicked back" and applied to the controlling ancilla qubit. This is repeated for each ancilla, with each one applying the `U` operation `2^k` times.
5.  This process systematically encodes the binary representation of the phase `φ` onto the states of the ancilla qubits in the counting register.
6.  Finally, an **Inverse Quantum Fourier Transform** is applied to the counting register, which transforms this phase encoding into a computational basis state that can be measured, revealing the value of `φ`.

In short, phase kickback is the engine that transfers the phase information from the target eigenvector onto the measurable ancilla qubits.

---

**16. Why is it impossible to clone an arbitrary quantum state, and how does this affect quantum communication?**

It is impossible to create an identical, independent copy of an unknown, arbitrary quantum state. This is a fundamental law of physics known as the **No-Cloning Theorem**.

**The Reason:** The theorem arises directly from the **linearity of quantum mechanics**. A hypothetical cloning device would have to be a unitary operator `U` that takes an initial state `|ψ⟩` and a blank state `|s⟩` and produces two copies: `U(|ψ⟩|s⟩) = |ψ⟩|ψ⟩`.

If we assume this works for two different states, `|ψ⟩` and `|φ⟩`, then by linearity, it must also work for their superposition, `a|ψ⟩ + b|φ⟩`. However, applying the cloning operator to the superposition results in `a|ψ⟩|ψ⟩ + b|φ⟩|φ⟩`, which is a highly entangled state and is fundamentally different from two independent copies of the original superposition, `(a|ψ⟩ + b|φ⟩) ⊗ (a|ψ⟩ + b|φ⟩)`. This contradiction proves that no such universal cloning operator `U` can exist.

**Effect on Quantum Communication:** The No-Cloning Theorem is the foundation of security for **Quantum Key Distribution (QKD)** protocols. If an eavesdropper ("Eve") tries to intercept a quantum key being sent from Alice to Bob, she cannot simply copy the qubit and pass the original along. The act of measuring the qubit to learn its state will inevitably disturb it (collapse the wavefunction). This disturbance can be detected by Alice and Bob, revealing Eve's presence. This makes quantum communication channels fundamentally "tap-proof."

---

**17. What are the main limitations of near-term quantum hardware (NISQ) in implementing large-scale algorithms?**

NISQ stands for "Noisy Intermediate-Scale Quantum," a term describing the current era of quantum computers. These devices are powerful but are limited by several key factors that prevent them from running large-scale, fault-tolerant algorithms like Shor's algorithm for factoring.

1.  **Decoherence (Noise):** Qubits are extremely fragile. They lose their quantum properties (superposition and entanglement) very quickly due to interactions with their environment (e.g., heat, magnetic fields). This "decoherence time" limits the number of operations (the "depth" of the circuit) that can be performed before the quantum information is lost to noise.
2.  **Gate Fidelity:** The quantum gates that manipulate qubits are not perfect. A typical two-qubit gate might have a fidelity of 99.5% - 99.9%. While this sounds high, in an algorithm with thousands or millions of gates, these small errors accumulate rapidly, making the final result meaningless.
3.  **Limited Qubit Count & Connectivity:** NISQ devices have a relatively small number of qubits (from tens to a few hundred). Furthermore, the **connectivity** is often limited—a qubit might only be able to directly interact with its immediate neighbors on the chip. This requires many additional `SWAP` gates to move quantum states around, which adds more time and more opportunities for errors.
4.  **Lack of Fault Tolerance:** Most importantly, NISQ devices lack enough high-quality qubits to implement quantum error correction (QEC). Without QEC, the errors that inevitably occur during a computation cannot be detected and fixed, making long computations unreliable.

---

**18. In a 5-qubit system, how can you prepare a GHZ state and verify it experimentally in Qiskit?**

A Greenberger–Horne–Zeilinger (GHZ) state is a specific type of maximally entangled multi-qubit state, `(|00...0⟩ + |11...1⟩) / √2`.

**Preparation in Qiskit:**
The strategy is to create a superposition on one qubit and then use a chain of CNOT gates to "copy" this entanglement across the other qubits.

```python
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# 1. Prepare the GHZ state circuit
qc_ghz = QuantumCircuit(5)
# Start with a Hadamard on the first qubit
qc_ghz.h(0)
# Create a chain of CNOTs
for i in range(4):
    qc_ghz.cx(i, i + 1)
print("GHZ Preparation Circuit:")
print(qc_ghz)
```

**Experimental Verification in Qiskit:**
Verification requires measuring in different bases to confirm both the correlations and the superposition.

1.  **Correlation Check (Z-basis measurement):** We measure all qubits directly. The only possible outcomes should be `00000` and `11111`.
    ```python
    # Z-basis measurement
    qc_verify_z = qc_ghz.copy()
    qc_verify_z.measure_all()
    # Execute and check results
    # counts_z should only contain '00000' and '11111'
    ```
2.  **Coherence Check (X-basis measurement):** To check the relative phase, we apply a Hadamard gate to every qubit *before* measuring. This rotates the measurement basis. For a true GHZ state, the measurement outcomes must have an **even number of 1s**.
    ```python
    # X-basis measurement
    qc_verify_x = qc_ghz.copy()
    qc_verify_x.h(range(5)) # Apply H to all qubits
    qc_verify_x.measure_all()
    # Execute and check results
    # counts_x should only contain bitstrings with an even number of 1s
    ```
By performing both experiments and confirming the results, you can verify the GHZ state was created successfully.

---

**19. What is the significance of logical qubit fidelity in fault-tolerant quantum computing?**

Logical qubit fidelity is arguably the **single most important metric** for progress toward large-scale, fault-tolerant quantum computing.

*   **Physical vs. Logical Qubit:** A **physical qubit** is the actual hardware component (an ion, a superconducting circuit) which is inherently noisy and prone to errors. A **logical qubit** is an abstract, more robust qubit whose quantum state is redundantly encoded across many physical qubits using a quantum error-correcting code.
*   **Fidelity:** This is a measure of how close a qubit's actual state is to its ideal, intended state after an operation. A fidelity of 1.0 is perfect.
*   **Significance:** The goal of quantum error correction is to produce a logical qubit that is *more reliable* than any of its individual physical components. The **fault-tolerance threshold theorem** states that if the error rate (or infidelity) of your physical gates is below a certain threshold (e.g., ~1%), then you can use QEC to make the error rate of your logical qubits *arbitrarily low* by adding more physical qubits to the encoding.

Therefore, logical qubit fidelity is the direct measure of how well your error correction is working. Achieving a logical fidelity that is significantly higher than your physical fidelity is the "break-even" point that proves your QEC scheme is actively suppressing errors rather than introducing more. This is the essential gateway to building quantum computers capable of running long, complex algorithms.

---

**20. Explain how monogamy of entanglement restricts quantum network design and what this implies for entanglement swapping.**

**Monogamy of Entanglement** is a fundamental principle of quantum mechanics with profound implications. It states that entanglement is a **private, non-shareable resource**.

*   **The Principle:** If qubit A is **maximally entangled** with qubit B, it **cannot be entangled at all** with any other qubit, C. A qubit has a finite "budget" of entanglement it can share. Unlike classical correlations (e.g., three people all agreeing to wear red shirts), quantum entanglement is exclusive.

*   **Restriction on Quantum Network Design:** This principle makes building a quantum internet fundamentally different from a classical one. You cannot have a central "entanglement server" or "quantum router" that is simultaneously entangled with hundreds of clients. A node cannot simply "broadcast" an entangled state to multiple recipients. This prohibits simple "star network" topologies where a central hub connects to many nodes.

*   **Implication for Entanglement Swapping:** Entanglement swapping is the clever protocol that allows us to overcome this restriction and build long-distance networks. It works as follows:
    1.  Alice and Bob create an entangled pair (A, B1).
    2.  Bob and Carol create another, independent entangled pair (B2, C).
    3.  Bob performs a special joint measurement (a Bell state measurement) on his two qubits, B1 and B2.
    4.  This measurement destroys the entanglement Bob had with both Alice and Carol. However, by communicating his measurement result to Alice and Carol, they can perform local corrections that "swap" the connection.
    5.  The final result is that qubits **A and C are now entangled**, even though they never directly interacted.

Entanglement swapping is the essential building block for **quantum repeaters**, which will be necessary to build a global-scale quantum internet by daisy-chaining these short-distance entangled links together.