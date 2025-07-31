# Monitor or cancel a job







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Jobs are listed on the Workloads page for your quantum service channel:

Use the job instance to check the job status or retrieve the results by calling the appropriate command:

Callservice.job(\<job\_id>)to retrieve a job you previously submitted. If you don't have the job ID, or if you want to retrieve multiple jobs at once; including jobs from retired QPUs (quantum processing units), callservice.jobs()with optional filters instead. SeeQiskitRuntimeService.jobs.

service.jobs()also returns jobs run from the deprecatedqiskit-ibm-providerpackage. Jobs submitted by the older (also deprecated)qiskit-ibmq-providerpackage are no longer available.

This example returns the 10 most recent runtime jobs that were run onmy_backend:

Output:

Output:

Output:

You can cancel a job from the IBM Quantum Platform dashboard either on the Workloads page or the details page for a specific workload. On the Workloads page, click the overflow menu at the end of the row for that workload, and select Cancel. If you are on the details page for a specific workload, use the Actions dropdown at the top of the page, and select Cancel.

In Qiskit, usejob.cancel()to cancel a job.

The results ofSamplerV2jobs executed in Qiskit Runtime contain execution timing information in their metadata.
This timing information can be used to place upper and lower timestamp bounds on when particular shots were executed on the QPU.
Shots are grouped intoExecutionSpanobjects, each of which indicates a start time, a stop time, and a specification of which shots were collected in the span.

An execution span specifies which data was executed during its window by providing anExecutionSpan.maskmethod. This method, given anyPrimitive Unified Block (PUB)index, returns a boolean mask that isTruefor all shots executed during its window. PUBs are indexed by the order in which they were given to the Sampler run call. If, for example, a PUB has shape(2, 3)and was run with four shots, then the mask's shape is(2, 3, 4). See theexecution_spanAPI page for full details.

Example:

To view execution span information, review the metadata of the result returned bySamplerV2, which comes in the form of anExecutionSpansobject. This object is a list-like container containing subclass instances ofExecutionSpans such asSliceSpan:

Execution spans can be filtered to include information pertaining to specific PUBs, selected by their indices:

View global information about the collection of execution spans:

Extract and inspect a particular span:

It is possible for time windows specified by distinct execution spans to overlap. This is not because a QPU was performing multiple executions at once, but is instead an artifact of certain classical processing that might happen concurrently with quantum execution. The guarantee being made is that the referenced data definitely occurred in the reported execution span, but not necessarily that the limits of the time window are as tight as possible.

On this page

© IBM Corp., 2017-2025


---

# Workload usage







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Usage is a measurement of the amount of time the QPU is locked for your workload, and it is calculated differently, depending on which execution mode you're using.

The usage reported on the dashboard or by using the API is the time a QPU is locked for your workload. Failed or canceled jobs count toward your usage in certain circumstances - see theFailed and canceled jobssection for details.

Your usage has different impacts, depending on which channel you're using:

When a job is failed or canceled, the reported usage is as follows:

Job or batch mode: The reported usage is the time the QPU was locked for executing your workload until the time it failed or was canceled. Therefore, if the failure or cancellation occurred before the lock, the reported usage is zero. Otherwise, the workload's reported usage is the amount of usage before the workload failed or was canceled. Thus, some failed jobs do not appear in your reported usage and others do.

Session mode: The reported usage is the wall-clock time from when the first job started executing in the session until the session terminates, regardless of the number of jobs that fail or are canceled.

After a workload has completed, there are several ways to view its actual usage:

After submitting a job to the IBM Quantum channel, you can see an estimation for how muchquantum timethe job will take to run by usingjob.usage_estimation.  Quantum time is the duration, in seconds, a QPU is committed to fulfilling a user request.

Alternatively, you can view this information on IBM Quantum Platform by opening the job details.

This only applies to jobs that use primitives.

Example:

Output:

While getting an accurate local estimation is complicated by the extra operations done for error suppression and mitigation, you can use this baseline formula to get an approximation of estimated usage:

<per sub-job overhead> + (rep_delay + <circuit length>) * <num executions>

If you aren't using any advanced error-mitigation techniques or customrep_delay, you can use2+0.00035*<num executions>as a quick formula.

On this page

© IBM Corp., 2017-2025


---

# Minimize job run time







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

There are several ways you can limit the amount of time spent processing and running a job:

Run only as many shots as you need: The quantum time a job takes (and therefore, its cost) scales with the number of shots. Therefore, you can manage your cost by running only as many shots as you need. For Estimator jobs, lower precision typically requires more shots and therefore longer execution time.

Set limits on execution time:  You can limit how long each job, batch, or session runs.  For details, seeMaximum execution time for Qiskit Runtime workloads.

Use only the necessary settings for error suppression and error mitigation, because higher values can cause your jobs to run longer. SeeIntroduction to options,Configure error suppression, andConfigure error mitigationfor details.

If you are running multiple jobs that contain the same (likely parameterized) circuits and are using an error mitigation method that requires noise models, such as PEA and PEC, consider usingNoiseLearner. With this helper program, you can learn the noise model of a circuit once and reuse the model in subsequent Estimator queries. Note that a noise model becomes stale after a certain time, so this is only practical if there is no long delay between jobs (for example, within a session). SeeNoise learning helperfor more details.

On this page

© IBM Corp., 2017-2025


---

# Maximum execution time for Qiskit Runtime workloads







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

To ensure fairness and help control costs, there is a maximum amount of time each Qiskit Runtime job can run. If a job exceeds this time limit, it is forcibly canceled and aRuntimeJobMaxTimeoutErrorexception is raised.

If you use Qiskit Runtime on IBM Cloud®, the session or batch is immediately terminated when the cost limit is reached.

The maximum execution time for a job is the smaller of these values:

Themax_execution_timevalue is based onquantum time, not wall clock time. Quantum time is the amount of time that the QPU is dedicated to processing your job. Simulator jobs use wall clock time because they do not have quantum time.

Set the maximum execution time (in seconds) on the job options, as shown in the following example.  SeeSpecify optionsfor information about setting options.

You can also find how much quantum time completed jobs have used by returning the job metrics as follows:

The service calculates an appropriate job timeout value based on the input circuits and options. This service-calculated timeout is capped at 3 hours to ensure fair device usage. If amax_execution_timeis also specified for the job, the lesser of the two values is used.

For example, if you specifymax_execution_time=5000(approximately 83 minutes), but the service determines it should not take more than 5 minutes (300 seconds) to execute the job, then the job is canceled after 5 minutes.

When a batch is started, it is assigned a maximum time to live (maximum TTL) value. After this TTL is reached, the batch is terminated, any jobs that are already running continue running, and any queued jobs that remain in the batch are put into a failed state.

Batches also have an interactive time to live (interactive TTL) value between jobs that cannot be configured. If you don't explicitly close a batch, it is deactivated after the interactive TTL expires and can be reactivated at any time until it reaches its  maximum TTL.

For instructions to work with these values, seeRun jobs in a batch.

When a session is started, it is assigned a maximum TTL value that determines how long a session can run. After this TTL is reached, the session is terminated, any jobs that are already running continue running, and any queued jobs that remain in the session are put into a failed state.

There is also an interactive TTL value that cannot be configured.  If no session jobs are queued within that window, the session is temporarily deactivated.

For instructions to work with these values, seeRun jobs in a session.

On this page

© IBM Corp., 2017-2025


---

# Job limits







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

When you send a job to an IBM® QPU, it is first sent to the job validation service.  This service tries to ensure that the job will be able to run on the QPU so you don't have to wait for it to go through the queue and then have the job fail.  These checks include enforcing the described limits.

Certain primitive options increase the circuit size.  The described limits are checkedafterthe expected increase in circuit size. In particular, these options increase circuit size:

At most,10 millionexecutions are allowed.  The number of executions is the number of circuits times the number of shots, where the circuits are those generated after PUB elements are broadcasted.

For example, if you have a PUB with one circuit, observables with shape (1, 6), and parameters with shape (4, 1), this would render4×6=244 \times 6 = 244×6=24circuits (or fewer, if some observables commute). If you requested 2,000 shots, then the total number of executions is24×2,000=48,00024 \times 2,000 = 48,00024×2,000=48,000.

The service permits up to26.8 million control-system instructions per qubit. This ensures that the user circuits fit within the control system's instruction memory.  The following table describes how the system translates instruction set architecture (ISA) circuit instructions to control system instructions when calculating this limit.

This table captures the heuristic used in validation and does not reflect the exact number of instructions used to implement an operation.

The maximum number of single-qubit gates are as follows:

The maximum number of two-qubit gates per circuit is 5 million for static circuits and 100,000 for dynamic circuits.
This ensures that the job can be manipulated within the memory limits of the low-level software stack.

For considerations and limitations related to runningdynamic circuitson quantum hardware, see theHardware considerations and limitations for classical feedforward and control flowguide.

On this page

© IBM Corp., 2017-2025


---

# Hardware considerations and limitations for classical feedforward and control flow







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Classical feedforward and control flowshows how to use Qiskit to build circuits that involve classical feedforward and control flow, also known as dynamic circuits. When actually running such circuits on quantum hardware, there are several considerations and limitations to be aware of. Many of these limitations exist because the underlying technology supporting these features is in an early stage of development, and we hope to be able to address them in the future.

Running circuits on quantum processors involves not only the qubits themselves, but also a system of classical electronics and computers to generate and receive waveforms and orchestrate the control logic. When a job is submitted to the IBM Quantum® service, it is processed into multiple classical programs that must be distributed between two kinds of units: central controllers and qubit controllers (see diagram above). A job may fail if it exceeds certain limitations of these controllers. There are two kinds of limitations to be aware of:

The memory requirements and classical latencies of a job are affected by the following factors:

Buffer overflow error. One of the most common limitations users can encounter when executing dynamic circuits is a buffer overflow during measurement result collection. The measurement buffer on the control system can only store a limited number of measurement results. If the circuit performs many measurements in rapid succession, the buffer might fill before the control system has time to stream the results to the host, causing a job failure.

If you encounter the error"RuntimeJobFailureError: unable to retrieve job result. A buffer overflow occurred during result collection...", try these strategies to mitigate this issue:

For more information, see theDynamic repetition rate executionguide.

On this page

© IBM Corp., 2017-2025


---

# Save and retrieve jobs







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Quantum workflows often take a while to complete and can run over many sessions. Restarting your Python kernel means you'll lose any results stored in memory. To avoid loss of data, you can save results to file and retrieve results of past jobs from IBM Quantum so your next session can continue where you left off.

IBM Quantum automatically stores results from every job for you to retrieve at a later date. Use this feature to continue quantum programs across kernel restarts and review past results. You can get the ID of a job programmatically through itsjob_idmethod, or you can see all your submitted jobs and their IDs on theWorkloads page.

To find a job programmatically, use theQiskitRuntimeService.jobsmethod. By default, this returns the most recent jobs, but you can also filter jobs by backend name, creation date, and more. The following cell finds any jobs submitted in the last three months. Thecreated_afterargument must be adatetime.datetimeobject.

Output:

You can also select by backend, job state, session, and more. For more information, seeQiskitRuntimeService.jobsin the API documentation.

Once you have the job ID, use theQiskitRuntimeService.jobmethod to retrieve it.

Output:

Output:

Always forgetting how to retrieve a job? Try this prompt with Qiskit Code Assistant:

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

You may also want to save results to disk. To do this, use Python's built-in JSON library with Qiskit Runtime's encoders.

You can then load this array from disk in a separate kernel.

Output:

On this page

© IBM Corp., 2017-2025


---

# Processor types







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Processor types are named for the general technology qualities that go into builds, consisting of the family and revision. Family (for example, Falcon) refers to the size and scale of circuits possible on the chip. This is primarily determined by the number of qubits and the connectivity graph. Revisions (for example, r1) are design variants within a given family, often leading to performance improvements or tradeoffs. Segments are comprised of chip sub-sections, and are defined within a given family. For instance, segment H of a Falcon consists of seven qubits arranged as seen in the illustration below. Segment H on a Hummingbird, if implemented, could be entirely different.

Quantum volume: 512

At 156 qubits, Heron is anEagle-sized upgrade toEgretthat pulls in substantial innovations in signal delivery that were previously deployed inOsprey. The signals required to enable the fast, high-fidelity two-qubit and single-qubit control are delivered with high-density flex cabling.

View available Heron processors

Native gates and operations:cz, id, delay, measure, reset, rz, sx, x, if_else, for_loop, switch_case

r2(July 2024) This is a revision of the original Heron processor. The chip has been redesigned to include 156 qubits in a heavy-hexagonal lattice. While continuing to make use of the innovations of the original Heron processors, it also introduces a new TLS mitigation feature that controls the TLS environment of the chip, thereby improving coherence and stability across the whole chip.

r1(December 2023) The first version of Heron with 133 qubits.

Osprey is nearly quadruple the size of Eagle at 433 qubits. The larger chip sizes have required further enhancements to device packaging, as well as custom flex cabling in the cryostat to fit the greater I/O requirements within the same wiring footprint.

Quantum volume: 128

At 127 qubits, the Eagle processor family incorporates more scalable packaging technologies than previous generations. In particular, signals pass through multiple chip layers so as to allow for high-density I/O without sacrificing performance.

SeeIBM Quantum breaks the 100‑qubit processor barrierfor more about the Eagle processor family.

View available Eagle processors

Native gates and operations:ecr, id, delay, measure, reset, rz, sx, x, if_else, for_loop, switch_case

r3(December 2022) Eagle r3 is a version of the 127-qubit processor with enhanced coherence properties but otherwise similar design parameters to Eagle r1.

r1(December 2021) At the qubit level, Eagle r1 uses similar design elements and parameters to Falcon r5.11, enabling similarly fast readout. Gate speeds and error rates should also be similar.

Quantum volume: 128

Using a heavy-hexagonal qubit layout, the Hummingbird family allows up to 65 qubits.

r3(December 2021) This version of Hummingbird with 65 qubits has enhanced coherence properties.

r2(August 2020) Released in 3Q 2020, this revision contains 65 qubits. Improvements previously demonstrated on Falcons, like readout multiplexing, space-efficient qubit-qubit couplers, and flip-chip technology enhanced the capabilities of the Hummingbird family and led to a scalable 65Q design.

r1(October 2019) This revision is the first attempt at supporting a large (>50) number of qubits on a chip.

Quantum volume: 512

Egret brings the innovations of tunable couplers onto a 33-qubit platform, resulting in faster and higher-fidelity two-qubit gates.

r1(December 2022) The first realization of the Egret processor has demonstrated the highest Quantum Volume among IBM® QPUs and a substantial improvement in two-qubit gate error rates (seePushing quantum performance forward with our highest Quantum Volume yet). This new quantum processor boasts a substantial speedup and fidelity improvement (many gates approaching 99.9%) in two-qubit gates while reducing spectator errors.

Quantum volume: 128

The Falcon family of devices offers a valuable platform for medium-scale circuits, and also serves as a valuable platform for demonstrating performance and scalability improvements before they’re pushed onto the larger devices.

View available Falcon processors

Native gates and operations:cx, id, delay, measure, reset, rz, sx, x, if_else, for_loop, switch_case

r8(September 2021) In addition to the features of r5.11, Falcon r8 has enhanced coherence properties.

r5.11(January 2021) In addition to the filtering in r5.10, design improvements target speed-ups in qubit state readout. An essential requirement for quantum error correction demonstrations is fast readout. To enable this, the paradoxical requirements of stronger readout coupling yet protection from qubit relaxation is accomplished with advanced filtering techniques and fine tuning of various components’ couplings on-chip. This revision, combined with the latest in control electronics, enables mid-circuit measurements.

r5.10(December 2020) This revision pioneered advanced on-chip filtering techniques that eventually led to the faster qubit state readout in r5.11. The filters reduce qubit relaxation and preserve lifetime. Additionally, space-saving “direct-couplers” are used to couple qubits together, essential for scaling to larger bird families.

r4(April 2020) Adding to the capabilities of r1, the r4 is the first revision in the large birds to deploy multiplexed readout. Previous designs required an independent signal pathway on the chip, as well as in the dilution refrigerator and control electronics for qubit state readout.

r1(February 2020) The first generation of the Falcon family, r1 is a 28Q offering independent readout, contrasting to the multiplexed configurations in the other revisions. The flip-chip technology allowed scaling to a larger number of qubits. The heavy-hex connectivity graph is employed for the first time here, optimal for our two-qubit gate of choice, cross-resonance.

The Canary family comprises small designs containing anywhere from 5 to 16 qubits. It uses an optimized 2D lattice.  That is, all of the qubits and readout resonators are on the same layer.

r1.3(December 2019) A stripped-down offering containing only a single qubit.

r1.1(May 2017) Using the similar design processes to r1, r1.1 extends the design to include 16 qubits.

r1(January 2017) Initial 5Q design with resonators and qubits all on a single lithography layer.

On this page

© IBM Corp., 2017-2025


---

# QPU information







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

IBM® offers both open and premium access to a wide variety of quantum processing units (QPUs). All QPUs deployed by IBM are based on superconducting qubit technology, as the control and scalability of this technology pave a clear path to achieving quantum advantage with these QPUs. You can see the full details of all IBM QPUs on theQuantum processing units page.

Each QPU has a version number in the form X.Y.Z (major.minor.revision). A circuit compiled for a given version number is guaranteed to run on that QPU. If the revision number changes, the circuit will continue to run. If the major or minor number changes, the circuit is not guaranteed to run, although it may do so. The conditions under which a version number may change are listed below:

The major version will increment for changes such as:

The minor version will increment for changes such as:

The revision version number will increment for fixes that do not break the existing compiled circuit. These changes include:

The following is a subset of QPU configuration values available in IBM Quantum Platform and fromQiskit.

These values are shown on both theCompute resources taband the details page for each QPU.

Note that the metric for median ECR error (for Eagle processors) and median CZ error (for Heron processors) is theaverage gate fidelity, which is the average over all possible input states of the fidelity between the state produced by the actual operation and the state produced by the ideal operation.

Additional information available on the details page for each QPU

To access the details page, click theCompute resourcestab, then click the name of the QPU.

Version- The version number of a QPU in the formmajor.minor.revision. SeeQPU versioningfor details on how this number is assigned.

Calibration data- Download the calibration data as a CSV file or click the arrow to display the Topology diagram, Individual qubit readout graph, or the Calibration data table. You can customize the data that is shown, depending on the view you have open. For example, on the Topology diagram, you can choose the data you want to see for connections and qubits. The colored bars associated with the diagram or graph indicate the range that is shown, with the average value marked. The color maximum and minimum change depending on the QPU.

Your access instance- Instances that you can use. Click the arrow on the right to expand or collapse this section. For each instance, you can see the following information:

To find your available QPUs, open theCompute resourcespage.  Click a QPU to view its details.

You can also view your available QPUs by using thebackends API.

View QPU configuration values by selecting a QPU on theQuantum processing unitspage from the Compute resources tab. The three tabs in the Calibration data section let you choose how to view the calibration data; the Map view tab is automatically selected.

Click the download icon in the upper right of any tab to download a CSV file of calibration data.

Graph view tab.

Table view tab

To find your available QPUs onIBM Cloud, view theIBM Cloud Compute resources page.You must be logged in to see your available compute resources. You are shown a snapshot of each QPU. To see full details, click the QPU name. You can also search for QPU from this page.

To see the QPUs available to you onIBM Quantum Platform, click theCompute resources tabfrom your dashboard. You are shown a snapshot of each QPU. To see full details, click the QPU name. You can also sort, filter, and search from this page.

On this page

© IBM Corp., 2017-2025


---

# Get backend information with Qiskit







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page explains how to use Qiskit to find information about your available backends.

To view the backends you have access to, you can either view a list on theCompute resources page,or you can use theQiskitRuntimeService.backends()method. This method returns a list ofIBMBackendinstances:

To run the following code, be sure you have already authenticated to the service. SeeSet up to use IBM Quantum Platformfor more details.

Output:

TheQiskitRuntimeService.backend()method (note that this is singular:backend) takes the name of the backend as the input parameter and returns anIBMBackendinstance representing that particular backend:

Output:

You can also filter the available backends by their properties. For more general filters, set thefiltersargument to a function that accepts a backend object and returnsTrueif it meets your criteria. Refer to theAPI documentationfor more details.

The following code returns only backends that fit these criteria:

Output:

Use these keyword arguments to filter by any attribute in backend configuration (JSON schema) or status (JSON schema). A similar method isQiskitRuntimeService.least_busy(), which takes the same filters asbackends()but returns the backend that matches the filters and has the least number of jobs pending in the queue:

Output:

Some information about a backend does not change regularly, such as its name, version, the number of qubits it has, and the types of features it supports. This information is available as attributes of thebackendobject.

The following cell builds a description of a backend.

Output:

For a full list of attributes, see theIBMBackendAPI documentation.

Backends can also have properties that change whenever the backed is calibrated, such as qubit frequency and operation error rates. Backends are usually calibrated every 24 hours, and their properties update after the calibration sequence completes. These properties can be used when optimizing quantum circuits or to construct noise models for a classical simulator.

Thebackend.properties().qubit_property()returns information about the qubits' physical attributes. It contains a dictionary of various properties of the qubit, each paired with its value and the timestamp of the last calibration.

T1 (Relaxation Time): The T1 time represents the average duration a qubit remains in its excited state∣1⟩|1\rangle∣1⟩before decaying to its ground state∣0⟩|0\rangle∣0⟩due to energy relaxation. This parameter is used to characterize the qubit's energy relaxation behavior, and is expressed in units of seconds (s).

T2 (Dephasing Time): The T2 time denotes the timescale over which a qubit maintains phase coherence of a superposition between the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states. It accounts for both energy relaxation and pure dephasing processes, providing insight into the qubit's coherence properties.

frequency: This parameter specifies the resonant frequency of the qubit, indicating the energy difference between the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states, expressed in hertz (Hz).

anharmonicity: Anharmonicity is the difference in energy between the first and second excited states of the qubit, also expressed in hertz (Hz).

readout_error: The readout error quantifies the average probability of incorrectly measuring a qubit's state. It is commonly calculated as the mean of prob_meas0_prep1 and prob_meas1_prep0, providing a single metric for measurement fidelity.

prob_meas0_prep1: This parameter indicates the probability of measuring a qubit in the 0 state when it was intended to be prepared in the∣1⟩|1\rangle∣1⟩state, denoted asP(0∣1)P(0 | 1)P(0 ∣ 1). It reflects errors in state preparation and measurement (SPAM), particularly measurement errors in superconducting qubits.

prob_meas1_prep0: Similarly, this parameter represents the probability of measuring a qubit in the 1 state when it was intended to be prepared in the∣0⟩|0\rangle∣0⟩state, denoted asP(1∣0)P(1 | 0)P(1 ∣ 0). Like prob_meas0_prep1, it reflects SPAM errors, with measurement errors being the predominant contributor in superconducting qubits.

readout_length: The readout_length specifies the duration of the readout operation for a qubit. It measures the time from the initiation of the measurement pulse to the completion of signal digitization, after which the system is ready for the next operation. Understanding this parameter is crucial for optimizing circuit execution, especially when incorporating mid-circuit measurements.

Output:

Output:

Output:

Thebackend.targetattribute is aqiskit.transpiler.Targetobject: an object that contains all the information needed to transpile a circuit for that backend. This includes instruction errors and durations. For example, the following cell gets the properties for anecrgateacting between qubits 1 and 0.

Output:

The following cell shows the properties for a measurement operation (including the readout error) on qubit 0.

Output:

On this page

© IBM Corp., 2017-2025


---

# Native gates and operations







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Eachprocessor familyhas a native gate set. By default, the QPUs in each family only support running the gates and operations in the native gate set. Thus, every gate in the circuit must be translated (by the transpiler) to the elements of this set.

You can view the native gates and operations for a QPU eitherwith Qiskitor on the IBM Quantum® PlatformCompute resources page.

The terms native gates and basis gates are often used interchangeably. However, you can specify a different set of basis gates to use, while the native gate set never changes. For information about changing the basis gates, see theRepresent quantum computerstopic.

Select any QPU on theCompute resourcestab. The default gates for that QPU are listed under Details. Note that the non-unitary operations are not listed here; use the method in Qiskit described above to see all native gates and operations for a QPU.

Theinit_qubitsflag, set as aprimitive execution option,controls whether qubits are reset to the zero state at the start of each circuit. Its default value isTrue, indicating that the qubits should be reset. IfFalse, the qubits will begin in the final state from the previous shot, and you must manually insertresetsif you want to reset them to the zero state. If a job consists of multiple circuits, then the shots are executed in a "round-robin" fashion. That is, each circuit will be executed in sequence to obtain one shot from each circuit. This process is then repeated until the requested number of shots has been obtained from all circuits.

On this page

© IBM Corp., 2017-2025


---

# Dynamic repetition rate execution







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

When a circuit is executed on an IBM® quantum processing unit (QPU), an implicit reset is typically inserted at the beginning of the circuit to ensure the qubits are initialized to zero. However, the reset process is not perfect, leading to state preparation errors. To alleviate the error, the system also inserts repetition delay time (orrep_delay) between circuits. Each backend has a different defaultrep_delay, but it's usually longer than T1 to allow the environment to reset the qubits. The defaultrep_delaycan be queried by runningbackend.default_rep_delay.

All IBM QPUs use dynamic repetition rate execution, which allows you to change therep_delayfor each job. Circuits you submit in a primitive job are batched together for execution on the QPU. These circuits are executed by iterating over the circuits for each shot requested; the execution is column-wise over a matrix of circuits and shots, as illustrated in the following figure.

Becauserep_delayis inserted between circuits, each shot of the execution encounters this delay. Therefore, lowering therep_delaydecreases the total QPU execution time, but at the expense of increased state preparation error rate, as can be seen in the following image:

Note that while circuits in a primitive job are batched together for QPU execution, there is no guarantee on the order the circuits from PUBs are executed. Thus, even though you submitpubs=[pub1, pub2], there is no guarantee the circuits frompub1will run before those frompub2. There is also no guarantee that circuits from the same job would run as a single batch on the QPU.

On this page

© IBM Corp., 2017-2025


---

# Retired QPUs







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The following IBM® quantum processing units (QPUs) have been retired. For the full list of available QPUs, see theCompute resources page. By default, the information is shown in the card view, but you can use the view switchers () at the top right to change to a sortable table view.

To retrieve jobs from a retired QPU, seethese instructions.

Use the following code to retrieve a job from a retired QPU.

service.jobs()returns jobs run from bothqiskit-ibm-runtimeand the deprecatedqiskit-ibm-providerpackage. Jobs submitted by the older (also deprecated)qiskit-ibmq-providerpackage are no longer available.

On this page

© IBM Corp., 2017-2025


---

# Create and manage instances







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Access to IBM Quantum Platform services is controlled by theinstances(previously called providers) to which you are assigned. An instance is defined by a hierarchical organization ofhub,group, andproject. A hub is the top level of a given hierarchy (organization) and contains within it one or more groups. These groups are in turn populated with projects. The combination of hub/group/project is called an instance. Users can belong to more than one instance at any given time.

IBM Cloud® instances are different from IBM Quantum Platform instances.  IBM Cloud does not use the hub/group/project structure for user management. This section describes instances in IBM Quantum Platform. To view, create, and edit IBM Cloud instances, visit theIBM Cloud Quantum Instances page. Click the name of an instance to see details such as your CRN for that instance, what compute resources are available to you by using that instance, and what jobs you have run on that instance.

The hub/group/project hierarchy that makes up an IBM Quantum instance.

Users with a public account automatically belong to the ibm-q/open/mainOpen Plan. For organizations outside of IBM®, designated hub or group administrators assign users to instances.

The instances that you can access are listed at the bottom of yourAccount page.

By default, users who sign up for an IBM Quantum account are assigned to the Open Plan and the Open Plan's instance,ibm-q/open/main. To guarantee that everyone can use the quantum computers allocated to the plan fairly,an individual can have no more than three jobs running and/or in the queue (across all quantum computers) at the same time.Submitting more than three jobs at a time will return error#3458, and additional jobs will be canceled.

Those using the Open Plan instance have up to 10 minutes total of quantum time per month, which resets at 00:00:00 UTC on the first of each calendar month. Open Plan users can track their usage on thePlatform dashboard,Workloads,andAccountpages.

You can see information about your instances programmatically or in the user interface.

You can usetheinstances()methodto list your instances programmatically.

The IBM Quantum Platform dashboard, Compute resources, and Workloads pages display information such as usage metrics, workloads, and quantum computers based on your instance. If you have access to multiple instances, use the dropdown in the menu bar to switch between instances.

The instance switcher does not appear in the Administration application.

If you switch to a different instance, it is remembered the next time you log on and, assuming that it's still a valid instance, information pertaining to that instance is displayed.  By default, the first premium instance you have access to is used.  If you do not have any premium instances, the first (alphabetically) open instance is shown.

When you execute a task using an IBM Quantum service (for example, sending circuits to a quantum computer), ajobinstance is returned to you. Regardless of which service is being used, a job can track the progress of the submission through IBM Quantum, and retrieve the final computation results. Because services are coupled to instances, the jobs created from these services are also tied to the specific instance being used. Therefore,if a user is removed from an instance, their jobs and the associated results are no longer accessible.

This section applies to Premium Plan users only, since their access includes multiple instances.When determining which jobs to run, thefair-share schedulertakes into account an instance'susagecompared to its allocation. For example, an instance with a large allocation that has already run many jobs, or has run one very long job, might have a lower priority when compared to an instance with a smaller allocation but very low usage.
The jobs you run and the jobs run by other collaborators in the same instance count toward the reported usage for that instance. You can see the usage for an instance on yourdashboard(use theinstance switcherat the top of the page to change which instance is reflected on your dashboard).

If an instance has been marked as "limited" by your administrator (you will see a "Remaining" column in the usage area) and the instance exceeds its allocation (defined by your administrator) within the 28-day rolling window, any active workload will continue running (including sessions) but pending workloads will remain in the queue until more time is available. If an instance is not limited and the instance exceeds its allocation, jobs run with that instance are likely to run at a lower priority and experience longer queue times.

An alert displays on an instance's usage when it has exceeded its allocation.

You can specify an instance when initializing the service or when choosing a quantum computer.  You can copy the service-level code by clicking the three dots by the instance name on the Instances section of theAccount overview page.

If you do not specify an instance, the code will select one in the following order:

To leave an instance, visit the instance list on yourAccount page.Select the instance you wish to leave, then select the overflow menu and chooseLeave instance.

On this page

© IBM Corp., 2017-2025


---

# Fair-share scheduler







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

When you submit a workload to a quantum processing unit (QPU), it enters the scheduler for the specific QPU, joining the pool of workloads (from all users) that are waiting to be executed on that QPU. The order in which these workloads are executed is, by default, determined by a fair-share formula. As discussed below, this formula attempts to balance the workload between differentinstancesaccording to the allocated QPU access amount over a given time window. In practice, this means that workloads from various instances are interweaved in such a way that the order in which workloads complete is not necessarily the order in which they were submitted. Because the order is calculated dynamically as new workloads arrive, it is generally impossible to guarantee when a workload will be executed from the fair-share scheduler.

IBM® assigns allocation to each hub based on their allotted capacity contracted under the Premium Plan subscription. Hub administrators then decide what portion of this allocation to assign to each of their groups. Similarly, group administrators will decide what portion of allocation to assign to each of their projects.

The hub administration user interface is used to assign allocation, in minutes, to groups. The entire hub allotted time can be distributed to the underlying groups, and the hub administrator can control the time distribution by specifying the allocation in minutes for each group.

The fair-share scheduler takes into consideration how the allotted time is distributed across groups and projects to determine workload prioritization.

The scheduler combines a group’s allocation with the allotted time of its hub, to determine the total fraction of computational power allocated to that group.

For example, assume only two groups maintain workloads in one queue. With all else being equal, a group with twice the number of minutes will have twice the number of workloads execute.

The fair-share scheduler selects workloads to execute on a QPU in a dynamic order so that no instance can monopolize the QPU. When a QPU is ready for additional work, it requests the next workload from the fair-share scheduler. The scheduler's default behavior is to select the next workload by first identifying the group that has used the least amount of their allocation within the current scheduling window. If the selected group has more than one project, and both have workloads waiting to be executed, then the scheduler identifies the project that has used the least of their allocation within the scheduling window. Finally, if the selected project has submitted more than one workload, the scheduler will select the oldest workload first. Thus, within a project, the scheduler works on a first-in-first-out (FIFO) basis.

A wait-time estimate is provided through IBM Quantum Platform. The computed time is the result of a scheduling simulation that predicts one possible execution pattern, given the current fair-share ordering of all the workloads waiting for that QPU and the approximate runtime of each workload. The dynamic nature of the fair-share scheduler means that this estimated time is not fixed and can vary, sometimes dramatically. This wait time is also subject to limitations inherent in estimating the execution time for Qiskit Runtime workloads. For these workloads, where an accurate estimation of time is not feasible, the maximum allowed runtime is used as a proxy. In practice, this means that the duration for a Qiskit Runtime workload can be over-estimated by up to eight hours, the maximum allowed Qiskit Runtime workload duration for Premium Plan users.

Your workload's position in the queue is listed in theQueue positioncolumn on theWorkloads page.

On this page

© IBM Corp., 2017-2025


---

# Manage cost on the Standard Plan







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The IBM Cloud® Quantum Standard plan is not free, except when running jobs on simulators. Use the information in this topic to help you understand how much you’re paying and how to limit your costs.

Learn how to limit your costs when using the Standard Plan on IBM Quantum Platform.

Thecost limitorinstance limitrefers to the total cost of all jobs run with this instance since it was created, and it will always be greater than or equal to the total cost. After the instance reaches the specified number of total seconds, no further jobs can be run and no more cost is incurred.

The cost limit is always specified in US dollars (USD), then converted to runtime seconds. However, for monthly billing purposes, you are charged in your local currency, specified on your IBM Cloud® account. Because currency exchange rates can fluctuate, the cost for X runtime seconds might be different when initially calculated in USD than when you’re actually charged in your local currency. As a result, if your local currency is not USD, the total amount charged for the number of seconds specified in this field could vary from the dollar amount you specify.

An instance administrator can limit how much is spent. There are several ways to set or change this limit:

IBM Quantum Platform: Open theInstances & allocation tab.Find the instance you want to limit, click the overflow menu at the end of the row, and then clickEdit details. Set the total cost limit or the usage limit, then clickSave changes.

You can also set the cost or usage limit when creating a new Standard Plan instance.

API: Set the instance limit in seconds.

IBM Cloud CLI: For instructions to use the CLI, refer toGetting started with the IBM Cloud CLI.

Log in to the CLI:ibmcloud login --sso.

Establish the API:ibmcloud api cloud.ibm.com.

Update an instance's cost limit:

where:

<instance_CRN> is the CRN of the instance you want to update. You can get it from theIBM Quantum Platform dashboard.

<seconds> is the maximum number of seconds that can be consumed by the instance. For example, to establish a limit of 1000 seconds ($1600), enter this command:

View the instance details to verify that it was updated:

This command returns the information in JSON.  For example:

There are several ways to view the current cost limit:

IBM Quantum Platform: The Max cost limit is shown on the Standard tab of theInstances & allocation tab.

API:

IBM Cloud CLI: For instructions to use the CLI, refer toGetting started with the IBM Cloud CLI.

An instance administrator can remove the cost limit in several ways:

IBM Quantum Platform: Open theInstances & allocation tab.Find the instance you want to update, click the overflow menu at the end of the row, and then clickEdit details. Delete the total cost limit or the usage, then clickSave changes.

API: Set the instance limit tonull.

IBM Cloud CLI: For instructions to use the CLI, refer toGetting started with the IBM Cloud CLI.

When the instance’s cost limit is reached, the currently running job is stopped. Its status is set to Canceled with a reason of Ran too long. Any available partial results are kept.

No further jobs can be submitted by using this instance until the cost limit is increased.

You are sent a monthly invoice that provides details about your resource charges. You can check how much has been spent at any time on theIBM Cloud Billing and usage page.

Additionally, you can determine cost per instance or per job at any time.

To view the instance's usage, follow the instructions in theanalyticsguide.

On the Standard Plan, you can set up spending notifications to get notified when your account or a particular service reaches a specific spending threshold that you set. For information, see theIBM Cloud account Type description. IBM Cloud spending notifications must be used with other methods of cost management for several reasons:

On this page

© IBM Corp., 2017-2025


---

# Visualize circuits







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

It's often useful to see the circuits you're creating. Use the following options to display Qiskit circuits.

TheQuantumCircuitclass supports drawing circuits through thedraw()method, or by printing the circuit object. By default, both render an ASCII art version of the circuit diagram.

Note thatprintreturnsNonebut has the side effect of printing the diagram, whereasQuantumCircuit.drawreturns the diagram with no side effects. Since Jupyter notebooks display the output of the last line of each cell, they appear to have the same effect.

Output:

Output:

A text output is useful for quickly seeing the output while developing a circuit, but it doesn't provide the most flexibility. There are two alternative output renderers for the quantum circuit. One usesMatplotliband the other usesLaTeX. The LaTeX renderer requires theqcircuit package. Select these renderers by setting the "output" argument to the stringsmplandlatex.

OSX users can get the required LaTeX packages through themactex package.

Output:

Output:

By default, thedraw()method returns the rendered image as an object and does not output anything. The exact class returned depends on the output specified:'text'(the default) returns aTextDrawerobject,'mpl'returns amatplotlib.Figureobject, andlatexreturns aPIL.Imageobject. Jupyter notebooks understand these return types and render them properly, but when running outside of Jupyter, images will not display automatically.

Thedraw()method has optional arguments to display or save the output. When specified, thefilenamekwarg takes a path to which it saves the rendered output. Alternatively, if you're using themplorlatexoutputs, you can use theinteractivekwarg to open the image in a new window (this will not always work from within a notebook).

Depending on the output, there are also options to customize the circuit diagram.

The first two options are shared among all three backends. They allow you to configure both the bit orders and whether or not you draw barriers. These can be set by thereverse_bitskwarg andplot_barrierskwarg, respectively. The following examples work with any output renderer;mplis used here for brevity.

Output:

Output:

Output:

Some available customizing options are specific to a renderer.

Thefoldargument sets a maximum width for the output. In thetextrenderer, this sets the length of the lines of the diagram before it is wrapped to the next line.  When using the 'mpl' renderer, this is the number of (visual) layers before folding to the next line.

Themplrenderer has thestylekwarg, which changes the colors and outlines. See theAPI documentationfor more details.

Thescaleoption scales the output of themplandlatexrenderers.

Output:

Output:

Output:

If you have an application where you prefer to draw a circuit with a self-contained function instead of as a method of a circuit object, you can directly use thecircuit_drawer()function, which is part of the public stable interface fromqiskit.visualization. The function behaves identically to thecircuit.draw()method, except that it takes in a circuit object as a required argument.

Output:

On this page

© IBM Corp., 2017-2025


---

# Plot quantum states







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

In many situations – such as learning or debugging – it's helpful to visualize the state of a quantum computer. Here we assume you already have a particular state from simulation or state tomography.  It's only possible to view the states of small quantum systems.

All functions on this page return rich objects. When the last line of a code cell outputs these objects, Jupyter notebooks display them below the cell. If you call these functions in some other environments or in scripts, you will need to explicitly show or save the outputs.

Most functions return images, which arematplotlib.Figureobjects. Two options are:

The LaTeX outputs areIPython.display.Latexobjects. The best option in a non-Jupyter environment is to avoid this output by either printing the state for a text representation, or switching to thelatex_sourcedrawer to return a LaTeX source string.

A quantum state is either a density matrixρ\rhoρ(Hermitian matrix) or statevector∣ψ⟩|\psi\rangle∣ψ⟩(complex vector). The density matrix is related to the statevector by

ρ=∣ψ⟩⟨ψ∣,\rho = |\psi\rangle\langle \psi|,ρ=∣ψ⟩⟨ψ∣,

and is more general, as it can represent mixed states (positive sum of statevectors)

ρ=∑kpk∣ψk⟩⟨ψk∣.\rho = \sum_k p_k |\psi_k\rangle\langle \psi_k |.ρ=∑k​pk​∣ψk​⟩⟨ψk​∣.

Qiskit represents quantum states through theStatevectorandDensityMatrixclasses and provides many visualization functions. See the sections after the following the code cell to see how Qiskit's different visualization functions plot the following quantum state.

While not technically a "plot", Qiskit can render LaTeX representations of bothStatevectorandDensityMatrixobjects that display nicely in Jupyter notebooks. These follow the standard mathematical conventions for writing down quantum states. Read more inBasics of quantum information: Single systems.

Statevectors default to "ket notation", whereas density matrices are displayed as a 2×2 matrix.

Output:

22∣00⟩+12∣01⟩−i2∣11⟩\frac{\sqrt{2}}{2} |00\rangle+\frac{1}{2} |01\rangle- \frac{i}{2} |11\rangle22​​∣00⟩+21​∣01⟩−2i​∣11⟩

Output:

You can also replace"latex"with"latex_source"to get the raw LaTeX string.

This plot displays the real and imaginary parts of each density matrix element in two three-dimensional bar charts.  It's called a "city" plot because the bars resemble skyscrapers in a city. The state we're plotting has the following density matrix.

Output:

See theAPI documentationfor more information.

This plot is very similar to the "city" plot, but the magnitude of each element is represented by the size of a square rather than the height of a bar. White squares represent elements with positive values, and black squares represent elements with negative values. The state we're plotting has the following density matrix.

Output:

See theAPI documentationfor more information.

An observable is a way of measuring a quantum state such that the possible measurement outcomes are real numbers. The expected value of the outcome is also known as the expectation value of the observable on that state, and it can be thought of as the average of infinitely many observations of that state.

Tensor products of Pauli matrices are all observables that return +1 or -1. This plot displays the expectation values of the state on different Pauli operators as a bar chart. All density matrices can be written as a sum of these Pauli matrices, weighted by their expectation values.

For example, this state can be written as the sum of terms:

Output:

You can also calculate these coefficients usingSparsePauliOp.

Output:

See theAPI documentationfor more information.

The "QSphere" is a Qiskit-unique view of a quantum state in which the amplitude and phase of each element in a statevector is plotted on the surface of a sphere. The thickness of each dot represents the amplitude, and the color represents the phase. For mixed states it will show a sphere for each component.

Output:

See theAPI documentationfor more information.

The Bloch vector of a qubit state is its expectation value in the X, Y, and Z Pauli observables mapped to the X, Y, and Z axes in three-dimensional space. This plot projects multi-qubit quantum states onto the single-qubit space and plots each qubit on a Bloch sphere. This visualization only shows the expectation values of individual qubits. It can't show correlations between qubits and so can't fully describe entangled quantum states.

Output:

See theAPI documentationfor more information.

All state-plotting functions accept the following arguments (except the LaTeX drawer, which doesn't return a Matplotlib figure, andplot_state_qsphere, which only acceptsfigsize):

Theplot_state_cityandplot_state_paulivecfunctions also accept acolorargument (list of strings) specifying the colors of the bars. See theAPI documentationfor more information.

Can't remember the name of the plotting function you need? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

On this page

© IBM Corp., 2017-2025


---

# Visualize results







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Theplot_histogramfunction visualizes the result of sampling a quantum circuit on a QPU or simulator.

This function returns amatplotlib.Figureobject. When the last line of a code cell outputs these objects, Jupyter notebooks display them below the cell. If you call these functions in some other environments or in scripts, you will need to explicitly show or save the outputs.

Two options are:

For example, make a two-qubit Bell state:

Output:

Output:

Use the following options forplot_histogramto adjust the output graph.

Output:

Qiskit does not have a built-in function for plotting Estimator results, but you can use Matplotlib'sbarplotfor a quick visualization.

To demonstrate, the following cell estimates the expectation values of seven different observables on a quantum state.

Output:

The following cell uses the estimatedstandard errorof each result and adds them as error bars. See thebarplot documentationfor a full description of the plot.

Output:

On this page

© IBM Corp., 2017-2025


---

# What is Qiskit Serverless?







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit Serverless provides a simple interface to run workloads across quantum-classical resources. This includes deploying programs to the IBM Quantum® Platform and running workloads remotely, as well as easy resource management for multi-cloud and quantum-centric supercomputing use cases.

Premium users can build, deploy, and run their workloads remotely on classical compute made available through IBM Quantum Platform. Try out the tutorials inIBM Quantum Learning(note: these are accessible in the Premium Plan once you have logged into your IBM Quantum account).

This is an experimental feature available only for IBM Quantum Premium Plan users.

Qiskit Serverless helps manage classical and quantum resources across the entireQiskit patternworkflow. This includes some of the following examples:

To use Qiskit Serverless on IBM Quantum Platform, install the following packages:

qiskit_ibm_catalogprovides the client-side tools to upload and run remote programs, whileqiskit_serverlessprovides server-side tools to distribute compute and manage data. These packages requirepython3.11+. For users and organizations who want to run Qiskit Serverless on custom infrastructure, follow theCloud infrastructure setupguide.

Currently, the IBM Quantum workloads table only reflects Qiskit Runtime workloads. Usejob.status()to see your Qiskit Serverless workload's current status.

Explore how towrite your first Qiskit Serverless program.

On this page

© IBM Corp., 2017-2025


---

# Write your first Qiskit Serverless program







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This example demonstrates how to useqiskit-serverlesstools to create a parallel transpilation program, and then implementqiskit-ibm-catalogto deploy your program to IBM Quantum Platform to use as a reusable remote service.

Start with the following example that transpiles acircuitagainst a givenbackendand targetoptimization_level, and gradually add more elements to deploy your workload to Qiskit Serverless.

Put the following code cell in the file./source_files/transpile_remote.py. This file is the program to upload to Qiskit Serverless.

Qiskit Serverless requires setting up your workload’s.pyfiles into a dedicated directory. The following structure is an example of good practice:

Serverless uploads the contents ofsource_filesto run remotely. Once these are set up, you can adjusttranspile_remote.pyto fetch inputs and return outputs.

Your initialtranspile_remote.pyhas three inputs:circuits,backend_name, andoptimization_level. Serverless is currently limited to only accept serializable inputs and outputs. For this reason, you cannot pass inbackenddirectly, so usebackend_nameas a string instead.

At this point, you can get your backend withQiskitRuntimeServiceand add your existing program with the following code. The following code requires that you have alreadysaved your credentials.

Finally, you can runtranspile_remote()across allcircuitspassed in, and return thetranspiled_circuitsas a result:

The previous section created a program to be run remotely. The code cells in this section upload that program to Qiskit Serverless.

Useqiskit-ibm-catalogto authenticate toQiskitServerlesswith your API key, which you can find in yourIBM Quantum account, and upload the program.

You can usesave_account()to save your credentials (See the "Authenticate to the service" step in theSet up to use IBM Quantum Platformsection). Note that this writes your credentials to the same file asQiskitRuntimeService.save_account().

Qiskit Serverless compresses the contents ofworking_dir(in this case,source_files) into atar, which is uploaded and cleaned up after. Theentrypointidentifies the main program executable for Qiskit Serverless to run. Additionally, if your program has custompipdependencies, you can add them to adependenciesarray:

Output:

To check if it successfully uploaded, useserverless.list():

Output:

On this page

© IBM Corp., 2017-2025


---

# Run your first Qiskit Serverless workload remotely







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This section explores how to useqiskit-ibm-catalogto list programs available in Qiskit Serverless, pass inputs into these programs, run them remotely, check their status, and retrieve results and logs.

Be sure you have authenticated to Qiskit Serverless with yourIBM Quantum account(seeDeploy to IBM Quantum Platformfor instructions).

You can useQiskitServerless.list()to fetch a list of the available programs to run with Qiskit Serverless. This includes the previously uploadedtranspile_remote_serverless.

Output:

First, set up your inputs. Your program has three inputs:circuits,backend, andoptimization_level. You can userandom_circuitto create 30 random circuits:

Output:

Next, useQiskitRuntimeServiceandleast_busyto select abackend:

Set your optimization level:

Select your program withserverless.load('PROGRAM_NAME'):

Next, pass your inputs and run it in a pythonic fashion as follows:

Output:

With your Qiskit Serverlessjob_id, you can check the status of running jobs. This includes the following statuses:

You can also set more detailed job statuses inManage Qiskit Serverless compute and data resources.

Output:

Currently, the IBM Quantum workloads table only reflects Qiskit Runtime workloads. Usejob.status()to see your Qiskit Serverless workload's current status.

You've successfully run your first Qiskit Serverless program!

As mentioned before, once a program isRUNNING, you can usejob.logs()to fetch logs created fromprint()outputs:

Output:

At any time, you can also cancel a job:

Output:

Once a program isDONE, you can usejob.results()to fetch the result stored insave_result():

Output:

You can usejobs()to list all jobs submitted to Qiskit Serverless:

Output:

On this page

© IBM Corp., 2017-2025


---

# Manage Qiskit Serverless compute and data resources







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

With Qiskit Serverless, you can manage compute and data across yourQiskit pattern, including CPUs, QPUs, and other compute accelerators.

Serverless workloads have several stages across a workflow. By default, the following statuses are viewable withjob.status():

You can also set custom statuses that further describe the specific workflow stage, as follows.

After successful completion of this workload (withsave_result()), this status will be updated toDONEautomatically.

For classical tasks that can be parallelized, use the@distribute_taskdecorator to define compute requirements needed to perform a task. Start by recalling thetranspile_remote.pyexample from theWrite your first Qiskit Serverless programtopic with the following code.

The following code requires that you have alreadysaved your credentials.

In this example, you decorated thetranspile_remote()function with@distribute_task(target={"cpu": 1}). When run, this creates an asynchronous parallel worker task with a single CPU core, and returns with a reference to track the worker. To fetch the result, pass the reference to theget()function. We can use this to run multiple parallel tasks:

You can flexibly allocate CPU, GPU, and memory for your tasks via@distribute_task(). For Qiskit Serverless on IBM Quantum® Platform, each program is equipped with 16 CPU cores and 32 GB RAM, which can be allocated dynamically as needed.

CPU cores can be allocated as full CPU cores, or even fractional allocations, as shown in the following.

Memory is allocated in number of bytes. Recall that there are 1024 bytes in a kilobyte, 1024 kilobytes in a megabyte, and 1024 megabytes in a gigabyte. To allocate 2 GB of memory for your worker, you need to allocate"mem": 2 * 1024 * 1024 * 1024.

On this page

© IBM Corp., 2017-2025


---

# Port code to Qiskit Serverless







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The following example demonstrates how to port existing code to leverage Qiskit Serverless.

The following code assumes that you have saved your credentials. If you have not, follow the instructions inSet up an IBM Quantum channelto authenticate with your API key.

Follow the instructions on theIntroduction to Qiskit Functionspage to authenticate with your API key.

Output

Output

On this page

© IBM Corp., 2017-2025


---

# Build a function template for Hamiltonian simulation







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

By now you've seen a basic example of how to get started writing, uploading, and running a program with Qiskit Serverless. If you haven't, start withWhat is Qiskit Serverless?for some background information first.

The workloads you are building for your own use cases are likely not as simple as the examples previously shown. For example, you might need to carefully consider what domain-level inputs and outputs are relevant for your application, how to make sure your program can be reusable across a range of those inputs, and what kind of information you need returned during the execution of the job so you can better evaluate the progress of your workload. You might even want to incorporate a "dry run" mode so you can test the impact of a set of particular inputs before sending the resulting circuits to hardware.

A function template is an example of a realistic workload that uses a specific application domain to contextualize these aspects. It is meant to be a starting point for you to modify for your own needs so you don't have to start from scratch.

This guide demonstrates creating a function template for addressing Hamiltonian simulation problems.

First, write a function template for Hamiltonian simulation that uses theAQC-Tensor Qiskit addonto map the problem description to a reduced-depth circuit for execution on hardware.

Throughout, the code is saved to./source_files/template_hamiltonian_simulation.py. This file is the function template you can upload to and run remotely with Qiskit Serverless.

Start by getting the inputs for the template. This example has domain-specific inputs relevant for Hamiltonian simulation (such as the Hamiltonian and observable) and capability-specific options (such as how much you want to compress the initial layers of the Trotter circuit using AQC-Tensor, or advanced options for fine-tuning error suppression and mitigation beyond the defaults that are part of this example).

When the function template is running, it is helpful to return information in the logs by using print statements, so that you can better evaluate the workload's progress. Following is a simple example of printing theestimator_optionsso  there is a record of the actual Estimator options used. There are many more similar examples throughout the program to report progress during execution, including the value of the objective function during the iterative component of AQC-Tensor, and the two-qubit depth of the final instruction set architecture (ISA) circuit intended for execution on hardware.

An important aspect of ensuring that the template can be reused across a range of inputs is input validation. The following code is an example of verifying that the stopping fidelity during AQC-Tensor has been specified appropriately and if not, returning an informative error message for how to fix the error.

First, prepare a dictionary to hold all of the function template outputs. Keys will be added to this dictionary throughout the workflow, and it is returned at the end of the program.

The AQC-Tensor optimization happens in step 1 of a Qiskit pattern.  First, a target state is constructed.  In this example, it is constructed from a target circuit that evolves the same Hamiltonian for the same time period as the AQC portion.  Then, an ansatz is generated from an equivalent circuit but with fewer Trotter steps.  In the main portion of the AQC algorithm, that ansatz is iteratively brought closer to the target state.  Finally, the result is combined with the remainder of the Trotter steps needed to reach the desired evolution time.

Note the additional examples of logging incorporated in the following code.

After the AQC portion of the workflow, thefinal_circuitistranspiled for the hardwareas usual.

If dry run mode has been selected, then the program is stopped before executing on hardware. This can be useful if, for example, you want first to inspect the two-qubit depth of the ISA circuit before deciding to execute on hardware.

This function template returns the relevant domain-level output for this Hamiltonian simulation workflow (expectation values) in addition to important metadata generated along the way.

The previous section created a program to be run remotely. The code in this section uploads that program to Qiskit Serverless.

Useqiskit-ibm-catalogto authenticate toQiskitServerlesswith your API key, which you can find in yourIBM Quantum® account, and upload the program.

You can optionally usesave_account()to save your credentials (see the"Authenticate to the service" step) in the Set up to use IBM Quantum Platform guide. Note that this writes your credentials to the same file asQiskitRuntimeService.save_account().

This program has custompipdependencies.  Add them to adependenciesarray when constructing theQiskitFunctioninstance:

Output:

To check if the program successfully uploaded, useserverless.list():

Output:

The function template has been uploaded, so you can run it remotely with Qiskit Serverless. First, load the template by name:

Next, run the template with the domain-level inputs for Hamiltonian simulation. This example specifies a 50-qubit XXZ model with random couplings, and an initial state and observable.

Output:

Check the status of the job:

Output:

After the job is running, you can fetch logs created from theprint()outputs. These can provide actionable information about the progress of the Hamiltonian simulation workflow. For example, the value of the objective function during the iterative component of AQC, or the two-qubit depth of the final ISA circuit intended for execution on hardware.

Output:

Block the rest of the program until a result is available. After the job is done, you can retrieve the results. These include the domain-level output of Hamiltonian simulation (expectation value) and useful metadata.

Output:

After the job completes, the entire logging output will be available.

Output:

For a deeper dive into the AQC-Tensor Qiskit addon, check out theImproved Trotterized Time Evolution with Approximate Quantum Compilationtutorial or theqiskit-addon-aqc-tensor repository.

Here is the entire source of./source_files/template_hamiltonian_simulation.pyas one code block.

On this page

© IBM Corp., 2017-2025


---

# Qiskit addons







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit addons are a collection of research capabilities for enabling algorithm discovery at the utility scale. These capabilities build on Qiskit's performant foundation of tools for creating and running quantum algorithms. They are provided as modular software components that can plug into aworkflowto scale or design new quantum algorithms.

Approximate quantum compilation with tensor networks (AQC-Tensor) enables the construction of high-fidelity circuits with reduced depth.

Multi-product formulas (MPF) reduce the Trotter error of Hamiltonian dynamics through a weighted combination of several circuit executions.

Operator backpropagation (OBP) reduces circuit depth by trimming operations from the end at the cost of more operator measurements.

Circuit cutting reduces the depth of transpiled circuits by decomposing entangling gates between non-adjacent qubits.

Sample-based quantum diagonalization (SQD) classically post-processes noisy quantum samples to yield more accurate eigenvalue estimations of quantum system Hamiltonians, for example in chemistry applications.

On this page

© IBM Corp., 2017-2025


---

# Qiskit addon utilities







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The Qiskit addon utilities package is a collection of functionalities to supplement workflows involving one or more Qiskit addons. For example, this package contains functions for creating Hamiltonians, generating Trotter time-evolution circuits, and slicing and combining quantum circuits.

There are two ways to install the Qiskit addon utilities: PyPI and building from source. It is recommended to install these packages in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install the Qiskit addon utilities package is via PyPI.

Click here to read how to install this package manually.

If you wish to contribute to this package or want to install it manually, first clone the repository:

and install the package viapip. If you plan to run the tutorials found in the package repository, install the notebook dependencies as well. If you plan to develop in the repository, install thedevdependencies.

There are several modules within theqiskit-addon-utilspackage, including one for problem generation for simulating quantum systems, graph coloring to more efficiently place gates in a quantum circuit, and circuit slicing, which can help withoperator backpropagation. The following sections summarize each module. The package'sAPI documentationalso contains helpful information.

The contents of theqiskit_addon_utils.problem_generatorsmodule include:

H=∑(j,k)∈E(JxXjXk+JyYjYk+JzZjZk)+∑j∈V(hxXj+hyYj+hzZj)H = \sum_{(j,k)\in E} \left(J_x X_jX_k + J_yY_jY_k + J_zZ_jZ_k\right) + \sum_{j\in V} \left(h_x X_j + h_y Y_j + h_z Z_j\right)H=∑(j,k)∈E​(Jx​Xj​Xk​+Jy​Yj​Yk​+Jz​Zj​Zk​)+∑j∈V​(hx​Xj​+hy​Yj​+hz​Zj​)

Theqiskit_addon_utils.coloringmodule is used to color the edges in a coupling map and use this coloring to more efficiently place gates in a quantum circuit. The purpose of this edge-colored coupling map is to find a set of edge colors such that no two edges of the same color share a common node. For a QPU, this means that gates along like-colored edges (qubit connections) can be run simultaneously and the circuit will execute faster.

As a quick example, you can use theauto_color_edges()function to generate an edge coloring for a naive circuit executing aCZGatealong each qubit connection. The code snippet below uses theFakeSherbrookebackend's coupling map, creates this naive circuit, then uses theauto_color_edges()function to create a more efficient equivalent circuit.

Output:

Lastly, theqiskit-addon-utils.slicingmodule contains functions and transpiler passes to work with creating circuit "slices", time-like partitions of aQuantumCircuitspanning across all qubits. These slices are primarily used foroperator backpropagation. The main four ways a circuit can be sliced are by gate type, depth, coloring, orBarrierinstructions. The output of these slicing functions returns a list ofQuantumCircuits. Sliced circuits can also be recombined using thecombine_slices()function. Read the module'sAPI referencefor more information.

Below are a few examples of how to create these slices using the following circuit:

Output:

In the case where there is no clear way to exploit the structure of a circuit for operator backpropagation, you can partition the circuit into slices of a given depth.

Output:

In cases such as when executing Trotter circuits to model the dynamics of a quantum system, it may be advantageous to slice by gate type.

Output:

If your workload is designed to exploit the physical qubit connectivity of the QPU it will be run on, you can create slices based on edge coloring. The code snippet below will assign a three-coloring to circuit edges and slice the circuit with respect to the edge coloring. (Note: this only affects non-local gates. Single-qubit gates will be sliced by gate type).

Output:

If you have a custom slicing strategy, you can instead place barriers in the circuit to delineate where it should be sliced and use theslice_by_barriersfunction.

Output:

Once the barriers are in place, you can examine each of the slices individually.

Output:

Output:

Output:

On this page

© IBM Corp., 2017-2025


---

# Sample-based quantum diagonalization (SQD) overview







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Sample-based quantum diagonalization (SQD) is a classicalpost-processingtechnique which acts on samples obtained from a quantum circuit after execution on a QPU. It is useful for finding eigenvalues and eigenvectors of quantum operators, such as the Hamiltonian of a quantum system, and uses quantum and distributed classical computing together. This post-processing technique may be especially useful for users simulating chemical or other quantum systems.

Classical computing is used to process samples obtained from a quantum processor, and to project and diagonalize a target Hamiltonian in a subspace spanned by them. This allows SQD to be robust to samples corrupted by quantum noise and manage large Hamiltonians, such as chemical systems with millions of interacting terms, beyond the reach of exact diagonalization methods.

The SQD tool can target Hamiltonians expressed as linear combinations of Pauli operators or second-quantized Fermionic operators. The input samples are obtained by quantum circuits defined by the user, which are believed to be good representations of eigenstates (for example, the ground state) of a target operator. The convergence rate of SQD as a function of the number of samples improves with the sparseness of the target eigenstate.

There are two ways to install the SQD package: PyPI and building from source. It is recommended to install these packages in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install theqiskit-addon-sqdpackage is via PyPI.

Click here to read how to install this package manually

If you wish to contribute to this package or want to install it manually, first clone the repository:

and install the package viapip. The repository also contains example notebooks that you can run. If you plan on developing in the repository, you can install thedevdependencies.

Adjust the options to suit your needs.

The SQD workflow using self-consistent configuration recovery is explained in detail in[1]. This section provides an overview to the technique depicted in the following diagram.

HereXˉ\bar{\mathcal{X}}Xˉis a set of noisy samples which contain, in the context of the Hamiltonian being simulated, physical and non-physical configurations (represented as bitstrings) obtained from execution on a QPU. The non-physical configurations are due to noise and can be processed by thesqd.configuration_recovery.recover_configurations()method to refine the samples into a new setXR\mathcal{X}_RXR​.

From this set, batches of configurationsS(1)...S(K)\mathcal{S}^{(1)}...\ \mathcal{S}^{(K)}S(1)...S(K)are collected according to a distribution proportional to the empirical frequencies of eachx\mathbf{x}xinXR\mathcal{X}_RXR​. Each batch of sampled configurations spans a subspace,S(k):k=1,...,K\mathcal{S}^{(k)}: k = 1, ..., KS(k):k=1,...,K, in which the Hamiltonian is projected and diagonalized:

H^S(k)=P^S(k)H^P^S(k), withP^S(k)=∑x∈S(k)∣x⟩⟨x∣,\hat{H}_{S^{(k)}} = \hat{P}_{\mathcal{S}^{(k)}}\hat{H}\hat{P}_{\mathcal{S}^{(k)}}\text{, with } \hat{P}_{\mathcal{S}^{(k)}} = \sum_{\mathbf{x} \in \mathcal{S}^{(k)}} |\mathbf{x}\rangle\langle\mathbf{x}|,H^S(k)​=P^S(k)​H^P^S(k)​, withP^S(k)​=∑x∈S(k)​∣x⟩⟨x∣,

whereH^S(k)\hat{H}_{\mathcal{S}^{(k)}}H^S(k)​is the Hamiltonian of a given subspace.

The bulk of the SQD workflow lies here wherein each of these subspace Hamiltonians is diagonalized. The ground states obtained from each of these subspaces,∣ψ(k)⟩|\psi^{(k)}\rangle∣ψ(k)⟩, are used to produce an estimate of a reference vector of occupanciesn(K)\mathbf{n}^{(K)}n(K)averaged over each of theKKKsubspaces. A new set of configurationsXR\mathcal{X}_RXR​is then generated by probabilistically flipping individual bits based on this average occupation and the known total number of particles (Hamming weight) in the system. This configuration recovery process is then repeated by preparing a new set of subspaces to diagonalize, obtaining new eigenstates and averaged orbital occupancy, and generating a new set of configurations. This loop is iterated until a user-specified criterion is met, and the overall process is analogous to filtering a noisy signal to improve its fidelity.

[1] Robledo-Moreno, Javier, et al."Chemistry beyond exact solutions on a quantum-centric supercomputer"arXiv preprint arXiv:2405.05068 (2024).

On this page

© IBM Corp., 2017-2025


---

# Getting started with Sample-based quantum diagonalization (SQD)







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This example uses thepyscfpackage, a Python-based chemistry simulation library, which is not natively supported on Windows; therefore, the examples below will not work.

In order to execute the code snippets below, Windows users need to create a Python environment using the Windows Subsystem for Linux, as suggested in thepyscfinstall guide.

This guide demonstrates a simple working example to get started with theqiskit-addons-sqdpackage. In this example, you can use SQD to obtain an approximation of the ground state of theN2N_2N2​molecule at equilibrium.

To begin, recall that the generic interacting-electron Hamiltonian has the form:

H^=∑prσhpra^pσ†a^rσ+∑prqsστ12(pr∣qs)a^pσ†a^qτ†a^sτa^rσ\hat{H} = \sum_{\substack{pr\\ \sigma}}h_{pr} \hat{a}_{p\sigma}^\dagger \hat{a}_{r\sigma} + \sum_{\substack{prqs\\ \sigma\tau}} \frac{1}{2}\left(pr|qs\right)\hat{a}_{p\sigma}^\dagger \hat{a}_{q\tau}^\dagger \hat{a}_{s\tau}\hat{a}_{r\sigma}H^=∑prσ​​hpr​a^pσ†​a^rσ​+∑prqsστ​​21​(pr∣qs)a^pσ†​a^qτ†​a^sτ​a^rσ​

wherea^pσ†\hat{a}_{p\sigma}^\daggera^pσ†​anda^pσ\hat{a}_{p\sigma}a^pσ​are the Fermionic creation and annihilation operators associated with theppp-th orbital with spinσ\sigmaσandhprh_{pr}hpr​and(pr∣qs)\left(pr|qs\right)(pr∣qs)are the one and two-body electronic integrals.

To begin, specify the molecule and its properties usingpyscfand the electronic integrals stored inn2_fci.txt.

This example ingests pre-generated data in a file calledn2_fci.txt, which contains one- and two-body electronic integrals. To run the code cells below on a local machine, copy and paste the data into a file with the same name. This example also requires thepyscfpackage to be installed.

Click here to examine the orbital information used to generate the ansatz.

Output:

Once the molecule information has been loaded in, you should specify an ansatz circuit and optimize it for execution. This involves considering any symmetries of your problem, the choice of ansatz, and optimize it to run on quantum hardware.

However, these choices are problem specific and out of scope for this guide. Instead, to demonstrate the SQD workflow, we will generate a random set of counts for the configuration recovery loop to post-process. This simulates the measurement data of a 32-qubit circuit sampled with 10,000 shots. After the count data has been generated, therecover_configurations()method requires that you convert the count data into a matrix of the bitstrings measured at each shot, as well as an array of probabilities for each state that was measured.

The artificial generation of samples is only used as a means to demonstrate the tooling ofqiskit-addon-sqd. The package is meant to be used as part of a larger workflow wherein an ansatz or other circuit is defined, optimized, and executed using the Sampler primitive. The code cell below contains commented-out code demonstrating what a typical workflow might look like given a circuit ansatz transpiled to an ISA circuit.

The measurement samples can then be refined by repeating the configuration recovery and diagonalizing sets of subsamples to approximate the ground state until convergence.

First, specify the following options:

Next, in order to plot the convergence, define arrays to store the approximation of the ground state energy, expectation value of the⟨S⟩2\langle S \rangle ^2⟨S⟩2, and the orbital occupancy of the molecule.

Now, run the configuration recovery loop. Each loop consists of three steps:

It is important to note how to address the first iteration of the configuration recovery loop. Since the average orbital occupancy is not yet available, only thepostselect_and_subsample()function is called. This removes any non-physical samples (samples with incorrect Hamming weight) before running the eigenstate solver,solve_fermion(). Afterward, the average orbital occupation is calculated across all batches and used as input to therecover_configurations()method, which flips individual bits probabilistically based on this average. See SectionII-Aof the supplementary information in theSQD paperfor more information.

Output:

Lastly, the results can be visualized by examining the approximated energy and average orbital occupancy at each iteration of the configuration recovery loop. The first plot shows that after a few iterations, the ground state energy is estimated to within approximately200 mH(chemical accuracy is typically accepted to be1 kcal/mol≈\approx≈1.6 mH). Recall that this demonstration used pure noise, and that the ability to approximate the energy to this degree comes from prior knowledge about the molecule and its electronic structure.

The second plot shows the average occupancy of each spatial orbital after the final iteration. Notice that both the spin-up and spin-down electrons occupy the first five orbitals with high probability in the solutions.

Output:

On this page

© IBM Corp., 2017-2025


---

# Approximate quantum compilation with tensor networks (AQC-Tensor)







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The Approximate quantum compilation with tensor networks (AQC-Tensor) Qiskit addon enables users to compile theinitial portionof a circuit into a nearly equivalent approximation of that circuit, but with much fewer layers. This is accomplished using tensor networks using the method described in[1]. Its primary utility is in circuits which simulate time evolution, but may be applicable to any class of circuits which has access to:

The technique generates an ansatz circuit based on a larger target circuit which a user ultimately wants to execute on a QPU. This is accomplished by first simulating some portion of the target circuit by tensor network methods and obtaining an accurate description of an intermediate state which the ansatz circuit will approximate. Once this intermediate state is found, it is used as a cost function in order to optimize the ansatz circuit's parameters. After the optimization is complete, the remaining portion of the target circuit is appended to the ansatz and then executed on quantum hardware.

There are two ways to install the AQC-Tensor package: PyPI and building from source. It is recommended to install these packages in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install the AQC-Tensor package is via PyPI. In order to use the package, you must also install at least one tensor network backend. The following code snippet will install the addon, along withquimb(for tensor network support) andjax(for automatic differentiation). If you are interested, check out the package onGitHub

Click here to read how to install this package manually.

If you wish to contribute to this package or want to install it manually, first clone the repository:

and install the package viapip. If you plan on running the tutorials found in the package repository, install the notebook dependencies as well. If you plan on developing in the repository, you may also want to install thedevdependencies.

The AQC-Tensor procedure is explained in detail in[1]. This section provides an overview of the technique.

In general, AQC-Tensor requires three things as input:

The technique is to then iteratively optimize the parameters of the ansatz circuit, such that the state it generates is as close to the target state as possible.

To generate (2) and (3) from the above list, theqiskit-addon-aqcpackage possesses a function,generated_ansatz_from_circuit()which will take an input circuit and outputs a parameterized ansatz and initial set of parameters. The parameters returned by the function are such that, when plugged into the ansatz, will generate a state that is exactly equivalent to the input circuit, up to a global phase.

The ansatz which is generated by this function uses 9 parameters per two-qubit block and is based on the KAK decomposition, which parametrizes any two-qubit gate in terms of three parameters, up to single-qubit rotations. The single-qubit rotations are then decomposed asZXZZXZZXZ, each of which has three parameters. This results in the ansatz circuit containing 3 parameters for each two-qubit block of the original circuit, plus 3 parameters for an outgoing single-qubit rotation on each of the two qubits (for a total of 9 parameters). After adding these blocks, the ansatz is completed by adding a layer of single-qubit rotations to each active qubit at the start of the circuit.

To obtain a description of the target state which is desired, this addon uses a matrix product state (the simplest form of a tensor network) and supports the following tensor-network simulators:

The most important parameter of a tensor network is its maximum bond dimension,χ\chiχ. This parameter limits how much entanglement can be represented with a tensor network, and thus to what depth a given circuit can be faithfully simulated.

Given a circuit withLLLqubits, a matrix-product state needs at most a bond dimension ofχexact=2L/2\chi_{exact} = 2^{L/2}χexact​=2L/2in order to exactly simulate the circuit toanydepth. This is out of reach for general utility-scale circuits acting on 100+ qubits. For this reason, if you are attempting to experiment with this addon for a toy-problem with few qubits, it is important to ensure thatχ<2L/2\chi < 2^{L/2}χ<2L/2. This way, when you scale the problem to a larger circuit, the target state remains classically simulable.

[1] Robertson, Niall F., et al."Approximate Quantum Compiling for Quantum Simulation: A Tensor Network based approach"arXiv preprint arXiv:2301.08609 (2023).

On this page

© IBM Corp., 2017-2025


---

# Getting started with Approximate quantum compilation with tensor networks (AQC-Tensor)







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This guide demonstrates a simple working example to get started with AQC-Tensor. In this example, you will take a Trotter circuit which simulates the evolution of a transverse field Ising model and use the AQC-Tensor method to reduce the resulting circuit depth. In addition, this example requires theqiskit-addon-utilspackage for the problem generator,qiskit-aerfor the tensor-network simulation, andscipyfor the parameter optimization.

To begin, recall that the Hamiltonian of the transverse field Ising model has the form

HIsing=∑i=1NJi,(i+1)ZiZi+1+hiXi\mathcal{H}_{Ising} = \sum_{i=1}^N J_{i,(i+1)}Z_iZ_{i+1} + h_i X_iHIsing​=∑i=1N​Ji,(i+1)​Zi​Zi+1​+hi​Xi​

where we'll assume periodic boundary conditions which imply that fori=10i=10i=10we obtaini+1=11→1i+1=11\rightarrow 1i+1=11→1andJJJis the coupling strength between two sites andhhhis the strength of the external magnetic field.

The following code snippet will generate the Hamiltonian of a 10-site Ising chain with periodic boundary conditions.

The overall goal of this example is to simulate time evolution of the model Hamiltonian. We do so here by Trotter evolution, which will be split into two portions.

We'll choose to evolve the system up to timetf=5t_f=5tf​=5and use AQC-Tensor to compress the time evolution up to timet=4t=4t=4, then evolve using ordinary Trotter steps up to timetft_ftf​.

From here we will next generate two circuits, one which will be compressed using AQC-Tensor and one which will be executed on a QPU. For the first circuit, since this will be simulated classically using matrix product states, we will use a generous number of layers to minimize Trotter error. Meanwhile the second circuit simulating time evolution fromti=4t_i=4ti​=4totf=5t_f=5tf​=5will use much fewer layers in order to minimize depth.

For comparison purposes, we will also generate a third circuit. One which evolves untilt=4t=4t=4, but which has the same number of layers as the second circuit evolving fromti=4t_i=4ti​=4totf=5t_f=5tf​=5. This is the circuit wewould haveexecuted has we not used the AQC-Tensor technique. We'll call this thecomparisoncircuit for now.

Next we will generate the ansatz we will optimize. It will evolve to the same evolution time as our first circuit (fromti=0t_i=0ti​=0totf=4t_f=4tf​=4), but with fewer Trotter steps.

Once the circuit has been generated, we then pass it to AQC-Tensor'sgenerate_ansatz_from_circuit()function which analyzes the two-qubit connectivity and returns two things. First is a generated ansatz circuit with the same two-qubit connectivity, and the second is a set of parameters which, when plugged into the ansatz, yield the input circuit.

Output:

Next we will build the MPS representation of the state to be approximated by AQC. We will also calculate the fidelity∣⟨ψ1∣ψ2⟩∣2|\langle\psi_1 | \psi_2 \rangle |^2∣⟨ψ1​∣ψ2​⟩∣2between the state prepared by the comparison circuit vs the one circuit which generates the target state (which used more Trotter steps).

Output:

Lastly, we will optimize the ansatz circuit such that it produces the target state better than ourcomparison_fidelity. The cost function to minimize will be theMaximizeStateFidelityand will be optimized using scipy's L-BFGS optimizer.

Output:

At this point we have a set of parameters which generate the target state with a higher fidelity than what the comparison circuit would have produced without using AQC. With these optimal parameters, the compressed circuit now has less Trotter errorandless depth than the original circuit.

As a final step, the following code snippet builds the full time evolution circuit which can be passed to a transpiler pipeline and executed on quantum hardware.

Output:

On this page

© IBM Corp., 2017-2025


---

# Operator backpropagation (OBP)







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Operator backpropagation (OBP) is a technique to reduce circuit depth by trimming operations from its end at the cost of more operator measurements. There are a number of ways in which operator backpropagation can be performed, and this package uses a method based on Clifford perturbation theory[1].

As one propagates an operator further through a circuit, the size of the observable to measure grows exponentially. This results in both a classical and quantum resource overhead. However, for some circuits, the resulting distribution of additional Pauli observables is more concentrated than the worst-case exponential scaling. This implies that some terms in an observable with small coefficients can be truncated to reduce the quantum overhead. The error incurred by doing so can be controlled to find a suitable tradeoff between precision and efficiency.

You can install the OBP package in one of two ways: via PyPI or building from source. Consider installing these packages in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install theqiskit-addon-obppackage is via PyPI.

Users who wish to contribute to this package or who want to install it manually may do so by first cloning the repository:

The OBP procedure implemented in this package is described in detail in[1]. When using the Estimator primitive, the output of a quantum workload is the estimation of one or more expectation values⟨O⟩\langle O \rangle⟨O⟩with respect to some state prepared using a QPU. This section summarizes the procedure.

First, start by writing the expectation value measurement of an observableOOOin terms of some initial state∣ψ⟩|\psi\rangle∣ψ⟩and a quantum circuitUQU_QUQ​:

⟨O⟩U∣ψ⟩=⟨ψ∣U†OU∣ψ⟩.\langle O \rangle_{U|\psi\rangle} = \langle\psi | U^\dagger O U |\psi \rangle.⟨O⟩U∣ψ⟩​=⟨ψ∣U†OU∣ψ⟩.

To distribute this problem across both classical and quantum resources, split the circuitUUUinto two subcircuits,UCU_CUC​andUQU_QUQ​, classically simulate the circuitUCU_CUC​, then execute the circuitUQU_QUQ​on quantum hardware and use the results of the classical simulation to reconstruct the measurement of the observableOOO.

The subcircuitUCU_CUC​should be selected to be classically simulable and will compute the expectation value

⟨O′⟩≡UC†OUC,\langle O' \rangle \equiv U_C^\dagger O U_C,⟨O′⟩≡UC†​OUC​,

which is the version of the initial operatorOOOevolved through the circuitUCU_CUC​. OnceO′O'O′has been determined, the quantum workload is prepared wherein the state∣ψ⟩|\psi\rangle∣ψ⟩is initiated, has the circuitUQU_QUQ​applied to it, and then measures the expectation valueO′O'O′. You can show that this is equivalent to measuring⟨O⟩\langle O \rangle⟨O⟩by writing:

⟨ψ∣UQ†O′UQψ⟩=⟨ψ∣UQ†UC†OUCUQψ⟩=⟨ψ∣U†OU∣ψ⟩=⟨O⟩U∣ψ⟩\langle \psi | U_Q^\dagger O' U_Q \psi \rangle = \langle \psi | U_Q^\dagger U_C^\dagger O U_CU_Q \psi \rangle = \langle\psi | U^\dagger O U |\psi \rangle = \langle O \rangle_{U|\psi\rangle}⟨ψ∣UQ†​O′UQ​ψ⟩=⟨ψ∣UQ†​UC†​OUC​UQ​ψ⟩=⟨ψ∣U†OU∣ψ⟩=⟨O⟩U∣ψ⟩​

Lastly, in order to measure the expectation value⟨O′⟩\langle O' \rangle⟨O′⟩, we must require it to be decomposable into a sum of Pauli strings

O′=∑PcPP,O' = \sum_P c_P P,O′=∑P​cP​P,

wherecPc_PcP​are real coefficients of the decomposition andPPPis some Pauli string composed ofIII,XXX,YYY, andZZZoperators. This ensures that you can reconstruct the expectation value ofOOOby

⟨ψ∣UQ†O′∣ψ⟩=∑PcP⟨ψ∣UQ†PUQ∣ψ⟩.\langle \psi | U_Q^\dagger O' |\psi \rangle = \sum_P c_P \langle \psi | U_Q^\dagger P U_Q | \psi \rangle.⟨ψ∣UQ†​O′∣ψ⟩=∑P​cP​⟨ψ∣UQ†​PUQ​∣ψ⟩.

This scheme offers a tradeoff between the required circuit depth ofUQU_QUQ​, the number of circuit executions on quantum hardware, and the amount of classical computing resources needed to computeO′O'O′. In general, as you choose to backpropagate further through a circuit, the number of Pauli strings to measure as well as the error-mitigation overhead both grow exponentially (alongside the classical resources needed to simulateUCU_CUC​).

Fortunately, the decomposition ofO′O'O′can often contain coefficients that are quite small and can be truncated from the final measurements used to reconstructOOOwithout incurring much error. Theqiskit-addon-obppackage possesses functionality to specify an error budget, which can automatically search for terms that can be truncated, to within some error tolerance.

Lastly, theqiskit-addon-obppackage approaches operator backpropagation based on Clifford perturbation theory. This method has the benefit that the overhead incurred by backpropagating various gates scales with the non-Cliffordness ofUCU_CUC​(i.e. how much of U C is comprised of non-Clifford instructions).

This approach to OBP begins by splitting the simulated circuit,UCU_CUC​, intoslices:

UC=∏s=1SUs=US...U2U1,U_C = \prod_{s=1}^S \mathcal{U}_s = \mathcal{U}_S...\mathcal{U}_2\mathcal{U}_1,UC​=∏s=1S​Us​=US​...U2​U1​,

whereSSSrepresents the total number of slices andUs\mathcal{U}_sUs​denotes a single slice of the circuitUCU_CUC​. Each of these slices are then analytically applied in sequence to measure the back propagated operatorO′O'O′and may or may not contribute to the overall size of the sum, depending on if the slice is a Clifford vs non-Clifford operation. If anerror budgetis allocated, truncation will then occur between the application of each slice.

[1] Fuller, Bryce, et al. "Improved Quantum Computation using Operator Backpropagation."arXiv:2502.01897 [quant-ph](2025).

On this page

© IBM Corp., 2017-2025


---

# Get started with OBP







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

When you prepare a quantum workload with operator backpropagation (OBP), first you must make a selection of "circuit slices", and second, you should specify a truncation threshold or "error budget" to remove terms with small coefficients in the backpropagated operator as well as set an upper bound to the overall size of the backpropagated operator. During backpropagation, the number of terms in the operator of anNNN-qubit circuit will approach4N4^N4Nquickly in the worst-case scenario. This guide demonstrates the steps involved in applying OBP to a quantum workload.

The main component of theqiskit-addons-obppackage is thebackpropagate()function. It ingests arguments for the final observable to reconstruct, a set of circuit slices to compute classically, and, optionally, aTruncationErrorBudgetorOperatorBudgetto provide constraints on the truncation that is done. Once these are specified, the classically computed backpropagated operatorO′O'O′is calculated iteratively by applying the gates from each slice,sss, in the following way:

O′(s)=US−s+1†O′(s−1)US−s+1O'^{(s)} = \mathcal{U}_{S-s+1}^\dagger O'^{(s-1)} \mathcal{U}_{S-s+1}O′(s)=US−s+1†​O′(s−1)US−s+1​

whereSSSis the total number of slices andUs\mathcal{U}_{s}Us​represents a single slice of the circuit. This example uses theqiskit-addons-utilspackage to prepare the circuit slices as well as generate the example circuit.

To begin, consider the time evolution of a Heisenberg XYZ chain. This Hamiltonian has the form

H^=∑(j,k)(JxXjXk+JyYjYk+JzZjZk)+∑j(hxXj+hyYj+hzZj)\hat{H} = \sum_{(j,k)} \left( J_xX_jX_k + J_yY_jY_k + J_z Z_jZ_k \right) + \sum_{j} \left(h_xX_j + h_yY_j + h_zZ_j\right)H^=∑(j,k)​(Jx​Xj​Xk​+Jy​Yj​Yk​+Jz​Zj​Zk​)+∑j​(hx​Xj​+hy​Yj​+hz​Zj​)

and the expectation value to measure will be⟨Z0⟩\langle Z_0 \rangle⟨Z0​⟩.

The following code snippet generates the Hamiltonian in the form of aSparsePauliOpby using theqiskit_addons_utils.problem_generatorsmodule and aCouplingMap. Set the coupling constants toJx=π/8J_x=\pi/8Jx​=π/8,Jy=π/4J_y=\pi/4Jy​=π/4,Jz=π/2J_z=\pi/2Jz​=π/2and external magnetic fields tohx=π/3h_x=\pi/3hx​=π/3,hy=π/6h_y=\pi/6hy​=π/6,hz=π/9h_z=\pi/9hz​=π/9, and then generate a circuit that models its time evolution.

Output:

Next, generate the circuit slices for backpropagation. In general, the choice of how to slice can have an impact on how well backpropagation performs for a given problem. Here, group gates of the same type into slices using theqiskit_addons_utils.slice_by_gate_typesfunction.

Output:

Once the slices have been generated, specify anOperatorBudgetto provide thebackpropagate()function with a condition to stop backpropagating the operator and prevent the classical overhead from growing further. You can also specify a truncation error budget for each slice wherein Pauli terms with small coefficients will be truncated from each slice until the error budget is filled. Any leftover budget will then be added to the following slice's budget.

Here, specify that backpropagation should stop when the number of qubit-wise commuting Pauli groups in the operator grows past888, and allocate an error budget of0.0050.0050.005for each slice.

In this step you will define the final observable to measure and run the backpropagation across each slice. Thebackpropagate()function returns three outputs: the backpropagated observable, the remaining circuit slices that were not backpropagated (and which should be run on quantum hardware), and metadata about the backpropagation.

Note that both theOperatorBudgetand theTruncationErrorBudgetare optional parameters for thebackpropagate()method. In general, the best choice for both should be heuristically chosen and requires some amount of experimentation. In this example we will backpropagate both with and without aTruncationErrorBudget.

By default,backpropagate()uses theL1L_1L1​norm of the truncated coefficients to bound the total error incurred from truncation, but otherLpL_pLp​can be used if you would like to modify how the truncation error is calculated.

Output:

Output:

The below code snippets backpropagates the circuitwitha truncation error budget.

Output:

Output:

Now that you have backpropagated the operator, you can execute the remaining portion of the circuit on a QPU. The quantum workload, using the Estimator, should include thebp_circuit_trunccircuit and must measure the backpropagated operatorbackpropagated_observable

To demonstrate the effectiveness of OBP on its own, the following code snippet transpiles both the original and backpropagated circuit (with and without truncation) and simulates the circuits classically using theStatevectorEstimator.

Output:

Lastly the following code snippet will transpile and execute the backpropagated circuit on a QPU (both with and without truncation).

Output:

On this page

© IBM Corp., 2017-2025


---

# Multi-product formulas (MPF)







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Multi-product formulas (MPF) can be used to more accurately simulate the dynamics of a quantum system, at the cost of increased circuit executions. This is a post-processing technique that mitigates the error of expectation values for time-evolved states.

Classical computing is used to solve a system of linear equations that provides coefficients to a weighted combination of several circuit executions. Using this weighted combination can reduce the error associated with simulating time evolution, given a good selection of Trotter steps. The MPF tool will ingest a selection of data --- including the number of Trotter steps and the order of the Trotter approximation --- to prepare and solve (or approximate the solution of) the associated system of linear equations, which you can then use to post-process expectation value measurements of a time-evolved state.

There are two ways to install the MPF package: via PyPI and building from source. It is recommended to install in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install theqiskit-addon-mpfpackage is via PyPI.

Users who wish to develop in the repository or who want to install it manually may do so by first cloning the repository:

and install the package viapip. The repository also contains a number of optional dependencies that enable certain features.

Adjust the options to suit your needs.

MPFs can reduce the Trotter approximation error associated with simulating the dynamics of quantum systems through a weighted combination of several circuit executions. This weighted sum is defined as:

μ(t)=∑jxjρjkj(tkj)+some remaining Trotter error,\mu(t) = \sum_j x_j\rho_j^{k_j}\left(\frac{t}{k_j}\right) + \text{some remaining Trotter error},μ(t)=∑j​xj​ρjkj​​(kj​t​)+some remaining Trotter error,

wherexjx_jxj​are the weighting coefficients,ρjkj\rho_j^{k_j}ρjkj​​is the density matrix that corresponds to the pure state obtained by evolving the initial state via a product formulaSkjS^{k_j}Skj​approximating the time-evolution operator usingkjk_jkj​Trotter steps, andjjjindexes each product formula used in the sum.

Generally, however, the goal of simulating quantum dynamics is to measure some observableO(t)\mathcal{O}(t)O(t), which is a function of time. When using MPFs, multiple circuits -- each usingkjk_jkj​Trotter steps -- are executed to obtain several measurements of the target observableOkj(t)\mathcal{O}_{k_j}(t)Okj​​(t). The measurement of the target observable is then obtained by computing:

⟨O(t)⟩=∑jxj(t)⟨Okj(t)⟩.\langle \mathcal{O}(t) \rangle = \sum_j x_j(t) \langle \mathcal{O}_{k_j}(t) \rangle.⟨O(t)⟩=∑j​xj​(t)⟨Okj​​(t)⟩.

In essence, you can reduce the overall Trotter error by approximating the time-evolution operator using several product formulas with a variable number of Trotter steps instead of a single product formula. You construct a circuit for each term in the weighted sum, which evolves the system according to each of thekjk_jkj​number of Trotter steps. Each circuit is then executed separately on a QPU to reconstruct the results in a post-processing step. The utility of this technique can be viewed from two perspectives:

The core functionality of theqiskit-addon-mpfpackage lies in determining the MPF coefficientsxj(t)x_j(t)xj​(t)(which may be time-dependent). The process to obtain eachxj(t)x_j(t)xj​(t)involves solving a system of linear equationsAx=bAx=bAx=bwherexxxis the vector of coefficients to be determined,AAAis a matrix that depends on each of thekjk_jkj​and the product formula usedSSS(as in, the approximation order and number of Trotter steps), andbbbis a vector of constraints. This system of equations can be solved either exactly or with an approximate model that minimizes the 1-norm of the coefficients. Additionally, the choice for eachkjk_jkj​is a heuristic process, but can be bounded by the following constraints:

On this page

© IBM Corp., 2017-2025


---

# 







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This guide demonstrates how to use theqiskit-addon-mpfpackage, using the time evolution of an Ising model as an example. With this package, you can build a Multi-Product Formula (MPF) that can achieve lower Trotter error on observable measurements. The tools provided allow you to determine the weights of a chosen MPF, which can then be used to recombine the estimated expectation values from several time evolution circuits, each with a different number of Trotter steps.

Begin by considering the Hamiltonian of an Ising model with 10 sites:

HIsing=∑i=19Ji,(i+1)ZiZi+1+∑i=110hiXiH_{\text{Ising}} = \sum_{i=1}^9 J_{i,(i+1)}Z_iZ_{i+1} + \sum_{i=1}^{10} h_i X_iHIsing​=∑i=19​Ji,(i+1)​Zi​Zi+1​+∑i=110​hi​Xi​

whereJi,(i+1)J_{i,(i+1)}Ji,(i+1)​is the coupling strength andhih_ihi​is an external magnetic field strength. To set up the problem, the observable to measure will be the total magnetization of the system

⟨M⟩=∑i=110⟨Zi⟩.\langle M \rangle = \sum_{i=1}^{10} \langle Z_i \rangle.⟨M⟩=∑i=110​⟨Zi​⟩.

The code snippet below prepares the Hamiltonian of the Ising chain using theqiskit-addon-utilspackage, and defines the observable that will be measured.

Output:

Next you prepare the MPF. The first choice to make is whether the coefficients will be static (time-independent) or dynamic; this tutorial uses a static MPF. The next choice to make is the set ofkjk_jkj​values. This determines how many terms will be in the MPF, as well as how many Trotter steps each term uses to simulate the time evolution. The choice ofkjk_jkj​values is heuristic, so you need to obtain your own set of "good"kjk_jkj​values. Read guidelines on finding a good set of values at the end of thegetting started page.

Then, once thekjk_jkj​values are determined, you can prepare the system of equations,Ax=bAx=bAx=b, to solve can be prepared. The matrixAAAis also determined by the product formula to use. The choices here are itsorder, which is set to222in this example, as well as whether or not the product formula should besymmetric, which is set toTruefor this example. The code snippet below selects a total time to evolve the system, thekjk_jkj​values to use, and the set of equations to solve using theqiskit_addon_mpf.static.setup_static_lsemethod.

Output:

Once the linear system of equations has been instantiated, it can be solved either exactly or through an approximate model using a sum of squares (or the Frobenius norm for dynamic coefficients; see theAPI referencefor more information). The choice to use an approximate model typically arises when the norm of the coefficients for the chosen set ofkjk_jkj​values is deemed too high and a different set ofkjk_jkj​values cannot be chosen. This guide demonstrates both to compare the results.

Output:

TheLSEobject also possesses anLSE.solve()method, which will solve the system of equations exactly. The reason thatsetup_exact_problem()is used in this guide is to demonstrate the interface provided by the other approximate methods.

Now that the coefficientsxjx_jxj​have been obtained, the last step is to generate the time evolution circuits for the order and chosen set of stepskjk_jkj​of the MPF. Theqiskit-addon-utilspackage can accelerate this process.

Output:

Output:

Output:

Once these circuits have been constructed, you can then transpile and execute them using a QPU. For this example, we'll just use one of the noise-free simulators to demonstrate how the Trotter error is reduced.

Output:

Now that the circuits have been executed, reconstructing the results is fairly straightforward. As mentioned in theMPF overviewpage, our observable is reconstructed through the weighted sum

⟨M⟩=∑jxj⟨Mj⟩.\langle M \rangle = \sum_j x_j \langle M_j \rangle.⟨M⟩=∑j​xj​⟨Mj​⟩.

wherexjx_jxj​are the coefficients we found and⟨Mj⟩\langle M_j \rangle⟨Mj​⟩is the estimation of the observable∑i⟨Zi⟩\sum_i \langle Z_i \rangle∑i​⟨Zi​⟩for each circuit. We can then compare the results we obtained with the exact value using thescipy.linalgpackage.

Output:

Here you can see that the MPF has reduced the Trotter error compared to the one obtained with just a single PF withkj=19k_j=19kj​=19. However, the approximate model resulted in an expectation value that is worse than the exact model. This demonstrates the importance of using tight convergence criteria on the approximate model and finding a "good" set ofkjk_jkj​values.

On this page

© IBM Corp., 2017-2025


---

# Circuit cutting







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Circuit cutting is a technique to increase the size of circuits that can run on quantum hardware, at the cost of an additional sampling overhead. This addon implements this technique, in which a handful of gates, wires, or both are cut, resulting in smaller circuits that are better suited for execution on hardware. These smaller circuits are then executed, and the results of the original circuit are reconstructed through classical post-processing. However, the trade-off is that the overall number of shots must increase by a factor that is dependent on the number and type of cuts made (known as the sampling overhead). Circuit cutting can also be used to engineer gates between distant qubits which would otherwise require a large SWAP overhead.

Subcircuits: The set of circuits resulting from cutting gates in aQuantumCircuitand then separating the disconnected qubit subsets into smaller circuits. These circuits containSingleQubitQPDGatesand are used to instantiate each subexperiment.

Subexperiment: A term used to describe the unique circuit samples associated with a subcircuit, which are sent to a QPU for execution.

There are three ways to install the circuit cutting package: PyPI, building from source, and running within a containerized environment. It is recommended to install these packages in avirtual environmentto ensure separation between package dependencies.

The most straightforward way to install theqiskit-addon-cuttingpackage is with PyPI:

Click here to read how to install this package manually.

To contribute to this package or to install it manually, first clone the repository:

and install the package withpip. To run the tutorials found in the package repository, install the notebook dependencies as well. Install thedevdependencies if you plan on developing in the repository.

The dockerfile included in the addon repository can be used to build a Docker image. The includedcompose.yamlfile allows you to use the Docker image with the following commands.

Click here to read how to use this package within Docker.

If you are usingpodmanandpodman-composeinstead ofdocker, the commands are:

Once the container is running, you should see a message similar to:

ThelastURL in this message will give you access to the Jupyter notebook interface.

Additionally, the home directory includes a subdirectory named persistent-volume. All work you would like to save should be placed in this directory, as it is the only one that will be saved across different container runs.

In the circuit cutting process, there are two types of cuts: agateor "space-like" cut, where a cut goes through a gate operating on two (or more) qubits, and awireor "time-like" cut, which cuts directly through a qubit wire (essentially a single-qubit identity gate that has been cut into two pieces).

The diagram below depicts an example of cutting gates so that the circuit can be split into two smaller pieces with fewer qubits.

There are three scenarios to consider when preparing a circuit cutting workflow, which center around the availability of classical communication between the circuit executions. The first is where only local operations (LO) are available, while the other two introduce classical communication between executions known as local operations and classical communication (LOCC). The LOCC scenarios are then grouped into either near-time, one-directional communication between circuit executions, or real-time, bi-directional communication (which you might see in a multi-QPU environment).

While circuit cutting can be used to execute quantum circuits larger than what is possible on currently available hardware, it does come at a cost. Because the technique can be framed as a quasi-probability decomposition (QPD) problem, there is an exponential sampling overhead required in order to reconstruct the results. This overhead is the factor by which the overall number of shots must increase in order for the quasi-probability decomposition to result in the same amount of error,ϵ\epsilonϵ, as you would get by executing the original circuit. Each cut gate contributes to this overhead, and the amount of overhead added depends on the type of gate that was cut (more details on the overhead sampling can be found in final appendix of[1]).

For example, a single cut CNOT gate incurs a sampling overhead of 9[2,6]and a circuit withnnnwire cuts incurs a sampling overhead ofO(16n)\mathcal{O}(16^n)O(16n)when classical communication is not available (the LO scenario). This is reduced toO(4n)\mathcal{O}(4^n)O(4n)when classical communication becomes available (LOCC scenario)[4]. However, wire cutting with classical communication (LOCC) is not supported by this package.

Formally, the QPD problem of circuit cutting can be expressed as follows:

U=∑iaiFi,\mathcal{U} = \sum_i a_i \mathcal{F}_i,U=∑i​ai​Fi​,

whereU\mathcal{U}Uis the quantum channel implementing the desired operation, and eachaia_iai​is a real coefficient corresponding to a channel,Fi\mathcal{F}_iFi​, that is executable on hardware.

The results equivalent to the desired channelU\mathcal{U}Uare obtained by first generating the coefficients,aia_iai​, then executing subexperiments to obtain the outcomes of the different channelsFi\mathcal{F}_iFi​in order to reconstruct the expectation values corresponding toU\mathcal{U}U.

As a basic explicit example, consider the decomposition of a cut RZZGate (details can be found in[2]). A quantum circuit that contains an RZZGate can be simulated by performing six subexperiments where the RZZGate has been replaced with only single-qubit operations (these are theFi\mathcal{F}_iFi​'s from the equation above). The results of this circuit are reconstructed by combining the results of each subexperiment alongside a set of coefficients (theaia_iai​'s from the equation above), which can be either positive or negative.

For some chosenθ\thetaθparameter for the RZZGate, the six subexperiments are as follows:

The following table provides the sampling overhead factor for a variety of two-qubit instructions, provided that only a single instruction is cut.

[1] Christophe Piveteau, David Sutter, Circuit knitting with classical communication,https://arxiv.org/abs/2205.00016

[2] Kosuke Mitarai, Keisuke Fujii, Constructing a virtual two-qubit gate by sampling single-qubit operations,https://arxiv.org/abs/1909.07534

[3] Kosuke Mitarai, Keisuke Fujii, Overhead for simulating a non-local channel with local channels by quasiprobability sampling,https://arxiv.org/abs/2006.11174

[4] Lukas Brenner, Christophe Piveteau, David Sutter, Optimal wire cutting with classical communication,https://arxiv.org/abs/2302.03366

[5] K. Temme, S. Bravyi, and J. M. Gambetta, Error mitigation for short-depth quantum circuits,https://arxiv.org/abs/1612.02058

[6] Lukas Schmitt, Christophe Piveteau, David Sutter, Cutting circuits with multiple two-qubit unitaries,https://arxiv.org/abs/2312.11638

[7] Jun Zhang, Jiri Vala, K. Birgitta Whaley, Shankar Sastry, A geometric theory of non-local two-qubit operations,https://arxiv.org/abs/quant-ph/0209120

On this page

© IBM Corp., 2017-2025


---

# Get started with circuit cutting using gate cuts







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This guide demonstrates two working examples of gate cuts with theqiskit-addon-cuttingpackage. The first example shows how to reduce circuit depth (the number of circuit instructions) by cutting entangling gates on non-adjacent qubits that would otherwise incur a SWAP overhead when transpiled to hardware. The second example covers how to use gate cutting to reduce the circuit width (the number of qubits) by splitting a circuit into several circuits with fewer qubits.

Both examples will use theefficient_su2ansatz and reconstructs the same observable.

The following workflow reduces a circuit's depth by cutting distant gates, avoiding a large series of SWAP gates that would otherwise be introduced.

Start with theefficient_su2ansatz, with "circular" entanglement to introduce distant gates.

Output:

Each of theCNOTgates between qubitsq0q_0q0​andq3q_3q3​introduce two SWAP gates after transpilation (assuming the qubits are connected in a straight line). To avoid this increase in depth, you can replace these distant gates withTwoQubitQPDGatesusing thecut_gates()method.  This function also returns a list ofQPDBasisinstances - one for each decomposition.

Output:

Now that the cut gate instructions have been added, the subexperiments will have a smaller depth after transpilation than the original circuit. The code snippet below generates the subexperiments using thegenerate_cutting_experiments, which ingests the circuit and observable to reconstruct.

Thenum_samplesargument specifies how many samples to draw from the quasi-probability distribution and determines the accuracy of the coefficients used for the reconstruction. Passing infinity (np.inf) will ensure all coefficients are calculated exactly. Read the API docs ongenerating weightsandgenerating cutting experimentsfor more information.

Once the subexperiments are generated, you can then transpile them and use theSamplerprimitive to sample the distribution and reconstruct the estimated expectation values. The following code block generates, transpiles, and executes the subexperiments. It then reconstructs the results and compares them to the exact expectation value.

Output:

To accurately reconstruct the expectation value, the coefficients of the original observable (which are different from the coefficients in the output ofgenerate_cutting_experiments()) must be applied to the output of the reconstruction, since this information was lost when the cutting experiments were generated or when the observable was expanded.

Typically these coefficients can be applied throughnumpy.dot()as shown above.

This section demonstrates using gate cutting to reduce circuit width. Start with the sameefficient_su2but use "linear" entanglement.

Output:

Then generate thesubcircuitsandsubobservablesyou'll execute using thepartition_problem()function. This function takes in the circuit, observable, and an optional partitioning scheme and returns the cut circuits and observables in the form of a dictionary.

The partitioning is defined by a label string of the form"AABB"where each label in this string corresponds to the qubit in the same index of thecircuitargument. Qubits sharing a common partition label are grouped together, and any non-local gates that span more than one partition will be cut.

Theobservableskwarg topartition_problemis of typePauliList. Observable term coefficients and phases are ignored during decomposition of the problem and execution of the subexperiments. They may be re-applied during reconstruction of the expectation value.

Output:

Output:

The next step is then to use the subcircuits and subobservables to generate thesubexperimentsto be executed on a QPU using thegenerate_cutting_experimentsmethod.

To estimate the expectation value of the full-sized circuit, many subexperiments are generated from the decomposed gates' joint quasi-probability distribution and then executed on one or more QPUs. The number of samples to be taken from this distribution is controlled by thenum_samplesargument.

The following code block generates the subexperiments and executes them using theSamplerprimitive on a local simulator. (To run these on a QPU, change thebackendto your chosen QPU resource.)

Lastly, the expectation value of the full circuit is reconstructed using thereconstruct_expectation_valuesmethod.

The code block below reconstructs the results and compares them with the exact expectation value.

Output:

On this page

© IBM Corp., 2017-2025


---

# Get started with circuit cutting using wire cuts







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This guide demonstrates a working example of wire cuts with theqiskit-addon-cuttingpackage. It covers reconstructing expectation values of a seven-qubit circuit using wire cutting.

A wire cut is represented in this package as a two-qubitMoveinstruction, which is defined as a reset of the second qubit the instruction acts on, followed by a swap of both qubits. This operation is equivalent to transferring the state of the first qubit to the second qubit, while simultaneously discarding the incoming state of the second qubit.

The package is designed to be consistent with the way you must treat wire cuts when acting on physical qubits. For example, a wire cut might take the state of physical qubitnnnand continue it as a physical qubitmmmafter the cut. You can think of "instruction cutting" as a unified framework for considering both wire and gate cuts within the same formalism (since a wire cut is just a cutMoveinstruction). Using this framework for wire cutting also allows for qubit re-use, which is explained in the section oncutting wires manually.

The single-qubitCutWireinstruction acts as a more abstracted, simpler interface for working with wire cuts. It allows you to denote where in the circuit a wire should be cut at a high level and have the circuit cutting addon insert the appropriateMoveinstructions for you.

The following example demonstrates expectation value reconstruction after wire cutting. You will create a circuit with several non-local gates and define observables to estimate.

Output:

Next, make wire cuts using the single-qubitCutWireinstruction on qubitq3q_3q3​. Once the subexperiments are prepared to be executed, use thecut_wires()function to transformCutWiretoMoveinstructions on newly allocated qubits.

Output:

When a circuit is expanded through one or more wire cuts, the observable needs to be updated to account for the extra qubits that are introduced. Theqiskit-addon-cuttingpackage has a convenience functionexpand_observables(), which takesPauliLists and the original and expanded circuits as arguments, and returns a newPauliList.

This returnedPauliListwill not contain any information about the original observable's coefficients, but these can be ignored until reconstruction of the final expectation value.

Output:

Now the problem can be separated into partitions. This is accomplished using thepartition_problem()function with an optional set of partition labels to specify how to separate the circuit. Qubits sharing a common partition label are grouped together, and any non-local gates spanning more than one partition are cut.

If no partition labels are provided, then the partitioning will be automatically determined based on the connectivity of the circuit. Read the next section oncutting wires manuallyfor more information on including partition labels.

Output:

Output:

In this partitioning scheme, you have cut two wires, resulting in a sampling overhead of444^444.

To estimate the expectation value of the full-sized circuit, several subexperiments are generated from the decomposed gates' joint quasi-probability distribution and then executed on one (or more) QPUs. Thegenerate_cutting_experimentsmethod does this by ingesting arguments for thesubcircuitsandsubobservablesdictionaries you created above, as well as for the number of samples to take from the distribution.

Thenum_samplesargument specifies how many samples to draw from the quasi-probability distribution and determines the accuracy of the coefficients used for the reconstruction. Passing infinity (np.inf) ensures all coefficients are calculated exactly. Read the API docs ongenerating weightsandgenerating cutting experimentsfor more information.

Lastly, the expectation value of the full circuit can be reconstructed using thereconstruct_expectation_values()method.

The code block below reconstructs the results and compares them with the exact expectation value.

Output:

To accurately reconstruct the expectation value, the coefficients of the original observable (which are different from the output ofgenerate_cutting_experiments()) must be applied to the output of the reconstruction, since this information was lost when the cutting experiments were generated or when the observable was expanded.

Typically these coefficients can be applied throughnumpy.dot()as shown previously.

One limitation of using the higher-levelCutWireinstruction is that it does not allow for qubit re-use. If this is desired for a cutting experiment, you can instead manually placeMoveinstructions. However, because theMoveinstruction discards the state of the destination qubit, it is important that this qubit does not share any entanglement with the remainder of the system. Otherwise, the reset operation will cause the state of the circuit to partially collapse after the wire cut.

The code block below performs a wire cut on qubitq3q_3q3​for the same example circuit as previously shown. The difference here is that you can reuse a qubit by reversing theMoveoperation where the second wire cut was made (however, this is not always possible and depends on the circuit being cut).

Output:

The circuit above can now be partitioned and cutting experiments generated. To explicitly specify how the circuit should be partitioned, you can add partition labels to thepartition_problem()function. Qubits that share a common partition label are grouped together, and any non-local gates spanning more than one partition are cut. The keys of the dictionary output bypartition_problem()will match those specified in the label string.

Output:

Output:

Now the cutting experiments can be generated and the expectation value reconstructed in the same way as the previous section.

On this page

© IBM Corp., 2017-2025


---

# Qiskit Code Assistant







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit Code Assistant aims to make quantum computing more accessible to new Qiskit adopters and to improve the coding experience for current users. It is a generative AI code assistant powered bywatsonx. It is trained using millions of text tokens from Qiskit SDK v1.x, years of Qiskit code examples and IBM Quantum® features. Qiskit Code Assistant can help your quantum development workflow by offering LLM-generated suggestions based onIBM Granite models,which incorporate the latest features and functionalities from IBM®.

The following features are included in theVisual Studio Code(VS Code) andJupyterLabextensions:

For instructions to integrate Qiskit Code Assistant directly into your development environment, follow the instructions in the appropriate topic:

To provide code suggestions, Qiskit Code Assistant uses a Large Language Model (LLM). In this case, Qiskit Code Assistant currently relies on the modelgranite-3.3-8b-qiskit, built on the IBMgranite-3.3-8b models.Thegranite-3.3-8b-qiskitmodel improves thegranite-3.3-8bmodels' code generation capabilities for Qiskit through extended pretraining and fine-tuning it on high-quality Qiskit data, as well as Python commits and chat. For more information about the IBM Granite models family, refer toGranite Code Models: A Family of Open Foundation Models for Code Intelligence.For more details about thegranite-.*-qiskitmodels, seeQiskit Code Assistant: Training LLMs for generating Quantum Computing Code.

Our LLMs specialized for Qiskit are available also as open-source models. Check all the models available athttps://huggingface.co/Qiskit.

To test thegranite-.*-qiskitmodels, we are creating, in collaboration with Qiskit Advocates and experts, a new execution-based benchmark called Qiskit HumanEval (QHE). This benchmark is similar toHumanEval, including multiple challenging code problems to solve, all based on the official Qiskit libraries.

The benchmark is composed of approximately 150 tests, each one made from a function definition, followed by a docstring that details the task the model is required to solve. Each example also includes a reference canonical solution, as well as unit tests, to evaluate the correctness of the generated solutions. There are three levels of difficulty for tests: basic, intermediate, and difficult.

The dataset for the Qiskit HumanEval is expected to be open source soon.

To learn more about Qiskit Code Assistant or the Qiskit HumanEval and cite it in your scientific publications, review these recommended citations:

On this page

© IBM Corp., 2017-2025


---

# Use Qiskit Code Assistant in JupyterLab







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Learn how to install, use, configure, and uninstall the official Qiskit Code Assistant extension in JupyterLab.

To install theJupyterLab extension, run the following command from a terminal:

After installing the extension, start JupyterLab:

The extension loads automatically and is listed on the bottom of the JupyterLab window. Refer to theJupyterLab documentationfor help working with JupyterLab.

It is recommended that you edit the following JupyterLab settings by going to Settings -> Settings Editor:

ClickInline Completer, find "Show widget" and chooseAlways.  This means that the inline completer widget will always be shown so you can cycle through and select a completion item.

ClickCode Completionand increase the value for "Default timeout for a provider." to10000or 10 seconds. The default value is 1 second, but the Qiskit Code Assistant API might take longer than this to find a suggestion. This setting only applies to the standard context menu that is invoked withTab. The inline completer has a default of 10 seconds.

Other settings you might want to change:

Keyboard shortcuts can be changed from Settings > Settings Editor > Keyboard Shortcuts.

You can change the IBM Quantum Classic API token to use in the JupyterLab command palette. To do that, typeAlt+Shift+C, search forqiskit, select theQiskit Code Assistant: Set IBM Quantum API tokencommand, and paste in your key.

[Advanced] To change the instance of the Qiskit Code Assistant service that the extension should use, edit Qiskit Code AssistantserviceUrlsetting.

[Advanced] Keyboard shortcuts can be changed by searching forcompleterin the Keyboard Shortcuts settings (Settings -> Settings Editor -> Keyboard Shortcuts) and adding new shortcuts for the relevant commands.

After installing the extension, it tries to authenticate you. By default, the package tries to authenticate to IBM Quantum services with the defined Qiskit API key, and uses your token from theQISKIT_IBM_TOKENenvironment variable or from the file~/.qiskit/qiskit-ibm.json(under the sectiondefault-ibm-quantum). If you need help configuring your account, follow the instructions inSet up to use IBM Quantum Platform.

By default, the extension uses thegranite-3.3-8b-qiskitmodel, which is listed in the Model Picker in the bottom status bar.

The first time you use thegranite-3.3-8b-qiskitmodel, a window opens that lists some major restrictions that you should be aware of when using the model. ClickAcceptto enable the model for code generation.

While you develop your code using Qiskit, you can ask to Qiskit Code Assistant to help you. In general, the assistant suggests better code as response to Python comments or docstrings, but you can use the assistant anywhere in your file.

To get a code suggestion, type a prompt, then typeAlt+.orAlt+\.  There are two types of prompts you can use:

Use the following to accept, reject, and cycle through suggestions:

Additionally, after the assistant runs, you can use the buttons on the widget to cycle or accept the suggestion:

The service can sometimes take a few seconds to return a suggestion, you can see when the service is working by checking the status bar.

Jupyterlab also includes a traditional suggestion context menu. Use theTabkey to run and display the context menu.

The context menu includes suggestions from JupyterLab in addition to suggestions made by Qiskit Code Assistant. The context menu also sanitizes and trims the suggestions, making it less useful for reviewing the code suggestion before inserting it.

To remove the Qiskit Code Assistant extension from JupyterLab, run:

If you see the frontend extension but it is not working, check that the server
extension is enabled:

If the server extension is installed and enabled, but you don't see the frontend
extension, check that the frontend extension is installed:

The code for this extension is publicly available and open source. Check it out inGitHub.

See examples to use Qiskit Code Assistant forcircuits,configuring error suppression, andtranspiling with pass managers.

On this page

© IBM Corp., 2017-2025


---

# Use Qiskit Code Assistant in Visual Studio Code







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Learn how to install, use, configure and uninstall the official Qiskit Code Assistant extension in Visual Studio Code (VS Code).

To install theVS Code extension, follow these steps:

Install directly from VS Code:

Alternatively, the extension is also available through theVS Code Marketplace.

The extension loads automatically and is listed on the bottom of the VS Code window.  If it is not listed, reload the extension or application.

The following settings can be configured:

To change keyboard shortcuts, open the Keyboard Shortcuts settings (Cmd/Ctrl+Shift+P->Preferences: Open Keyboard Shortcuts (JSON)) and search forqiskit-vscode.

You can change the IBM Quantum Classic API token to use in the VS Code command palette. To do that, typeCmd/Ctrl+Shift+P, search forqiskit, select theQiskit Code Assistant: Set IBM Quantum API tokencommand, and paste your IBM Quantum Classic API token.

[Advanced] To change the instance of the Qiskit Code Assistant Service that the extension should use, go to File -> Preferences -> Settings.  On the User tab,  search for Qiskit, and edit theQiskit Code Assistant: Url.

After installing the extension, it tries to authenticate you. By default, the package tries to authenticate to IBM Quantum services with the defined Qiskit API key, and uses your token from theQISKIT_IBM_TOKENenvironment variable or from the file~/.qiskit/qiskit-ibm.json(under the sectiondefault-ibm-quantum). If you need help configuring your account, follow the instructions inSet up to use IBM Quantum Platform.

By default, the extension uses thegranite-3.3-8b-qiskitmodel, which is listed in the Model Picker in the bottom status bar.

The first time you use thegranite-3.3-8b-qiskitmodel, a modal opens listing some major restrictions that you should be aware of when using the model. ClickAcceptto enable the model for code generation.

While you develop your code using Qiskit, you can ask Qiskit Code Assistant to help you. In general, the Assistant suggests better code in response to Python comments or docstrings, but you can use the Assistant anywhere in your file.

To get a code suggestion, type a prompt, thenCtrl+..  There are two types of prompts you can use:

Use the following to accept, reject, and cycle through suggestions:

To remove Qiskit Code Assistant from VS Code, follow these steps:

If you don't see the extension status bar in VS Code, check that the extension is installed and enabled under the extensions tab.

If the extension is installed and enabled, but it cannot select a model, verify that your current API key has been added and theQiskit Code Assistant: Urlis properly set.

The code for this official extension is publicly available and open source. Check it out inGitHub.

See examples to use Qiskit Code Assistant forcircuits,configuring error suppression, andtranspiling with pass managers.

On this page

© IBM Corp., 2017-2025


---

# Use Qiskit Code Assistant in local mode







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Learn how to install, configure, and use any of Qiskit Code Assistant models on your local machine.

The Open Source Qiskit Code Assistant models are available insafetensorsSafetensors is a file format designed specifically for storing machine learning model weights and tensors in a secure and efficient manner.orGGUF file formatGGUF is a binary format that is designed for fast loading and saving of models, and for ease of reading.and can be downloaded from the Hugging Face Hub in one of two ways.

Follow these steps to download any Qiskit Code Assistant-related model from the Hugging Face website:

Publicly available open source models:

To download any of the available Qiskit Code Assistant models using the Hugging Face CLI, follow these steps:

Install theHugging Face CLI

Log in to your Hugging Face account

Download the model you prefer from the previous list

There are multiple ways to deploy and interact with the downloaded Qiskit Code Assistant model. This guide demonstrates usingOllamaas follows: either with theOllama applicationusing the Hugging Face Hub integration or local model, or with thellama-cpp-pythonpackage.

The Ollama application provides a simple solution to run the LLMs locally. It is easy to use, with a CLI that makes the whole setup process, model management, and interaction fairly straightforward. It’s ideal for quick experimentation and for users that want fewer technical details to handle.

Download theOllama application

Install the downloaded file

Launch the installed Ollama application

Try Ollama in your terminal and start running models. For example:

TheOllama/Hugging Face Hub integrationprovides a way to interact with models hosted on the Hugging Face Hub without needing to create a new modelfile nor manually downloading the GGUF or safetensors files. The defaulttemplateandparamsfiles are already included for the model on the Hugging Face Hub.

Make sure the Ollama application is running.

Go the desired model page, and copy the URL. For example,https://huggingface.co/Qiskit/granite-3.3-8b-qiskit.

From your terminal, run the command:

If you have manually downloaded a GGUF model such ashttps://huggingface.co/Qiskit/granite-8b-qiskit-GGUFand you want to experiment with different templates and parameters, you can follow these steps to load it into your local Ollama application.

Create aModelfileentering the following content and be sure to update<PATH-TO-GGUF-FILE>to the actual path of your downloaded model.

Run the following command to create a custom model instance based on theModelfile.

After thegranite-8b-qiskitGGUF model has been set up in Ollama, run the following command to launch the model and interact with it in the terminal (in chat mode).

Some useful commands:

An alternative to the Ollama application is thellama-cpp-pythonpackage, which is a Python binding forllama.cpp. It gives you more control and flexibility to run the GGUF model locally, and is ideal for users who wish to integrate the local model in their workflows and Python applications.

You can also add text generation parameters to the model to customize the inference:

Use the VS Code extension and JupyterLab extension for the Qiskit Code Assistant to prompt the locally deployed Qiskit Code Assistant model. Once you have the Ollama applicationset up with the model, you can configure the extensions to connect to the local service.

With the Qiskit Code Assistant VS Code extension, you can interact with the model and perform code completion while writing your code. This can work well for users looking for assistance writing Qiskit code for their Python applications.

The Qiskit Code Assistant model configured in Ollama should appear in the status bar and is then ready to use.

With the Qiskit Code Assistant JupyterLab extension, you can interact with the model and perform code completion directly in your Jupyter Notebook. Users who predominantly work with Jupyter Notebooks can take advantage of this extension to further enhance their experience writing Qiskit code.

The Qiskit Code Assistant model configured in Ollama should appear in the status bar and is then ready to use.

On this page

© IBM Corp., 2017-2025


---

# Qiskit Code Assistant - OpenAI API compatibility







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit Code Assistant offers compatibility with a subset of the OpenAI API specification, specifically with thecompletions API endpoints. The goal of this compatibility is to allow third-party packages to connect to Qiskit Code Assistant seamlessly by using well-known AI-related libraries and methods such asOpenAI,LiteLLM, or others.

The/v1/completionsendpoint fails with a403error if the model disclaimer has been accepted. See the following for how to view and accept the model disclaimer.

Additional endpoints (not part of OpenAI schema, provided for convenience) include:

To retrieve/view the model disclaimer, make aGETrequest to the disclaimer endpoint. For example:

If you agree with the model disclaimer, to accept it,POSTto the disclaimer endpoint providing the disclaimer's ID and whether it is accepted or rejected. For example:

The OpenAI Python library provides convenient access to the OpenAI REST API (such as the one provided by Qiskit Code Assistant) from any Python 3.8+ application. See more details in theInstallation sectionof the OpenAI Python API library Readme.

LiteLLM is a convenient Python library to access multiple LLM APIs using the OpenAI format (Bedrock, Huggingface, VertexAI, TogetherAI, Azure, OpenAI, Groq, and so on). See theLiteLLM docsfor more details.

On this page

© IBM Corp., 2017-2025


---

