# Single systems

Download the slidesfor this lesson.

Open theYouTube videofor this lesson in a separate window.

This lesson introduces the basic framework ofquantum information, including the description of quantum states as vectors with complex number entries, measurements that allow classical information to be extracted from quantum states, and operations on quantum states that are described by unitary matrices. We will restrict our attention in this lesson to the comparatively simple setting in which asingle systemis considered in isolation. In the next lesson, we'll expand our view tomultiple systems,which can interact with one another and be correlated.

There are, in fact, two common mathematical descriptions of quantum information. The one introduced in this course is the simpler of the two. This description is sufficient for understanding many (or perhaps most) quantum algorithms, and is a natural place to start from a pedagogical viewpoint.

A more general, and ultimately more powerful description of quantum information, in which quantum states are represented bydensity matrices, is introduced in theGeneral formulation of quantum informationcourse, which is the third course in theUnderstanding Quantum Information and Computationseries. The density matrix description is essential to the study of quantum information, for several reasons. As examples, it can be used to model the effects ofnoiseon quantum computations, or the state of one piece of an entangled pair. More generally, density matrices serve as a mathematical basis for quantum information theory and quantum cryptography, and are quite beautiful from a mathematical perspective. For these reasons, you are encouraged you to learn more about it when the time is right, but for now our focus will be on the simpler description of quantum information.

Before we begin, please take a moment to complete ourpre-course survey, which is important to help improve our content offerings and user experience.

To describe quantum information and how it works, we will begin with an overview ofclassicalinformation.

Some may wonder why so much attention is paid to classical information in a course on quantum information, but there are good reasons. For one, although quantum and classical information are different in some spectacular ways, their mathematical descriptions are actually quite similar.

Classical information also serves as a familiar point of reference when studying quantum information, as well as a source of analogy that goes a surprisingly long way. It is common that people ask questions about quantum information that have natural classical analogs, and often those questions have simple answers that can provide both clarity and insight into the original questions about quantum information. Indeed, it is not at all unreasonable to claim that one cannot truly understand quantum information without understanding classical information.

Some readers may already be familiar with the material to be discussed in this section, while others may not — but the discussion is meant for both audiences. In addition to highlighting the aspects of classical information that are most relevant to an introduction to quantum information, this section introduces theDirac notation, which is often used to describe vectors and matrices in quantum information and computation. As it turns out, the Dirac notation is not specific to quantum information; it can equally well be used in the context of classical information, as well as for many other settings in which vectors and matrices arise.

Suppose that we have asystemthat stores information. More specifically, we shall assume that this system can be in one of a finite number ofclassical statesat each instant. Here, the termclassical stateshould be understood in intuitive terms, as a configuration that can be recognized and described unambiguously.

The archetypal example, which we will come back to repeatedly, is that of abit, which is a system whose classical states are000and1.1.1.Other examples include a standard six-sided die, whose classical states are1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,and666(represented by the corresponding number of dots on whatever face is on top); a nucleobase in a strand of DNA, whose classical states areA,C,G, andT;and a switch on an electric fan, whose classical states are (commonly)high,medium,low, andoff. In mathematical terms, the specification of the classical states of a system are, in fact, the starting point: wedefinea bit to be a system that has classical states000and1,1,1,and likewise for systems having different classical state sets.

For the sake of this discussion, let us give the nameX\mathsf{X}Xto the system being considered, and let us use the symbolΣ\SigmaΣto refer to the set of classical states ofX.\mathsf{X}.X.In addition to the assumption thatΣ\SigmaΣis finite, which was already mentioned, we naturally assume thatΣ\SigmaΣisnonempty— for it is nonsensical for a physical system to have no states at all. And while it does make sense to consider physical systems havinginfinitelymany classical states, we will disregard this possibility, which is certainly interesting but is not relevant to this course. For these reasons, and for the sake of convenience and brevity, we will hereafter use the termclassical state setto mean any finite and nonempty set.

Here are a few examples:

When thinking aboutX\mathsf{X}Xas a carrier of information, the different classical states ofX\mathsf{X}Xcould be assigned certain meanings, leading to different outcomes or consequences. In such cases, it may be sufficient to describeX\mathsf{X}Xas simply being in one of its possible classical states. For instance, ifX\mathsf{X}Xis a fan switch, we might happen to know with certainty that it is set tohigh,which might then lead us to switch it tomedium.

Often in information processing, however, our knowledge is uncertain. One way to represent our knowledge of the classical state of a systemX\mathsf{X}Xis to associateprobabilitieswith its different possible classical states, resulting in what we shall call aprobabilistic state.

For example, supposeX\mathsf{X}Xis a bit. Based on what we know or expect about what has happened toX\mathsf{X}Xin the past, we might perhaps believe thatX\mathsf{X}Xis in the classical state000with probability3/43/43/4and in the state111with probability1/4.1/4.1/4.We may represent these beliefs by writing this:

A more succinct way to represent this probabilistic state is by a column vector.

The probability of the bit being000is placed at the top of the vector and the probability of the bit being111is placed at the bottom, because this is the conventional way to order the set{0,1}.\{0,1\}.{0,1}.

In general, we can represent a probabilistic state of a system having any classical state set in the same way, as a vector of probabilities. The probabilities can be ordered in any way we choose — but it is typical that there is a natural or default way to do this. To be precise, we can represent any probabilistic state through a column vector satisfying two properties:

Conversely, any column vector that satisfies these two properties can be taken as a representation of a probabilistic state. Hereafter, we will refer to vectors of this form asprobability vectors.

Alongside the succinctness of this notation, identifying probabilistic states as column vectors has the advantage that operations on probabilistic states are represented through matrix–vector multiplication, as will be discussed below.

Next let us consider what happens if wemeasurea system when it is in a probabilistic state. In this context, by measuring a system we simply mean that we look at the system and recognize whatever classical state it is in without unambiguity. Intuitively speaking, we can't "see" a probabilistic state of a system; when we look at it, we just see one of the possible classical states.

By measuring a system, we may also change our knowledge of it, and therefore the probabilistic state we associate with it can change. That is, if we recognize thatX\mathsf{X}Xis in the classical statea∈Σ,a\in\Sigma,a∈Σ,then the new probability vector representing our knowledge of the state ofX\mathsf{X}Xbecomes the vector having a111in the entry corresponding toaaaand000for all other entries. This vector indicates thatX\mathsf{X}Xis in the classical stateaaawith certainty — which we know having just recognized it — and we denote this vector by∣a⟩,\vert a\rangle,∣a⟩,which is read as "ketaaa" for a reason that will be explained shortly. Vectors of this sort are also calledstandard basisvectors.

For example, assuming that the system we have in mind is a bit, the standard basis vectors are given by

Notice that any two-dimensional column vector can be expressed as a linear combination of these two vectors. For example,

This fact naturally generalizes to any classical state set: any column vector can be written as a linear combination of standard basis states. Quite often we express vectors in precisely this way.

Returning to the change of a probabilistic state upon being measured, we may note the following connection to our everyday experiences. Suppose we flip a fair coin, but cover up the coin before looking at it. We would then say that its probabilistic state is

Here, the classical state set of our coin is{heads,tails}.\{\text{heads},\text{tails}\}.{heads,tails}.We'll choose to order these states as heads first, tails second.

If we were to uncover the coin and look at it, we would see one of the two classical states: heads or tails. Supposing that the result were tails, we would naturally update our description of the probabilistic state of the coin so that it becomes∣tails⟩.|\text{tails}\rangle.∣tails⟩.Of course, if we were then to cover up the coin, and then uncover it and look at it again, the classical state would still be tails, which is consistent with the probabilistic state being described by the vector∣tails⟩.|\text{tails}\rangle.∣tails⟩.

This may seem trivial, and in some sense it is. However, while quantum systems behave in an entirely analogous way, their measurement properties are frequently considered strange or unusual. By establishing the analogous properties of classical systems, the way quantum information works might seem less unusual.

One final remark concerning measurements of probabilistic states is this: probabilistic states describe knowledge or belief, not necessarily something actual, and measuring merely changes our knowledge and not the system itself. For instance, the state of a coin after we flip it, but before we look, is either heads or tails — we just don't know which until we look. Upon seeing that the classical state is tails, say, we would naturally update the vector describing our knowledge to∣tails⟩,|\text{tails}\rangle,∣tails⟩,but to someone else who didn't see the coin when it was uncovered, the probabilistic state would remain unchanged. This is not a cause for concern; different individuals may have different knowledge or beliefs about a particular system, and hence describe that system by different probability vectors.

In the last part of this brief summary of classical information, we will consider the sorts of operations that can be performed on a classical system.

First, there aredeterministicoperations, where each classical statea∈Σa\in\Sigmaa∈Σis transformed intof(a)f(a)f(a)for some functionfffof the formf:Σ→Σ.f:\Sigma\rightarrow\Sigma.f:Σ→Σ.

For example, ifΣ={0,1},\Sigma = \{0,1\},Σ={0,1},there are four functions of this form,f1,f_1,f1​,f2,f_2,f2​,f3,f_3,f3​,andf4,f_4,f4​,which can be represented by tables of values as follows:

The first and last of these functions areconstant:f1(a)=0f_1(a) = 0f1​(a)=0andf4(a)=1f_4(a) = 1f4​(a)=1for eacha∈Σ.a\in\Sigma.a∈Σ.The middle two are not constant, they arebalanced:each of the two output values occurs the same number of times (once, in this case) as we range over the possible inputs. The functionf2f_2f2​is theidentity function:f2(a)=af_2(a) = af2​(a)=afor eacha∈Σ.a\in\Sigma.a∈Σ.Andf3f_3f3​is the functionf3(0)=1f_3(0) = 1f3​(0)=1andf3(1)=0,f_3(1) = 0,f3​(1)=0,which is better-known as the NOT function.

The actions of deterministic operations on probabilistic states can be represented by matrix-vector multiplication. Specifically, the matrixMMMthat represents a given functionf:Σ→Σf:\Sigma\rightarrow\Sigmaf:Σ→Σis the one that satisfies

for everya∈Σ.a\in\Sigma.a∈Σ.Such a matrix always exists and is uniquely determined by this requirement. Matrices that represent deterministic operations always have exactly one111in each column, and000for all other entries.

For instance, the matricesM1,…,M4M_1,\ldots,M_4M1​,…,M4​corresponding to the functionsf1,…,f4f_1,\ldots,f_4f1​,…,f4​above are as follows:

Here's a quick verification showing that the first matrix is correct. The other three can be checked similarly.

A convenient way to represent matrices of these and other forms makes use of an analogous notation for row vectors to the one for column vectors discussed previously: we denote by⟨a∣\langle a \vert⟨a∣therowvector having a111in the entry corresponding toaaaand zero for all other entries, for eacha∈Σ.a\in\Sigma.a∈Σ.This vector is read as "braa.a.a."

For example, ifΣ={0,1},\Sigma = \{0,1\},Σ={0,1},then

For any classical state setΣ,\Sigma,Σ,we can view row vectors and column vectors as matrices, and perform the matrix multiplication∣b⟩⟨a∣.\vert b\rangle \langle a\vert.∣b⟩⟨a∣.We obtain a square matrix having a111in the entry corresponding to the pair(b,a),(b,a),(b,a),meaning that the row of the entry corresponds to the classical statebbband the column corresponds to the classical statea,a,a,with000for all other entries. For example,

Using this notation, we may express the matrixMMMthat corresponds to any given functionf:Σ→Σf:\Sigma\rightarrow\Sigmaf:Σ→Σas

For example, consider the functionf4f_4f4​above, for whichΣ={0,1}.\Sigma = \{0,1\}.Σ={0,1}.We obtain the matrix

The reason why this works is as follows. If we again think about vectors as matrices, and this time consider the multiplication⟨a∣∣b⟩,\langle a \vert \vert b \rangle,⟨a∣∣b⟩,we obtain a1×11\times 11×1matrix, which we can think about as a scalar (i.e., a number). For the sake of tidiness, we write this product as⟨a∣b⟩\langle a \vert b\rangle⟨a∣b⟩rather than⟨a∣∣b⟩.\langle a \vert \vert b \rangle.⟨a∣∣b⟩.This product satisfies the following simple formula:

Using this observation, together with the fact that matrix multiplication is associative and linear, we obtain

for eachb∈Σ,b\in\Sigma,b∈Σ,which is precisely what we require of the matrixM.M.M.

As we will discuss in greater detail later on in theQuantum circuitslesson,⟨a∣b⟩\langle a \vert b \rangle⟨a∣b⟩may also be seen as aninner productbetween the vectors∣a⟩\vert a\rangle∣a⟩and∣b⟩.\vert b\rangle.∣b⟩.Inner products are critically important in quantum information, but we'll delay a discussion of them until they are needed.

At this point the names "bra" and "ket" may be evident: putting a "bra"⟨a∣\langle a\vert⟨a∣together with a "ket"∣b⟩\vert b\rangle∣b⟩yields a "bracket"⟨a∣b⟩.\langle a \vert b\rangle.⟨a∣b⟩.This notation and terminology is due toPaul Dirac, and for this reason is known as theDirac notation.

In addition to deterministic operations, we haveprobabilistic operations.

For example, consider the following operation on a bit. If the classical state of the bit is0,0,0,it is left alone; and if the classical state of the bit is1,1,1,it is flipped, so that it becomes000with probability1/21/21/2and111with probability1/2.1/2.1/2.This operation is represented by the matrix

One can check that this matrix does the correct thing by multiplying the two standard basis vectors by it.

For an arbitrary choice of a classical state set, we can describe the set of all probabilistic operations in mathematical terms as those that are represented bystochasticmatrices, which are matrices satisfying these two properties:

Equivalently, stochastic matrices are matrices whose columns all form probability vectors.

We can think about probabilistic operations at an intuitive level as ones where randomness might somehow be used or introduced during the operation, just like in the example above. With respect to the stochastic matrix description of a probabilistic operation, each column can be viewed as a vector representation of the probabilistic state that is generated given whatever classical state input corresponds to that column.

We can also think about stochastic matrices as being exactly those matrices that always map probability vectors to probability vectors. That is, stochastic matrices always map probability vectors to probability vectors, and any matrix that always maps probability vectors to probability vectors must be a stochastic matrix.

Finally, a different way to think about probabilistic operations is that they are random choicesofdeterministic operations. For instance, we can think about the operation in the example above as applying either the identity function or the constant 0 function, each with probability1/2.1/2.1/2.This is consistent with the equation

Such an expression is always possible, for an arbitrary choice of a classical state set and any stochastic matrix with rows and columns identified with that classical state set.

Suppose thatX\mathsf{X}Xis a system having classical state setΣ,\Sigma,Σ,andM1,…,MnM_1,\ldots,M_nM1​,…,Mn​are stochastic matrices representing probabilistic operations on the systemX.\mathsf{X}.X.

If the first operationM1M_1M1​is applied to the probabilistic state represented by a probability vectoru,u,u,the resulting probabilistic state is represented by the vectorM1u.M_1 u.M1​u.If we then apply the second probabilistic operationM2M_2M2​to this new probability vector, we obtain the probability vector

The equality follows from the fact that matrix multiplication (which includes matrix-vector multiplication as a special case) is anassociativeoperation. Thus, the probabilistic operation obtained bycomposingthe first and second probabilistic operations, where we first applyM1M_1M1​and then applyM2,M_2,M2​,is represented by the matrixM2M1,M_2 M_1,M2​M1​,which is necessarily stochastic.

More generally, composing the probabilistic operations represented by the matricesM1,…,MnM_1,\ldots,M_nM1​,…,Mn​in this order, meaning thatM1M_1M1​is applied first,M2M_2M2​is applied second, and so on, withMnM_nMn​applied last, is represented by the matrix product

Note that the ordering is important here: although matrix multiplication is associative, it is not acommutativeoperation. For example, if

then

That is, the order in which probabilistic operations are composed matters; changing the order in which operations are applied in a composition can change the resulting operation.

Now we're ready to move on to quantum information, where we make a different choice for the type of vector that represents a state — in this case aquantum state— of the system being considered. Like in the previous section, we'll be concerned with systems having finite and nonempty sets of classical states, and we'll make use of much of the notation that was introduced in that section.

Aquantum stateof a system is represented by a column vector, similar to a probabilistic state. As before, the indices of the vector label the classical states of the system. Vectors representing quantum states are characterized by these two properties:

Thus, in contrast to probabilistic states, vectors representing quantum states need not have nonnegative real number entries, and it is the sum of the absolute values squared of the entries (as opposed to the sum of the entries) that must equal1.1.1.Simple as these changes are, they give rise to the differences between quantum and classical information; any speedup from a quantum computer, or improvement from a quantum communication protocol, is ultimately derived from these simple mathematical changes.

TheEuclidean normof a column vector

is denoted and defined as follows:

The condition that the sum of the absolute values squared of a quantum state vector equals111is therefore equivalent to that vector having Euclidean norm equal to1.1.1.That is, quantum state vectors areunit vectorswith respect to the Euclidean norm.

The termqubitrefers to a quantum system whose classical state set is{0,1}.\{0,1\}.{0,1}.That is, a qubit is really just a bit — but by using this name we explicitly recognize that this bit can be in a quantum state.

These are examples of quantum states of a qubit:

and

The first two examples,∣0⟩\vert 0\rangle∣0⟩and∣1⟩,\vert 1\rangle,∣1⟩,illustrate that standard basis elements are valid quantum state vectors: their entries are complex numbers, where the imaginary part of these numbers all happens to be0,0,0,and computing the sum of the absolute values squared of the entries yields

as required. Similar to the classical setting, we associate the quantum state vectors∣0⟩\vert 0\rangle∣0⟩and∣1⟩\vert 1\rangle∣1⟩with a qubit being in the classical state000and1,1,1,respectively.

For the other two examples, we again have complex number entries, and computing the sum of the absolute value squared of the entries yields

and

These are therefore valid quantum state vectors. Note that they are linear combinations of the standard basis states∣0⟩\vert 0 \rangle∣0⟩and∣1⟩,\vert 1 \rangle,∣1⟩,and for this reason we often say that they'resuperpositionsof the states000and1.1.1.Within the context of quantum states,superpositionandlinear combinationare essentially synonymous.

The example(1)(1)(1)of a qubit state vector above is very commonly encountered — it is called theplus stateand is denoted as follows:

We also use the notation

to refer to a related quantum state vector where the second entry is negative rather than positive, and we call this state theminus state.

This sort of notation, where some symbol other than one referring to a classical state appears inside of a ket, is common — we can use whatever name we wish inside of a ket to name a vector. Indeed, it is quite common to use the notation∣ψ⟩,\vert\psi\rangle,∣ψ⟩,or other names in place ofψ,\psi,ψ,to refer to an arbitrary vector that may not necessarily be a standard basis vector.

Notice that, if we have a vector∣ψ⟩\vert \psi \rangle∣ψ⟩whose indices correspond to some classical state setΣ,\Sigma,Σ,and ifa∈Σa\in\Sigmaa∈Σis an element of this classical state set, then the matrix product⟨a∣∣ψ⟩\langle a\vert \vert \psi\rangle⟨a∣∣ψ⟩is equal to the entry of the vector∣ψ⟩\vert \psi \rangle∣ψ⟩whose index corresponds toa.a.a.As we did when∣ψ⟩\vert \psi \rangle∣ψ⟩was a standard basis vector, we write⟨a∣ψ⟩\langle a \vert \psi \rangle⟨a∣ψ⟩rather than⟨a∣∣ψ⟩\langle a\vert \vert \psi\rangle⟨a∣∣ψ⟩for the sake of readability.

For example, ifΣ={0,1}\Sigma = \{0,1\}Σ={0,1}and

then

It must be understood that, when using the Dirac notation for arbitrary vectors, the notation⟨ψ∣\langle \psi \vert⟨ψ∣refers to the row vector obtained by taking theconjugate-transposeof the column vector∣ψ⟩,\vert\psi\rangle,∣ψ⟩,where the vector is transposed from a column vector to a row vector and each entry is replaced by its complex conjugate. For example, if∣ψ⟩\vert\psi\rangle∣ψ⟩is the vector defined in(2),(2),(2),then

The reason we take the complex conjugate, in addition to the transpose, will be made more clear in theQuantum circuitslesson when we discussinner products.

We can consider quantum states of systems having arbitrary classical state sets.

For example, here is a quantum state vector for an electrical fan switch:

The assumption here is that the classical states are ordered ashigh,medium,low,off. There may be no particular reason why one would want to consider a quantum state of an electrical fan switch, but it is possible in principle.

Here's another example, this time of a quantum decimal digit whose classical states are0,1,…,9:0, 1, \ldots, 9:0,1,…,9:

This example illustrates the convenience of writing state vectors using the Dirac notation. For this particular example, the column vector representation is merely cumbersome — but if there were significantly more classical states it would become unusable. The Dirac notation, in contrast, supports precise descriptions of large and complicated vectors in a compact form.

The Dirac notation also allows for the expression of vectors where different aspects of the vectors areindeterminate,meaning that they are unknown or not yet established. For example, for an arbitrary classical state setΣ,\Sigma,Σ,we can consider the quantum state vector

where the notation∣Σ∣\vert\Sigma\vert∣Σ∣refers to the number of elements inΣ.\Sigma.Σ.In words, this is auniform superpositionover the classical states inΣ.\Sigma.Σ.We'll encounter much more complicated expressions of quantum state vectors in later lessons, where the use of column vectors would be impractical or impossible. In fact, we'll mostly abandon the column vector representation of state vectors, except for vectors having a small number of entries (often in the context of examples), where it may be helpful to display and examine the entries explicitly.

Here's one more reason why expressing state vectors using the Dirac notation is convenient: it alleviates the need to explicitly specify an ordering of the classical states (or, equivalently, the correspondence between classical states and vector indices). For example, a quantum state vector for a system having classical state set{♣,♢,♡,♠},\{\clubsuit,\diamondsuit,\heartsuit,\spadesuit\},{♣,♢,♡,♠},such as

is unambiguously described by this expression, and there's really no need to choose or specify an ordering of this classical state set in order to make sense of the expression. In this case, it's not difficult to specify an ordering of the standard card suits — for instance, we might choose to order them like this:♣,\clubsuit,♣,♢,\diamondsuit,♢,♡,\heartsuit,♡,♠.\spadesuit.♠.If we choose this particular ordering, the quantum state vector above would be represented by the column vector

In general, however, it is convenient to be able to simply ignore the issue of how classical state sets are ordered.

Next let us consider what happens when a quantum state ismeasured, focusing on a simple type of measurement known as astandard basis measurement. (There are more general notions of measurement that will be discussed later on.)

Similar to the probabilistic setting, when a system in a quantum state is measured, the hypothetical observer performing the measurement won't see a quantum state vector, but rather will see some classical state. In this sense, measurements act as an interface between quantum and classical information, through which classical information is extracted from quantum states.

The rule is simple: if a quantum state is measured, each classical state of the system appears with probability equal to theabsolute value squaredof the entry in the quantum state vector corresponding to that classical state. This is known as theBorn rulein quantum mechanics. Notice that this rule is consistent with the requirement that the absolute values squared of the entries in a quantum state vector sum to1,1,1,as it implies that the probabilities of different classical state measurement outcomes sum to1.1.1.

For example, measuring the plus state

results in the two possible outcomes,000and1,1,1,with probabilities as follows.

Interestingly, measuring the minus state

results in exactly the same probabilities for the two outcomes.

This suggests that, as far as standard basis measurements are concerned, the plus and minus states are no different. Why, then, would we care to make a distinction between them? The answer is that these two states behave differently when operations are performed on them, as we will discuss in the next subsection below.

Of course, measuring the quantum state∣0⟩\vert 0\rangle∣0⟩results in the classical state000with certainty, and likewise measuring the quantum state∣1⟩\vert 1\rangle∣1⟩results in the classical state111with certainty. This is consistent with the identification of these quantum states with the systembeingin the corresponding classical state, as was suggested previously.

As a final example, measuring the state

causes the two possible outcomes to appear with probabilities as follows:

and

Thus far, it may not be evident why quantum information is fundamentally different from classical information. That is, when a quantum state is measured, the probability to obtain each classical state is given by the absolute value squared of the corresponding vector entry — so why not simply record these probabilities in a probability vector?

The answer, at least in part, is that the set of allowableoperationsthat can be performed on a quantum state is different than it is for classical information. Similar to the probabilistic setting, operations on quantum states are linear mappings — but rather than being represented by stochastic matrices, like in the classical case, operations on quantum state vectors are represented byunitarymatrices.

A square matrixUUUhaving complex number entries isunitaryif it satisfies the equations

Here,I\mathbb{I}Iis the identity matrix, andU†U^{\dagger}U†is theconjugate transposeofU,U,U,meaning the matrix obtained by transposingUUUand taking the complex conjugate of each entry.

If either of the two equalities numbered(3)(3)(3)above is true, then the other must also be true. Both equalities are equivalent toU†U^{\dagger}U†being the inverse ofU:U:U:

(Warning: ifMMMis not a square matrix, then it could be thatM†M=IM^{\dagger} M = \mathbb{I}M†M=IandMM†≠I,M M^{\dagger} \neq \mathbb{I},MM†=I,for instance. The equivalence of the two equalities in the first equation above is only true for square matrices.)

The condition thatUUUis unitary is equivalent to the condition that multiplication byUUUdoes not change the Euclidean norm of any vector. That is, ann×nn\times nn×nmatrixUUUis unitary if and only if∥U∣ψ⟩∥=∥∣ψ⟩∥\| U \vert \psi \rangle \| = \|\vert \psi \rangle \|∥U∣ψ⟩∥=∥∣ψ⟩∥for everynnn-dimensional column vector∣ψ⟩\vert \psi \rangle∣ψ⟩with complex number entries. Thus, because the set of all quantum state vectors is the same as the set of vectors having Euclidean norm equal to1,1,1,multiplying a unitary matrix to a quantum state vector results in another quantum state vector.

Indeed, unitary matrices are exactly the set of linear mappings that always transform quantum state vectors to other quantum state vectors. Notice here a resemblance to the classical probabilistic case, where operations are associated with stochastic matrices, which are the ones that always transform probability vectors into probability vectors.

The following list describes some commonly encountered unitary operations on qubits.

Pauli operations.The four Pauli matrices are as follows:

A common alternative notation isX=σx,X = \sigma_x,X=σx​,Y=σy,Y = \sigma_y,Y=σy​,andZ=σzZ = \sigma_zZ=σz​(but be aware that the lettersX,X,X,Y,Y,Y,andZZZare also commonly used for other purposes). TheXXXoperation is also called abit flipor aNOT operationbecause it induces this action on bits:

TheZZZoperation is also called aphase flip,and it has this action:

Hadamard operation. The Hadamard operation is described by this matrix:

Phase operations.A phase operation is one described by the matrix

for any choice of a real numberθ.\theta.θ.The operations

are particularly important examples. Other examples includeI=P0\mathbb{I} = P_0I=P0​andZ=Pπ.Z = P_{\pi}.Z=Pπ​.

All of the matrices just defined are unitary, and therefore represent quantum operations on a single qubit. For example, here is a calculation that verifies thatHHHis unitary:

And here's the action of the Hadamard operation on a few commonly encountered qubit state vectors.

More succinctly, we've obtained these four equations.

It's worth pausing to consider the fact thatH∣+⟩=∣0⟩H\vert {+} \rangle = \vert 0\rangleH∣+⟩=∣0⟩andH∣−⟩=∣1⟩,H\vert {-} \rangle = \vert 1\rangle,H∣−⟩=∣1⟩,in light of the question suggested in the previous section concerning the distinction between the states∣+⟩\vert {+} \rangle∣+⟩and∣−⟩.\vert {-} \rangle.∣−⟩.Imagine a situation in which a qubit is prepared in one of the two quantum states∣+⟩\vert {+} \rangle∣+⟩and∣−⟩,\vert {-} \rangle,∣−⟩,but where it is not known to us which one it is. Measuring either state produces the same output distribution as the other, as we already observed:000and111both appear with equal probability1/2,1/2,1/2,which provides no information whatsoever about which of the two states was prepared.

However, if we first apply a Hadamard operation and then measure, we obtain the outcome000with certainty if the original state was∣+⟩,\vert {+} \rangle,∣+⟩,and we obtain the outcome1,1,1,again with certainty, if the original state was∣−⟩.\vert {-} \rangle.∣−⟩.The quantum states∣+⟩\vert {+} \rangle∣+⟩and∣−⟩\vert {-} \rangle∣−⟩can therefore be discriminatedperfectly. This reveals that sign changes, or more generally changes to thephases(which are also traditionally calledarguments) of the complex number entries of a quantum state vector, can significantly change that state.

Here's another example, showing how a Hadamard operation acts on a state vector that was mentioned previously.

Next, let's consider the action of aTTToperation on a plus state.

Notice here that we did not bother to convert to the equivalent matrix/vector forms, and instead used the linearity of matrix multiplication together with the formulas

Along similar lines, we may compute the result of applying a Hadamard operation to the quantum state vector just obtained:

The two approaches — one where we explicitly convert to matrix representations and the other where we use linearity and plug in the actions of an operation on standard basis states — are equivalent. We can use whichever one is more convenient in the case at hand.

Compositions of unitary operations are represented by matrix multiplication, just like we had in the probabilistic setting.

For example, suppose we first apply a Hadamard operation, followed by anSSSoperation, followed by another Hadamard operation. The resulting operation, which we shall nameRRRfor the sake of this example, is as follows:

This unitary operationRRRis an interesting example. By applying this operation twice, which is equivalent to squaring its matrix representation, we obtain a NOT operation:

That is,RRRis asquare root of NOToperation. Such a behavior, where the same operation is applied twice to yield a NOT operation, is not possible for a classical operation on a single bit.

In later lessons, we will see many examples of unitary operations on systems having more than two classical states. An example of a unitary operation on a system having three classical states is given by the following matrix.

Assuming that the classical states of the system are0,0,0,1,1,1,and2,2,2,we can describe this operation as addition modulo3.3.3.

The matrixAAAis an example of apermutation matrix, which is a matrix in which every row and column has exactly one1.1.1.Such matrices merely rearrange, or permute, the entries of the vectors they act upon. The identity matrix is perhaps the simplest example of a permutation matrix, and another example is the NOT operation on a bit or qubit. Every permutation matrix, in any positive integer dimension, is unitary. These are the only examples of matrices that represent both classical and quantum operations: a matrix is both stochastic and unitary if and only if it is a permutation matrix.

Another example of a unitary matrix, this time being a4×44\times 44×4matrix, is this one:

This matrix describes an operation known as thequantum Fourier transform, specifically in the4×44\times 44×4case. The quantum Fourier transform can be defined more generally, for any positive integer dimensionn,n,n,and plays a key role in quantum algorithms.

In this section, we'll take a look at some Qiskit implementations of the concepts introduced in this lesson. If you wish to run these implementations yourself, which is strongly encouraged, please consult theInstall Qiskitpage onIBM Quantum Documentationfor details on how to get up and running with Qiskit.

It should be understood that Qiskit is under continual development, and is principally focused on maximizing the performance of the quantum computers it is used to operate, which themselves continue to evolve. As a result, Qiskit is subject to changes that may occasionally lead to code deprecation. With this in mind, we'll shall always execute the following commands prior to presenting examples of Qiskit code in this course, so that it is clear which version of Qiskit has been used. Starting with Qiskit 1.0, this is a simple way to see what version of Qiskit is currently installed.

Output:

Qiskit uses the Python programming language, so before discussing Qiskit specifically, it may be helpful to some to very briefly discuss matrix and vector computations in Python.

In Python, matrix and vector computations can be performed using thearrayclass from theNumPylibrary, which provides functionality for many numerical and scientific computations. The following code loads this library, defines two column vectors,ket0andket1, corresponding to the qubit state vectors∣0⟩\vert 0\rangle∣0⟩and∣1⟩,\vert 1\rangle,∣1⟩,and then prints their average.

Output:

We can also usearrayto create matrices that can represent operations.

Output:

Please note that all code appearing within a given lesson in this course is expected to be run sequentially. So, we don't need to importNumPyagain here, because it has already been imported.

Matrix multiplication, including matrix-vector multiplication as a special case, can be performed using thematmulfunction fromNumPy.

Output:

This output formatting leaves something to be desired, visually speaking. One solution, for situations that demand something prettier, is to use Qiskit'sarray_to_latexfunction from theqiskit.visualizationmodule. Note that, in the code that follow, we're using Python's genericdisplayfunction. In contrast, the specific behavior ofprintmay depending on what is printed, such as it does for arrays defined byNumPy.

Output:

Qiskit includes several classes that allow for states, measurements, and operations to be created and manipulated — so starting from scratch and programming everything needed to simulate quantum states, measurements, and operations in Python is not required. Some examples to help you to get started are included below.

Qiskit'sStatevectorclass provides functionality for defining and manipulating quantum state vectors. In the code that follows, theStatevectorclass is imported and a few vectors are defined. (We're also importing thesqrtfunction from theNumPylibrary to compute a square root. This function could, alternatively, be called asnp.sqrtprovided thatNumPyhas already been imported, as it has above; this is just a different way to import and use this specific function alone.)

No output produced

TheStatevectorclass includes adrawmethod for displaying state vectors in a variety of ways, includingtextfor plain text,latexfor rendered LaTeX, andlatex_sourcefor LaTeX code, which can be handy for cutting and pasting into documents. (Useprintrather thandisplayto show LaTeX code for best results.)

Output:

22∣0⟩+22∣1⟩\frac{\sqrt{2}}{2} |0\rangle+\frac{\sqrt{2}}{2} |1\rangle22​​∣0⟩+22​​∣1⟩

TheStatevectorclass also includes theis_validmethod, which checks to see if a given vector is a valid quantum state vector (i.e., that it has Euclidean norm equal to 1):

Output:

Next we will see one way that measurements of quantum states can be simulated in Qiskit, using themeasuremethod from theStatevectorclass. Let's use the same qubit state vectorvdefined previously.

Output:

(13+2i3)∣0⟩−23∣1⟩(\frac{1}{3} + \frac{2 i}{3}) |0\rangle- \frac{2}{3} |1\rangle(31​+32i​)∣0⟩−32​∣1⟩

Running themeasuremethod simulates a standard basis measurement. It returns the outcome of that measurement, plus the new quantum state vector of the system after the measurement. (Here we're using Python'sprintfunction with anfprefix for formatted printing with embedded expressions.)

Output:

−∣1⟩- |1\rangle−∣1⟩

Measurement outcomes are probabilistic, so this method can return different results when run multiple times. For the particular example of the vectorvdefined above, themeasuremethod defines the quantum state vector after the measurement takes place to be

(rather than∣0⟩\vert 0\rangle∣0⟩) or

(rather than∣1⟩\vert 1\rangle∣1⟩), depending on the measurement outcome. In both cases, the alternatives to∣0⟩\vert 0\rangle∣0⟩and∣1⟩\vert 1\rangle∣1⟩are, in fact, equivalent to these state vectors; they are said to toequivalent up to a global phasebecause one is equal to the other multiplied by a complex number on the unit circle. This issue is discussed in greater detail in theQuantum circuitslesson, and can safely be ignored for now.

Statevectorwill throw an error if themeasuremethod is applied to an invalid quantum state vector.

Statevectoralso comes with asample_countsmethod that allows for the simulation of any number of measurements on the system, each time starting with a fresh copy of the state. For example, the following code shows the outcome of measuring the vectorv100010001000times, which (with high probability) results in the outcome000approximately555out of every999times (or about556556556of the100010001000trials) and the outcome111approximately444out of every999times (or about444444444out of the100010001000trials). The code that follows also demonstrates theplot_histogramfunction from theqiskit.visualizationmodule for visualizing the results.

Output:

Running this code on your own multiple times, with different numbers of samples in place of1000,1000,1000,may be helpful for developing some intuition for how the number of trials influences the number of times each outcome appears. With more and more samples, the fraction of samples for each possibility is likely to get closer and closer to the corresponding probability. This phenomenon, more generally speaking, is known as thelaw of large numbersin probability theory.

Unitary operations can be defined in Qiskit using theOperatorclass, as in the example that follows. This class includes adrawmethod with similar arguments toStatevector. Note that thelatexoption produces results equivalent toarray_from_latex.

Output:

We can apply a unitary operation to a state vector using theevolvemethod.

Output:

(0.1464466094−0.3535533906i)∣0⟩+(−0.3535533906+0.8535533906i)∣1⟩(0.1464466094 - 0.3535533906 i) |0\rangle+(-0.3535533906 + 0.8535533906 i) |1\rangle(0.1464466094−0.3535533906i)∣0⟩+(−0.3535533906+0.8535533906i)∣1⟩

Quantum circuits won't be formally introduced until theQuantum circuitslesson, which is the third lesson in this course, but we can nevertheless experiment with composing qubit unitary operations using Qiskit'sQuantumCircuitclass. In particular, we may define a quantum circuit (which, in this case, will simply be a sequence of unitary operations performed on a single qubit) as follows.

Output:

Here we're using thedrawmethod from theQuantumCircuitclass with themplrenderer (short forMatplotlib, a Python visualization library). This is the only renderer we'll use for quantum circuits in this course, but there are other options, including a text-based and a LaTeX-based renderer.

The operations are applied sequentially, starting on the left and ending on the right in the diagram. A handy way to get the unitary matrix corresponding to this circuit is to use thefrom_circuitmethod from theOperatorclass.

Output:

One can also initialize a starting quantum state vector and then evolve that state according to the sequence of operations described by the circuit.

Output:

(0.1464466094−0.3535533906i)∣0⟩+(−0.3535533906+0.8535533906i)∣1⟩(0.1464466094 - 0.3535533906 i) |0\rangle+(-0.3535533906 + 0.8535533906 i) |1\rangle(0.1464466094−0.3535533906i)∣0⟩+(−0.3535533906+0.8535533906i)∣1⟩

The following code simulates an experiment where the state obtained from the circuit above is measured with a standard basis measurement 4,000 times (using a fresh copy of the state each time).

Output:

Was this page helpful?


---

# Multiple systems

Download the slidesfor this lesson.

Open theYouTube videofor this lesson in a separate window.

This lesson focuses on the basics of quantum information in the context ofmultiplesystems. This context arises both commonly and naturally in information processing, classical and quantum; information-carrying systems are typically constructed from collections of smaller systems, such as bits or qubits.

A simple, yet critically important idea to keep in mind going into this lesson is that we can always choose to view multiple systemstogetheras if they form a single, compound system — to which the discussion in the previous lesson applies. Indeed, this idea very directly leads to a description of how quantum states, measurements, and operations work for multiple systems.

There is, however, more to understanding multiple quantum systems than simply recognizing that they may be viewed collectively as single systems. For instance, we may have multiple quantum systems that are collectively in a particular quantum state, and then choose to measure some but not all of the individual systems. In general, this will affect the state of the systems that were not measured, and it is important to understand exactly how when analyzing quantum algorithms and protocols. An understanding of the sorts ofcorrelationsamong multiple systems — and particularly a type of correlation known asentanglement— is also important in quantum information and computation.

Like we did in the previous lesson, we'll begin this lesson with a discussion of classical information. Once again, the probabilistic and quantum descriptions are mathematically similar, and recognizing how the mathematics works in the familiar setting of classical information is helpful in understanding why quantum information is described in the way that it is.

We'll start at a very basic level, with classical states of multiple systems. For simplicity, we'll begin by discussing just two systems, and then generalize to more than two systems.

To be precise, letX\mathsf{X}Xbe a system whose classical state set isΣ,\Sigma,Σ,and letY\mathsf{Y}Ybe a second system whose classical state set isΓ.\Gamma.Γ.Note that, because we have referred to these sets asclassical state sets, our assumption is thatΣ\SigmaΣandΓ\GammaΓare both finite and nonempty. It could be thatΣ=Γ,\Sigma = \Gamma,Σ=Γ,but this is not necessarily so — and regardless, it will be helpful to use different names to refer to these sets in the interest of clarity.

Now imagine that the two systems,X\mathsf{X}XandY,\mathsf{Y},Y,are placed side-by-side, withX\mathsf{X}Xon the left andY\mathsf{Y}Yon the right. If we so choose, we can view these two systems as if they form a single system, which we can denote by(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)orXY\mathsf{XY}XYdepending on our preference. A natural question to ask about this compound system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is, "What are its classical states?"

The answer is that the set of classical states of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is theCartesian productofΣ\SigmaΣandΓ,\Gamma,Γ,which is the set defined as

In simple terms, the Cartesian product is precisely the mathematical notion that captures the idea of viewing an element of one set and an element of a second set together, as if they form a single element of a single set. In the case at hand, to say that(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is in the classical state(a,b)∈Σ×Γ(a,b)\in\Sigma\times\Gamma(a,b)∈Σ×Γmeans thatX\mathsf{X}Xis in the classical statea∈Σa\in\Sigmaa∈ΣandY\mathsf{Y}Yis in the classical stateb∈Γ;b\in\Gamma;b∈Γ;and if the classical state ofX\mathsf{X}Xisa∈Σa\in\Sigmaa∈Σand the classical state ofY\mathsf{Y}Yisb∈Γ,b\in\Gamma,b∈Γ,then the classical state of the joint system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is(a,b).(a,b).(a,b).

For more than two systems, the situation generalizes in a natural way. If we suppose thatX1,…,Xn\mathsf{X}_1,\ldots,\mathsf{X}_nX1​,…,Xn​are systems having classical state setsΣ1,…,Σn,\Sigma_1,\ldots,\Sigma_n,Σ1​,…,Σn​,respectively, for any positive integern,n,n,the classical state set of thennn-tuple(X1,…,Xn),(\mathsf{X}_1,\ldots,\mathsf{X}_n),(X1​,…,Xn​),viewed as a single joint system, is the Cartesian product

Of course, we are free to use whatever names we wish for systems, and to order them as we choose. In particular, if we havennnsystems like above, we could instead choose to name themX0,…,Xn−1\mathsf{X}_{0},\ldots,\mathsf{X}_{n-1}X0​,…,Xn−1​and arrange them from right to left, so that the joint system becomes(Xn−1,…,X0).(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0).(Xn−1​,…,X0​).Following the same pattern for naming the associated classical states and classical state sets, we might then refer to a classical state

of this compound system. Indeed, this is the ordering convention used by Qiskit when naming multiple qubits. We'll come back to this convention and how it connects to quantum circuits in the next lesson, but we'll start using it now to help to get used to it.

It is often convenient to write a classical state of the form(an−1,…,a0)(a_{n-1},\ldots,a_0)(an−1​,…,a0​)as astringan−1⋯a0a_{n-1}\cdots a_0an−1​⋯a0​for the sake of brevity, particularly in the very typical situation that the classical state setsΣ0,…,Σn−1\Sigma_0,\ldots,\Sigma_{n-1}Σ0​,…,Σn−1​are associated with sets ofsymbolsorcharacters. In this context, the termalphabetis commonly used to refer to sets of symbols used to form strings, but the mathematical definition of an alphabet is precisely the same as the definition of a classical state set: it is a finite and nonempty set.

For example, suppose thatX0,…,X9\mathsf{X}_0,\ldots,\mathsf{X}_9X0​,…,X9​are bits, so that the classical state sets of these systems are all the same.

There are then210=10242^{10} = 1024210=1024classical states of the joint system(X9,…,X0),(\mathsf{X}_9,\ldots,\mathsf{X}_0),(X9​,…,X0​),which are the elements of the set

Written as strings, these classical states look like this:

For the classical state0000000110,0000000110,0000000110,for instance, we see thatX1\mathsf{X}_1X1​andX2\mathsf{X}_2X2​are in the state1,1,1,while all other systems are in the state0.0.0.

Recall from the previous lesson that aprobabilistic stateassociates a probability with each classical state of a system. Thus, a probabilistic state of multiple systems — viewed collectively as a single system — associates a probability with each element of the Cartesian product of the classical state sets of the individual systems.

For example, suppose thatX\mathsf{X}XandY\mathsf{Y}Yare both bits, so that their corresponding classical state sets areΣ={0,1}\Sigma = \{0,1\}Σ={0,1}andΓ={0,1},\Gamma = \{0,1\},Γ={0,1},respectively. Here is a probabilistic state of the pair(X,Y):(\mathsf{X},\mathsf{Y}):(X,Y):

This probabilistic state is one in which bothX\mathsf{X}XandY\mathsf{Y}Yare random bits — each is000with probability1/21/21/2and111with probability1/21/21/2— but the classical states of the two bits always agree. This is an example of acorrelationbetween these systems.

Probabilistic states of systems can be represented by probability vectors, as was discussed in the previous lesson. In particular, the vector entries represent probabilities for the system to be in the possible classical states of that system, and the understanding is that a correspondence between the entries and the set of classical states has been selected. Choosing such a correspondence effectively means deciding on an ordering of the classical states, which is often natural or determined by a standard convention. For example, the binary alphabet{0,1}\{0,1\}{0,1}is naturally ordered with000first and111second, so the first entry in a probability vector representing a probabilistic state of a bit is the probability for it to be in the state0,0,0,and the second entry is the probability for it to be in the state1.1.1.

None of this changes in the context of multiple systems, but there is a decision to be made. The classical state set of multiple systems together, viewed collectively as a single system, is a Cartesian product of the classical state sets of the individual systems — so we must decide how the elements of Cartesian products of classical state sets are ordered.

There is a simple convention that we follow for doing this, which is to start with whatever orderings are already in place for the individual classical state sets, and then to order the elements of the Cartesian productalphabetically.Another way to say this is that the entries in eachnnn-tuple (or, equivalently, the symbols in each string) are treated as though they have significance thatdecreases from left to right.For example, according to this convention, the Cartesian product{1,2,3}×{0,1}\{1,2,3\}\times\{0,1\}{1,2,3}×{0,1}is ordered like this:

Whennnn-tuples are written as strings and ordered in this way, we observe familiar patterns, such as{0,1}×{0,1}\{0,1\}\times\{0,1\}{0,1}×{0,1}being ordered as00,01,10,11,00, 01, 10, 11,00,01,10,11,and the set{0,1}10\{0,1\}^{10}{0,1}10being ordered as it was written earlier in the lesson. As another example, viewing the set{0,1,…,9}×{0,1,…,9}\{0, 1, \dots, 9\} \times \{0, 1, \dots, 9\}{0,1,…,9}×{0,1,…,9}as a set of strings, we obtain the two-digit numbers000000through99,99,99,ordered numerically. This is obviously not a coincidence; our decimal number system uses precisely this sort of alphabetical ordering, where the wordalphabeticalshould be understood as having a broad meaning that includes numerals in addition to letters.

Returning to the example of two bits from above, the probabilistic state described previously is therefore represented by the following probability vector, where the entries are labeled explicitly for the sake of clarity.

A special type of probabilistic state of two systems is one in which the systems areindependent. Intuitively speaking, two systems are independent if learning the classical state of either system has no effect on the probabilities associated with the other. That is, learning what classical state one of the systems is in provides no information at all about the classical state of the other.

To define this notion precisely, let us suppose once again thatX\mathsf{X}XandY\mathsf{Y}Yare systems having classical state setsΣ\SigmaΣandΓ,\Gamma,Γ,respectively. With respect to a given probabilistic state of these systems, they are said to beindependentif it is the case that

for every choice ofa∈Σa\in\Sigmaa∈Σandb∈Γ.b\in\Gamma.b∈Γ.

To express this condition in terms of probability vectors, assume that the given probabilistic state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is described by a probability vector, written in the Dirac notation as

The condition(2)(2)(2)for independence is then equivalent to the existence of two probability vectors

representing the probabilities associated with the classical states ofX\mathsf{X}XandY,\mathsf{Y},Y,respectively, such that

for alla∈Σa\in\Sigmaa∈Σandb∈Γ.b\in\Gamma.b∈Γ.

For example, the probabilistic state of a pair of bits(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)represented by the vector

is one in whichX\mathsf{X}XandY\mathsf{Y}Yare independent. Specifically, the condition required for independence is true for the probability vectors

For instance, to make the probabilities for the000000state match, we need16=14×23,\frac{1}{6} = \frac{1}{4} \times \frac{2}{3},61​=41​×32​,and indeed this is the case. Other entries can be verified in a similar manner.

On the other hand, the probabilistic state(1),(1),(1),which we may write as

does not represent independence between the systemsX\mathsf{X}XandY.\mathsf{Y}.Y.A simple way to argue this follows.

Suppose that there did exist probability vectors∣ϕ⟩\vert \phi\rangle∣ϕ⟩and∣ψ⟩,\vert \psi \rangle,∣ψ⟩,as in equation(3)(3)(3)above, for which the condition(4)(4)(4)is satisfied for every choice ofaaaandb.b.b.It would then necessarily be that

This implies that eitherq0=0q_0 = 0q0​=0orr1=0,r_1 = 0,r1​=0,because if both were nonzero, the productq0r1q_0 r_1q0​r1​would also not be zero. This leads to the conclusion that eitherq0r0=0q_0 r_0 = 0q0​r0​=0(in caseq0=0q_0 = 0q0​=0) orq1r1=0q_1 r_1 = 0q1​r1​=0(in caser1=0r_1 = 0r1​=0). We see, however, that neither of those equalities can be true because we must haveq0r0=1/2q_0 r_0 = 1/2q0​r0​=1/2andq1r1=1/2.q_1 r_1 = 1/2.q1​r1​=1/2.Hence, there do not exist vectors∣ϕ⟩\vert\phi\rangle∣ϕ⟩and∣ψ⟩\vert\psi\rangle∣ψ⟩satisfying the property required for independence.

Having defined independence between two systems, we can now define what is meant bycorrelation:it is alack of independence. For example, because the two bits in the probabilistic state represented by the vector(5)(5)(5)are not independent, they are, by definition, correlated.

The condition of independence just described can be expressed succinctly through the notion of atensor product. Although tensor products are a very general notion, and can be defined quite abstractly and applied to a variety of mathematical structures, we can adopt a simple and concrete definition in the case at hand.

Given two vectors

the tensor product∣ϕ⟩⊗∣ψ⟩\vert \phi \rangle \otimes \vert \psi \rangle∣ϕ⟩⊗∣ψ⟩is the vector defined as

The entries of this new vector correspond to the elements of the Cartesian productΣ×Γ,\Sigma\times\Gamma,Σ×Γ,which are written as strings in the previous equation. Equivalently, the vector∣π⟩=∣ϕ⟩⊗∣ψ⟩\vert \pi \rangle = \vert \phi \rangle \otimes \vert \psi \rangle∣π⟩=∣ϕ⟩⊗∣ψ⟩is defined by the equation

being true for everya∈Σa\in\Sigmaa∈Σandb∈Γ.b\in\Gamma.b∈Γ.

We can now recast the condition for independence: for a joint system(X,Y)(\mathsf{X}, \mathsf{Y})(X,Y)in a probabilistic state represented by a probability vector∣π⟩,\vert \pi \rangle,∣π⟩,the systemsX\mathsf{X}XandY\mathsf{Y}Yare independent if∣π⟩\vert\pi\rangle∣π⟩is obtained by taking a tensor product

of probability vectors∣ϕ⟩\vert \phi \rangle∣ϕ⟩and∣ψ⟩\vert \psi \rangle∣ψ⟩on each of the subsystemsX\mathsf{X}XandY.\mathsf{Y}.Y.In this situation,∣π⟩\vert \pi \rangle∣π⟩is said to be aproduct stateorproduct vector.

We often omit the symbol⊗\otimes⊗when taking the tensor product of kets, such as writing∣ϕ⟩∣ψ⟩\vert \phi \rangle \vert \psi \rangle∣ϕ⟩∣ψ⟩rather than∣ϕ⟩⊗∣ψ⟩.\vert \phi \rangle \otimes \vert \psi \rangle.∣ϕ⟩⊗∣ψ⟩.This convention captures the idea that the tensor product is, in this context, the most natural or default way to take the product of two vectors. Although it is less common, the notation∣ϕ⊗ψ⟩\vert \phi\otimes\psi\rangle∣ϕ⊗ψ⟩is also sometimes used.

When we use the alphabetical convention for ordering elements of Cartesian products, we obtain the following specification for the tensor product of two column vectors.

As an important aside, notice the following expression for tensor products of standard basis vectors:

We could alternatively write(a,b)(a,b)(a,b)as an ordered pair, rather than a string, in which case we obtain∣a⟩⊗∣b⟩=∣(a,b)⟩.\vert a \rangle \otimes \vert b \rangle = \vert (a,b) \rangle.∣a⟩⊗∣b⟩=∣(a,b)⟩.It is, however, more common to omit the parentheses in this situation, instead writing∣a⟩⊗∣b⟩=∣a,b⟩.\vert a \rangle \otimes \vert b \rangle = \vert a,b \rangle.∣a⟩⊗∣b⟩=∣a,b⟩.This is typical in mathematics more generally; parentheses that don't add clarity or remove ambiguity are often simply omitted.

The tensor product of two vectors has the important property that it isbilinear, which means that it is linear in each of the two arguments separately, assuming that the other argument is fixed. This property can be expressed through these equations:

1. Linearity in the first argument:

2. Linearity in the second argument:

Considering the second equation in each of these pairs of equations, we see that scalars "float freely" within tensor products:

There is therefore no ambiguity in simply writingα∣ϕ⟩⊗∣ψ⟩,\alpha\vert\phi\rangle\otimes\vert\psi\rangle,α∣ϕ⟩⊗∣ψ⟩,or alternativelyα∣ϕ⟩∣ψ⟩\alpha\vert\phi\rangle\vert\psi \rangleα∣ϕ⟩∣ψ⟩orα∣ϕ⊗ψ⟩,\alpha\vert\phi\otimes\psi\rangle,α∣ϕ⊗ψ⟩,to refer to this vector.

The notions of independence and tensor products generalize straightforwardly to three or more systems. IfX0,…,Xn−1\mathsf{X}_0,\ldots,\mathsf{X}_{n-1}X0​,…,Xn−1​are systems having classical state setsΣ0,…,Σn−1,\Sigma_0,\ldots,\Sigma_{n-1},Σ0​,…,Σn−1​,respectively, then a probabilistic state of the combined system(Xn−1,…,X0)(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0)(Xn−1​,…,X0​)is aproduct stateif the associated probability vector takes the form

for probability vectors∣ϕ0⟩,…,∣ϕn−1⟩\vert \phi_0 \rangle,\ldots,\vert \phi_{n-1}\rangle∣ϕ0​⟩,…,∣ϕn−1​⟩describing probabilistic states ofX0,…,Xn−1.\mathsf{X}_0,\ldots,\mathsf{X}_{n-1}.X0​,…,Xn−1​.Here, the definition of the tensor product generalizes in a natural way: the vector

is defined by the equation

being true for everya0∈Σ0,…an−1∈Σn−1.a_0\in\Sigma_0, \ldots a_{n-1}\in\Sigma_{n-1}.a0​∈Σ0​,…an−1​∈Σn−1​.

A different, but equivalent, way to define the tensor product of three or more vectors is recursively in terms of tensor products of two vectors:

Similar to the tensor product of just two vectors, the tensor product of three or more vectors is linear in each of the arguments individually, assuming that all other arguments are fixed. In this case, it is said that the tensor product of three or more vectors ismultilinear.

Like in the case of two systems, we could say that the systemsX0,…,Xn−1\mathsf{X}_0,\ldots,\mathsf{X}_{n-1}X0​,…,Xn−1​areindependentwhen they are in a product state, but the termmutually independentis more precise. There happen to be other notions of independence for three or more systems, such aspairwise independence, that are both interesting and important — but not in the context of this course.

Generalizing the observation earlier concerning tensor products of standard basis vectors, for any positive integernnnand any classical statesa0,…,an−1,a_0,\ldots,a_{n-1},a0​,…,an−1​,we have

Now let us move on to measurements of probabilistic states of multiple systems. By choosing to view multiple systems together as single systems, we immediately obtain a specification of how measurements must work for multiple systems — provided thatallof the systems are measured.

For example, if the probabilistic state of two bits(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is described by the probability vector

then the outcome000000— meaning000for the measurement ofX\mathsf{X}Xand000for the measurement ofY\mathsf{Y}Y— is obtained with probability1/21/21/2and the outcome111111is also obtained with probability1/2.1/2.1/2.In each case we update the probability vector description of our knowledge accordingly, so that the probabilistic state becomes∣00⟩|00\rangle∣00⟩or∣11⟩,|11\rangle,∣11⟩,respectively.

We could, however, choose to measure noteverysystem, but instead just some of the systems. This will result in a measurement outcome for each system that gets measured, and will also (in general) affect our knowledge of the remaining systems that we didn't measure.

To explain how this works, we'll focus on the case of two systems, one of which is measured. The more general situation — in which some proper subset of three or more systems is measured — effectively reduces to the case of two systems when we view the systems that are measured collectively as if they form one system and the systems that are not measured as if they form a second system. To be precise, let's suppose thatX\mathsf{X}XandY\mathsf{Y}Yare systems whose classical state sets areΣ\SigmaΣandΓ,\Gamma,Γ,respectively, and that the two systems together are in some probabilistic state. We'll consider what happens when we measure justX\mathsf{X}Xand do nothing toY.\mathsf{Y}.Y.The situation where justY\mathsf{Y}Yis measured and nothing happens toX\mathsf{X}Xis handled symmetrically.

First, we know that the probability to observe a particular classical statea∈Σa\in\Sigmaa∈Σwhen justX\mathsf{X}Xis measured must be consistent with the probabilities we would obtain under the assumption thatY\mathsf{Y}Ywas also measured. That is, we must have

This is the formula for the so-calledreduced(ormarginal) probabilistic state ofX\mathsf{X}Xalone.

This formula makes perfect sense at an intuitive level, in the sense that something very strange would have to happen for it to be wrong. If it were wrong, that would mean that measuringY\mathsf{Y}Ycould somehow influence the probabilities associated with different outcomes of the measurement ofX,\mathsf{X},X,irrespective of the actual outcome of the measurement ofY.\mathsf{Y}.Y.IfY\mathsf{Y}Yhappened to be in a distant location, such as somewhere in another galaxy for instance, this would allow for faster-than-light signaling — which we reject based on our understanding of physics. Another way to understand this comes from the interpretation of probability as reflecting a degree of belief. The mere fact that someone else might decide to look atY\mathsf{Y}Ycannot change the classical state ofX,\mathsf{X},X,so without any information about what they did or didn't see, one's beliefs about the state ofX\mathsf{X}Xshould not change as a result.

Now, given the assumption that onlyX\mathsf{X}Xis measured andY\mathsf{Y}Yis not, there may still exist uncertainty over the classical state ofY.\mathsf{Y}.Y.For this reason, rather than updating our description of the probabilistic state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)to∣ab⟩\vert ab\rangle∣ab⟩for some selection ofa∈Σa\in\Sigmaa∈Σandb∈Γ,b\in\Gamma,b∈Γ,we must update our description so that this uncertainty aboutY\mathsf{Y}Yis properly reflected. The followingconditional probabilityformula reflects this uncertainty.

Here, the expressionPr⁡(Y=b∣X=a)\operatorname{Pr}(\mathsf{Y} = b \,\vert\, \mathsf{X} = a)Pr(Y=b∣X=a)denotes the probability thatY=b\mathsf{Y} = bY=bconditionedon (orgiventhat)X=a.\mathsf{X} = a.X=a.Technically speaking, this expression only makes sense ifPr⁡(X=a)\operatorname{Pr}(\mathsf{X}=a)Pr(X=a)is nonzero, for ifPr⁡(X=a)=0,\operatorname{Pr}(\mathsf{X}=a) = 0,Pr(X=a)=0,then we're dividing by zero and we obtain indeterminate form00.\frac{0}{0}.00​.This is not a problem, though, because if the probability associated withaaais zero, then we'll never obtainaaaas an outcome of a measurement ofX,\mathsf{X},X,so we don't need to be concerned with this possibility.

To express these formulas in terms of probability vectors, consider a probability vector∣ψ⟩\vert \psi \rangle∣ψ⟩describing a joint probabilistic state of(X,Y).(\mathsf{X},\mathsf{Y}).(X,Y).

MeasuringX\mathsf{X}Xalone yields each possible outcomea∈Σa\in\Sigmaa∈Σwith probability

The vector representing the probabilistic state ofX\mathsf{X}Xalone (i.e., the reduced probabilistic state ofX\mathsf{X}X) is therefore given by

Having obtained a particular outcomea∈Σa\in\Sigmaa∈Σof the measurement ofX,\mathsf{X},X,the probabilistic state ofY\mathsf{Y}Yis updated according to the formula for conditional probabilities, so that it is represented by this probability vector:

In the event that the measurement ofX\mathsf{X}Xresulted in the classical statea,a,a,we therefore update our description of the probabilistic state of the joint system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)to∣a⟩⊗∣πa⟩.\vert a\rangle \otimes \vert\pi_a\rangle.∣a⟩⊗∣πa​⟩.

One way to think about this definition of∣πa⟩\vert\pi_a\rangle∣πa​⟩is to see it as anormalizationof the vector∑b∈Γpab∣b⟩,\sum_{b\in\Gamma} p_{ab} \vert b\rangle,∑b∈Γ​pab​∣b⟩,where we divide by the sum of the entries in this vector to obtain a probability vector. This normalization effectively accounts for a conditioning on the event that the measurement ofX\mathsf{X}Xhas resulted in the outcomea.a.a.

For a specific example, suppose that classical state set ofX\mathsf{X}XisΣ={0,1},\Sigma = \{0,1\},Σ={0,1},the classical state set ofY\mathsf{Y}YisΓ={1,2,3},\Gamma = \{1,2,3\},Γ={1,2,3},and the probabilistic state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is

Our goal will be to determine the probabilities of the two possible outcomes (000and111), and to calculate what the resulting probabilistic state ofY\mathsf{Y}Yis for the two outcomes, assuming the systemX\mathsf{X}Xis measured.

Using the bilinearity of the tensor product, and specifically the fact that it is linear in thesecondargument, we may rewrite the vector∣ψ⟩\vert \psi \rangle∣ψ⟩as follows:

In words, what we've done is to isolate the distinct standard basis vectors for the first system (i.e., the one being measured), tensoring each with the linear combination of standard basis vectors for the second system we get by picking out the entries of the original vector that are consistent with the corresponding classical state of the first system. A moment's thought reveals that this is always possible, regardless of what vector we started with.

Having expressed our probability vector in this way, the effects of measuring the first system become easy to analyze. The probabilities of the two outcomes can be obtained by summing the probabilities in parentheses.

These probabilities sum to one, as expected — but this is a useful check on our calculations.

And now, the probabilistic state ofY\mathsf{Y}Yconditioned on each possible outcome can be quickly inferred by normalizing the vectors in parentheses. That is, we divide these vectors by the associated probabilities we just calculated, so that they become probability vectors. Thus, conditioned onX\mathsf{X}Xbeing0,0,0,the probabilistic state ofY\mathsf{Y}Ybecomes

and conditioned on the measurement ofX\mathsf{X}Xbeing 1, the probabilistic state ofY\mathsf{Y}Ybecomes

To conclude this discussion of classical information for multiple systems, we'll consideroperationson multiple systems in probabilistic states. Following the same idea as before, we can view multiple systems collectively as single, compound systems, and then look to the previous lesson to see how this works.

Returning to the typical set-up where we have two systemsX\mathsf{X}XandY,\mathsf{Y},Y,let us consider classical operations on the compound system(X,Y).(\mathsf{X},\mathsf{Y}).(X,Y).Based on the previous lesson and the discussion above, we conclude that any such operation is represented by a stochastic matrix whose rows and columns are indexed by the Cartesian productΣ×Γ.\Sigma\times\Gamma.Σ×Γ.

For example, suppose thatX\mathsf{X}XandY\mathsf{Y}Yare bits, and consider an operation with the following description.

IfX=1,\mathsf{X} = 1,X=1,then perform a NOT operation onY.\mathsf{Y}.Y.Otherwise do nothing.

This is a deterministic operation known as acontrolled-NOToperation, whereX\mathsf{X}Xis thecontrolbit that determines whether or not a NOT operation should be applied to thetargetbitY.\mathsf{Y}.Y.Here is the matrix representation of this operation:

Its action on standard basis states is as follows.

If we were to exchange the roles ofX\mathsf{X}XandY,\mathsf{Y},Y,takingY\mathsf{Y}Yto be the control bit andX\mathsf{X}Xto be the target bit, then the matrix representation of the operation would become

and its action on standard basis states would be like this:

Another example is the operation having this description:

Perform one of the following two operations, each with probability1/2:1/2:1/2:

The matrix representation of this operation is as follows:

The action of this operation on standard basis vectors is as follows:

In these examples, we are simply viewing two systems together as a single system and proceeding as in the previous lesson.

The same thing can be done for any number of systems. For example, imagine that we have three bits, and we increment the three bits modulo888— meaning that we think about the three bits as encoding a number between000and777using binary notation, add1,1,1,and then take the remainder after dividing by8.8.8.One way to express this operation is like this:

Another way to express it is as

assuming we've agreed that numbers from000to777inside of kets refer to the three-bit binary encodings of those numbers. A third option is to express this operation as a matrix.

Now suppose that we have multiple systems and weindependentlyperform different operations on the systems separately.

For example, taking our usual set-up of two systemsX\mathsf{X}XandY\mathsf{Y}Yhaving classical state setsΣ\SigmaΣandΓ,\Gamma,Γ,respectively, let us suppose that we perform one operation onX\mathsf{X}Xand, completely independently, another operation onY.\mathsf{Y}.Y.As we know from the previous lesson, these operations are represented by stochastic matrices — and to be precise, let us say that the operation onX\mathsf{X}Xis represented by the matrixMMMand the operation onY\mathsf{Y}Yis represented by the matrixN.N.N.Thus, the rows and columns ofMMMhave indices that are placed in correspondence with the elements ofΣ\SigmaΣand, likewise, the rows and columns ofNNNcorrespond to the elements ofΓ.\Gamma.Γ.

A natural question to ask is this: if we viewX\mathsf{X}XandY\mathsf{Y}Ytogether as a single, compound system(X,Y),(\mathsf{X},\mathsf{Y}),(X,Y),what is the matrix that represents the combined action of the two operations on this compound system? To answer this question, we must first introduce tensor products of matrices — which are similar to the tensor product of vectors and are defined analogously.

The tensor productM⊗NM\otimes NM⊗Nof the matrices

and

is the matrix

Equivalently, the tensor product ofMMMandNNNis defined by the equation

being true for every selection ofa,b∈Σa,b\in\Sigmaa,b∈Σandc,d∈Γ.c,d\in\Gamma.c,d∈Γ.

An alternative, but equivalent, way to describeM⊗NM\otimes NM⊗Nis that it is the unique matrix that satisfies the equation

for every possible choice of vectors∣ϕ⟩\vert\phi\rangle∣ϕ⟩and∣ψ⟩,\vert\psi\rangle,∣ψ⟩,assuming that the indices of∣ϕ⟩\vert\phi\rangle∣ϕ⟩correspond to the elements ofΣ\SigmaΣand the indices of∣ψ⟩\vert\psi\rangle∣ψ⟩correspond toΓ.\Gamma.Γ.

Following the convention described previously for ordering the elements of Cartesian products, we can also write the tensor product of two matrices explicitly as follows:

Tensor products of three or more matrices are defined in an analogous way. IfM0,…,Mn−1M_0, \ldots, M_{n-1}M0​,…,Mn−1​are matrices whose indices correspond to classical state setsΣ0,…,Σn−1,\Sigma_0,\ldots,\Sigma_{n-1},Σ0​,…,Σn−1​,then the tensor productMn−1⊗⋯⊗M0M_{n-1}\otimes\cdots\otimes M_0Mn−1​⊗⋯⊗M0​is defined by the condition that

for every choice of classical statesa0,b0∈Σ0,…,an−1,bn−1∈Σn−1.a_0,b_0\in\Sigma_0,\ldots,a_{n-1},b_{n-1}\in\Sigma_{n-1}.a0​,b0​∈Σ0​,…,an−1​,bn−1​∈Σn−1​.Alternatively, tensor products of three or more matrices can be defined recursively, in terms of tensor products of two matrices, similar to what we observed for vectors.

The tensor product of matrices is sometimes said to bemultiplicativebecause the equation

is always true, for any choice of matricesM0,…,Mn−1M_0,\ldots,M_{n-1}M0​,…,Mn−1​andN0…,Nn−1,N_0\ldots,N_{n-1},N0​…,Nn−1​,provided that the productsM0N0,…,Mn−1Nn−1M_0 N_0, \ldots, M_{n-1} N_{n-1}M0​N0​,…,Mn−1​Nn−1​make sense.

We can now answer the question asked previously: ifMMMis a probabilistic operation onX,\mathsf{X},X,NNNis a probabilistic operation onY,\mathsf{Y},Y,and the two operations are performed independently, then the resulting operation on the compound system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is the tensor productM⊗N.M\otimes N.M⊗N.

So, for both probabilistic states and probabilistic operations,tensor products represent independence.If we have two systemsX\mathsf{X}XandY\mathsf{Y}Ythat are independently in the probabilistic states∣ϕ⟩\vert\phi\rangle∣ϕ⟩and∣π⟩,\vert\pi\rangle,∣π⟩,then the compound system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is in the probabilistic state∣ϕ⟩⊗∣π⟩;\vert\phi\rangle\otimes\vert\pi\rangle;∣ϕ⟩⊗∣π⟩;and if we apply probabilistic operationsMMMandNNNto the two systems independently, then the resulting action on the compound system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is described by the operationM⊗N.M\otimes N.M⊗N.

Let's take a look at an example, which recalls a probabilistic operation on a single bit from the previous lesson: if the classical state of the bit is0,0,0,it is left alone; and if the classical state of the bit is1,1,1,it is flipped to 0 with probability1/2.1/2.1/2.We observed that this operation is represented by the matrix

If this operation is performed on a bitX,\mathsf{X},X,and a NOT operation is (independently) performed on a second bitY,\mathsf{Y},Y,then the joint operation on the compound system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)has the matrix representation

By inspection, we see that this is a stochastic matrix. This will always be the case: the tensor product of two or more stochastic matrices is always stochastic.

A common situation that we encounter is one in which one operation is performed on one system andnothingis done to another. In such a case, exactly the same prescription is followed, bearing in mind thatdoing nothingis represented by the identity matrix. For example, resetting the bitX\mathsf{X}Xto the000state and doing nothing toY\mathsf{Y}Yyields the probabilistic (and in fact deterministic) operation on(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)represented by the matrix

We're now prepared to move on to quantum information in the setting of multiple systems. Much like in the previous lesson on single systems, the mathematical description of quantum information for multiple systems is quite similar to the probabilistic case and makes use of similar concepts and techniques.

Multiple systems can be viewed collectively as single, compound systems. We've already observed this in the probabilistic setting, and the quantum setting is analogous. Quantum states of multiple systems are therefore represented by column vectors having complex number entries and Euclidean norm equal to1,1,1,just like quantum states of single systems. In the multiple system case, the entries of these vectors are placed in correspondence with theCartesian productof the classical state sets associated with each of the individual systems, because that's the classical state set of the compound system.

For instance, ifX\mathsf{X}XandY\mathsf{Y}Yare qubits, then the classical state set of the pair of qubits(X,Y),(\mathsf{X},\mathsf{Y}),(X,Y),viewed collectively as a single system, is the Cartesian product{0,1}×{0,1}.\{0,1\}\times\{0,1\}.{0,1}×{0,1}.By representing pairs of binary values as binary strings of length two, we associate this Cartesian product set with the set{00,01,10,11}.\{00,01,10,11\}.{00,01,10,11}.The following vectors are therefore all examples of quantum state vectors of the pair(X,Y):(\mathsf{X},\mathsf{Y}):(X,Y):

There are variations on how quantum state vectors of multiple systems are expressed, and we can choose whichever variation suits our preferences. Here are some examples for the first quantum state vector above.

We may use the fact that∣ab⟩=∣a⟩∣b⟩\vert ab\rangle = \vert a\rangle \vert b\rangle∣ab⟩=∣a⟩∣b⟩(for any classical statesaaaandbbb) to instead write

We may choose to write the tensor product symbol explicitly like this:

We may subscript the kets to indicate how they correspond to the systems being considered, like this:

Of course, we may also write quantum state vectors explicitly as column vectors:

Depending upon the context in which it appears, one of these variations may be preferred — but they are all equivalent in the sense that they describe the same vector.

Similar to what we have for probability vectors, tensor products of quantum state vectors are also quantum state vectors — and again they representindependenceamong systems.

In greater detail, and beginning with the case of two systems, suppose that∣ϕ⟩\vert \phi \rangle∣ϕ⟩is a quantum state vector of a systemX\mathsf{X}Xand∣ψ⟩\vert \psi \rangle∣ψ⟩is a quantum state vector of a systemY.\mathsf{Y}.Y.The tensor product∣ϕ⟩⊗∣ψ⟩,\vert \phi \rangle \otimes \vert \psi \rangle,∣ϕ⟩⊗∣ψ⟩,which may alternatively be written as∣ϕ⟩∣ψ⟩\vert \phi \rangle \vert \psi \rangle∣ϕ⟩∣ψ⟩or as∣ϕ⊗ψ⟩,\vert \phi \otimes \psi \rangle,∣ϕ⊗ψ⟩,is then a quantum state vector of the joint system(X,Y).(\mathsf{X},\mathsf{Y}).(X,Y).Again we refer to a state of this form as a being aproduct state. Intuitively speaking, when a pair of systems(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is in a product state∣ϕ⟩⊗∣ψ⟩,\vert \phi \rangle \otimes \vert \psi \rangle,∣ϕ⟩⊗∣ψ⟩,we may interpret this as meaning thatX\mathsf{X}Xis in the quantum state∣ϕ⟩,\vert \phi \rangle,∣ϕ⟩,Y\mathsf{Y}Yis in the quantum state∣ψ⟩,\vert \psi \rangle,∣ψ⟩,and the states of the two systems have nothing to do with one another.

The fact that the tensor product vector∣ϕ⟩⊗∣ψ⟩\vert \phi \rangle \otimes \vert \psi \rangle∣ϕ⟩⊗∣ψ⟩is indeed a quantum state vector is consistent with the Euclidean norm beingmultiplicativewith respect to tensor products:

Because∣ϕ⟩\vert \phi \rangle∣ϕ⟩and∣ψ⟩\vert \psi \rangle∣ψ⟩are quantum state vectors, we have∥∣ϕ⟩∥=1\|\vert \phi \rangle\| = 1∥∣ϕ⟩∥=1and∥∣ψ⟩∥=1,\|\vert \psi \rangle\| = 1,∥∣ψ⟩∥=1,and therefore∥∣ϕ⟩⊗∣ψ⟩∥=1,\|\vert \phi \rangle \otimes \vert \psi \rangle\| = 1,∥∣ϕ⟩⊗∣ψ⟩∥=1,so∣ϕ⟩⊗∣ψ⟩\vert \phi \rangle \otimes \vert \psi \rangle∣ϕ⟩⊗∣ψ⟩is also a quantum state vector.

This discussion may be generalized to more than two systems. If∣ψ0⟩,…,∣ψn−1⟩\vert \psi_0 \rangle,\ldots,\vert \psi_{n-1} \rangle∣ψ0​⟩,…,∣ψn−1​⟩are quantum state vectors of systemsX0,…,Xn−1,\mathsf{X}_0,\ldots,\mathsf{X}_{n-1},X0​,…,Xn−1​,then∣ψn−1⟩⊗⋯⊗∣ψ0⟩\vert \psi_{n-1} \rangle\otimes\cdots\otimes \vert \psi_0 \rangle∣ψn−1​⟩⊗⋯⊗∣ψ0​⟩is a quantum state vector representing aproduct stateof the joint system(Xn−1,…,X0).(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0).(Xn−1​,…,X0​).Again, we know that this is a quantum state vector because

Not all quantum state vectors of multiple systems are product states. For example, the quantum state vector

of two qubits is not a product state. To reason this, we may follow exactly the same argument that we used to prove that the probabilistic state represented by the vector(5)(5)(5)is not a product state. That is, if(6)(6)(6)were a product state, there would exist quantum state vectors∣ϕ⟩\vert\phi\rangle∣ϕ⟩and∣ψ⟩\vert\psi\rangle∣ψ⟩for which

But then it would necessarily be the case that

implying that⟨0∣ϕ⟩=0\langle 0 \vert \phi\rangle = 0⟨0∣ϕ⟩=0or⟨1∣ψ⟩=0\langle 1 \vert \psi\rangle = 0⟨1∣ψ⟩=0(or both). That contradicts the fact that

and

are both nonzero.

Notice that the specific value1/21/\sqrt{2}1/2​is not important to this argument — all that is important is that this value is nonzero. Thus, for instance, the quantum state

is also not a product state, by the same argument.

It follows that the quantum state vector(6)(6)(6)represents acorrelationbetween two systems, and specifically we say that the systems areentangled.

Entanglement is a quintessential feature of quantum information that will be discussed in much greater detail in later lessons. Entanglement can be complicated, particularly for the sorts of noisy quantum states that can be described by density matrices in the general formulation of quantum information, which was mentioned in the previous lesson. For quantum state vectors in the simplified formulation of quantum information that we're focusing on in this course, however, entanglement is equivalent to correlation: any quantum state vector that is not a product state represents an entangled state.

In contrast, the quantum state vector

is an example of a product state.

Hence, this state is not entangled.

We'll now take a look as some important examples of multiple-qubit quantum states, beginning with theBell states. These are the following four two-qubit states:

The Bell states are so-named in honor ofJohn Bell. Notice that the same argument that establishes that∣ϕ+⟩\vert\phi^+\rangle∣ϕ+⟩is not a product state reveals that none of the other Bell states is a product state either: all four of the Bell states represent entanglement between two qubits.

The collection of all four Bell states

is known as theBell basis.True to its name, this is a basis; any quantum state vector of two qubits, or indeed any complex vector at all having entries corresponding to the four classical states of two bits, can be expressed as a linear combination of the four Bell states. For example,

Next we will consider two interesting examples of states of three qubits. The first example is theGHZ state(so named in honor of Daniel Greenberger, Michael Horne, and Anton Zeilinger, who first studied some of its properties):

The second example is the so-called W state:

Neither of these states is a product state, meaning that they cannot be written as a tensor product of three qubit quantum state vectors. We'll examine both of these two states further when we discuss partial measurements of quantum states of multiple systems, and they'll arise from time to time throughout this series.

The examples of quantum states of multiple systems we've seen so far are states of two or three qubits, but we can also consider quantum states of multiple systems having different classical state sets.

For example, here's a quantum state of three systems,X,\mathsf{X},X,Y,\mathsf{Y},Y,andZ,\mathsf{Z},Z,where the classical state set ofX\mathsf{X}Xis the binary alphabet (soX\mathsf{X}Xis a qubit) and the classical state set ofY\mathsf{Y}YandZ\mathsf{Z}Zis{♣,♢,♡,♠}:\{\clubsuit,\diamondsuit,\heartsuit,\spadesuit\}:{♣,♢,♡,♠}:

And here's an example of a quantum state of three systems,X,\mathsf{X},X,Y,\mathsf{Y},Y,andZ,\mathsf{Z},Z,that all share the same classical state set{0,1,2}:\{0,1,2\}:{0,1,2}:

Systems having the classical state set{0,1,2}\{0,1,2\}{0,1,2}are often calledtritsor (assuming that they can be in a quantum state)qutrits. The termquditrefers to a system having classical state set{0,…,d−1}\{0,\ldots,d-1\}{0,…,d−1}for an arbitrary choice ofd.d.d.

Standard basis measurements of quantum states of single systems were discussed in the previous lesson: if a system having classical state setΣ\SigmaΣis in a quantum state represented by the vector∣ψ⟩,\vert \psi \rangle,∣ψ⟩,and that system is measured (with respect to a standard basis measurement), then each classical statea∈Σa\in\Sigmaa∈Σappears with probability∣⟨a∣ψ⟩∣2.\vert \langle a \vert \psi \rangle\vert^2.∣⟨a∣ψ⟩∣2.

This tells us what happens when we have a quantum state of multiple systems and choose to measure the entire compound system (which is equivalent to measuringallof the systems). To state this precisely, let us suppose thatX0,…,Xn−1\mathsf{X}_0,\ldots,\mathsf{X}_{n-1}X0​,…,Xn−1​are systems having classical state setsΣ0,…,Σn−1,\Sigma_0,\ldots,\Sigma_{n-1},Σ0​,…,Σn−1​,respectively. We may then view(Xn−1,…,X0)(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0)(Xn−1​,…,X0​)collectively as a single system whose classical state set is the Cartesian productΣn−1×⋯×Σ0.\Sigma_{n-1}\times\cdots\times\Sigma_0.Σn−1​×⋯×Σ0​.If a quantum state of this system is represented by the quantum state vector∣ψ⟩,\vert\psi\rangle,∣ψ⟩,and all of the systems are measured, then each possible outcome(an−1,…,a0)∈Σn−1×⋯×Σ0(a_{n-1},\ldots,a_0)\in\Sigma_{n-1}\times\cdots\times\Sigma_0(an−1​,…,a0​)∈Σn−1​×⋯×Σ0​appears with probability∣⟨an−1⋯a0∣ψ⟩∣2.\vert\langle a_{n-1}\cdots a_0\vert \psi\rangle\vert^2.∣⟨an−1​⋯a0​∣ψ⟩∣2.

For example, if systemsX\mathsf{X}XandY\mathsf{Y}Yare jointly in the quantum state

then measuring both systems with standard basis measurements yields the outcome(0,♡)(0,\heartsuit)(0,♡)with probability9/259/259/25and the outcome(1,♠)(1,\spadesuit)(1,♠)with probability16/25.16/25.16/25.

Now let us consider the situation in which we have multiple systems in some quantum state, and we measure a proper subset of the systems. As before, we will begin with two systemsX\mathsf{X}XandY\mathsf{Y}Yhaving classical state setsΣ\SigmaΣandΓ,\Gamma,Γ,respectively.

In general, a quantum state vector of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)takes the form

where{αab:(a,b)∈Σ×Γ}\{\alpha_{ab} : (a,b)\in\Sigma\times\Gamma\}{αab​:(a,b)∈Σ×Γ}is a collection of complex numbers satisfying

which is equivalent to∣ψ⟩\vert \psi \rangle∣ψ⟩being a unit vector.

We already know, from the discussion above, that if bothX\mathsf{X}XandY\mathsf{Y}Yare measured, then each possible outcome(a,b)∈Σ×Γ(a,b)\in\Sigma\times\Gamma(a,b)∈Σ×Γappears with probability

If we suppose instead that just the first systemX\mathsf{X}Xis measured, the probability for each outcomea∈Σa\in\Sigmaa∈Σto appear must therefore be equal to

This is consistent with what we already saw in the probabilistic setting, as well as our current understanding of physics; the probability for each outcome to appear whenX\mathsf{X}Xis measured can't possibly depend on whether or notY\mathsf{Y}Ywas also measured, as that would allow for faster-than-light communication.

Having obtained a particular outcomea∈Σa\in\Sigmaa∈Σof a standard basis measurement ofX,\mathsf{X},X,we naturally expect that the quantum state ofX\mathsf{X}Xchanges so that it is equal to∣a⟩,\vert a\rangle,∣a⟩,just like we had for single systems. But what happens to the quantum state ofY\mathsf{Y}Y? To answer this question, we can first express the vector∣ψ⟩\vert\psi\rangle∣ψ⟩as

where

for eacha∈Σ.a\in\Sigma.a∈Σ.Here we're following the same methodology as in the probabilistic case, of isolating the standard basis states of the system being measured. The probability for the standard basis measurement ofX\mathsf{X}Xto give each outcomeaaais as follows:

And, as a result of the standard basis measurement ofX\mathsf{X}Xgiving the outcomea,a,a,the quantum state of the pair(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)together becomes

That is, the state "collapses" like in the single-system case, but only as far as is required for the state to be consistent with the measurement ofX\mathsf{X}Xhaving produced the outcomea.a.a.

Informally speaking,∣a⟩⊗∣ϕa⟩\vert a \rangle \otimes \vert \phi_a\rangle∣a⟩⊗∣ϕa​⟩represents the component of∣ψ⟩\vert \psi\rangle∣ψ⟩that is consistent with the a measurement ofX\mathsf{X}Xresulting in the outcomea.a.a.We thennormalizethis vector — by dividing it by its Euclidean norm, which is equal to∥∣ϕa⟩∥\|\vert\phi_a\rangle\|∥∣ϕa​⟩∥— to obtain a valid quantum state vector having Euclidean norm equal to1.1.1.This normalization step is analogous to what we did in the probabilistic setting when we divided vectors by the sum of their entries to obtain a probability vector.

As an example, consider the state of two qubits(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)from the beginning of the section:

To understand what happens when the first systemX\mathsf{X}Xis measured, we begin by writing

We now see, based on the description above, that the probability for the measurement to result in the outcome000is

in which case the state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)becomes

and the probability for the measurement to result in the outcome111is

in which case the state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)becomes

The same technique, used in a symmetric way, describes what happens if the second systemY\mathsf{Y}Yis measured rather than the first. This time we rewrite the vector∣ψ⟩\vert \psi \rangle∣ψ⟩as

The probability that the measurement ofY\mathsf{Y}Ygives the outcome000is

in which case the state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)becomes

and the probability that the measurement outcome is111is

in which case the state of(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)becomes

The previous example shows a limitation of the simplified description of quantum information, which is that it does not offer us a way to describe the reduced (or marginal) quantum state of just one of two systems (or of a proper subset of any number of systems) like in the probabilistic case.

Specifically, for a probabilistic state of two systems(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)described by a probability vector

we can write thereduced(ormarginal) probabilistic state ofX\mathsf{X}Xalone as

For quantum state vectors, there is no analogous way to do this. In particular, for a quantum state vector

the vector

is not a quantum state vector in general, and does not properly represent the concept of a reduced or marginal state.

What we may do instead is turn to theGeneral formulation of quantum information, which is the subject of the third course in theUnderstanding Quantum Information and Computation Series.That formulation provides with a meaningful way to define reduced quantum states that is analogous to the probabilistic setting.

Partial measurements for three or more systems, where some proper subset of the systems are measured, can be reduced to the case of two systems by dividing the systems into two collections, those that are measured and those that are not. Here is a specific example that illustrates how this can be done. It demonstrates how subscripting kets by the names of the systems they represent can be useful — in this case because it gives us a simple way to describe permutations of the systems.

For this example, we'll consider a quantum state of a 5-tuple of systems(X4,…,X0),(\mathsf{X}_4,\ldots,\mathsf{X}_0),(X4​,…,X0​),where all five of these systems share the same classical state set{♣,♢,♡,♠}:\{\clubsuit,\diamondsuit,\heartsuit,\spadesuit\}:{♣,♢,♡,♠}:

We'll consider the situation in which the first and third systems are measured, and the remaining systems are left alone.

Conceptually speaking, there's no fundamental difference between this situation and one in which one of two systems is measured. Unfortunately, because the measured systems are interspersed with the unmeasured systems, we face a hurdle in writing down the expressions needed to perform these calculations. One way to proceed, as suggested above, is to subscript the kets to indicate which systems they refer to. This gives us a way to keep track of the systems as we permute the ordering of the kets, which makes the mathematics simpler.

First, the quantum state vector above can alternatively be written as

Nothing has changed, except that each ket now has a subscript indicating which system it corresponds to. Here we've used the subscripts0,…,4,0,\ldots,4,0,…,4,but the names of the systems themselves could also be used (in a situation where we have system names such asX,\mathsf{X},X,Y,\mathsf{Y},Y,andZ,\mathsf{Z},Z,for instance).

We can now re-order the kets and collect terms as follows:

The tensor products are still implicit, even when parentheses are used, as in this example.

To be clear about permuting the kets, tensor products are not commutative: if∣ϕ⟩\vert \phi\rangle∣ϕ⟩and∣π⟩\vert \pi \rangle∣π⟩are vectors, then, in general,∣ϕ⟩⊗∣π⟩\vert \phi\rangle\otimes\vert \pi \rangle∣ϕ⟩⊗∣π⟩is different from∣π⟩⊗∣ϕ⟩,\vert \pi\rangle\otimes\vert \phi \rangle,∣π⟩⊗∣ϕ⟩,and likewise for tensor products of three or more vectors. For instance,∣♡⟩∣♣⟩∣♢⟩∣♠⟩∣♠⟩\vert\heartsuit\rangle \vert\clubsuit\rangle \vert\diamondsuit\rangle \vert\spadesuit\rangle \vert\spadesuit\rangle∣♡⟩∣♣⟩∣♢⟩∣♠⟩∣♠⟩is a different vector than∣♡⟩∣♢⟩∣♣⟩∣♠⟩∣♠⟩.\vert\heartsuit\rangle \vert\diamondsuit\rangle \vert\clubsuit\rangle \vert\spadesuit\rangle \vert\spadesuit\rangle.∣♡⟩∣♢⟩∣♣⟩∣♠⟩∣♠⟩.Re-ordering the kets as we have just done should not be interpreted as suggesting otherwise. Rather, for the sake of performing calculations, we're simply making a decision that it's more convenient to collect the systems together as(X4,X2,X3,X1,X0)(\mathsf{X}_4,\mathsf{X}_2,\mathsf{X}_3,\mathsf{X}_1,\mathsf{X}_0)(X4​,X2​,X3​,X1​,X0​)rather than(X4,X3,X2,X1,X0).(\mathsf{X}_4,\mathsf{X}_3,\mathsf{X}_2,\mathsf{X}_1,\mathsf{X}_0).(X4​,X3​,X2​,X1​,X0​).The subscripts on the kets serve to keep this all straight, and we're free to revert back to the original order later if we wish to do that.

We now see that, if the systemsX4\mathsf{X}_4X4​andX2\mathsf{X}_2X2​are measured, the (nonzero) probabilities of the different outcomes are as follow:

If the measurement outcome is(♡,♢),(\heartsuit,\diamondsuit),(♡,♢),for instance, the resulting state of our five systems becomes

Here, for the final answer, we've reverted back to our original ordering of the systems, just to illustrate that we can do this. For the other possible measurement outcomes, the state can be determined in a similar way.

Finally, here are two examples promised earlier, beginning with the GHZ state

If just the first system is measured, we obtain the outcome000with probability1/2,1/2,1/2,in which case the state of the three qubits becomes∣000⟩;\vert 000\rangle;∣000⟩;and we also obtain the outcome111with probability1/2,1/2,1/2,in which case the state of the three qubits becomes∣111⟩.\vert 111\rangle.∣111⟩.

For a W state, on the other hand, assuming again that just the first system is measured, we begin by writing this state like this:

The probability that a measurement of the first qubit results in the outcome 0 is therefore equal to

and conditioned upon the measurement producing this outcome, the quantum state of the three qubits becomes

The probability that the measurement outcome is 1 is1/3,1/3,1/3,in which case the state of the three qubits becomes∣100⟩.\vert 100\rangle.∣100⟩.

The W state is symmetric, in the sense that it doens't change if we permute the qubits. We therefore obtain a similar description for measuring the second or third qubit rather than the first.

In principle, any unitary matrix whose rows and columns correspond to the classical states of a system represents a valid quantum operation on that system. This, of course, holds true for compound systems, whose classical state sets happen to be Cartesian products of the classical state sets of the individual systems.

Focusing in on two systems, ifX\mathsf{X}Xis a system having classical state setΣ,\Sigma,Σ,andY\mathsf{Y}Yis a system having classical state setΓ,\Gamma,Γ,then the classical state set of the joint system(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)isΣ×Γ.\Sigma\times\Gamma.Σ×Γ.Therefore, quantum operations on this joint system are represented by unitary matrices whose rows and columns are placed in correspondence with the setΣ×Γ.\Sigma\times\Gamma.Σ×Γ.The ordering of the rows and columns of these matrices is the same as the ordering used for quantum state vectors of the system(X,Y).(\mathsf{X},\mathsf{Y}).(X,Y).

For example, let us suppose thatΣ={1,2,3}\Sigma = \{1,2,3\}Σ={1,2,3}andΓ={0,1},\Gamma = \{0,1\},Γ={0,1},and recall that the standard convention for ordering the elements of the Cartesian product{1,2,3}×{0,1}\{1,2,3\}\times\{0,1\}{1,2,3}×{0,1}is this:

Here's an example of a unitary matrix representing an operation on(X,Y):(\mathsf{X},\mathsf{Y}):(X,Y):

This unitary matrix isn't special, it's just an example. To check thatUUUis unitary, it suffices to compute and check thatU†U=I,U^{\dagger} U = \mathbb{I},U†U=I,for instance. Alternatively, we can check that the rows (or the columns) are orthonormal, which is made simpler in this case given the particular form of the matrixU.U.U.

The action ofUUUon the standard basis vector∣1,1⟩,\vert 1, 1 \rangle,∣1,1⟩,for instance, is

which we can see by examining the second column ofU,U,U,considering our ordering of the set{1,2,3}×{0,1}.\{1,2,3\}\times\{0,1\}.{1,2,3}×{0,1}.

As with any matrix, it is possible to expressUUUusing Dirac notation, which would require 20 terms for the 20 nonzero entries ofU.U.U.If we did write down all of these terms, however, rather than writing a6×66\times 66×6matrix, it would be messy and the patterns that are evident from the matrix expression would not likely be as clear. Simply put, Dirac notation is not always the best choice.

Unitary operations on three or more systems work in a similar way, with the unitary matrices having rows and columns corresponding to the Cartesian product of the classical state sets of the systems. We've already seen one example in this lesson: the three-qubit operation

where numbers in bras and kets mean their333-bit binary encodings. In addition to being a deterministic operation, this is also a unitary operation. Operations that are both deterministic and unitary are calledreversibleoperations. The conjugate transpose of this matrix can be written like this:

This represents thereverse, or in mathematical terms theinverse, of the original operation — which is what we expect from the conjugate transpose of a unitary matrix. We'll see other examples of unitary operations on multiple systems as the lesson continues.

When unitary operations are performed independently on a collection of individual systems, the combined action of these independent operations is described by the tensor product of the unitary matrices that represent them. That is, ifX0,…,Xn−1\mathsf{X}_{0},\ldots,\mathsf{X}_{n-1}X0​,…,Xn−1​are quantum systems,U0,…,Un−1U_0,\ldots, U_{n-1}U0​,…,Un−1​are unitary matrices representing operations on these systems, and the operations are performed independently on the systems, the combined action on(Xn−1,…,X0)(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0)(Xn−1​,…,X0​)is represented by the matrixUn−1⊗⋯⊗U0.U_{n-1}\otimes\cdots\otimes U_0.Un−1​⊗⋯⊗U0​.Once again, we find that the probabilistic and quantum settings are analogous in this regard.

One would naturally expect, from reading the previous paragraph, that the tensor product of any collection of unitary matrices is unitary. Indeed this is true, and we can verify it as follows.

Notice first that the conjugate transpose operation satisfies

for any chosen matricesM0,…,Mn−1.M_0,\ldots,M_{n-1}.M0​,…,Mn−1​.This can be checked by going back to the definition of the tensor product and of the conjugate transpose, and checking that each entry of the two sides of the equation are in agreement. This means that

Because the tensor product of matrices is multiplicative, we find that

Here we have writtenI0,…,In−1\mathbb{I}_0,\ldots,\mathbb{I}_{n-1}I0​,…,In−1​to refer to the matrices representing the identity operation on the systemsX0,…,Xn−1,\mathsf{X}_0,\ldots,\mathsf{X}_{n-1},X0​,…,Xn−1​,which is to say that these are identity matrices whose sizes agree with the number of classical states ofX0,…,Xn−1.\mathsf{X}_0,\ldots,\mathsf{X}_{n-1}.X0​,…,Xn−1​.

Finally, the tensor productIn−1⊗⋯⊗I0\mathbb{I}_{n-1} \otimes \cdots \otimes \mathbb{I}_0In−1​⊗⋯⊗I0​is equal to the identity matrix for which we have a number of rows and columns that agrees with the product of the number of rows and columns of the matricesIn−1,…,I0.\mathbb{I}_{n-1},\ldots,\mathbb{I}_0.In−1​,…,I0​.This larger identity matrix represents the identity operation on the joint system(Xn−1,…,X0).(\mathsf{X}_{n-1},\ldots,\mathsf{X}_0).(Xn−1​,…,X0​).

In summary, we have the following sequence of equalities:

We therefore conclude thatUn−1⊗⋯⊗U0U_{n-1} \otimes \cdots \otimes U_0Un−1​⊗⋯⊗U0​is unitary.

An important situation that often arises is one in which a unitary operation is applied to just one system — or a proper subset of systems — within a larger joint system. For instance, suppose thatX\mathsf{X}XandY\mathsf{Y}Yare systems that we can view together as forming a single, compound system(X,Y),(\mathsf{X},\mathsf{Y}),(X,Y),and we perform an operation just on the systemX.\mathsf{X}.X.To be precise, let us suppose thatUUUis a unitary matrix representing an operation onX,\mathsf{X},X,so that its rows and columns have been placed in correspondence with the classical states ofX.\mathsf{X}.X.

To say that we perform the operation represented byUUUjust on the systemX\mathsf{X}Ximplies that we do nothing toY,\mathsf{Y},Y,meaning that we independently performUUUonX\mathsf{X}Xand theidentity operationonY.\mathsf{Y}.Y.That is, "doing nothing" toY\mathsf{Y}Yis equivalent to performing the identity operation onY,\mathsf{Y},Y,which is represented by the identity matrixIY.\mathbb{I}_\mathsf{Y}.IY​.(Here, by the way, the subscriptY\mathsf{Y}Ytells us thatIY\mathbb{I}_\mathsf{Y}IY​refers to the identity matrix having a number of rows and columns in agreement with the classical state set ofY.\mathsf{Y}.Y.) The operation on(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)that is obtained when we performUUUonX\mathsf{X}Xand do nothing toY\mathsf{Y}Yis therefore represented by the unitary matrix

For example, ifX\mathsf{X}XandY\mathsf{Y}Yare qubits, performing a Hadamard operation onX\mathsf{X}X(and doing nothing toY\mathsf{Y}Y) is equivalent to performing the operation

on the joint system(X,Y).(\mathsf{X},\mathsf{Y}).(X,Y).

Along similar lines, if an operation represented by a unitary matrixUUUis applied toY\mathsf{Y}Yand nothing is done toX,\mathsf{X},X,the resulting operation on(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is represented by the unitary matrix

For example, if we again consider the situation in which bothX\mathsf{X}XandY\mathsf{Y}Yare qubits andUUUis a Hadamard operation, the resulting operation on(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is represented by the matrix

Not every unitary operation on a collection of systems can be written as a tensor product of unitary operations like this, just as not every quantum state vector of these systems is a product state. For example, neither the swap operation nor the controlled-NOT operation on two qubits, which are described below, can be expressed as a tensor product of unitary operations.

To conclude the lesson, let's take a look at two classes of examples of unitary operations on multiple systems, beginning with theswap operation.

Suppose thatX\mathsf{X}XandY\mathsf{Y}Yare systems that share the same classical state setΣ.\Sigma.Σ.Theswapoperation on the pair(X,Y)(\mathsf{X},\mathsf{Y})(X,Y)is the operation that exchanges the contents of the two systems, but otherwise leaves the systems alone — so thatX\mathsf{X}Xremains on the left andY\mathsf{Y}Yremains on the right. We'll denote this operation asSWAP⁡,\operatorname{SWAP},SWAP,and it operates like this for every choice of classical statesa,b∈Σ:a,b\in\Sigma:a,b∈Σ:

One way to write the matrix associated with this operation using the Dirac notation is as follows:

It may not be immediately clear that this matrix representsSWAP⁡,\operatorname{SWAP},SWAP,but we can check it satisfies the conditionSWAP⁡∣a⟩∣b⟩=∣b⟩∣a⟩\operatorname{SWAP} \vert a \rangle \vert b \rangle = \vert b \rangle \vert a \rangleSWAP∣a⟩∣b⟩=∣b⟩∣a⟩for every choice of classical statesa,b∈Σ.a,b\in\Sigma.a,b∈Σ.As a simple example, whenX\mathsf{X}XandY\mathsf{Y}Yare qubits, we find that

Now let us suppose thatQ\mathsf{Q}Qis a qubit andR\mathsf{R}Ris an arbitrary system, having whatever classical state set we wish. For every unitary operationUUUacting on the systemR,\mathsf{R},R,acontrolledUUUoperation is a unitary operation on the pair(Q,R)(\mathsf{Q},\mathsf{R})(Q,R)defined as follows:

For example, ifR\mathsf{R}Ris also a qubit, and we consider the PauliXXXoperation onR,\mathrm{R},R,then a controlled-XXXoperation is given by

We already encountered this operation in the context of classical information and probabilistic operations earlier in the lesson. Replacing the PauliXXXoperation onR\mathsf{R}Rwith aZZZoperation gives operation:

If instead we takeR\mathsf{R}Rto be two qubits, and we takeUUUto be theswap operationbetween these two qubits, we obtain this operation:

This operation is also known as aFredkin operation(or, more commonly, aFredkin gate), named for Edward Fredkin. Its action on standard basis states can be described as follows:

Finally, acontrolled-controlled-NOT operation, which we may denote asCCX,CCX,CCX,is called aToffoli operation(orToffoli gate), named for Tommaso Toffoli. Its matrix representation looks like this:

We may alternatively express it using the Dirac notation as follows:

In the previous lesson, we took a first look at Qiskit'sStatevectorandOperatorclasses, and used them to simulate operations and measurements on single qubits. In this section, we'll use these classes to explore the behavior of multiple qubits.

Output:

We'll start by importing theStatevectorandOperatorclasses, as well as the square root function fromNumPy. Hereafter, generally speaking, we'll take care of all of our required imports first within each lesson.

No output produced

TheStatevectorclass has atensormethod, which returns the tensor product of thatStatevectorwith another, given as an argument. The argument is interpreted as the tensor factor on the right.

For example, below we create two state vectors representing∣0⟩\vert 0\rangle∣0⟩and∣1⟩,\vert 1\rangle,∣1⟩,and use thetensormethod to create a new vector,∣ψ⟩=∣0⟩⊗∣1⟩.\vert \psi\rangle = \vert 0\rangle \otimes \vert 1\rangle.∣ψ⟩=∣0⟩⊗∣1⟩.Notice here that we're using thefrom_labelmethod to define the states∣0⟩\vert 0\rangle∣0⟩and∣1⟩,\vert 1\rangle,∣1⟩,rather than defining them ourselves.

Output:

∣01⟩|01\rangle∣01⟩

Other allowed labels include "+" and "-" for the plus and minus states, as well as "r" and "l" (short for "right" and "left") for the states

Here's an example, of the tensor product of∣+⟩\vert {+} \rangle∣+⟩and∣−i⟩.\vert {-i} \rangle.∣−i⟩.

Output:

12∣00⟩−i2∣01⟩+12∣10⟩−i2∣11⟩\frac{1}{2} |00\rangle- \frac{i}{2} |01\rangle+\frac{1}{2} |10\rangle- \frac{i}{2} |11\rangle21​∣00⟩−2i​∣01⟩+21​∣10⟩−2i​∣11⟩

An alternative is to use the^operation for tensor products, which naturally gives the same results.

Output:

12∣00⟩−i2∣01⟩+12∣10⟩−i2∣11⟩\frac{1}{2} |00\rangle- \frac{i}{2} |01\rangle+\frac{1}{2} |10\rangle- \frac{i}{2} |11\rangle21​∣00⟩−2i​∣01⟩+21​∣10⟩−2i​∣11⟩

TheOperatorclass also has atensormethod (as well as afrom_labelmethod), as we see in the following examples.

Output:

Again, like in the vector case, the^operation is equivalent.

Output:

Compound states can be evolved using compound operations as we would expect — just like we saw for single systems in the previous lesson. For example, the following code computes the state(H⊗I)∣ϕ⟩(H\otimes I)\vert\phi\rangle(H⊗I)∣ϕ⟩for∣ϕ⟩=∣+⟩⊗∣−i⟩\vert\phi\rangle = \vert + \rangle \otimes \vert {-i}\rangle∣ϕ⟩=∣+⟩⊗∣−i⟩(which was already defined above).

Output:

22∣00⟩−2i2∣01⟩\frac{\sqrt{2}}{2} |00\rangle- \frac{\sqrt{2} i}{2} |01\rangle22​​∣00⟩−22​i​∣01⟩

Here is some code that defines aCXCXCXoperation and calculatesCX∣ψ⟩CX \vert\psi\rangleCX∣ψ⟩for∣ψ⟩=∣+⟩⊗∣0⟩.\vert\psi\rangle = \vert + \rangle \otimes \vert 0 \rangle.∣ψ⟩=∣+⟩⊗∣0⟩.To be clear, this is aCXCXCXoperation for which the left-hand qubit is the control and the right-hand qubit is the target. The result is the Bell state∣ϕ+⟩.\vert\phi^{+}\rangle.∣ϕ+⟩.

Output:

22∣00⟩+22∣11⟩\frac{\sqrt{2}}{2} |00\rangle+\frac{\sqrt{2}}{2} |11\rangle22​​∣00⟩+22​​∣11⟩

In the previous lesson, we used themeasuremethod to simulate a measurement of a quantum state vector. This method returns two items: the simulated measurement result, and the newStatevectorgiven this measurement.

By default,measuremeasures all qubits in the state vector. We can, alternatively, provide a list of integers as an argument, which causes only those qubit indices to be measured. To demonstrate this, the code below creates the state

and measures qubit number 0, which is the rightmost qubit. (Qiskit numbers qubits starting from 0, from right to left. We'll return to this numbering convention in the next lesson.)

Output:

33∣001⟩+33∣010⟩+33∣100⟩\frac{\sqrt{3}}{3} |001\rangle+\frac{\sqrt{3}}{3} |010\rangle+\frac{\sqrt{3}}{3} |100\rangle33​​∣001⟩+33​​∣010⟩+33​​∣100⟩

22∣010⟩+22∣100⟩\frac{\sqrt{2}}{2} |010\rangle+\frac{\sqrt{2}}{2} |100\rangle22​​∣010⟩+22​​∣100⟩

∣001⟩|001\rangle∣001⟩

Was this page helpful?


---

# Quantum computing for the very curious

Andy MatuschakandMichael Nielsen

Part of aseries of essaysin a mnemonic medium which makes it almost effortless to remember what you read.

byAndy MatuschakandMichael Nielsen

Presented in a new mnemonic medium which makes it almost effortless to remember what you read.

Our future projects are funded in part by readers like you.

Special thanks to our sponsor-level patrons,Adam Wiggins,Andrew Sutherland,Bert Muthalaly,Calvin French-Owen,Dwight Crow,fnnch,James Hill-Khurana,Lambda AI Hardware,Ludwig Petersson,Mickey McManus,Mintter,Patrick Collison, Paul Sutter,Peter Hartree,Sana Labs,Shripriya Mahesh,Tim O'Reilly.

If humanity ever makes contact with alien intelligences, will those aliens possess computers? In science fiction, alien computers are commonplace. If that's correct, it means there is some way aliens can discover computers independently of humans. After all, we’d be very surprised if aliens had independently invented Coca-Cola or Pokémon or the Harry Potter books. If aliens have computers, it’s because computers are the answer to a question that naturally occurs to both human and alien civilizations.

Here on Earth, the principal originator of computers was the English mathematician Alan Turing. In his paper, published in 1936Alan M. Turing,On Computable Numbers, with an Application to the Entscheidungsproblem(1936)., Turing wasn’t trying to invent a clever gadget or to create an industry. Rather, he was attacking a problem about the nature of mathematics posed by the German mathematician David Hilbert in 1928. That sounds abstruse, but it’s worth understanding the gist of Hilbert and Turing’s thinking, since it illuminates where computers come from, and what computers will become in the future.

Through his career, Hilbert was interested in the ultimate limits of mathematical knowledge: what can humans know about mathematics, in principle, and what (if any) parts of mathematics are forever unknowable by humans? Roughly speaking, Hilbert’s 1928 problem asked whether there exists a general algorithm a mathematician can follow which would let them figure out whether any given mathematical statement is provable. Hilbert’s hoped-for algorithm would be a little like the paper-and-pencil algorithm for multiplying two numbers. Except instead of starting with two numbers, you’d start with a mathematical conjecture, and after going through the steps of the algorithm you’d know whether that conjecture was provable. The algorithm might be too time-consuming to use in practice, but if such an algorithm existed, then there would be a sense in which mathematics was knowable, at least in principle.

In 1928, the notion of an algorithm was pretty vague. Up to that point, algorithms were often carried out by human beings using paper and pencil, as in the multiplication algorithm just mentioned, or the long-division algorithm. Attacking Hilbert’s problem forced Turing to make precise exactly what was meant by an algorithm. To do this, Turing described what we now call aTuring machine: a single, universal programmable computing device that Turing argued could perform any algorithm whatsoever.

Today we’re used to the idea that computers can be programmed to do many different things. In Turing’s day, however, the idea of a universal programmable computer was remarkable. Turing was arguing that a single, fixed device could imitateanyalgorithmic process whatsoever, provided the right program was supplied. It was an amazing leap of imagination, and the foundation of modern computing.

In order to argue that his machine could imitate any algorithmic process, Turing considered what operations a human mathematician could perform when carrying out an algorithm. For each such operation, he had to argue that his machine could always do the same thing. His argument is too long to reproduce in full here, but it’s fun and instructive to see the style of Turing’s reasoning:

Obviously, this was an informal and heuristic argument! Invoking a child’s arithmetic book, or someone’s mental state is not the stuff of a rigorous, bulletproof argument. But Turing’s argument was convincing enough that later mathematicians and scientists have for the most part been willing to accept it. Turing’s machine became the gold standard: an algorithm was what we could perform on a Turing machine. And since that time, computing has blossomed into an industry, and billions of computers based on Turing’s model have been sold.

Still, there’s something discomforting about Turing’s analysis. Might he have missed something in his informal reasoning about what an algorithm is? In 1985, the English physicist David Deutsch suggested a deeper approach to the problem of defining what is meant by an algorithmDavid Deutsch, “Quantum theory, the Church-Turing principle and the universal quantum computer” (1985).. Deutsch pointed out that every algorithm is carried out by a physical system, whether it be a mathematician with paper-and-pencil, a mechanical system such as an abacus, or a modern computer. Deutsch then considered the following question (I've slightly rephrased to make it easier to read):

If there was such a device, you could use it to perform any algorithm whatsoever, because algorithms have to be performed on some kind of physical system. And so the device would be a truly universal computer. What’s more, Deutsch pointed out, you wouldn’t need to rely on informal, heuristic arguments to justify your notion of algorithm, as Turing had done. You could use the laws of physics to prove your device was universal.

So let’s come back to our opening question: will aliens have computers? Deutsch’s question above is a simple, fundamental question about the nature of the universe. It’s the kind of question which alien counterparts to Deutsch could plausibly come to ponder. And the alien civilizations of which they are a part would then be led inexorably to invent computers.

In this sense, computers aren’t just human inventions. They are a fundamental feature of the universe, the answer to a simple and profound question about how the universe works. And they have likely been discovered over and over again by many alien intelligences.

There’s a wrinkle in this story. Deutsch is a physicist with a background in quantum mechanics. And in trying to answer his question, Deutsch observed that ordinary, everyday computers based on Turing’s model have a lot of trouble simulating quantum mechanical systemsResearchers such as Yu Manin and Richard Feynman had previously observed this, and as a result had speculated about computers based on quantum mechanics.. In particular, they seem to be extraordinarily slow and inefficient at doing such simulations. To answer his question affirmatively, Deutsch was forced to invent a new type of computing system, aquantum computer. Those quantum computers can do everything conventional computers can do, but are also capable of efficiently simulating quantum-mechanical processes. And so they are arguably a more natural computing model than conventional computers. If we ever meet aliens, my bet is that they’ll use quantum computers (or, perhaps, will have quantum computing brains). After all, it’s likely that aliens will be far more technologically advanced than current human civilization. And so they’ll use the computers natural for any technologically advanced society.

This essay explains how quantum computers work. It’s not a survey essay, or a popularization based on hand-wavy analogies. We’re going to dig down deep so you understand the details of quantum computing. Along the way, we’ll also learn the basic principles of quantum mechanics, since those are required to understand quantum computation.

Learning this material is challenging. Quantum computing and quantum mechanics are famously “hard” subjects, often presented as mysterious and forbidding. If this were a conventional essay, chances are that you’d rapidly forget the material. But the essay is also an experiment in the essay form. As I’ll explain in detail belowthe essay incorporates new user interface ideas to help you remember what you read. That may sound surprising, but uses a well-validated idea from cognitive science known as spaced-repetition testing. More detail on how it works below. The upshot is that anyone who is curious and determined can understand quantum computing deeply and for the long term.

That said, you need some mathematical background to understand the essay. I’ll assume you’re comfortable with complex numbers and with linear algebra – vectors, matrices, and so on. I’ll also assume you’re comfortable with the logic gates used in conventional computers – gates such as AND, OR, NOT, and so on.

If you don’t have that mathematical background, you’ll need to acquire it. How you do that depends on your prior experience and learning preferences – there’s no one-size-fits-all approach, you’ll need to figure it out for yourself. But two resources you may find helpful are: (1)3Blue1Brown’s seriesof YouTube videos on linear algebra; and (2) the more in-depthlinear algebra lectures by Gil Strang. Try them out, and if you find them helpful, keep going. If not, explore other resources.

It may seem tempting to try to avoid this mathematics. If you look around the web, there are many flashy introductions to quantum computing that avoid mathematics. There are, for instance, many rather slick videos on YouTube. They can be fun to watch, and the better ones give you some analogies to help make sense of quantum computing. But there’s a hollowness to them. Bluntly, if they don’t explain the actual underlying mathematical model, then you could spend years watching and rewatching such videos, and you’d never really get it. It’s like hanging out with a group of basketball players and listening to them talk about basketball. You might enjoy it, and feel as though you’re learning about basketball. But unless you actually spend a lot of time playing, you’re never going to learn to play basketball. To understand quantum computing, you absolutely must become fluent in the mathematical model.

As you know, in ordinary, everyday computers the fundamental unit of information is the bit. It’s a familiar but astonishing fact that all the things those computers do can be broken down into patterns of000sand111s, and simple manipulations of000sand111s. For me, I feel this most strongly when playing video games. I’ll be enjoying playing a game, when I’ll suddenly be hit by a realization of the astounding complexity behind the imaginary world visible on my screen:

SourceCopyright Wildfire Games, used under aCreative Commons Attribution-Share Alike 3.0 license..

Underlying every such image is millions of pixels, described by tens of millions of bits. When I move the game controller, I am effectively conducting an orchestra, tens of millions strong, organized through many layers of intermediary ideas, in such a way as to create enjoyment and occasionally sheer delight.

I’ve described a bit as an abstract entity, whose state is000or111.But in the real world, not the world of mathematics, we must find some way of storing our bits in a physical system. That can be done in many different ways. In your computer’s memory chips, bits are most likely stored as tiny electric charges on nanometer-scale capacitors (i.e., little reservoirs of charge), just above the surface of the chip. Old-fashioned hard disks take a different approach, using tiny magnets to store bits. Furthermore, different types of memory use different types of capacitor; different types of hard disk use different approaches to magnetization.

For the most part you don’t notice these differences when you use your computer. Computer designers work very, very hard to make the details of the physical instantiation of the bits invisible not just to the user, but also (often) invisible even to programmers. Many programmers never think about whether a bit is stored in fast on-microprocessor cache memory, in the dynamic RAM chips, or in some type of virtual memory (say, on a hard disk). There are exceptions – programmers working on high-performance programs sometimes do think about these things, to make their programs as fast as possible. But for many programmers it doesn’t much matter how bits are stored. Rather, they can think of the bit in purely abstract terms, as having a state which is either000or111.

In a manner similar to the way conventional computers are made up of bits, quantum computers are made up ofquantum bits, orqubits. Just like a bit, a qubit has astate. But whereas the state of a bit is a number (000or111), the state of a qubit is avector. More specifically,the state of a qubit is a vector in a two-dimensional vector space. This vector space is known as state space.For instance, here’s a possible state for a qubit:

[10]\left[ \begin{array}{c} 1 \\ 0 \end{array} \right][10​]

That perhaps sounds strange! What does it mean that the state of a qubit is a two-dimensional vector? We’re going to unpack the answer slowly and gradually. You won’t have a single epiphany where you think “ahah, that’s what a qubit is!” Rather, you’ll gradually build up many details in your understanding, until you get to the point where you’re comfortable working with qubits, with quantum computations, and more generally with quantum mechanics.

One way qubits are similar to bits: we’ve said absolutely nothing about what the qubit actuallyis, physically. Maybe the state of the qubit is being stored somehow on an electron, or a photon, or an atom. Or maybe it’s being stored in something stranger, perhaps inside some exotic particle or state of matter, even further removed from our everyday experience.

For our purposes in this essay none of this matters, no more than you should worry about what type of capacitor is storing the bits inside your computer’s RAM. What you should take away is that: (a) qubits have a state; (b) much like a bit, that state is an abstract mathematical object; but (c) whereas a bit’s abstract state is a number,000or111,the state of a qubit is a222-dimensional vector; (d) we call the222-dimensional vector space where states live state space.

Alright, let’s review what we’ve learnt. Please indulge me by answering the questions just below. It’ll only take a few seconds – for each question, think about what you believe the answer to be, click to reveal the actual answer, and then mark whether you remembered or not. If you can recall, that’s great. If not, that’s also fine, just note the correct answer, and continue.

Perhaps you correctly recalled the answers to all three questions just now. Even if so, will you remember the answers in a week? In a year? Human memory is fallible. If your memory is like mine, youmightvaguely remember the answers in a week: “what’s the state of a qubit, oh yes, it’s a vector!” But the chances you’ll remember in a month or a year are low. And if you forget such things, you won’t have any durable understanding of quantum computing.

How can we ensure you don’t remember these answers for just a few minutes or a few hours, but well into the future, perhaps even permanently?

One way is for you to be supremely virtuous, to keep coming back and re-reviewing the material until it’s firmly locked in your memory. If you are such a virtuous person, congratulations! But for the other 99 percent of us that’s not likely. What can we do?

For more than a century, cognitive scientists have studied human memory. And they’ve figured out some simple strategies that ensure you’ll remember something permanently. The single most important idea is tore-test you on your knowledge, with expanding time intervals between tests.

As an example, consider the question above: “How many dimensions does the state space of a qubit have?” If you got it right, you’d ideally be tested again in a few weeks. And if you got it right again, you’d be tested again a few months after that. And so on, a gradually expanding schedule. If you get the question wrong on one of those tests, the schedule would contract, so you can relearn the answer.

It turns out that such an expanding schedule is the optimal way to retain information. Each time you’re re-tested your brain consolidates the answer a little better into long-term memory, until eventually it’s permanent.

Spaced-repetition testing is a simple idea, but has profound consequences. First, it doesn’t take much overall time. Because of the expanding test schedule, it typically only takes a few minutes of total review time to memorize the answer to a question for years or decades. I won’t go through the math showing that, but you can see itworked out elsewhere.

Second, spaced-repetition testing gives you a guarantee you will remember the answer to the question. For the most part our memories work in a haphazard manner. We read or hear something interesting, and hope we remember it in future. Spaced-repetition testing makes memory into a choice.

This sounds great, but also like you’ll need to be very disciplined in re-testing yourself. Fortunately, the computer can handle all the scheduling for you. And so this essay isn’t just a conventional essay, it’s also a new medium, amnemonic mediumwhich integrates spaced-repetition testing.The medium itself makes memory a choice.

This comes at some cost: you’re committing to future review. But consider what that buys you. This essay will likely take you an hour or two to read. In a conventional essay, you’d forget most of what you learned over the next few weeks, perhaps retaining a handful of ideas. But with spaced-repetition testing built into the medium, a small additional commitment of time means you will remember all the core material of the essay. Doing this won’t be difficult, it will be easier than the initial read. Furthermore, you’ll be able to read other material which builds on these ideas; it will open up an entire world.

This spaced-repetition approach is why the questions only require a few seconds to read and answer. They’re not complex exercises, in the style of a textbook. Rather, the questions have a different point: the promise each question makes is that you will remember the answer forever. It’s to permanently change your thinking.

So, I invite you to set up an account by signing in below. If you do so, your review schedule for each question in the essay will be tracked, and you’ll receive periodic reminders containing a link which takes you to an online review session. That review session isn’t this full essay – rather, it looks just like the question set you answered above, but contains insteadallthe questions which are due, so you can quickly run through them. The time commitment will usually be a few minutes per session – a little more early on, when questions need frequent re-testing, but rapidly dropping off. You can study on your phone while grabbing coffee, or standing in line, or going for a walk, or in transit. The return for that small time commitment is greatly improved fluency in basic quantum computing and quantum mechanics. And that understanding will be internalized, a part of who you are, retained for years instead of days.

To keep this promise, we’re tracking your review schedule for each question, and sending you occasional reminders to check in, and to run through the questions which are due. You can review on your phone while grabbing coffee, or standing in line, or going for a walk, or on transit. The return for that commitment is greatly improved fluency in basic quantum computing and quantum mechanics. And that understanding will be internalized, a part of who you are, retained for years instead of weeks.

Having extolled the virtues of spaced-repetition testing, let’s try another question:

This question is similar to an earlier question: “How many dimensions does the state space of a qubit have?” It may seem inefficient to have such similar questions, but it helps build fluency with the material when you have the “same” information encoded into memory in multiple ways, triggering off different associations. And so many of the questions below have this nature, elaborating ideas in multiple ways.

Let’s get back to understanding qubits. I’ve described what the state of a qubit is, but given no hint about how (or whether) that’s connected to the state of a classical bit. (Henceforth we’ll use the phrase “classical bit” instead of “conventional bit”, after “classical physics”). In fact, there are two special quantum states which correspond to the000and111states of a classical bit. The quantum state corresponding to000is usually denoted∣0⟩|0\rangle∣0⟩.That’s a fancy notation for the following vector:

∣0⟩:=[10].|0\rangle := \left[ \begin{array}{c} 1 \\ 0 \end{array} \right].∣0⟩:=[10​].

This special state∣0⟩|0\rangle∣0⟩is called acomputational basis state.

It’s tempting to see the∣0⟩|0\rangle∣0⟩notation and wonder what all the separate pieces mean – what, for instance, does the∣|∣mean; what does the⟩\rangle⟩mean; and so on?

In fact, it’s best to regard∣0⟩|0\rangle∣0⟩as a single symbol, standing for a single mathematical object – that vector we just saw above,[10]\left[ \begin{array}{c} 1 \\ 0 \end{array} \right][10​].The∣|∣and⟩\rangle⟩don’t really have separate meanings except to signify this is a quantum state. In this,∣0⟩|0\rangle∣0⟩is much like the symbol000:both stand for a single mathematical entity. And, as we’ll gradually come to see, a quantum computer can manipulate∣0⟩|0\rangle∣0⟩in ways very similar to how a conventional computer can manipulate000.

This notation with∣|∣and⟩\rangle⟩is called theketnotation, and things like∣0⟩|0\rangle∣0⟩are calledkets. But don’t be thrown off by the unfamiliar terminology – a ket is just a vector, and when we say something is a ket, all we mean is that it’s a vector.

That said, the term ket is most often used in connection with notations like∣0⟩|0\rangle∣0⟩.That is, we wouldn’t usually refer to[10]\left[ \begin{array}{c} 1 \\ 0 \end{array} \right][10​]as a ket; we’d call it a vector, instead. If you’re a fan of really sharp definitions and strict consistency, this may seem vague and wishy-washy, but in practice doesn’t cause confusion. It’s just a convention to be aware of!

Alright, so∣0⟩|0\rangle∣0⟩is a computational basis state for a qubit, and plays much the same role as000does for a classical bit. It won’t surprise you to learn that there is another computational basis state, denoted∣1⟩|1\rangle∣1⟩,which plays the same role as111does for a bit. Like∣0⟩|0\rangle∣0⟩,∣1⟩|1\rangle∣1⟩is just a notation for a two-dimensional vector, in this case:

∣1⟩:=[01].|1\rangle := \left[ \begin{array}{c} 0 \\ 1 \end{array} \right].∣1⟩:=[01​].

Again, we’ll gradually come to see that∣1⟩|1\rangle∣1⟩has all the properties we expect of the111state of a classical bit.

Time for a few more questions. A reminder that these have a different purpose to conventional textbook exercises. Textbook exercises are about setting you challenges; the point of the questions below is instead to help you commit the answer to long-term memory.

— William Thurston,Fields-medal winning mathematician

How should you think about it when you get one of these embedded questions wrong? Often in life testing means being judged, and being judged can be uncomfortable. If you don’t know the answer to a question you may feel like you’ve failed.

But the purpose of these questions has nothing to do with external judgment. Rather, they have two quite different purposes. One purpose is, as explained earlier, to help strengthen your memory, so your new knowledge is consolidated in your long-term memory. The second purpose is to help you diagnose what you do and don’t know, and to help you fill the gaps as rapidly as possible.

In this view, getting a question wrong is useful information. It pinpoints exactly what you need to understand, and puts the onus on you to figure it out. Honestly, the appropriate response to getting a question wrong is probably to throw your hands up in the air and shout “wonderful!”, since it’s at those points of what may appear to be “failure” that your learning rate will be at its highest.

With that said, it’s a common canard in education that “it doesn’t matter if you get something right or wrong, so long as you’re learning”. Unfortunately, that statement is often bullshit. If getting something right or wrong is used to determine your grade, or to influence other people’s opinion of you, then it damn well does matter.

For that reason, I suggest keeping your results private. They are for you alone, and their purpose should be solely to help you learn as rapidly as possible. If they’re not helping you – if they’re making you feel bad, for instance, or being used to judge you – then stop doing the questions.

You’ve probably noticed the questions are self-assessed. If you want to mark yourself “correct” sometimes, even when you’re not, go for it! What impact do you think that will have on your learning? Do you enjoy the slightly transgressive feeling? I must admit that I do. Don’t be embarrassed, if so: this is supposed to be, above all else, fun. Or try marking yourself wrong when you’re correct, or skipping the questions entirely. What impact do these actions have on your learning? The point is to figure out how to engage with the questions to learn as rapidly as possible. And that means experimenting playfully with how you engage, to find what works for you.

This essay is an unusual form. It’s certainly not a product in the conventional startup sense; it’s a research project, an experiment in developing a new and improved form of reading. A conventional product would aim to draw you in, and form a regular, long-term habit. There’d be tens (or hundreds) of millions of words of content for you to read, and lots of people on social media excitedly pointing you toward that content. You’d engage every day, learning more and more and more.

That’s not what’s going on here. “Quantum Computing for the Very Curious” is, instead, like a video game or book or movie, a single one-off project for you to work through. So you commit to it for a while, and then the experience is over. (Also, like a video game, book, or movie, sequels are planned!)

With that said, it’s different from those forms too. Many people consume games, books, and movies as binge activities, hungrily devouring them until complete. “Quantum Computing for the Very Curious” is, by contrast, intentionally an experience spread out over time. Yes, you probably binge at first, working your way quickly through the text over a couple of hours. But then you return occasionally for brief review sessions, prompted by our notifications. That form of spaced testing is the best way for you to remember what you read. Still, while it might be optimal from the point of view of memory formation, it means not using some of the techniques that games, books, and movies use to keep you interested. Nonetheless, I hope you’ll be willing to trust the team at “Quantum Computing for the Very Curious”, and to participate in the experiment.

How can you get the most out of reading in this new mnemonic medium? The ideal is to do an initial read, followed by a few short review sessions over the coming weeks (prompted by our notifications) to help you internalize the ideas. Then (optionally) a followup read, where you can more deeply understand the material. And finally, some sessions of followup review to ensure you remember for the long term:

As you work through this process, we’ll track your overall progress toward completion (meaning: most questions reliably committed to memory), and each time you review we’ll show you that progress.

This is a larger commitment than traditional reading. But for a small factor in effort, you will understand the material far more deeply, and remember it for more than 10x as long. What’s more, while the reading process above looks complex, you’ll be cued at each step by reminders that will help the review process become a habit. Trust the reminders, and this will all happen as a matter of course.

You may find the essay particularly helpful if you’re taking an introductory class on quantum computing. If that’s your situation, I advise you to read the entire essay immediately at the beginning of semester (or even before), answering all the questions as you go. Then continue to follow the procedure described just above, taking a few minutes to complete each review session, prompted by the reminders you’ll be sent. This will make it far easier to understand the rest of the course you’re taking, and help you get much more out of it.

The computational basis states∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩are just two possible states for a qubit. Many more states are possible, and those extra states endow qubits with capabilities not available to ordinary classical bits. In general, remember, a quantum state is a two-dimensional vector. Here’s an example, with a graphical illustration emphasizing the vector nature of the state:





In this example, the state0.6∣0⟩+0.8∣1⟩0.6|0\rangle+0.8|1\rangle0.6∣0⟩+0.8∣1⟩is just0.60.60.6times the∣0⟩|0\rangle∣0⟩vector, plus0.80.80.8times the∣1⟩|1\rangle∣1⟩vector. In the usual vector notation that means the state is:

0.6∣0⟩+0.8∣1⟩=0.6[10]+0.8[01]=[0.60.8].0.6|0\rangle + 0.8 |1\rangle = 0.6 \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] + 0.8 \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] = \left[ \begin{array}{c} 0.6 \\ 0.8 \end{array} \right].0.6∣0⟩+0.8∣1⟩=0.6[10​]+0.8[01​]=[0.60.8​].

I’ve been talking about quantum states as two-dimensional vectors. What I didn’t yet mention is that in general they’recomplex vectors, that is, they can have complex numbers as entries. Of course, the example just shown has real entries, as do the computational basis states. But for a general quantum state the entries can be complex numbers. So, for instance, another quantum state is the vector

1+i2∣0⟩+i2∣1⟩,\frac{1+i}{2} |0\rangle + \frac{i}{\sqrt{2}} |1\rangle,21+i​∣0⟩+2​i​∣1⟩,

which can be written in the conventional component vector representation as

[1+i2i2].\left[ \begin{array}{c} \frac{1+i}{2} \\ \frac{i}{\sqrt{2}} \end{array} \right].[21+i​2​i​​].

Because quantum states are in general vectors with complex entries, the illustration above shouldn’t be taken too literally – the plane is a real vector space, not a complex vector space. Still, visualizing it as a plane is sometimes a handy way of thinking.

I’ve said what a quantum state is, as a mathematical object: it’s a two-dimensional vector in a complex vector space. But why is that true? What does it mean, physically, that it’s a vector? Why a complex vector space, and how should we think about the complex numbers? And what’s a quantum state good for, anyway?

These are good questions. But they do take some time to answer. For context consider that the discovery of quantum mechanics wasn’t a single event, but occurred over 25 years of work, from 1900 to 1925. Many Nobel prizes were won for milestones along the way. That includes Albert Einstein’s Nobel Prize, won primarily for work related to quantum mechanics (not relativity, as people sometimes assume).

When some of the brightest people in the world struggle for 25 years to develop a theory, it’s not an obvious theory! In fact, the idea of describing a simple quantum system using a complex vector in two dimensions summarizes much of what was learned over that 25 years. In that sense, it’s quite a simple and beautiful statement. But it’s not an obvious statement, and it’s not unreasonable that it might take a few hours to understand. That’s better than taking 25 years to understand!

As part of that journey toward understanding, let’s get familiar with some more nomenclature commonly used for quantum states.

One of the most common terms issuperposition. People will say a state like0.6∣0⟩+0.8∣1⟩0.6|0\rangle+0.8|1\rangle0.6∣0⟩+0.8∣1⟩is asuperpositionof∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩.All they mean is that the state is a linear combination of∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩.You may wonder why they don’t just say “linear combination” (and sometimes they do), but the reason is pretty much the same reason English-speakers say “hello” while Spanish-speakers say “hola” – the two terms come out of different cultures and different histories.

Another common term isamplitude. An amplitude is the coefficient for a particular state in superposition. For instance, in the state0.6∣0⟩+0.8∣1⟩0.6|0\rangle+0.8|1\rangle0.6∣0⟩+0.8∣1⟩the amplitude for∣0⟩|0\rangle∣0⟩is0.60.60.6,and the amplitude for∣1⟩|1\rangle∣1⟩is0.80.80.8.

We’ve learnt that a quantum state is a two-dimensional complex vector. Actually, it can’t be just any old vector, a fact you might have guessed from the very particular amplitudes in some of the examples above. There’s a constraint. The constraint is this:the sums of the squares of the amplitudes must be equal to111.

So, for example, for the state0.6∣0⟩+0.8∣1⟩0.6 |0\rangle+0.8 |1\rangle0.6∣0⟩+0.8∣1⟩the sum of the squares of the amplitudes is0.62+0.820.6^2+0.8^20.62+0.82,which is0.36+0.64=10.36+0.64 = 10.36+0.64=1,as we desired.

For a more general quantum state, the amplitudes can be complex numbers, let’s denote them byα\alphaαandβ\betaβso the state isα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩.The constraint is now that the sum of the squares of the amplitudes is111,i.e.,∣α∣2+∣β∣2=1|\alpha|^2+|\beta|^2 = 1∣α∣2+∣β∣2=1.

This is called thenormalization constraint.

It’s called that because if you think of∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩as orthonormal vectors, as I drew them earlier,

then the normalization constraint is the requirement that the length of the state is equal to111.So it’s a unit vector, or anormalizedvector, and that’s why this is called a normalization constraint.

Summing up all these ideas in one sentence:the quantum state of a qubit is a vector of unit length in a two-dimensional complex vector space known as state space.

We’ve gone through a few refinements of this sentence but that sentence is the final version – there’s no missing parts, or further refinement necessary! That’s what the quantum state of a qubit is. Of course, we will explore the definition further, deepening our understanding, but it will always come back to that basic fact.

One common gotcha in thinking about qubits is to look at the∣0⟩|0\rangle∣0⟩state and think it must be the zero vector in the vector space, often denoted000.But that’s not right at all. The zero vector is at the origin,0=[00]0 = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right]0=[00​],while the∣0⟩|0\rangle∣0⟩vector is quite different,∣0⟩=[10]≠0|0\rangle = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] \neq 0∣0⟩=[10​]​=0.It’s just an unfortunate notational accident that∣0⟩|0\rangle∣0⟩looks as though it should be the000vector. Fortunately, in practice this distinction is easy to get used to, and doesn’t cause confusion. But it’s worth noting.

— Steven Weinberg,Nobel Laureate in Physics

Let’s come back to the question of what the quantum state means, and why it’s a vector in a complex vector space.

In the case of classical bits, it’s pretty easy to think about the state. You can think of the000or111states of a bit as corresponding to two very different (but stable) states of a physical system. For instance, a000or111can be indicated by the presence or absence of a hole at some location in a punch card. And so a single punch card can be used to store hundreds or thousands of bits:

Source:Gwern(2006).

Most ways of storing classical bits are variations on this idea. For instance, the dynamic random access memory (RAM) inside your computer is based on the idea of having two tiny metal plates separated by a miniscule gap. Electric charge is stored on those plates, setting up an electric field between them. The000and111states of the bit correspond to two different configurations of charge on the plates. In practice, real dynamic RAM systems use slightly more elaborate ideas, but that’s the heart of it. This is harder to think about than punch cards – most of us don’t have so much experience thinking about moving electric charges around metal plates. But it’s still pretty concrete.

So, how should we think about quantum states? The∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states often aren’t difficult to think about, since they often correspond to very concrete physical states of the world, much like classical bits. Indeed, in some proposals they may correspond to different charge configurations, similar to dynamic RAM. Or perhaps a photon being in one of two different locations in space – again, a pretty simple, concrete notion, even if photons aren’t that familiar. There are also many more exotic proposals for the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states. But by and large you can think of the computational basis states as representing a physical system in one of two well-defined configurations.

Of course, qubits have states which aren’t computational basis states, states like0.6∣0⟩+0.8∣1⟩0.6|0\rangle+0.8|1\rangle0.6∣0⟩+0.8∣1⟩.How should we think about such superposition states? At least in popular media accounts, a very common description is that a state like0.6∣0⟩+0.8∣1⟩0.6|0\rangle + 0.8|1\rangle0.6∣0⟩+0.8∣1⟩is“simultaneously”in the∣0⟩|0\rangle∣0⟩state and the∣1⟩|1\rangle∣1⟩state.

I must confess, I don’t understand what people mean by this. As far as I can tell, what they’re trying to do is explain the quantum state in terms of classical concepts they’re already familiar with. But I can’t make much sense of it – saying0.6∣0⟩+0.8∣1⟩0.6|0\rangle + 0.8|1\rangle0.6∣0⟩+0.8∣1⟩issimultaneouslyin the∣0⟩|0\rangle∣0⟩state and the∣1⟩|1\rangle∣1⟩state seems like word salad, and makes about as much sense to me as Lewis Carroll’s nonsense poemJabberwocky:

Of course, lacking any other interpretation it’s tempting to try to impose our classical prejudices on the quantum state. Or, even if you reject that, to get hung up worrying about what a quantum state is. But the trouble is that there is enormous disagreement amongst physicists themselves about how to think about the quantum state. Indeed, many active researchers are trying to understand what the correct way of thinking about the quantum state is, exploring multiple approaches in great depth. So we’re going to defer worrying too much about this until later.

To understand why we’re deferring, suppose someone gives you a Rubik’s cube (or some other challenging puzzle or game) for the first time, all scrambled up. You start to theorize about the best ways of solving it, how to understand it, and so on. But you never actually play around with it, getting familiar with how it behaves.

Often the best way to understand something is to first use it, to get comfortable, to play a lot, and to do lots of informal experiments. As you build familiarity you understand why things are the way they are. At that point, you can go back and better understand the meaning of the basics.

Well, we can think of quantum computing and quantum mechanics as an especially complicated type of puzzle! So the strategy we’re taking is to start with the mathematics of quantum computing – we’ll keep getting familiar with qubits and the quantum state, and developing the consequences. Doing that is how we’ll build up intuition, and will give us the chops needed to come back and think harder about the meaning of the quantum state.

In Part I we learned about the state of a qubit. But in order to quantum compute, it’s not enough just to understand quantum states. We need to be able to do things with them! We do that usingquantum logic gates.

A quantum logic gate is simply a way of manipulating quantum information, that is, the quantum state of a qubit or a collection of qubits. They’re analogous to the classical logic gates used in ordinary, everyday computers – gates such as the AND, OR, and NOT gates. And, much like classical gates’ role in conventional computers, quantum gates are the basic building blocks of quantum computation. They’re also a convenient way of describing many other quantum information processing tasks, such as quantum teleportation.

In Part II of this essay we’ll discuss several types of quantum logic gate. As we’ll see, the gates we discuss are sufficient to do any quantum computation. In particular, much as any classical computation can be built up using AND, OR, and NOT gates, the quantum gates we describe over the next few sections suffice to do any quantum computation.

Many of the quantum gates we’ll learn about are based on familiar classical logic gates. But a few are different. Those differences appear innocuous, almost trivial. But in those differences lies the power of quantum computation, and the possibility for quantum computers to be vastly superior to classical computers.

Part II is, frankly, a bit of a slog. Learning quantum gates is like learning basic vocabulary in a new language: there’s no getting round spending a fair bit of time working on it. Still, the spaced-repetition testing should make this basic memory work much easier than is ordinarily the case. And it will prepare you well for some of the more conceptual issues discussed in Part III, where we return to high-level questions about the ultimate nature of computation, and what quantum computers are good for.

Let’s take a look at our very first quantum logic gate, thequantum NOT gate. As you can no doubt surmise, the quantum NOT gate is a generalization of the classical NOT gate. On the computational basis states the quantum NOT gate does just what you’d expect, mimicking the classical NOT gate. That is, it takes the∣0⟩|0\rangle∣0⟩state to∣1⟩|1\rangle∣1⟩,and vice versa:

NOT∣0⟩=∣1⟩NOT|0\rangle = |1\rangleNOT∣0⟩=∣1⟩

NOT∣1⟩=∣0⟩NOT|1\rangle = |0\rangleNOT∣1⟩=∣0⟩

But the computational basis states aren’t the only states possible for a qubit. What happens when we apply the NOT gate to a general superposition state, that is,α∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩?In fact, it does pretty much the simplest possible thing: it acts linearly on the quantum state, interchanging the role of∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩:

NOT(α∣0⟩+β∣1⟩)=α∣1⟩+β∣0⟩.NOT (\alpha|0\rangle +\beta|1\rangle) = \alpha|1\rangle+\beta |0\rangle.NOT(α∣0⟩+β∣1⟩)=α∣1⟩+β∣0⟩.

I’ve been using the notation NOT for the quantum NOT gate. But for historical reasons people working on quantum computing usually use a different notation, the notationXXX.And so the above may be rewritten:

X(α∣0⟩+β∣1⟩)=α∣1⟩+β∣0⟩.X (\alpha|0\rangle +\beta|1\rangle) = \alpha|1\rangle+\beta |0\rangle.X(α∣0⟩+β∣1⟩)=α∣1⟩+β∣0⟩.

I’ll use the termsXXXgate and NOT gate interchangeably.

Historically, the notationXXXtraces its origin to 1927, when the physicist Wolfgang Pauli introduced an operationsxs_xsx​(often writtenσx\sigma_xσx​in textbooks today) to help describe rotations of certain objects around thexxxspatial axis. This operation later became of interest to people working on quantum computing. But by that point thesss(and the connection to rotation) was irrelevant, and sosxs_xsx​just becameXXX.

What we’ve seen so far are very algebraic ways of writing down the way theXXXgate works. There’s an alternate representation, thequantum circuitrepresentation. In a quantum circuit we depict anXXXgate as follows:





The line from left to right is what’s called aquantum wire. A quantum wire represents a single qubit. The term “wire” and the way it’s drawn looks like the qubit is moving through space. But it's often helpful to instead think of left-to-right as representing the passage of time. So the initial segment of wire is just the passage of time, with nothing happening to the qubit. Then theXXXgate is applied. And then the quantum wire continues, leaving the desired output.

Sometimes we’ll put the input and output states explicitly in the quantum circuit, so we have something like:





So that’s the quantum circuit representation of theXXXgate. It is, in fact, our first quantum computation. A simple computation, involving just a single qubit and a single gate, but a genuine quantum computation nonetheless!

There’s a third representation for theXXXgate that’s worth knowing about, a representation as a2×22 \times 22×2matrix:

X=[0110].X = \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right].X=[01​10​].

To understand in what sense this is a representation of the NOT gate, recall thatα∣0⟩+β∣1⟩\alpha|0\rangle + \beta|1\rangleα∣0⟩+β∣1⟩is just the vector[αβ]\left[ \begin{array}{c} \alpha \\ \beta \end{array} \right][αβ​].And so we have:

[0110](α∣0⟩+β∣1⟩)=[0110][αβ]=[βα]=α∣1⟩+β∣0⟩=X(α∣0⟩+β∣1⟩).\begin{aligned} \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right] (\alpha|0\rangle + \beta|1\rangle) & = \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} \alpha \\ \beta \end{array} \right] \\ & = \left[ \begin{array}{c} \beta \\ \alpha \end{array} \right] \\ & = \alpha|1\rangle+\beta|0\rangle \\ & = X (\alpha|0\rangle + \beta|1\rangle). \end{aligned}[01​10​](α∣0⟩+β∣1⟩)​=[01​10​][αβ​]=[βα​]=α∣1⟩+β∣0⟩=X(α∣0⟩+β∣1⟩).​

This tells us thatXXXand[0110]\left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right][01​10​]act in exactly the same way on all vectors, and thus are the same operation. In fact, as we’ll see later, it turns out that all quantum gates can be thought of as matrices, with the matrix entries specifying the exact details of the gate.

By the way, regarding theXXXgate as a matrix clarifies what may have been a confusing point earlier. I wrote theXXXgate as having the actionX∣0⟩=∣1⟩X|0\rangle = |1\rangleX∣0⟩=∣1⟩,X∣1⟩=∣0⟩X|1\rangle = |0\rangleX∣1⟩=∣0⟩.Implicitly – I never quite said this, though it’s true – theXXXgate is a mathematical function, taking input states to output states. But when we write functions we usually use parentheses, so why didn’t I writeX(∣0⟩)X(|0\rangle)X(∣0⟩)and similarly for∣1⟩|1\rangle∣1⟩?The reason is that for linear functions, i.e., matrices, it’s conventional to omit parentheses and just writeX∣0⟩X|0\rangleX∣0⟩– function applicationisjust matrix multiplication.

We’ve now seen a simple quantum circuit and quantum logic gate. But it’s not quite the simplest possible quantum circuit. The simplest possible quantum circuit does nothing at all. That is, it’s a single quantum wire:





This circuit is just a single qubit being preserved in time. To be more explicit, if some arbitrary quantum state∣ψ⟩|\psi\rangle∣ψ⟩is input to the circuit, then the exact same state∣ψ⟩|\psi\rangle∣ψ⟩is output (it’s common practice to use the Greek letterψ\psiψto denote an arbitrary quantum state):





Mathematically, this circuit is trivial. But physically it’s far from trivial. In many physical systems, the quantum wire is actually one of the hardest quantum computations to implement!

The reason is that quantum states are often incredibly fragile. If your qubit is being stored in some tiny system – perhaps a single photon or a single atom – then it’s very, very easy to disturb that state. It really doesn’t take much to upset an atom or a photon. And so while quantum wires are mathematically trivial, they can be one of the hardest elements to build in real systems.

That said, there are some systems where quantum wires are easy to implement. If you store your qubit in a neutrino then the state will actually be pretty well preserved. The reason is that neutrinos barely interact with other forms of matter at all – a neutrino can easily pass through a mile of lead without being disturbed. But while it’s intriguing that neutrinos are so stable, it doesn’t mean they make good qubits. The trouble is that since there’s no easy way of using ordinary matter to interact with them, we can’t manipulate their quantum state in a controlled fashion, and so can’t implement a quantum gate.

There’s a tension here that applies to many proposals to do quantum information processing, not just neutrinos. If we want to store the quantum state, then it’s helpful if our qubits only interact very weakly with other systems, so those systems don’t disrupt them. But if the qubits only interact weakly with other systems then that also makes it hard to manipulate the qubits. Thus, systems which make good quantum wires are often hard to build quantum gates for. Much of the art of designing quantum computers is about finding ways to navigate this tension. Often, that means trying to design systems which interact weakly most of the time, but some of the time can be caused to interact strongly, and so serve as part of a quantum gate.

You’ll note that some of the questions above have a different flavor to the questions earlier in the essay. Early questions had cut-and-dried answers. The answer to the question “What’s the standard notation for the quantum NOT gate?” is just: “XXX”. But some of the questions above have less well-specified answers. They’re a little fluffy.

This fluffiness may cause you difficulties as you decide how to respond. Your answer to the question “Why is it that systems which make good quantum wires are often hard to build quantum gates for?” may not quite match the answer given. If this is the case, don’t worry. You should mark yourself correct if you’re confident you’ve understood the point, even in terms different from my phrasing. And mark yourself incorrect if the point still needs reinforcement.

Let’s take a look at a simple multiple-gate quantum circuit. It’s just a circuit with twoXXXgates in a row:





It’s worth pausing for a moment, and trying to guess what this circuit does to the input state. It’s worth doing this even if you usually find this kind of guessing frustrating. Even when you get stuck, building up strategies for dealing with stuckness is part of learning any difficult subject. So take a minute or so now.

We’ll try two different ways of figuring out what’s going on. Here’s one approach, based on applyingXXXtwice to an arbitrary input state,α∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩.It’s simple algebra, using the factXXXinterchanges the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states:

X(X(α∣0⟩+β∣1⟩))=X(α∣1⟩+β∣0⟩)=α∣0⟩+β∣1⟩\begin{aligned} X(X(\alpha|0\rangle+\beta|1\rangle)) & = X(\alpha|1\rangle + \beta|0\rangle) \\ & = \alpha|0\rangle + \beta|1\rangle \end{aligned}X(X(α∣0⟩+β∣1⟩))​=X(α∣1⟩+β∣0⟩)=α∣0⟩+β∣1⟩​

So the net effect is to recover the original quantum state, no matter what that state was. In other words, this circuit is equivalent to a quantum wire:





A second way of seeing this is based on the matrix representation we found earlier for theXXXgate. Observe that if the input is some arbitrary quantum state∣ψ⟩|\psi\rangle∣ψ⟩,then after the first gate the state isX∣ψ⟩X|\psi\rangleX∣ψ⟩,and after the second gate the state isXX∣ψ⟩X X |\psi\rangleXX∣ψ⟩.Then we observe that the productXXX XXXis

XX=[0110][0110]=[1001].\begin{aligned} XX & = \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right] \\ & = \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right]. \end{aligned}XX​=[01​10​][01​10​]=[10​01​].​

That is,XXXXXXis the identity operation, and so the outputXX∣ψ⟩XX|\psi\rangleXX∣ψ⟩is just the original input∣ψ⟩|\psi\rangle∣ψ⟩.In other words, twoXXXgates is the same as a quantum wire. And so we’ve arrived at the same conclusion in a different way, using matrix multiplication. Doing such matrix multiplications is a pretty common way of analyzing quantum circuits.

We’ve seen our first quantum gate, the NOT orXXXgate. Of course, theXXXdidn’t appear to do all that much beyond what is possible with a classical NOT gate. In this section I introduce a gate that clearly involves quantum effects, theHadamardgate.

As with theXXXgate, we’ll start by explaining how the Hadamard gate acts on computational basis states. Denoting the gate byHHH,here’s what it does:

H∣0⟩=∣0⟩+∣1⟩2H|0\rangle = \frac{|0\rangle +|1\rangle}{\sqrt 2}H∣0⟩=2​∣0⟩+∣1⟩​

H∣1⟩=∣0⟩−∣1⟩2H|1\rangle = \frac{|0\rangle -|1\rangle}{\sqrt 2}H∣1⟩=2​∣0⟩−∣1⟩​

Of course,∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩aren’t the only quantum states. How does the Hadamard gate act on more general quantum states?

It won’t surprise you to learn that it acts linearly, as did the quantum NOT gate. In particular, the Hadamard gate takes a superpositionα∣0⟩+β∣1⟩\alpha|0\rangle + \beta|1\rangleα∣0⟩+β∣1⟩to the corresponding superposition of outputs:

H(α∣0⟩+β∣1⟩)=α(∣0⟩+∣1⟩2)+β(∣0⟩−∣1⟩2).H(\alpha|0\rangle + \beta|1\rangle) = \alpha \left( \frac{|0\rangle+|1\rangle}{\sqrt 2} \right) + \beta \left( \frac{|0\rangle-|1\rangle}{\sqrt 2} \right).H(α∣0⟩+β∣1⟩)=α(2​∣0⟩+∣1⟩​)+β(2​∣0⟩−∣1⟩​).

That’s a mess. We can make it less of a mess by combining the∣0⟩|0\rangle∣0⟩terms together, and also the∣1⟩|1\rangle∣1⟩terms together:

H(α∣0⟩+β∣1⟩)=α+β2∣0⟩+α−β2∣1⟩.H(\alpha|0\rangle + \beta|1\rangle) = \frac{\alpha+\beta}{\sqrt 2} |0\rangle + \frac{\alpha-\beta}{\sqrt 2}|1\rangle.H(α∣0⟩+β∣1⟩)=2​α+β​∣0⟩+2​α−β​∣1⟩.

That’s better, but still not pretty! Fortunately, we mostly won’t be dealing with such complex expressions. The only reason I’ve done it here is to be really explicit. Instead of dealing with such explicit expressions, we’ll mostly work with theHHHgate in its circuit and matrix representations (see below). Those let us focus at a more enlightening level of abstraction, rather than messing around with coefficients.

Indeed, much work on quantum computing is about attempting to develop ways of moving from low levels of abstraction to higher, more conceptual levels. Up to now most of our work has been at a very low level, seeming more an exercise in linear algebra than a discussion of a new model of computing. That perhaps seems strange. After all, if you were explaining classical computers to someone, you wouldn’t start in the weeds, with AND and NOT gates and the like. You’d start with a well-designed high-level programming language, and then bounce back and forth between different layers of abstraction. Modern computers aren’t just about logic gates – they’re at least as much about beautiful higher-level ideas: say, lazy evaluation, or higher-order functions, or homoiconicity, and so on.

I wish I could start with high-level abstractions for quantum computers. However, we’re still in the early days of quantum computing, and for the most part humanity hasn’t yet discovered such high-level abstractions. People are still scratching around, trying to find good ideas.

That’s an exciting situation: it means almost all the big breakthroughs are ahead. There’s a sense in which we still understand very little about quantum computing. That might sound surprising: after all, there aregreat big fat textbooks on the subject. But you could have written a great big fat textbook about the ENIAC computer in the late 1940s. It was, after all, a very complex system. That textbook would have looked intimidating, but it wouldn’t have been the final word in computing. For the most part the way we understand quantum computing today is at an ENIAC-like level, looking at the nuts-and-bolts of qubits and logic gates and linear algebra, and wondering what the higher-level understanding may be. The situation can be thought of as much like programming language design before the breakthroughs that led to languages such as Lisp and Haskell and Prolog and Smalltalk. That makes it a remarkable creative opportunity, a challenge for the decades and centuries ahead.

Speaking of nuts-and-bolts, let’s get back to the Hadamard gate. Here’s the circuit representation for the Hadamard gate. It looks just like theXXXgate in the circuit representation, except we change the gate label toHHH:





Just like theXXXgate,HHHhas a matrix representation:

H=12[111−1].H = \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right].H=2​1​[11​1−1​].

To see that this matrix representation is correct, let’s check the action of the matrix on the∣0⟩|0\rangle∣0⟩and the∣1⟩|1\rangle∣1⟩states. Here we check for the∣0⟩|0\rangle∣0⟩state:

12[111−1]∣0⟩=12[111−1][10]=12[11]=∣0⟩+∣1⟩2.\begin{aligned} \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right] |0\rangle & = \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right] \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] \\ & = \frac{1}{\sqrt 2} \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \\ & = \frac{|0\rangle+|1\rangle}{\sqrt 2}. \end{aligned}2​1​[11​1−1​]∣0⟩​=2​1​[11​1−1​][10​]=2​1​[11​]=2​∣0⟩+∣1⟩​.​

That is, this matrix acts the same way as the Hadamard gate on the∣0⟩|0\rangle∣0⟩state. Now let’s check on the∣1⟩|1\rangle∣1⟩state:

12[111−1]∣1⟩=12[111−1][01]=12[1−1]=∣0⟩−∣1⟩2.\begin{aligned} \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right] |1\rangle & = \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ & = \frac{1}{\sqrt 2} \left[ \begin{array}{c} 1 \\ -1 \end{array} \right] \\ & = \frac{|0\rangle-|1\rangle}{\sqrt 2}. \end{aligned}2​1​[11​1−1​]∣1⟩​=2​1​[11​1−1​][01​]=2​1​[1−1​]=2​∣0⟩−∣1⟩​.​

So the matrix acts the same way as the Hadamard gate on both the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states. By the linearity of matrix multiplication it follows that the matrix acts the same way as the Hadamard on all input states, and so they are the same operation.

What makes the Hadamard gate interesting as a quantum gate? What can we use it to do?

We don’t (quite) have enough background to give precise answers to these questions yet. But there is an analogy which gives insight.

Imagine you are living in North Africa, thousands of years in the past, and decide for some reason that you want to get over to the Iberian peninsula. If you don’t yet have boats or some other reliable method of moving across large bodies of water, you need to go all the way across Africa, past the Arabian peninsula, up and around through Europe, back to the Iberian peninsula:

Original photo source: Reto Stöckli,NASA Earth Observatory(2004).

Suppose, however, that you invent a new device, the boat, which expands the range of locations you can traverse. Then you can take a much more direct route over to the Iberian peninsula, greatly cutting down the time required:

What the Hadamard and similar gates do is expand the range of operations that it’s possible for a computer to perform. That expansion makes it possible for the computer to take shortcuts, as the computer “moves” in a way that’s not possible in a conventional classical computer. And, we hope, that may enable us to solve some computational problems faster.

Another helpful analogy is to the game of chess. Imagine you’re playing chess and the rules are changed in your favor, enabling your rook an expanded range of moves. That extra flexibility might enable you to achieve checkmate much faster because you can get to new positions much more quickly.

A similar thing is going on with the Hadamard gate. By expanding the range of states we can access (or, more precisely, the range of dynamical operations we can generate) beyond what’s possible on a classical computer, it becomes possible to take shortcuts in our computation.

We’ll see explicit examples in subsequent essays.

To get more familiar with the Hadamard gate, let’s analyze a simple circuit:





What’s this circuit do?

Before we compute, it’s worth pausing for a second to try guessing the result. The point of guessing isn’t to get it right – rather, it’s to challenge yourself to start coming up with heuristic mental models for thinking about what’s going on in quantum circuits. Those mental models likely won’t be very good at first, but that’s okay – if you keep doing this, they’ll get better.

Here’s one heuristic you can use to think about this circuit: you can think ofHHHas sort of mixing the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states together. So if you applyHHHtwice to∣0⟩|0\rangle∣0⟩,perhaps it would thoroughly mix the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩up together. What sort of state do you think would result, according to this heuristic? Do you believe the result? Why or why not? Can you think of other heuristics that might help you guess an answer?

Alright, let’s compute what actually happens. After we apply the first Hadamard to∣0⟩|0\rangle∣0⟩we get

∣0⟩+∣1⟩2.\frac{|0\rangle+|1\rangle}{\sqrt{2}}.2​∣0⟩+∣1⟩​.

Then we apply a second Hadamard gate. This takes the∣0⟩|0\rangle∣0⟩term above to∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​and the∣1⟩|1\rangle∣1⟩term to∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​,so the output is:

12(∣0⟩+∣1⟩2+∣0⟩−∣1⟩2).\frac{1}{\sqrt 2} \left( \frac{|0\rangle+|1\rangle}{\sqrt 2} + \frac{|0\rangle-|1\rangle}{\sqrt 2} \right).2​1​(2​∣0⟩+∣1⟩​+2​∣0⟩−∣1⟩​).

If you look at the expression above, you’ll notice that the∣1⟩|1\rangle∣1⟩terms cancel each other out, so you’re just left with the∣0⟩|0\rangle∣0⟩terms. Collecting them up, we’re left with the∣0⟩|0\rangle∣0⟩state, same as we started with:

12(∣0⟩2+∣0⟩2)=∣0⟩.\frac{1}{\sqrt 2} \left(\frac{|0\rangle}{\sqrt 2}+ \frac{|0\rangle}{\sqrt 2} \right) = |0\rangle.2​1​(2​∣0⟩​+2​∣0⟩​)=∣0⟩.

In a similar fashion, after we run the∣1⟩|1\rangle∣1⟩state through the first Hadamard gate, we get:

∣0⟩−∣1⟩2.\frac{|0\rangle-|1\rangle}{\sqrt{2}}.2​∣0⟩−∣1⟩​.

Then we apply a second Hadamard gate to get:

12(∣0⟩+∣1⟩2−∣0⟩−∣1⟩2).\frac{1}{\sqrt 2} \left( \frac{|0\rangle+|1\rangle}{\sqrt 2} - \frac{|0\rangle-|1\rangle}{\sqrt 2} \right).2​1​(2​∣0⟩+∣1⟩​−2​∣0⟩−∣1⟩​).

This time it’s the∣0⟩|0\rangle∣0⟩terms which cancel out, and the∣1⟩|1\rangle∣1⟩terms reinforce. When we collect up these terms, we see that the output is just the∣1⟩|1\rangle∣1⟩state, same as we started with. And so both the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states are left unchanged by this quantum circuit, and the net effect of the circuit is exactly the same as a quantum wire:



There’s an alternate way of seeing this, which I’ll sketch out without working through in detail. It’s to note that if we input an arbitrary quantum state∣ψ⟩|\psi\rangle∣ψ⟩to the circuit, then the output must beHH∣ψ⟩H H |\psi\rangleHH∣ψ⟩,i.e., the result of applying twoHHHmatrices to∣ψ⟩|\psi\rangle∣ψ⟩.But if you just compute the matrix productHHH HHHit turns out to be the2×22 \times 22×2identity matrix,HH=IH H = IHH=I.And so the output from the circuit must be the same as the input,HH∣ψ⟩=I∣ψ⟩=∣ψ⟩HH|\psi\rangle = I |\psi\rangle = |\psi\rangleHH∣ψ⟩=I∣ψ⟩=∣ψ⟩,just as from a quantum wire.

Of course, this result violates our intuitive guess, which was that two Hadamards would thoroughly mix up the∣0⟩|0\rangle∣0⟩and the∣1⟩|1\rangle∣1⟩.It’s interesting to ponder what went wrong with our intuition, say by looking through the calculation forHHHacting twice on∣0⟩|0\rangle∣0⟩.You see that after the second gate the∣1⟩|1\rangle∣1⟩terms exactly cancel one another out, while the∣0⟩|0\rangle∣0⟩terms reinforce one another.

This seems innocuous, almost like a mathematical accident. Still, I draw your attention to it because this type of cancellation or reinforcement is crucial in many algorithms for quantum computers. Without getting into details, the rough way many such algorithms work is to first use Hadamard gates to “spread out” in quantum states like∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​(or many-qubit analogs), i.e., in superpositions of multiple computational basis states. At the end of the algorithm they use clever patterns of cancellation and reinforcement to bring things back together again into one (or possibly a few, in the many-qubit case) computational basis state, containing the desired answer. That’s a somewhat vague and perhaps tantalizing description, but the point to take away is that the kind of cancellation-or-reinforcement we saw above is actually crucial in many quantum computations.

I’ll now pose a few simple exercises related to the Hadamard gate. Unlike the spaced-repetition questions, the point of the exercises below isn’t as an aid to memory, and so you won’t see these exercises repeatedly. Rather, they’re here because (should you choose to work through them) they will help you better understand the material of the essay. But they’ll only incidentally help with memorization. We’ll follow them with some spaced-repetition questions. Note that even if you don't work through the exercises, it's worth at least reading through them, since some of the results will be tested in the spaced-repetition questions.

Exercise:Verify thatHH=IHH = IHH=I,whereIIIis the2×22 \times 22×2identity matrix,I=[1001]I = \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right]I=[10​01​].

Exercise:Suppose that instead ofHHHwe’d defined a matrixJJJby:

J:=12[1111]J := \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & 1 \end{array} \right]J:=2​1​[11​11​]

At first, it might seem thatJJJwould make an interesting quantum gate, along lines similar toHHH.For instance,J∣0⟩=∣0⟩+∣1⟩2J|0\rangle = \frac{|0\rangle+|1\rangle}{\sqrt 2}J∣0⟩=2​∣0⟩+∣1⟩​,andJ∣1⟩=∣0⟩+∣1⟩2J|1\rangle = \frac{|0\rangle+|1\rangle}{\sqrt 2}J∣1⟩=2​∣0⟩+∣1⟩​.These are both good, normalized quantum states. But what happens if we applyJJJto the quantum state∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​?Why does this makeJJJunsuitable for use as a quantum gate?

Exercise:Consider the quantum circuit:

Explain why the output from this circuit isXH∣ψ⟩XH|\psi\rangleXH∣ψ⟩,notHX∣ψ⟩HX|\psi\rangleHX∣ψ⟩,as you might naively assume if you wrote down gates in the order they occur in the circuit. This is a common gotcha to be aware of – it occurs because quantum gates compose left-to-right in the circuit representation, while matrix multiplications compose right-to-left.

Suppose a (hypothetical!) quantum physicist named Alice prepares a qubit in her laboratory, in a quantum stateα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩.Then she gives her qubit to another quantum physicist, Bob, but doesn’t tell him the values ofα\alphaαandβ\betaβ.Is there some way Bob can figure outα\alphaαandβ\betaβ?That is, is there some experiment Bob can do to figure out the identity of the quantum state?

The surprising answer to this question turns out to beNO!There is, in fact, no way to figure outα\alphaαandβ\betaβif they start out unknown. To put it a slightly different way, the quantum state of any system – whether it be a qubit or a some other system – is not directly observable.

I say this is surprising, because it’s very different from our usual everyday way of thinking about how the world works. If there’s something wrong with your car, a mechanic can use diagnostic tools to learn about the internal state of the engine. The better the diagnostic tools, the more they can learn. Of course, there may be parts of the engine that would be impractical to access – maybe they’d have to break a part, or use a microscope, for instance. But you’d probably be rather suspicious if the mechanic told you the laws of physics prohibited them from figuring out the internal state of the engine.

Similarly, when you first start learning about quantum circuits, it seems like we should be able to observe the amplitudes of a quantum state whenever we like. But that turns out to be prohibited by the laws of physics. Those amplitudes are better thought of as a kind of hidden information.

So, what can we figure out from the quantum state? Rather than somehow measuringα\alphaαandβ\betaβ,there are other ways of getting useful information out of a qubit. Let me describe an especially important process calledmeasurement in the computational basis. This is a fundamental primitive in quantum computing: it’s the way we typically extract information from our quantum computers. I’ll explain now how it works for a single qubit, and later generalize to multi-qubit systems.

Suppose a qubit is in the stateα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩.When you measure this qubit in the computational basis it gives you a classical bit of information: it gives you the outcome000with probability∣α∣2|\alpha|^2∣α∣2,and the outcome111with probability∣β∣2|\beta|^2∣β∣2.

To think a little more concretely about this process, suppose your qubit is instantiated in some physical system. Perhaps it’s being stored in the state of an atom somehow. It doesn’t matter exactly what, but you have this qubit in your laboratory. And you have some measurement apparatus, probably something large and complicated, maybe involving lasers and microprocessors and a screen for readout of the measurement result. And this measurement apparatus interacts in some way with your qubit.

After the measurement interaction, your measurement apparatus registers an outcome. For instance, it might be that you get the outcome000.Or maybe instead you get the outcome111.The crucial fact is that the outcome is ordinary classical information – the stuff you already know how to think about – which you can then use to do other things, and to control other processes.

So the way a quantum computation works is that we manipulate a quantum state using a series of quantum gates, and then at the end of the computation (typically) we do a measurement to read out the result of the computation. If our quantum computer is just a single qubit, then that result will be a single classical bit. If, as is more usually the case, it’s multiple qubits, then the measurement result will be multiple classical bits.

A fundamental fact about this measurement process is that it disturbs the state of the quantum system. In particular, it doesn’t just leave the quantum state alone. After the measurement, if you get the outcome000then the state of the qubit afterwards (the “posterior state”) is the computational basis state∣0⟩|0\rangle∣0⟩.On the other hand, if you get the outcome111then the posterior state of the qubit is the computational basis state∣1⟩|1\rangle∣1⟩.

Summing all this up: if we measure a qubit with stateα∣0⟩+β∣1⟩\alpha |0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩in the computational basis, then the outcome is a classical bit: either000,with probability∣α∣2|\alpha|^2∣α∣2,or111,with probability∣β∣2|\beta|^2∣β∣2.The corresponding state of the qubit after the measurement is∣0⟩|0\rangle∣0⟩or∣1⟩|1\rangle∣1⟩.

A key point to note is that after the measurement, no matter what the outcome,α\alphaαandβ\betaβare gone. No matter whether the posterior state is∣0⟩|0\rangle∣0⟩or∣1⟩|1\rangle∣1⟩,there is no trace ofα\alphaαorβ\betaβ.And so you can’t get any more information about them. In that sense,α\alphaαandβ\betaβare a kind of hidden information – the measurement doesn’t tell you what they were.

One reason this is important is because it means you can’t store an infinite amount of classical information in a qubit. After all,α\alphaαis a complex number, and you could imagine storing lots of classical bits in the binary expansion of the real component ofα\alphaα.If there was some experimental way you could measure the value ofα\alphaαexactly, then you could extract that classical information. But without a way of measuringα\alphaαthat’s not possible.

I’ve been talking about measurement in the computational basis. In fact, there are other types of measurement you can do in quantum systems. But there’s a sense in which computational basis measurements turn out to be fundamental. The reason is that by combining computational basis measurements with quantum gates like the Hadamard and NOT (and other) gates, it’s possible to simulate arbitrary quantum measurements. So this is all you absolutely need to know about measurement, from an in-principle point of view.

It’s useful to have a way of denoting measurements in the quantum circuit model. Here’s a simple example:



It’s a single-qubit quantum circuit, with input the state∣ψ⟩|\psi\rangle∣ψ⟩.A NOT gate is applied, followed by a Hadamard gate. The circuit finishes with a measurement in the computational basis, denoted by the slightly elongated semi-circle. Themmmis a classical bit denoting the measurement result – either000or111– and we use the double wire to indicate the classical bitmmmgoing off and being used to do something else.

Of course, I said above that after measurement the qubit is in either the∣0⟩|0\rangle∣0⟩or the∣1⟩|1\rangle∣1⟩state. You might think we’d draw a corresponding quantum wire coming out the other side of the measurement. But often in quantum circuits the qubit is discarded after measurement, and that’s assumed by this notation.

One final comment on measurement is that it’s connected to the normalization condition for quantum states that we discussed earlier. Suppose we have the quantum state:

α∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩

Then the probability of the two possible measurement outcomes,000and111,must sum to111,and so we have:

∣α∣2+∣β∣2=1.|\alpha|^2+|\beta|^2 = 1.∣α∣2+∣β∣2=1.

This is exactly the normalization condition for quantum states – i.e., the quantum state must have length111.The origin of that constraint is really just the fact that measurement probabilities must add up to111.

Exercise:Suppose we’ve been given either the state∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​or the state∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​,but not told which state we’ve been given. We’d like to figure out which state we’ve been given. If we just do a computational basis measurement, then for both states we get outcome000with probability12\frac 1221​,and outcome111with probability12\frac 1221​.So we can’t distinguish the states directly using a computational basis measurement. But suppose instead we put the state into the following circuit:



Show that if the state∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​is input then the output ism=0m = 0m=0with probability111,while if the state∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​is input then the output ism=1m = 1m=1with probability111.Thus while these two states are indistinguishable if just measured in the computational basis, they can be distinguished with the help of a simple quantum circuit.

So far we’ve learned about two quantum gates, the NOT and the Hadamard gate, and also about the measurement process that can be used to extract classical information from our quantum circuits. In this section, I return to quantum gates, and take a look at the most general single-qubit gate. To do that it helps to recall the matrix representations of the NOT and Hadamard gates:

X=[0110];H=12[111−1]\begin{aligned} X = \left[ \begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right]; \,\,\,\, H = \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right] \end{aligned}X=[01​10​];H=2​1​[11​1−1​]​

If the input to these gates is the quantum state∣ψ⟩|\psi\rangle∣ψ⟩,then the output isX∣ψ⟩X|\psi\rangleX∣ψ⟩andH∣ψ⟩H|\psi\rangleH∣ψ⟩respectively.

A general single-qubit gate works similarly. In particular, a general single-qubit gate can be represented as a2×22 \times 22×2unitary matrix,UUU.(If you’re rusty, I’ll remind you what it means for a matrix to be unitary in a moment, and you can just think of it as a matrix for now.) If the input to the gate is the state∣ψ⟩|\psi\rangle∣ψ⟩then the output from the gate isU∣ψ⟩U|\psi\rangleU∣ψ⟩.And so the NOT and Hadamard gates correspond to the special cases whereU=XU = XU=XandU=HU = HU=H,respectively.

What does it mean for a matrixUUUto be unitary? It’s easiest to answer this question algebraically, where it simply means thatU†U=IU^\dagger U = IU†U=I,that is, the adjoint ofUUU,denotedU†U^\daggerU†,timesUUU,is equal to the identity matrix. That adjoint is, recall, the complex transpose ofUUU:

U†:=(UT)∗.U^\dagger := (U^T)^*.U†:=(UT)∗.

So for a2×22 \times 22×2matrix, the adjoint operation is just:

[abcd]†=[a∗c∗b∗d∗].\left[ \begin{array}{cc} a & b \\ c & d \end{array} \right]^\dagger = \left[ \begin{array}{cc} a^* & c^* \\ b^* & d^* \end{array} \right].[ac​bd​]†=[a∗b∗​c∗d∗​].

(Note that the†\dagger†is also sometimes called thedagger operation, orHermitian conjugation, or just theconjugationoperation. We’ll use all three terms on occasion.)

There are a few basic questions you might ask: why are single-qubit gates described by unitary matrices? And how can we get an intuitive feel for what it means for a matrix to be unitary, anyway? While the equationU†U=IU^\dagger U = IU†U=Iis easy to check algebraically, we’d like some intuition for what that equation means.

Another natural question is whether the NOT gate and the Hadamard gate are unitary? Of course, we’ll see that they are – I wouldn’t have described them as quantum gates if not – but we should go to the trouble of checking.

Yet another good question is whether there are useful examples of single-qubit gates that aren’t the NOT or Hadamard gates? The equationU†U=IU^\dagger U = IU†U=Iis all very well, but it’d be nice to have more concrete examples than just an abstract equation.

We’ll answer all these questions over the next few sections.

Let’s start by checking the unitarity of the Hadamard gate. We start by computing the adjoint ofHHH:

H†=((12[111−1])T)∗.H^\dagger = \left( \left( \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right]\right)^T\right)^*.H†=((2​1​[11​1−1​])T)∗.

Note that taking the transpose doesn’t change the matrix, since it is already symmetric. And taking the complex conjugate doesn’t change anything, since all the entries are real. So we haveH†=HH^\dagger = HH†=H,and thusH†H=HHH^\dagger H = HHH†H=HH.But we saw earlier in the essay thatHH=IHH = IHH=I.SoHHHis, indeed, unitary.

Exercise:Show thatXXXis unitary.

Exercise:Show that the identity matrixIIIis unitary.

Exercise:Can you find an example of a2×22 \times 22×2matrix that is unitary, and is notIII,XXX,orHHH?

For flavor, let’s give a few more examples of single-qubit quantum gates. Earlier in the essay, I mentioned that the NOT gateXXXwas introduced by the physicist Wolfgang Pauli in the early days of quantum mechanics. He introduced two other matrices,YYYandZZZ,which are also useful quantum gates. The three gates,X,YX, YX,Y,andZZZare known collectively as thePauli matrices. TheYYYandZZZgates will be useful extra tools in our toolkit of quantum gates; in terms of the earlier analogy they expand the repertoire of moves we have available to us. They’re crucial, for example, in protocols such as quantum teleportation and quantum error correction.

TheYYYgate is similar to theXXXgate, but instead of111son the off-diagonal, it hasiiiand−i-i−i,so it takes∣0⟩|0\rangle∣0⟩toi∣1⟩i|1\ranglei∣1⟩and∣1⟩|1\rangle∣1⟩to−i∣0⟩-i|0\rangle−i∣0⟩:

Y:=[0−ii0].Y := \left[ \begin{array}{cc} 0 & -i \\ i & 0 \end{array} \right].Y:=[0i​−i0​].

TheZZZgate leaves∣0⟩|0\rangle∣0⟩unchanged, and takes∣1⟩|1\rangle∣1⟩to−∣1⟩-|1\rangle−∣1⟩:

Z:=[100−1].Z := \left[ \begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array} \right].Z:=[10​0−1​].

Exercise:Show that theYYYandZZZmatrices are unitary, and so legitimate quantum gates.

Another good example of a quantum gate is a rotation, the kind of matrix you’ve most likely been seeing since high school. It’s just the ordinary rotation of the222-dimensional plane by an angleθ\thetaθ:

[cos⁡(θ)−sin⁡(θ)sin⁡(θ)cos⁡(θ)].\left[ \begin{array}{cc} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{array} \right].[cos(θ)sin(θ)​−sin(θ)cos(θ)​].

You can easily check that this is a unitary matrix, and so it’s valid quantum gate. And sometimes it’s a very useful quantum gate!

That mostly wraps up our little library of single-qubit gates. In the next couple of sections we’ll build up some intuition about what unitarity means, but we won’t add any extra elements to our quantum computing model. In fact, at this point we know almost everything needed for quantum computation. There are just two extra elements needed: extending our description of single qubits to multiple qubits, and describing a simple two-qubit quantum gate. We’ll get to those things shortly – not surprisingly, they look much like what we’ve already seen.

I am, by the way, somewhat uncomfortable with some of the questions just asked. My personal experience is that spaced-repetition learning works well when learning facts I have a lot of context for, and care a lot about. It’s a rare person who finds the detailed entries in a unitary matrix fascinating! That’s not to say they aren’t – actually, theyare, but you need a lot more context than I’ve provided to see why (for instance) that−i-i−iin theYYYis just so darn interesting.

With that said, this essay is genuinely an experiment, and the questions above are included in that spirit. Maybe it will turn out that readers can use spaced-repetition to learn the entries of unitary matrices. And maybe they cannot. No matter which that’ll be a valuable thing to learn about the world, and to inform future experiments with spaced-repetition learning.

Can we get an intuition for what it means for a matrix to be unitary? It turns out that unitary matricespreserve the length of their inputs. In other words, if we take any vector∣ψ⟩|\psi\rangle∣ψ⟩and compute the length∥U∣ψ⟩∥\| U|\psi\rangle \|∥U∣ψ⟩∥it’s always equal to the length∥∣ψ⟩∥\||\psi\rangle\|∥∣ψ⟩∥of the original vector. In this, they’re much like rotations or reflections in ordinary (real) space, which also don’t change lengths. In a sense, the unitary matrices are a complex generalization of real rotations and reflections.

Up to now we’ve been dealing mostly with vectors which are states of qubits, i.e., normalized 2-dimensional vectors. But in fact the statement of the last paragraph is true ford×dd \times dd×dunitary matrices, too, i.e.,∥U∣ψ⟩∥=∥∣ψ⟩∥\|U|\psi\rangle\| = \||\psi\rangle\|∥U∣ψ⟩∥=∥∣ψ⟩∥is true for any vector∣ψ⟩|\psi\rangle∣ψ⟩inddddimensions.

The proof is actually pretty simple – mostly, we just compute∥U∣ψ⟩∥\|U|\psi\rangle \|∥U∣ψ⟩∥and use a little algebra to check that it’s equal to the length∥∣ψ⟩∥\||\psi\rangle\|∥∣ψ⟩∥.But before we get to the proof, observe that this result is good news for quantum gates. The reason is that in a quantum gate the input state will be normalized (have length111), since that’s a requirement for a quantum state. And we’d expect the corresponding output state to also be normalized, otherwise it wouldn’t be a legitimate quantum state. Fortunately, the length-preserving property of unitary matrices ensures the output state is properly normalized.

Recall also the larger story this is part of: not only are gates unitary, to ensure that states remain normalized; also, quantum states are normalized, since measurement probabilities must sum to111.It all fits together.

In fact it turns out that unitary matrices are theonlymatrices which preserve length in this way. And so a good way of thinking about unitary matrices is that they’re exactly the class of matrices which preserve length. That’s the geometric interpretation (and intuitive meaning) of the algebraic conditionU†U=IU^\dagger U = IU†U=I.

Let’s prove now that unitary matrices really are length-preserving.

The proof is straightforward. The main thing is to compute∥U∣ψ⟩∥\|U|\psi\rangle\|∥U∣ψ⟩∥.Actually, it’s a little easier to compute the square of the length,∥U∣ψ⟩∥2\|U|\psi\rangle\|^2∥U∣ψ⟩∥2.This is just the sum of the squares of the absolute values of the components of the vectorU∣ψ⟩U|\psi\rangleU∣ψ⟩:

∥U∣ψ⟩∥2=∑j(Uψ)j∗(Uψ)j\|U|\psi\rangle\|^2 = \sum_j (U\psi)_j^* (U\psi)_j∥U∣ψ⟩∥2=j∑​(Uψ)j∗​(Uψ)j​

Note that I’ve used(Uψ)j(U\psi)_j(Uψ)j​to denote thejjjth component ofU∣ψ⟩U|\psi\rangleU∣ψ⟩,dropping the full ket notation, and just usingψ\psiψalone. To proceed, we’ll expand the equation above out, and look for opportunities to apply the unitarity ofUUU.In particular, the component(Uψ)j(U\psi)_j(Uψ)j​is given by∑lUjlψl\sum_l U_{jl} \psi_l∑l​Ujl​ψl​and similarly for the complex conjugate term. So we can rewrite the above equation as:

∥U∣ψ⟩∥2=∑jklUjk∗ψk∗Ujlψl\|U|\psi\rangle\|^2 = \sum_{jkl} U_{jk}^*\psi_k^* U_{jl}\psi_l∥U∣ψ⟩∥2=jkl∑​Ujk∗​ψk∗​Ujl​ψl​

To make use of the unitarity ofUUUwe’ll move theUUUterms together, and rewrite in terms ofU†U^\daggerU†.This gives

∥U∣ψ⟩∥2=∑jklUkj†Ujlψk∗ψl,\|U|\psi\rangle\|^2 = \sum_{jkl} U_{kj}^\dagger U_{jl} \psi_k^* \psi_l,∥U∣ψ⟩∥2=jkl∑​Ukj†​Ujl​ψk∗​ψl​,

where we interchanged thejkjkjkindices on the firstUUUin order to rewrite it in terms ofU†U^\daggerU†.The only place thejjjindex appears anywhere in this equation is in theUkj†UjlU_{kj}^\dagger U_{jl}Ukj†​Ujl​term. We can therefore perform the sum overjjjand those terms become(U†U)kl(U^\dagger U)_{kl}(U†U)kl​,which is just theklklklth term in the identity matrix, sinceU†U=IU^\dagger U = IU†U=I.So the above equation becomes:

∥U∣ψ⟩∥2=∑klδklψk∗ψl.\|U|\psi\rangle\|^2 = \sum_{kl} \delta_{kl} \psi_k^* \psi_l.∥U∣ψ⟩∥2=kl∑​δkl​ψk∗​ψl​.

When we sum, the only timeδkl\delta_{kl}δkl​is not equal to zero is whenk=lk=lk=l,in which case it’s111.And so we can get rid of one of the summation indices, and the equation simplifies to:

∥U∣ψ⟩∥2=∑kψk∗ψk.\|U|\psi\rangle\|^2 = \sum_{k} \psi_k^* \psi_k.∥U∣ψ⟩∥2=k∑​ψk∗​ψk​.

The right-hand side is, of course, equal to the norm of∣ψ⟩|\psi\rangle∣ψ⟩squared. And so we’ve shown∥U∣ψ⟩∥2=∥∣ψ⟩∥2\|U|\psi\rangle\|^2 = \||\psi\rangle\|^2∥U∣ψ⟩∥2=∥∣ψ⟩∥2,and therefore∥U∣ψ⟩∥=∥∣ψ⟩∥\|U|\psi\rangle\| = \||\psi\rangle\|∥U∣ψ⟩∥=∥∣ψ⟩∥.That completes the proof that unitary matrices are length-preserving.QED

In fact, as I mentioned earlier, it’s also possible to prove that unitary matrices are the only matrices which preserve lengths in this way. Let me state that a little more precisely:

Theorem:LetMMMbe a matrix. Then∥M∣ψ⟩∥=∥∣ψ⟩∥\|M|\psi\rangle \| = \||\psi\rangle\|∥M∣ψ⟩∥=∥∣ψ⟩∥for all vectors∣ψ⟩|\psi\rangle∣ψ⟩if and only ifMMMis unitary.

We’ve proved one half of this already; we’ll prove the other half in the next section. This theorem answers many of our questions from earlier: we see why quantum gates must be unitary, since they’re the only matrices which preserve normalization. Of course, it doesn’t completely answer the question, since it doesn’t tell us why quantum gates should be matrices (i.e., linear operations) in the first place. That fact we’re simply going to accept. In fact, it is possible to develop deeper levels of understanding of why that is true, but in this essay we’ll be satisfied with the partial explanation that unitary matrices are length-preserving.

Alright, let’s prove the missing part from the last section: let’s show that unitaries are the only matrices which preserve length.

The proof is a little messy. But it turns out to be a good way to get familiar with a few extra pieces of standard quantum mechanical terminology and notation. I’ll be frank: while these pieces of terminology are extremely useful in quantum computing, we don’t strictly need them elsewhere in this essay (though we will in later essays). If you want to skip the section, or skim it, that’s okay – this is the best section of the essay to skip. But at some point you should come back and work through the material. And there is, in any case, a certain beauty to the proof.

We’ve been dealing with 2-dimensional vectors up to now, but what I’m about to say applies no matter how many dimensions we’re working in. So suppose we have a vector∣ψ⟩|\psi\rangle∣ψ⟩which can be written in component form as:

∣ψ⟩=[ab⋮z].|\psi\rangle = \left[ \begin{array}{c} a \\ b \\ \vdots \\ z \end{array} \right].∣ψ⟩=⎣⎢⎢⎢⎡​ab⋮z​⎦⎥⎥⎥⎤​.

We’re going to define a new object, also labeled with aψ\psiψ,but now with a bracket in the other direction:

⟨ψ∣:=[a∗b∗…z∗].\langle \psi| := [a^* b^* \dots z^*].⟨ψ∣:=[a∗b∗…z∗].

That is,⟨ψ∣\langle\psi|⟨ψ∣is a row vector, whose entries are the same as∣ψ⟩|\psi\rangle∣ψ⟩,but complex conjugated. The vector∣ψ⟩|\psi\rangle∣ψ⟩was called a ket, and (you’re going to groan)⟨ψ∣\langle \psi|⟨ψ∣is called abra, making this thebra-ket, orbracketnotation. Yes, theoretical physicists make dad jokes, too. These names were given by the theoretical physicist Paul Dirac in 1939, and it’s often called the Dirac bra-ket notation, or sometimes just the Dirac notation.

A key fact about the bra⟨ψ∣\langle \psi|⟨ψ∣is that it’s related to the ket∣ψ⟩|\psi\rangle∣ψ⟩by the dagger operation:

∣ψ⟩†=⟨ψ∣.|\psi\rangle^\dagger = \langle \psi|.∣ψ⟩†=⟨ψ∣.

It’s easy to see why this identity is true. Take the vector

∣ψ⟩=[ab⋮z],|\psi\rangle = \left[ \begin{array}{c} a \\ b \\ \vdots \\ z \end{array} \right],∣ψ⟩=⎣⎢⎢⎢⎡​ab⋮z​⎦⎥⎥⎥⎤​,

and apply the dagger operation, which means taking the transpose, turning it into a row vector with entriesa,b,…,za, b, \ldots, za,b,…,z,and then take the complex conjugate, giving us[a∗b∗…z∗][a^* b^* \ldots z^*][a∗b∗…z∗],which is just the definition of⟨ψ∣\langle \psi|⟨ψ∣.

In a similar way we see that⟨ψ∣†=∣ψ⟩\langle \psi|^\dagger = |\psi\rangle⟨ψ∣†=∣ψ⟩.

Another useful identity expresses the length of∣ψ⟩|\psi\rangle∣ψ⟩in terms of the Dirac notation:

∥∣ψ⟩∥2=⟨ψ∣∣ψ⟩.\||\psi\rangle\|^2 = \langle \psi| |\psi\rangle.∥∣ψ⟩∥2=⟨ψ∣∣ψ⟩.

That is, the length squared is just equal to the product of the row vector⟨ψ∣\langle \psi|⟨ψ∣with the column vector∣ψ⟩|\psi\rangle∣ψ⟩.To prove it just notice that the right-hand side is

[a∗b∗…][ab⋮]=∣a∣2+∣b∣2+…[a^* b^* \ldots ] \left[ \begin{array}{c} a \\ b \\ \vdots \end{array} \right] = |a|^2 + |b|^2 + \ldots[a∗b∗…]⎣⎢⎡​ab⋮​⎦⎥⎤​=∣a∣2+∣b∣2+…

And that, of course, is∥∣ψ⟩∥2\||\psi\rangle\|^2∥∣ψ⟩∥2,just as we wanted.

Physicists using the Dirac notation don’t usually write⟨ψ∣∣ψ⟩\langle \psi| |\psi\rangle⟨ψ∣∣ψ⟩.They simplify it slightly, omitting one of the vertical bars∣|∣in the middle, and just write it as:

⟨ψ∣ψ⟩.\langle \psi| \psi \rangle.⟨ψ∣ψ⟩.

It’s only a slight simplification, but this omission of the extra bar turns out to make life considerably easier, and is well worth it. I’ve shown it above just for the special case of⟨ψ∣ψ⟩\langle \psi| \psi \rangle⟨ψ∣ψ⟩but the same omission of a vertical bar is done often in other contexts. In practice, it rarely causes confusion, although of course you do need to get used to it.

Another useful identity is that ifMMMis a matrix and∣ψ⟩|\psi\rangle∣ψ⟩is a ket, then

(M∣ψ⟩)†=⟨ψ∣M†.(M|\psi\rangle)^\dagger = \langle \psi|M^\dagger.(M∣ψ⟩)†=⟨ψ∣M†.

If you think of⟨ψ∣\langle \psi|⟨ψ∣as the dagger of∣ψ⟩|\psi\rangle∣ψ⟩,then what this equation means is that taking the dagger of the productM∣ψ⟩M|\psi\rangleM∣ψ⟩is the same as taking the product of the dagger ofMMMwith the dagger∣ψ⟩|\psi\rangle∣ψ⟩,but reversing the order. This is a useful little mnemonic for remembering the above identity.

The identity is easy to prove. As a challenge to yourself you might want to stop right now and take a shot at proving it. Here’s the details if you get stuck.

Proof:The way to prove the identity is to apply the definitions. We’re going to look at thejjjth component of the left-hand side,(M∣ψ⟩)j†(M|\psi\rangle)^\dagger_j(M∣ψ⟩)j†​,and we’ll show it’s equal to thejjjth component of the right-hand side. By definition, thejjjth row component(M∣ψ⟩)j†(M|\psi\rangle)^\dagger_j(M∣ψ⟩)j†​is equal to the complex conjugate of thejjjth column component ofM∣ψ⟩M|\psi\rangleM∣ψ⟩,i.e.,(M∣ψ⟩)j∗(M|\psi\rangle)^*_j(M∣ψ⟩)j∗​.That column component is∑kMjk∗ψk∗\sum_k M_{jk}^* \psi_k^*∑k​Mjk∗​ψk∗​.We can move theψ\psiψterms to the left, and swap the indices on theMMMterm to convert the∗*∗to a dagger, giving∑kψk∗Mkj†\sum_k \psi_k^* M_{kj}^\dagger∑k​ψk∗​Mkj†​.That’s just thejjjth component of the row vector⟨ψ∣M†\langle \psi|M^\dagger⟨ψ∣M†,as we set out to show.QED

With all these ideas in mind, here’s an exercise for you to work through, putting several of these ideas together:

Exercise:Show that for any matrixMMMand vector∣ψ⟩|\psi\rangle∣ψ⟩,the following identity holds, expressing the length ofM∣ψ⟩M|\psi\rangleM∣ψ⟩:

∥M∣ψ⟩∥2=⟨ψ∣M†M∣ψ⟩.\|M|\psi\rangle\|^2 = \langle\psi|M^\dagger M |\psi\rangle.∥M∣ψ⟩∥2=⟨ψ∣M†M∣ψ⟩.

You may be wondering why we care about all these identities? Of course, really I’m just frontloading them – they’re all identities we’re going to find useful in a moment in the proof. So in some sense they are a bitad hocin motivation. But an underlying theme is that they’re about relating lengths to matrix operations. And it’s not so surprising that’s of interest – we’re going to assume we have a length-preserving operation. It’s very convenient to be able to relate that property to familiar operations about matrix multiplication. That’s the essential source of the interest in the above identities.

Alright, we’ve been working through some heavy, detailed material. We’ve got just a little more background to get through, but it’s easier going. I’m going to introduce a unit vector, denoted∣ej⟩|e_j\rangle∣ej​⟩,meaning the vector with a111in thejjjth component, and000severywhere else. So, for instance, for a qubit:

∣e0⟩=[10]∣e1⟩=[01]\begin{aligned} |e_0\rangle & = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] \\ |e_1\rangle & = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \end{aligned}∣e0​⟩∣e1​⟩​=[10​]=[01​]​

From elementary linear algebra, ifMMMis a matrix, thenM∣ek⟩M|e_k\rangleM∣ek​⟩is just thekkkth column ofMMM.(If you don’t recall that from elementary linear algebra, I encourage you to stop and figure out why it’s true.) And from that you can deduce easily that⟨ej∣M∣ek⟩\langle e_j|M|e_k\rangle⟨ej​∣M∣ek​⟩is thejkjkjkth entry ofMMM.

Exercise:If you’re not familiar with the proof, show thatM∣ek⟩M|e_k\rangleM∣ek​⟩is thekkkth column of the matrixMMM,and that⟨ej∣M∣ek⟩\langle e_j|M|e_k\rangle⟨ej​∣M∣ek​⟩is thejkjkjkth entry ofMMM.

Alright, that’s more than enough notational background! Let’s get to the main event. In particular, let’s recall the statement of the theorem we want to complete the proof of. Also recall that we proved the reverse implication in the last section, so we just need to prove the forward implication:

Theorem:LetMMMbe a matrix. Then∥M∣ψ⟩∥=∥∣ψ⟩∥\|M|\psi\rangle \| = \| |\psi\rangle\|∥M∣ψ⟩∥=∥∣ψ⟩∥for all vectors∣ψ⟩|\psi\rangle∣ψ⟩if and only ifMMMis unitary.

Proof:We’ll assumeMMMis length-preserving, and analyze the matrixM†MM^\dagger MM†M.Our goal is to show that this is the identity matrix, and thusMMMis unitary. To do this, we’re going to start by analyzing the diagonal elements(M†M)jj(M^\dagger M)_{jj}(M†M)jj​,and show that they’re all equal to111.Then we’ll turn our attention to the off-diagonal elements and show that they’re all equal to000.

To understand the diagonal elements, we know from earlier that:(M†M)jj=⟨ej∣M†M∣ej⟩=∥M∣ej⟩∥2(M^\dagger M)_{jj} = \langle e_j|M^\dagger M|e_j\rangle = \|M|e_j\rangle\|^2(M†M)jj​=⟨ej​∣M†M∣ej​⟩=∥M∣ej​⟩∥2.But sinceMMMis length-preserving, the latter is just∥∣ej⟩∥2\||e_j\rangle\|^2∥∣ej​⟩∥2,which is111.And so we conclude that all the diagonal elements are, indeed,111.

What about the off-diagonal elements, i.e.,(M†M)jk(M^\dagger M)_{jk}(M†M)jk​wherej≠kj \neq kj​=k?Can we show that these are all equal to000?Well, what we’d like to do is somehow to relate(M†M)jk(M^\dagger M)_{jk}(M†M)jk​to the length of some vectorM∣ψ⟩M|\psi\rangleM∣ψ⟩,and then use the length-preserving property. One idea is to try using∣ψ⟩=∣ej⟩+∣ek⟩|\psi\rangle = |e_j\rangle + |e_k\rangle∣ψ⟩=∣ej​⟩+∣ek​⟩,since that involves both thejjjth andkkkth directions. From the length-preserving property we have:

∥M∣ψ⟩∥2=∥∣ψ⟩∥2=12+12=2.\|M|\psi\rangle\|^2 = \| |\psi\rangle\|^2 = 1^2+1^2 = 2.∥M∣ψ⟩∥2=∥∣ψ⟩∥2=12+12=2.

We also have:

∥M∣ψ⟩∥2=⟨ψ∣M†M∣ψ⟩=⟨ej∣M†M∣ej⟩+⟨ej∣M†M∣ek⟩==+⟨ek∣M†M∣ej⟩+⟨ek∣M†M∣ek⟩=1+⟨ej∣M†M∣ek⟩+⟨ek∣M†M∣ej⟩+1\begin{aligned} \|M|\psi\rangle\|^2 & = \langle \psi| M^\dagger M |\psi\rangle \\ & = \langle e_j|M^\dagger M|e_j\rangle + \langle e_j|M^\dagger M|e_k\rangle \\ & \hphantom{ == } + \langle e_k|M^\dagger M|e_j\rangle + \langle e_k|M^\dagger M |e_k\rangle \\ & = 1 + \langle e_j|M^\dagger M|e_k\rangle + \langle e_k|M^\dagger M|e_j\rangle + 1 \end{aligned}∥M∣ψ⟩∥2​=⟨ψ∣M†M∣ψ⟩=⟨ej​∣M†M∣ej​⟩+⟨ej​∣M†M∣ek​⟩==+⟨ek​∣M†M∣ej​⟩+⟨ek​∣M†M∣ek​⟩=1+⟨ej​∣M†M∣ek​⟩+⟨ek​∣M†M∣ej​⟩+1​

Comparing the last two sets of equations, we have:

⟨ej∣M†M∣ek⟩+⟨ek∣M†M∣ej⟩=0.\langle e_j|M^\dagger M|e_k\rangle + \langle e_k|M^\dagger M|e_j\rangle = 0.⟨ej​∣M†M∣ek​⟩+⟨ek​∣M†M∣ej​⟩=0.

This is close to what we want, but isn’t quite right. It tells us that(M†M)jk+(M†M)kj=0(M^\dagger M)_{jk} + (M^\dagger M)_{kj} = 0(M†M)jk​+(M†M)kj​=0.Can we do better? It’s tempting to go back and fiddle around and try to find some way of eliminating one or the other of those terms. But there’s no direct way to do it – at least, no direct way that I know of.

But what if we’d done something slightly different, and instead of using∣ψ⟩=∣ej⟩+∣ek⟩|\psi\rangle = |e_j\rangle+|e_k\rangle∣ψ⟩=∣ej​⟩+∣ek​⟩we’d used∣ψ⟩=∣ej⟩+i∣ek⟩|\psi\rangle = |e_j\rangle+i|e_k\rangle∣ψ⟩=∣ej​⟩+i∣ek​⟩?It seems pretty plausible that following the same line of reasoning we’d get an equation involving(M†M)jk(M^\dagger M)_{jk}(M†M)jk​and(M†M)kj(M^\dagger M)_{kj}(M†M)kj​again. I won’t explicitly go through the steps – you can do that yourself – but if you do go through them you end up with the equation:

(M†M)jk−(M†M)kj=0.(M^\dagger M)_{jk} - (M^\dagger M)_{kj} = 0.(M†M)jk​−(M†M)kj​=0.

This is great! We can add it to the earlier equation to deduce that(M†M)jk=0(M^\dagger M)_{jk} = 0(M†M)jk​=0wheneverj≠kj \neq kj​=k,and so we conclude thatM†M=IM^\dagger M = IM†M=I,i.e.,MMMis unitary.QED

We’ve developed most of the ideas needed to do universal quantum computing. We understand qubits, quantum states, and have a repertoire of quantum gates. However, all our gates involve just a single qubit. To compute, we need some way for qubits to interact with one another. That is, we need quantum gates which involve two (or more) qubits.

An example of such a gate is the controlled-NOT (or CNOT) gate. In the quantum circuit language we have two wires, representing two qubits, and the following notation to represent the CNOT gate:



The wire with the small, filled dot on it (the top wire, in this example) is called thecontrolqubit, for reasons which will become clear in a moment. And the wire with the larger, unfilled circle on it is called thetargetqubit.

Up to now I haven’t said what the possible states of a two-qubit system are, but you can probably guess. We now have four computational basis states, corresponding to the four possible states of a two-bit system:∣00⟩,∣01⟩,∣10⟩|00\rangle, |01\rangle, |10\rangle∣00⟩,∣01⟩,∣10⟩,and∣11⟩|11\rangle∣11⟩.And, for a two-qubit system, not only can we have those four states, we can also have superpositions (i.e., linear combinations) of them:

α∣00⟩+β∣01⟩+γ∣10⟩+δ∣11⟩\alpha|00\rangle+\beta|01\rangle+\gamma |10\rangle+\delta|11\rangleα∣00⟩+β∣01⟩+γ∣10⟩+δ∣11⟩

Here, the amplitudesα,β,γ,δ\alpha, \beta, \gamma, \deltaα,β,γ,δare just complex numbers, and the sum of the squares of the absolute values is111,i.e,∣α∣2+∣β∣2+∣γ∣2+∣δ∣2=1|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2 = 1∣α∣2+∣β∣2+∣γ∣2+∣δ∣2=1.This is the same kind of normalization condition as we had for a single qubit.

Now, the CNOT gate is, much like the quantum NOT gate, inspired directly by a classical gate. What it does is very simple. If the control qubit is set to111,as in the states∣10⟩|10\rangle∣10⟩and∣11⟩|11\rangle∣11⟩,then it flips (i.e., NOTs) the target qubit. And otherwise it does nothing. Writing out the action on all four computational basis states we have:

∣00⟩→∣00⟩∣01⟩→∣01⟩∣10⟩→∣11⟩∣11⟩→∣10⟩\begin{aligned} |00\rangle & \rightarrow & |00\rangle \\ |01\rangle & \rightarrow & |01\rangle \\ |10\rangle & \rightarrow & |11\rangle \\ |11\rangle & \rightarrow & |10\rangle \end{aligned}∣00⟩∣01⟩∣10⟩∣11⟩​→→→→​∣00⟩∣01⟩∣11⟩∣10⟩​

If you’re familiar with classical programming languages, then you can think of the CNOT as a very simple kind ofif-thenstatement:ifthe control qubit is set,thenNOT the target qubit. But while simple, it can be used as a building block to build up other, more complex kinds of conditional behavior.

There’s a way of summing up all four of the equations above in a single equation. Supposexxxandyyyare classical bits, i.e.,000or111.Then we can rewrite the equations above in a single equation as:

∣x,y⟩→∣x,y⊕x⟩.\begin{aligned} |x, y\rangle & \rightarrow & |x, y\oplus x\rangle. \end{aligned}∣x,y⟩​→​∣x,y⊕x⟩.​

Note the commas inserted to make this easier to read – this is pretty common in working with multi-qubit states.

The above equation makes clear that the CNOT leaves the control qubitxxxalone, but flips the target qubityyyifxxxis set to111.Note that⊕\oplus⊕is addition modulo222,where1⊕1=01 \oplus 1 = 01⊕1=0,as we would expect from the fact that the CNOT takes∣11⟩|11\rangle∣11⟩to∣10⟩|10\rangle∣10⟩.

That’s all there is to the CNOT. It’s really a very simple idea and quantum gate. Note that it of course acts linearly on superpositions of computational basis states, as we expect for a quantum gate. So:

→α∣00⟩+β∣01⟩+γ∣10⟩+δ∣11⟩→α∣00⟩+β∣01⟩+γ∣11⟩+δ∣10⟩\begin{aligned} & \hphantom{ \rightarrow } \alpha|00\rangle+\beta|01\rangle+\gamma |10\rangle+\delta|11\rangle \\ & \rightarrow \alpha|00\rangle+\beta|01\rangle+\gamma |11\rangle+\delta|10\rangle \end{aligned}​→α∣00⟩+β∣01⟩+γ∣10⟩+δ∣11⟩→α∣00⟩+β∣01⟩+γ∣11⟩+δ∣10⟩​

And, though I won’t explicitly carry out the verification, the CNOT is unitary, and thus preserves the length of quantum states, as we expect.

Of course, the CNOT doesn’t just appear in two-qubit computations. It also appears in computations involving more qubits. Let’s suppose we have three qubits, for instance, and computational basis states such as∣000⟩,∣001⟩|000\rangle, |001\rangle∣000⟩,∣001⟩,and so on. Here’s a CNOT with the second qubit as the control qubit and the third qubit as the target:



What goes on? Well, we can write out what happens on an arbitrary computational basis state,∣x,y,z⟩|x, y, z\rangle∣x,y,z⟩,wherex,yx, yx,yandzzzare all classical bits. Of course, the first bitxxxisn’t changed at all, since it’s not involved in the CNOT. The second bityyyis the control bit, and so isn’t changed. But the third bitzzzis flipped if the control bityyyis set to111.And so we can write the action of the CNOT as:

∣x,y,z⟩→∣x,y,z⊕y⟩|x,y,z\rangle \rightarrow |x,y, z\oplus y\rangle∣x,y,z⟩→∣x,y,z⊕y⟩

I’ve described the CNOT as a “classical” gate, but it can be combined with single-qubit gates to do non-classical things. Let me give you an explicit example. It’s another two-qubit computation. It starts with the∣00⟩|00\rangle∣00⟩computational basis state, we apply a Hadamard gate to the first qubit, and then do a CNOT:



Recall that for a single qubit the Hadamard gate takes∣0⟩|0\rangle∣0⟩to an equal superposition(∣0⟩+∣1⟩)/2(|0\rangle+|1\rangle)/\sqrt{2}(∣0⟩+∣1⟩)/2​.For these two qubits it doesn’t affect the second qubit at all, and so it takes∣00⟩|00\rangle∣00⟩to(∣00⟩+∣10⟩)/2(|00\rangle+|10\rangle)/\sqrt{2}(∣00⟩+∣10⟩)/2​.

Next we apply the CNOT gate. This leaves the∣00⟩|00\rangle∣00⟩state unchanged, since the control bit is000.And it takes∣10⟩|10\rangle∣10⟩to∣11⟩|11\rangle∣11⟩,since the control bit is111.And so the output from the circuit is:

∣00⟩+∣11⟩2.\frac{|00\rangle+|11\rangle}{\sqrt 2}.2​∣00⟩+∣11⟩​.

This output state is a highly non-classical state – it’s actually a type of state called anentangled state. There’s no obvious interpretation of this state as a classical state, unlike say a computational basis state such as∣00⟩|00\rangle∣00⟩.In fact, entangled states can be used to do all sorts of interesting information processing tasks, including quantum teleportation and fast quantum algorithms.

A point I glossed over above, but worth mentioning: in the circuit I drew∣0⟩|0\rangle∣0⟩and∣0⟩|0\rangle∣0⟩separately as input qubits. It’s conventional to do that kind of thing to denote a combined input of∣00⟩|00\rangle∣00⟩.More generally, people use∣0⟩∣0⟩|0\rangle|0\rangle∣0⟩∣0⟩interchangeably with∣00⟩|00\rangle∣00⟩,∣0⟩∣1⟩|0\rangle|1\rangle∣0⟩∣1⟩interchangeably with∣01⟩|01\rangle∣01⟩,and so on. Going back and forth takes a bit of getting used to, but everything works pretty much as you expect, and you just need a little practice before it seems quite natural.

More generally, if we have single-qubit statesα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩andγ∣0⟩+δ∣1⟩\gamma|0\rangle+\delta|1\rangleγ∣0⟩+δ∣1⟩,then the combined state when the two qubits are put together is just:

=(α∣0⟩+β∣1⟩)(γ∣0⟩+δ∣1⟩)=αγ∣00⟩+αδ∣01⟩+βγ∣10⟩+βδ∣11⟩.\begin{aligned} & \hphantom{ = } (\alpha|0\rangle+\beta|1\rangle)(\gamma|0\rangle+\delta|1\rangle) \\ & = \alpha\gamma|00\rangle+\alpha\delta |01\rangle+ \beta\gamma |10\rangle+ \beta\delta |11\rangle. \end{aligned}​=(α∣0⟩+β∣1⟩)(γ∣0⟩+δ∣1⟩)=αγ∣00⟩+αδ∣01⟩+βγ∣10⟩+βδ∣11⟩.​

I said that the CNOT leaves the control qubit alone, and modifies the target qubit. That’s true in the computational basis. In fact, it’s actually possible for the target qubit to affect the control qubit. It’s worth taking a minute or two to at least understand (and, if you’re feeling energetic, attempting to solve) the following exercise:

Exercise:Can you find single-qubit states∣a⟩|a\rangle∣a⟩and∣b⟩|b\rangle∣b⟩so that applying a CNOT to the combined state∣ab⟩|ab\rangle∣ab⟩changes the first qubit, i.e., the control qubit?

Let me give you an example which solves the above exercise. Suppose we introduce single-qubit states∣+⟩|+\rangle∣+⟩and∣−⟩|-\rangle∣−⟩,defined by:

∣+⟩:=∣0⟩+∣1⟩2∣−⟩:=∣0⟩−∣1⟩2\begin{aligned} |+\rangle & := \frac{|0\rangle+|1\rangle}{\sqrt 2} \\ |-\rangle & := \frac{|0\rangle-|1\rangle}{\sqrt 2} \end{aligned}∣+⟩∣−⟩​:=2​∣0⟩+∣1⟩​:=2​∣0⟩−∣1⟩​​

A mnemonic for this notation is that these are both equal superpositions of∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩,but the “+” or “-” corresponds to the sign of the amplitude for the∣1⟩|1\rangle∣1⟩state. The following circuit identity holds:



That is, if we put∣+−⟩|+-\rangle∣+−⟩in, then∣−−⟩|--\rangle∣−−⟩comes out, i.e., the target qubit isn’t changed, but the control qubit is! The proof is just to follow the definitions and the algebra through. It’s honestly not terribly enlightening to follow the algebra through at this point – it’s a lot easier once certain other facts are known to you. But, again, if you’re feeling enthusiastic it’s a good exercise to work through to become familiar with how things work.

It’s worth taking some caution from this example. It means that intuitions coming from the computational basis can sometimes be incomplete or misleading. The CNOT isn’t simply doing something to the target, conditional on the control. It’s also doing something to the control, conditional on the target.

Exercise:Show that the inverse of the CNOT gate is just the CNOT gate.

— Alan Kay

Let’s return to the question we began with: is there a single computing device that can efficiently simulateanyother physical system? At the moment, the best candidate humanity has for such a computing device is a quantum computer. As you’ve probably guessed, you make such a device by combining all the elements we’ve been discussing. In Part III of this essay we’ll discuss what a quantum computer is, why they’re useful, and whether they can be used to efficiently simulate any other physical system.

— David Deutsch

In a general quantum computation, you start out with many qubits – I’ll draw four here, but in general it might be many more (or less). You apply quantum gates of various kinds, in particular, single-qubit gates and CNOT gates. And at the end of the circuit you read out the result by measuring in the computational basis. Here’s what it all looks like:



I haven’t labeled the single-qubit gates explicitly, but they might be various things – Hadamard gates, NOT gates, rotations, and perhaps others. Note also that while the computation starts in the computational basis state∣0000⟩|0000\rangle∣0000⟩,you can also start in some other computational basis state. I’ve just chosen∣0000⟩|0000\rangle∣0000⟩for definiteness.

We can summarize the three steps in a quantum computation as follows:





That’s all a general quantum computation is! If you understand this model, you know what a quantum computer is. It's pretty simple, really – enough so that I've sometimes heard people say “Is that all there is to it?” But while the model is simple, it contains remarkable depths, and exploring it could occupy many lifetimes.

In practice, people sometimes introduce other ideas into the way they describe quantum computations. If you’re a programmer, you can think of this as like the way programming language designers introduce higher-level abstractions to help people design different kinds of programs. In principle, those abstractions can always be reduced down to the level of AND and NOT gates. And if you understand that level – AND and NOT, or the type of quantum circuit shown above – then you have a foundation for building an understanding of the other ideas.

That may leave you wondering: does that mean youalsoneed to master all the higher-level abstractions? The answer is no!

There are several reasons for this. One reason is that, as we discussed earlier, humanity doesn’t yet know what the higher-level abstractions are. We’re still trying to figure them out. A second reason is that it seems likely that the list of higher-level abstractions is inexhaustible. My guess – and it’s just a guess – is that we will continue to discover beautiful new abstractionsforever, in both classical and quantum computing.

A related idea is that there are models of quantum computation different to the quantum circuit model. Some are merely small variations on the model I’ve described. For instance, instead of only using CNOT gates, we might allow any two-qubit unitary gate to be used in the circuit. Or perhaps instead of using qubits, we might use some other type of basic quantum system – say, thequtrit, which has three computational basis states,∣0⟩,∣1⟩|0\rangle, |1\rangle∣0⟩,∣1⟩,and∣2⟩|2\rangle∣2⟩.It probably won’t surprise you that the resulting models of computation are essentially equivalent to the quantum circuit model I’ve described. By this, I mean they can simulate the quantum circuit model (and vice versa) using roughly comparable numbers of gates and other physical resources.

There are also much more exotic variations, ideas such as measurement-based quantum computation, topological quantum computation, and others. I won’t describe these in any detail here, but suffice to say that they appear superficially very different to the circuit model. Nonetheless, they’re all mathematically equivalent to one another, including to the quantum circuit model. Thus a quantum computation in any of those models can be translated into an equivalent in the quantum circuit model, with only a small overhead in the cost of computation. And vice versa.

You may wonder why people bother thinking about other models, if they’re mathematically equivalent to the quantum circuit model. The reason is that just because two models are mathematically equivalent doesn’t mean they’re psychologically equivalent. Different models of computation stimulate different ways of thinking, and give rise to different ideas. And so it’s valuable to have other equivalent models.

Exercise:We saw earlier that composition of quantum gates corresponds to matrix multiplication (in reverse order). Show that the product of two unitary matricesUUUandVVVis also unitary. As a consequence, the net effect of any quantum circuit (before measurement) is to effect a unitary operation on the state space of the system.

Let me conclude this section with a brief comment about a particular class of quantum gates. These are gates which are multiples of the identity matrix,III:

[eiθ00eiθ]=eiθ[1001]=eiθI.\begin{aligned} \left[ \begin{array}{cc} e^{i\theta} & 0 \\ 0 & e^{i\theta} \end{array} \right] = e^{i\theta} \left[ \begin{array}{cc} 1 & 0 \\ 0 & 1 \end{array} \right] = e^{i \theta} I. \end{aligned}[eiθ0​0eiθ​]=eiθ[10​01​]=eiθI.​

Whenθ\thetaθis a real number this is a unitary matrix, and so a valid quantum gate. The effect of the gate is simply to multiply the state of the quantum computer byeiθe^{i\theta}eiθ.The numbereiθe^{i\theta}eiθis called aglobal phase factor. But even though the gate is valid, we rarely explicitly put such gates into quantum circuits. The reason is that such global phase factors have no impact on the results of the computation. To see why, imagine a quantum circuit which includes many such quantum gates, possibly for different values,θ1,θ2,…\theta_1, \theta_2, \ldotsθ1​,θ2​,….No matter where in the circuit the gates occur, the net effect is to multiply the state output from the circuit by an overall factor ofeiθ1+iθ2+…e^{i \theta_1 + i\theta_2 + \ldots}eiθ1​+iθ2​+….This doesn’t change the squared amplitudes of the computational basis states, and so has no impact on the measurement probabilities at the end of the computation. We could have left the gates out and it would make no difference.

Quantum computing people tend to be rather blase about such global phase factors. They’ll do things like not bother to distinguish between unitary gates such asXXXand−X-X−X,saying these gates are “the same up to a global phase factor”. They simply mean the−X-X−Xgate is the same as doing theXXXgate, followed by the−I-I−Igate. Since the latter gate makes no difference to the output from the computation, it can safely be omitted. We’ll see examples in the next essay, about the quantum search algorithm, where at a couple of places it makes sense to multiply the quantum state by a global phase factor of−1-1−1.

Now we know what a quantum computer is, what are they good for? Earlier, I suggested quantum computers expand the range of operations available when computing. This is similar to the way boats expand the range of ways we can traverse space, so instead of having to get from point A to point B by land,

we can take a shortcut greatly cutting down the time required:

In order for the analogous story to hold for quantum computers, they need to be at least as capable as classical computers. Fortunately, it’s possible to convert any classical circuit into a quantum circuit. This requires some care. The obvious thing to do is to imagine that your classical circuit is expressed in terms of some standard universal set – say, the AND and NOT gates – and then to convert those gates into equivalent quantum gates.

This is easy to do with the NOT gate – we just turn it into anXXXgate. But what’s not so easy is the AND gate. You might wonder if there’s some quantum gate which takes two bitsxxxandyyyas input, in the computational basis,∣x,y⟩|x,y\rangle∣x,y⟩,and then outputs a single qubit∣x∧y⟩|x \wedge y\rangle∣x∧y⟩,wherex∧yx \wedge yx∧yis just the logical AND of the bitsxxxandyyy.

Unfortunately, that “quantum gate” makes no sense at all! Not only is it not unitary, it’s not even close: a unitary gate with two qubits as input necessarily has two qubits as output. The “gate” I described has just a single qubit as output, so there’s no way it can be unitary.

You might wonder if instead there’s some way we can find a two-qubit quantum gate which hasx∧yx \wedge yx∧yas one output, and something else as the other output. I won’t prove it, but it turns out that this is impossible. The proof actually isn’t all that hard – it’s a fun exercise to think through, if you want a challenge – but is more of a digression than I want to get into here.

That’s all rather disappointing. But there is a solution. It’s to use a three-qubit quantum gate called theToffoli gate. The Toffoli gate is much like the CNOT gate, but instead of having a single control qubit, it has two control qubits,xxxandyyy,and a single target qubit,zzz.If both controls qubits are set, then the target is flipped. Otherwise, the target is left alone:



If the target starts out asz=0z = 0z=0,then you can see that the target output is justx∧yx \wedge yx∧y,and so the Toffoli gate can be used to simulate a classical AND gate. So if we have any classical circuit of AND and NOT gates then there’s a corresponding quantum circuit involving the same number ofXXXand Toffoli gates which computes the same function.

Exercise:What’s a quantum circuit that can compute the NAND gate? Recall that the NAND of two bitsxxxandyyyis just the NOT ofx∧yx \wedge yx∧y.

Exercise:Can you find a way of implementing a NAND gate using just a single Toffoli gate and no other quantum gates? Note that your answer here may be the same as your answer to the previous exercise, if you answered that exercise using just a single Toffoli gate and no other quantum gates.

A wrinkle in all this is that the Toffoli gate isn’t in our standard set of basic quantum gates. However, it’s possible to build the Toffoli gate up out of CNOT and single-qubit unitary gates. One way of doing the breakdown is shown below:



There are various slick ways of “explaining” why this circuit works, but I’ll let you in on a secret: much of the earliest work on this was done by pure brute force, people simply trying lots and lots of different ways of implementing the Toffoli gate (sometimes, using a computer to assist in doing the search). Frankly, I wouldn’t worry too much about why this circuit works, just take it for granted that it does. You can look it up if you ever need to, or dig down into why. Needing to know the circuit details actually isn’t all that common, so I wouldn’t suggest memorizing it – not until you have a good reason.

Exercise:Show that the inverse of the Toffoli gate is just the Toffoli gate.

It’s comforting that we can always simulate a classical circuit – it means quantum computers aren’t slower than classical computers – but doesn’t answer the question of the last section: what problems are quantum computers good for? Can we find shortcuts that make them systematically faster than classical computers? It turns out there’s no general way known to do that. But there are some interesting classes of computation where quantum computers outperform classical.

Over the long term, I believe the most important use of quantum computers will be simulating other quantum systems. That may sound esoteric – why would anyone apart from a quantum physicist care about simulating quantum systems? Buteverybodyin the future will (or, at least, will care about the consequences). The world is made up of quantum systems. Pharmaceutical companies employ thousands of chemists who synthesize molecules and characterize their properties. This is currently a very slow and painstaking process. In an ideal world they’d get the same information thousands or millions of times faster, by doing highly accurate computer simulations. And they’d get much more useful information, answering questions chemists can’t possibly hope to answer today. Unfortunately, classical computers are terrible at simulating quantum systems.

The reason classical computers are bad at simulating quantum systems isn’t difficult to understand. Suppose we have a molecule containingnnnatoms – for a small molecule,nnnmay be111-101010,for a complex molecule it may be hundreds or thousands or even more. And suppose we think of each atom as a qubit (not true, but go with it): to describe the system we’d need2n2^n2ndifferent amplitudes, one amplitude for eachnnn-bit computational basis state, e.g.,∣010011…⟩|010011\ldots\rangle∣010011…⟩.

Of course, atoms aren’t qubits. They’re more complicated, and we need more amplitudes to describe them. Without getting into details, the rough scaling for annnn-atom molecule is that we needknk^nknamplitudes, wherek≥2k \geq 2k≥2.The value ofkkkdepends upon context – which aspects of the atom’s behavior are important. For generic quantum simulationskkkmay be in the hundreds or more.

That’s alotof amplitudes! Even for comparatively simple atoms and small values ofnnn,it means the number of amplitudes will be in the trillions. And it rises very rapidly, doubling or more for each extra atom. Ifk=100k=100k=100,then evenn=10n = 10n=10atoms will require 100 million trillion amplitudes. That’s a lot of amplitudes for a pretty simple molecule.

The result is that simulating such systems is incredibly hard. Just storing the amplitudes requires mindboggling amounts of computer memory. Simulating how they change in time is even more challenging, involving immensely complicated updates to all the amplitudes.

Physicists and chemists have found some clever tricks for simplifying the situation. But even with those tricks simulating quantum systems on classical computers seems to be impractical, except for tiny molecules, or in special situations. The reason most educated people today don’t know simulating quantum systems is important is because classical computers are so bad at it that it’s never been practical to do. We’ve been living too early in history to understand how incredibly important quantum simulation really is.

That’s going to change over the coming century. Many of these problems will become vastly easier when we have scalable quantum computers, since quantum computers turn out to be fantastically well suited to simulating quantum systems. Instead of each extra simulated atom requiring a doubling (or more) in classical computer memory, a quantum computer will need just a small (and constant) number of extra qubits. One way of thinking of this is as a loose quantum corollary to Moore’s law:

In the long run, quantum computers will win, and win easily.

The punchline is that it’s reasonable to suspect that if we could simulate quantum systems easily, we could greatly speed up drug discovery, and the discovery of other new types of materials.

I will risk the ire of my (understandably) hype-averse colleagues and say bluntly what I believe the likely impact of quantum simulation will be: there’s at least a 50 percent chance quantum simulation will result in one or more multi-trillion dollar industries. And there’s at least a 30 percent chance it will completely change human civilization. The catch: I don’t mean in 5 years, or 10 years, or even 20 years. I’m talking more over 100 years. And I could be wrong.

What makes me suspect this may be so important?

For most of history we humans understood almost nothing about what matter is. That’s changed over the past century or so, as we’ve built an amazingly detailed understanding of matter. But while that understanding has grown, our ability to control matter has lagged. Essentially, we’ve relied on what nature accidentally provided for us. We’ve gotten somewhat better at doing things like synthesizing new chemical elements and new molecules, but our control is still very primitive.

We’re now in the early days of a transition where we go from having almost no control of matter to having almost complete control of matter. Matter will become programmable; it will be designable. This will be as big a transition in our understanding of matter as the move from mechanical computing devices to modern computers was for computing. What qualitatively new forms of matter will we create? I don’t know, but the ability to use quantum computers to simulate quantum systems will be an essential part of this burgeoning design science.

Alright, enough speculation.

Let me also briefly mention the sober-minded conventional answer given to the question “what are quantum computers good for?” That answer is to list various algorithmic problems that we have some evidence can be solved faster on a quantum computer than on a classical computer.

The most famous example is Peter Shor’s beautiful quantum factoring algorithm. To find the prime factors of annnn-bit integer seems to be a very difficult problem on a classical computer. The best existing algorithms are incredibly computationally expensive, with a cost that rises exponentially withnnn.Even numbers with just a few hundred digits aren’t currently feasible to factor on classical computers. By contrast, Shor’s quantum factoring algorithm would make factoring into a comparatively easy task, if large-scale quantum computers can be built.

Factoring perhaps doesn’t seem like a very interesting application. But it turns out that the ability to factor lets you break some of the most widely-used encryption schemes, used by services such as Gmail and Amazon to keep your communications private. This ability to break encryption has made the world’s intelligence agencies very interested in factoring, and they’ve poured enormous sums of money into quantum computing research since the mid-1990s. Indeed, there’s a good (as yet unwritten) history book to be written about how the rise of quantum computing was caused by the interest of the world’s intelligence agencies in accessing humanity’s private thoughts.

There’s been surprisingly little public reflection about this on the part of the quantum computing community. I occasionally meet quantum computing researchers who complain in private about what they perceive as privacy violations by governments, and the dangers of surveillance states. But then some of those same people will take money to help those governments in their plans for surveillance, usually with some transparently self-serving justification about how they’re notreallyhelping. One exception to this lack of public reflection is a brief discussion in Ronald de Wolf’s thoughtful essayThe Potential Impact of Quantum Computers on Society(2017).

— Albert Einstein

At the beginning of this essay I asked whether there is any single universal computing device that can efficiently simulate any other physical system? We’ve learned that classical computers seem to have a lot of trouble efficiently simulating quantum systems.

What about quantum computers? While they can certainly simulate many quantum systems, does that mean they can be used to efficiently simulateanyphysical system?

This question is an open problem! We don’t yet know the answer.

Part of the trouble in answering the question is that humanity hasn’t yet discovered the final fundamental laws of physics. Modern physics is based on two astonishingly effective theories: Einstein’s general theory of relativity, which describes how gravitation works; and the standard model of particle physics, which explains how pretty much everything else (electromagnetism, the strong and weak nuclear forces) work.

Trouble is, we don’t yet have a good theory of quantum gravity which combines general relativity and the standard model. Without such a theory of quantum gravity we’re not able to answer the question of whether quantum computers can efficiently simulate any other physical system. Perhaps some future class of quantum gravitating computers, more powerful even than quantum computers, will be needed to simulate quantum gravity.

Let’s ask a slightly less ambitious question, which is whether we can use quantum computers to efficiently simulate general relativity and the standard model?

The standard model is an example of a particular type of quantum mechanical theory called a quantum field theory. John Preskill and his collaborators have written a series of papersFor a review of progress see: John Preskill,Simulating quantum field theory with a quantum computer(2018).explaining how to use quantum computers to efficiently simulate quantum field theories. Those papers don’t yet simulate the full standard model, but they do make considerable progress. It remains an exciting open problem, albeit a problem where much encouraging progress has been made.

In the case of general relativity, as far as I know the problem remains open. Indeed, even stating what the problem means is not trivial. General relativity supports the existence of closed timelike curves, which can be used in some sense to send information back in time. This has interesting consequences for computation: there’s a way in which the computer can know the results of future computations. Unsurprisingly, this changes what is possible! Another complication is that when you talk about an “efficient simulation” in computation you mean the time and space overhead isn’t too large. But in general relativity even the basic units of space and time aren’t so clear. It’s hard to say what efficiency means. Finally, near singularities time and space get distorted in strange ways, again making it challenging to say exactly what it means to do an efficient computation.

There is, by the way, significant issue that I've been sweeping under the rug, and which may be bugging you: as I've explained it, a quantum computer isn't asinglecomputing device at all, since there are many possible quantum circuits. This is okay, though, since there's a model known as the universal quantum Turing machine, which is a single computing device, and which can simulate any quantum circuit. So you should understand the discussion above as being implicitly about the universal quantum Turing machine. I won't explain the details of the universal quantum Turing machine in this essay, since in practice the quantum circuit model is far more commonly used. But if you're interested in the details, I recommend thispaper by Bernstein and Vazirani.

The existence of universal computers is easy to take for granted. But there’s noa priorilogical reason there should be a single machine that can efficiently simulate every other physical system. It’s like being able to use your car also as a surfboard, a supermarket trolley, and a rainforestIn fact, there’s a sense in which this is possible, within limits: if you could rearrange protons, neutrons, and electrons arbitrarily well, you could turn a car into a surfboard, a supermarket trolley, or a (small) part of a rainforest. So matter does have intriguing universality properties. This is also remarkable, of course.. Yet the evidence so far suggests our universe does allow such universal machines. It’s a good problem – and, so far as I know, largely unexplored – to think about sets of laws of physics in which such a universal machine is not possible. That might sound pointless – why imagine other possible universes? Yet exploring such radical counterfactuals is often an excellent strategy for better understanding our own universe.

So there’s a very strange loop here. It’s that the laws of physics determine what kind of computations can be done. And yet the kind of computations which can be done seem to be powerful enough to describe the laws of physics. And that description can then be used to (efficiently!) simulate any physical system:

The top part of the loop is almost tautological. The bottom half of the loop is extraordinary. There’s noa priorireason the laws of physics should enable the existence of machines which can simulate physical systems. You might argue on anthropic grounds – we humans are here in the universe, and doing physics pretty successfully, so conditioned on that, it must be true. But that’s not a very satisfactory explanation of why. It remains a mystery. Einstein was right: the fact that the world is comprehensible at all is a miracle.

We’ve worked through all the basics of the quantum computing model, but we haven’t yet used it in a full-on application – the sort of application which make people excited about quantum computing. But there will soon be available two considerably shorter(!) followup essays, explaining the quantum search algorithm and quantum teleportation. Someone who understands all three essays will have a good understanding of elementary quantum computing.

And what of the experimental mnemonic medium we’ve developed in this essay? Mastering new subjects requires internalizing the basic terminology and ideas of the subject. The mnemonic medium should radically speed up this memory step, converting it from a challenging obstruction into a routine step. Frankly, I believe it would accelerate human progress if all the deepest ideas of our civilization were available in a form like this. Perhaps some day.

With that said, memory is only part of what it means to understand. Is it possible to build powerful environments which enable deeper forms of understanding? That enable people to take action in new ways, to grow their sense of agency and of ability to contribute? This requires many things beyond memory: the ability to problem solve and to problem find; to connect with opportunities that genuinely matter, and to find pathways for meaningful contribution. We, the team at “Quantum Computing for the Very Curious”, believe there are many powerful and under-exploited patterns available to achieve these goals. In future projects we will explore and develop these patterns. Some of this exploration will continue to be done in the context of quantum computing. But we also hope to launch projects discussing some of humanity’s other great challenges, including optimistic, detailed visions of problems such as space travel, climate change, longevity, and the development of new forms of matter.

Thanks for reading this far. In a few days, you’ll receive a notification containing a link to your first review session. In that review session you’ll be retested on the material you’ve learned, helping you further commit it to memory. It should only take a few minutes. In subsequent days you’ll receive more notifications linking you to re-review, gradually working toward genuine long-term memory of all the core material in the essay.

Thanks for reading this far. If you’d like to remember the core ideas of this essay durably, please sign in below to set up an account. We’ll track your review schedule and send you occasional reminders containing links that will take you to the review experience.



Michael Nielsen is supported byY Combinator Research. This essay is based in part on Michael’s earlier lecture series onQuantum Computing for the Determined.

In academic work, please cite this as:

Authors are listed in alphabetical order.

This work is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported License. This means you’re free to copy, share, and build on this essay, but not to sell it. If you’re interested in commercial use, pleasecontact us.

March 18, 2019

See ourUser Agreement and Privacy Policy.


---

# How the quantum search algorithm works

Andy MatuschakandMichael Nielsen

Part of aseries of essaysin a mnemonic medium which makes it almost effortless to remember what you read.

byAndy MatuschakandMichael Nielsen

Presented in a new mnemonic medium which makes it almost effortless to remember what you read.

Our future projects are funded in part by readers like you.

Special thanks to our sponsor-level patrons,Adam Wiggins,Andrew Sutherland,Bert Muthalaly,Calvin French-Owen,Dwight Crow,fnnch,James Hill-Khurana,Lambda AI Hardware,Ludwig Petersson,Mickey McManus,Mintter,Patrick Collison, Paul Sutter,Peter Hartree,Sana Labs,Shripriya Mahesh,Tim O'Reilly.

Imagine you’re the star of an action movie about a kidnapping. As part of the story, you come into possession of a secret message, which says where the victim is hidden. Unfortunately, the message is encrypted using a 12-digit secret key, i.e., a string of digits such as8409…8409\ldots\8409….But you don’t know the secret key. The only way to unlock the message and find the victim is by searching through theN=1012N = 10^{12}N=1012(one trillion) possible keys. While you may get lucky and find the right key early on, on average you’ll need to tryN/2N/2N/2different keys, and in the worst case you’ll need to try allNNN.

I’ve painted a fanciful picture, but similar search-based algorithms are used frequently in computing. They’re often the first approach we try when solving a problem. For example, suppose you’re trying to attack the famoustraveling salesperson problem(TSP), that is, trying to find the shortest route that visits every city in a list of cities, while returning to the origin city. A simple approach is to search through all the possible routes, while keeping track of the minimal route found. Of course, it’s possible to develop more sophisticated algorithms for TSP, algorithms that make it unnecessary to search through every route. But that doesn’t take away from the core point: for many problems in computing a search-based approach is a good first-cut way to attack the problem. Indeed, search is sometimes a good final-cut approach, or even provably optimal. Overall, search is an exceptionally useful general-purpose algorithm.

As mentioned above, on a conventional classical computer, if we have a search space ofNNNitems, we need to examine the search space on the order ofNNNtimes to find the item we’re looking for. Remarkably, quantum computers can do far better. It turns out that you can use a quantum computer to solve the search problem after examining the search space roughlyN\sqrt{N}N​times! A little more precisely, it needs to examine the search space aboutπN/4\pi\sqrt{N}/4πN​/4times. That square root factor makes a big difference. IfNNNwas a trillion, as in our opening scenario, then a classical computer will need to examine the search space a trillion times, while the quantum computer will need to examine it fewer than 800 thousand times. That’s an improvement of more than a factor of a million.

When I first heard about the quantum search algorithm I thought it sounded impossible. I just couldn’t imagine any way it could be true. But it is true. In this essay I explain in detail how the quantum search algorithm works. I’ll also explain some limitations of the quantum search algorithm, and discuss what we can learn about quantum computing in general from the quantum search algorithm.

To read this essay you need to be familiar with the quantum circuit model of computation. If you’re not, you can learn the elements from the earlier essayQuantum Computing for the Very Curious.

It may be tempting to think “Oh, I'm not that interested in the problem of search, why should I bother learning about it?” But the point of this essay is deeper than search. It's to begin answering the question: how can we use quantum computers to do things which are genuinely different and better than a conventional classical computer? The particular problem (search) is almost incidental. And so the essay is about learning to think in the quantum realm, finding non-classical heuristics that let us beat classical computers. This turns out to be immensely challenging, but also immensely fun.

Because of these aspirations, I won’t just explain how the search algorithm works. We'll dig down and try to understand why it works, and how you might have discovered the algorithm in the first place. That takes more time than just laying out the quantum circuit, but is also more rewarding. Along the way we’ll learn many other techniques widely used in quantum algorithm design, ideas such as clean computation, the phase trick, quantum parallelism, and others. All this is great experience in learning how to think about quantum algorithm design in general.

This essay is an example of what Andy Matuschak and I have dubbed amnemonic medium– it’s like a regular essay, but incorporates new user interface elements intended to make it almost effortless for you to remember the content of the essay. The motivator is that most people (myself included) quickly forget much of what we read in books and articles. But cognitive scientists studying human memory have understood how to guarantee you will remember something permanently. This mnemonic medium builds those ideas into the essay, making it easy to remember the material for the long term.

The core idea of the mnemonic medium is this: throughout the essay we occasionally pause to ask you a few simple questions, testing you on the material just explained. In the weeks ahead we’ll re-test you in followup review sessions. By carefully expanding the testing schedule, we can ensure you consolidate the answers into your long-term memory, while minimizing the study time required. The review sessions take no more than a few minutes per session, and we’ll notify you when you need to review. The benefit is that instead of remembering how the quantum search algorithm works for a few hours or days, you’ll remember for years; it’ll become a much more deeply internalized part of your thinking.

Of course, you can just read this as a conventional essay. But I hope you’ll at least try out the mnemonic medium. To do so please sign up below. This will enable us to track the best review schedule for each question, and to remind you to sign in for occasional short review sessions. And if you’d like to learn more about how the mnemonic medium works, please seeA medium which makes memory a choice,How to approach this essay?, andHow to use (or not use!) the questions.

As an example, let’s take a look at a couple of simple questions reviewing what you’ve just learned. Please indulge me by answering the questions just below. It’ll only take a few seconds – for both questions, think about what you believe the answer to be, click to reveal the actual answer, and then mark whether you remembered or not. If you can recall, that’s great. If not, that’s also fine, just mentally note the correct answer, and continue. Since you probably weren't expecting to be tested like this, it seems only fair to give you a hint for the second question: the somewhat hard-to-remember prefactor in the answer isπ/4\pi/4π/4.Later in the essay I won't always provide such reminders, so you'll need to be paying attention!

In the introduction I gave an informal description of what the quantum search algorithm achieves. To make the search algorithm more concrete, let’s think about the special case of using search to attack the traveling salesperson problem (TSP). Of course, there are better approaches to TSP than search, but the purpose of this section is to show the overall building blocks that go into the search algorithm. For that purpose, TSP is a useful concrete example. In the next section we’ll understand the details of how the buildings blocks work.

It’ll help to consider a variation on TSP, namely, searching for a route shorter than some specified threshold distance,TTT.In other words, we’ll be using search to solve problems like:

This isn’t quite the same as find-the-minimal-route, but this variation turns out to be a little easier to connect to the quantum search algorithm. Variation noted, here’s what a quantum search algorithm might look like:





The search register contains candidate solutions∣x⟩=∣x1,x2,…,xn⟩|x\rangle = |x_1, x_2, \ldots, x_n\rangle∣x⟩=∣x1​,x2​,…,xn​⟩to the search problem. In this case, our search register will contain potential routes through the cities, written out as bit stringsx=x1,x2,…x = x_1, x_2, \ldotsx=x1​,x2​,….I won’t get into the bit string representation explicitly – there are many ways to make such a representation, and the details don’t much matter. The key point is that you should think of the search register as being in some superposition∑xαx∣x⟩\sum_x \alpha_x |x\rangle∑x​αx​∣x⟩of different possible routes through the cities, andxxxas being some bit string representation of a route.

For definiteness, I’ll also assume the search register starts in the all∣0⟩|0\rangle∣0⟩state. That’s just a convention: we need to start somewhere.

Step 1 of the quantum search algorithm will just be some fixed quantum circuit, made up of standard quantum gates – things like the Hadamard and CNOT gates, as discussed in theprevious essay. Of course, eventually we need to figure out what those gates should be. We’ll do that in later sections. But for now we’re just sticking at a broad conceptual level, trying to figure out what a quantum search algorithm might look like.

The next step is to check if the search register state∣x⟩|x\rangle∣x⟩corresponds to what we’ll call ashort routethrough the cities, i.e., a route of less distance than the thresholdTTT.To do this, we introduce a check qubit to store the results of this step, initialized in the state∣0⟩|0\rangle∣0⟩.So we start in the state∣x⟩∣0⟩|x\rangle|0\rangle∣x⟩∣0⟩,and change to∣x⟩∣1⟩|x\rangle|1\rangle∣x⟩∣1⟩ifxxxrepresents a short route through the cities, and otherwise are left as∣x⟩∣0⟩|x\rangle|0\rangle∣x⟩∣0⟩,whenxxxdoesn’t represent a short route. We can write this compactly as∣x⟩∣0⟩→∣x⟩∣s(x)⟩|x\rangle|0\rangle \rightarrow |x\rangle|s(x)\rangle∣x⟩∣0⟩→∣x⟩∣s(x)⟩,where thesearch functions(x)s(x)s(x)is equal to111ifxxxis a solution to the problem (i.e., a route of length less thanTTT), and000ifxxxis not a solution.

Of course, in general the search register is in a superposition∑xαx∣x⟩\sum_x \alpha_x |x\rangle∑x​αx​∣x⟩.We’ll assume (and justify later) that this checking-if-short-route step acts linearly, taking∑xαx∣x⟩∣0⟩\sum_x \alpha_x |x\rangle |0\rangle∑x​αx​∣x⟩∣0⟩to∑xαx∣x⟩∣s(x)⟩\sum_x \alpha_x |x\rangle |s(x)\rangle∑x​αx​∣x⟩∣s(x)⟩.

How is this checking-if-short-route step implemented? Of course, in principle it’s easy to construct a conventional classical circuit which does the trick – the circuit would just check that the bit stringx=x1x2…x = x_1 x_2 \ldotsx=x1​x2​…is a valid route through all the cities, and if so would add up the corresponding distances, and compare it to the thresholdTTT.We can just take that classical circuit – whatever it is – and translate it into the equivalent quantum circuit. I explained how to do such translations using Toffoli and NOT gates in theearlier essay, and I won’t re-explain it here. Of course, we still need to figure out the exact details of the classical circuit, but: (a) that’s part of classical computing, not quantum computing; and (b) in any case is a detail unrelated to making search work. With one slight caveat (to be discussed shortly), we’ll take for granted we have a quantum circuit which can do the job.

After that is Step 2 in the quantum search algorithm. Again, we need to figure out exactly what quantum gates to use here, and we’ll do that in the next section.

Next, we check again if the search register state∣x⟩|x\rangle∣x⟩is a short route. It works just as before, with a check qubit and so on.

We continue in this way, alternating steps in our search algorithm with checking whether or not the search register state is a solution to our search problem, i.e., a short route through the cities. At the end of the algorithm we measure the search register. If we’ve designed the search algorithm well, then the result of the measurement will be a solutionsssto the search problem, in this case a route through the cities of distance less thanTTT.

A challenge is that sometimes such a solution may not exist. In our example, that’ll happen when there is no route through the cities of distance less thanTTT.In that case, whatever measurement result we get at the end of the search algorithm, it won’t be a solution to the search problem. That’s okay, though, since it’s easy to just check and make sure we’ve got a legitimate solution.

I’ve been talking about the problem of searching for short routes in TSP. But there’s little here that has to do with the details of TSP. We can imagine a general quantum search algorithm which works along the same lines:





Everything is the same, except that we’ve replaced the check-if-short-route step byCsC_sCs​.We can think of this as a subroutine or black box which checks whether or not the search register is a solutionsssto the search problem. In particular, we’ll assume thatCsC_sCs​takes∑xαx∣x⟩∣0⟩\sum_x \alpha_x |x\rangle|0\rangle∑x​αx​∣x⟩∣0⟩to∑xαx∣x⟩∣s(x)⟩\sum_x \alpha_x |x\rangle|s(x)\rangle∑x​αx​∣x⟩∣s(x)⟩,where (to recap) the search functions(x)=0s(x) = 0s(x)=0whenxxxis not a solution to the search problem, ands(x)=1s(x) = 1s(x)=1whenxxxis a solution to the search problem. More informally, we can think ofCsC_sCs​as examining the search space to see if the search register contains a solution to the search problem. The hope motivating the quantum search algorithm is that we can reduce the number of times we need to do such examinations. In particular, we’ll try to minimize the number of times the search black boxCsC_sCs​needs to be applied.

As another example, suppose the search problem is the one I opened the essay with – searching for a key to decode a kidnapper’s note. In that case, you’d designCsC_sCs​so it does two things: (1) decodes the kidnapper’s note, assuming the search register contains a possible key; and (2) examines the decoded text from step 1 to see whether or not it’s plausibly a message in English. If it is a plausibly an English message then almost certainly it’s the correct text, since for most ciphers decodings for anything other than the correct key will look like gibberish. All of this is easily done using classical circuits, and those classical circuits can then be converted into a suitable quantum circuit forCsC_sCs​.

As still another example, consider the protein folding problem – the problem of figuring out what shapes proteins take on in nature. A way of phrasing this in our framework is as a search for a way of spatially arranging the protein’s amino acids so the protein’s energy is below some threshold energy,EEE?If you can answer this question reliably, then by gradually lowering the thresholdEEEyou can find the lowest-energy states for the protein. These lowest-energy states correspond to the shapes we find in nature. Again, it’s easy to figure out a circuitCsC_sCs​which checks whether or not some potential spatial arrangement of the amino acids has energy less thanEEE.

For the purpose of designing the quantum search algorithm we’re not going to worry about how the search black boxCsC_sCs​works. We’ll just assume you’ve got access to a suitableCsC_sCs​.Indeed, much of the utility of the quantum search algorithm comes from the fact that it works with anyCsC_sCs​.Of course, to actually implement the quantum search algorithm in practice we’d need to have an actual implementation of a suitableCsC_sCs​.But to design a useful quantum search algorithm, we can treatCsC_sCs​as a black box.

So our main job through the remainder of this essay is to figure out how to design the quantum circuits for step 1, step 2, and so on, in order to minimize the total number of times we need to apply the search black box. We’ll design those quantum circuits in the next section.

Incidentally, people new to the quantum search algorithms sometimes get a little hung up because of the slightly mysterious-sounding term “black box”. They worry that it implies there’s some sort of sleight-of-hand or magic going on, that quantum search must require some sort of genie wandering around giving out black boxes. Of course, it’s not magical at all. To repeat what I said above: if you were actually running the search algorithm, you’d need an implementation of the black box for your particular problem. But the point is to design a search algorithm which works no matter the internal details of the search black box – it abstracts those away.

Another common misconception is that to implement the search black boxCsC_sCs​we would need to know the value ofsssin advance. That’s not necessary because there’s a big difference between a circuit which can recognize a solution and which knows the solution. All the search black box needs is to be able to recognize a solution. For instance, it’s obviously possible to design a circuit which can recognize a short tour through a list of cities, without explicitly knowing a short tour in advance. Similarly for recognizing low-energy protein shapes, recognizing a decoded kidnapper’s note, and so on.

Having spent so much time saying that we’re not going to worry about the details ofCsC_sCs​I’ll now turn around and say that it simplifies things a little if we make one extra assumption about the search black box: we’ll suppose there isexactly onesolutionsssto the search problem. This assumption is ultimately not essential – the search algorithm can be extended to the case of multiple (or zero) solutions. But for now it simplifies life to assume there’s exactly one single solution, which we’ll labelsss.That, by the way, is why I labeled the black boxCsC_sCs​.

(Incidentally, the search black boxCsC_sCs​is sometimes called a searchoracle, since it’s this oracular thing which tells us whether we have a solution to the search problem or not. I use the term black box in this essay, but many people use the term “oracle”, and it’s worth being aware of both terms.)

Getting a clean black box:Earlier, I blithely asserted you can take a classical circuit for computing the search functions(x)s(x)s(x),and turn it into a quantum circuit which has the effectCs∣x⟩∣0⟩=∣x⟩∣s(x)⟩C_s|x\rangle|0\rangle = |x\rangle|s(x)\rangleCs​∣x⟩∣0⟩=∣x⟩∣s(x)⟩.

Actually, there’s a slight complication. To illustrate the issue concretely, suppose you’re trying to computes(x)=x1∧x2∧x3s(x) = x_1 \wedge x_2 \wedge x_3s(x)=x1​∧x2​∧x3​,that is, the AND of three bits (corresponding to a search solutions=111s = 111s=111,in binary). To do this, we’d start by using a Toffoli gate to compute the AND of the first two bits,x1∧x2x_1 \wedge x_2x1​∧x2​:





Then we’d use another Toffoli gate to AND the result withx3x_3x3​:





So we’ve indeed computeds(x)=x1∧x2∧x3s(x) = x_1 \wedge x_2 \wedge x_3s(x)=x1​∧x2​∧x3​,but along the way we’ve also generated an intermediate working qubit in the state∣x1∧x2⟩|x_1 \wedge x_2\rangle∣x1​∧x2​⟩.That working state wasn’t part of our original specification. Put another way, we wanted to compute

∣x1,x2,x3⟩∣0⟩→∣x1,x2,x3⟩∣x1∧x2∧x3⟩,|x_1, x_2, x_3\rangle|0\rangle \rightarrow |x_1, x_2, x_3\rangle|x_1 \wedge x_2 \wedge x_3\rangle,∣x1​,x2​,x3​⟩∣0⟩→∣x1​,x2​,x3​⟩∣x1​∧x2​∧x3​⟩,

and instead we ended up computing

∣x1,x2,x3⟩∣0⟩∣0⟩→∣x1,x2,x3⟩∣x1∧x2⟩∣x1∧x2∧x3⟩.|x_1, x_2, x_3\rangle|0\rangle|0\rangle \rightarrow |x_1, x_2, x_3\rangle|x_1\wedge x_2\rangle |x_1 \wedge x_2 \wedge x_3\rangle.∣x1​,x2​,x3​⟩∣0⟩∣0⟩→∣x1​,x2​,x3​⟩∣x1​∧x2​⟩∣x1​∧x2​∧x3​⟩.

More generally, suppose we try to convert a classical circuit computing the search functions(x)s(x)s(x)into a quantum circuit. If we do it using the recipe described in the last essay – converting AND gates to Toffoli gates, and classical NOT gates to quantum NOT gates – it won’t take∣x⟩∣0⟩|x\rangle|0\rangle∣x⟩∣0⟩to∣x⟩∣s(x)⟩|x\rangle|s(x)\rangle∣x⟩∣s(x)⟩.There will be extra qubits involved, arising as intermediaries during the computation. The result will be something more like

∣x⟩∣0⟩∣0⟩→∣x⟩∣s(x)⟩∣w(x)⟩,|x\rangle|0\rangle|0\rangle \rightarrow |x\rangle|s(x)\rangle |w(x)\rangle,∣x⟩∣0⟩∣0⟩→∣x⟩∣s(x)⟩∣w(x)⟩,

where the extra register is a supply of one-or-more working qubits, and they end up in some state∣w(x)⟩|w(x)\rangle∣w(x)⟩produced along the way.

The difference might seem small. We’re certainly close to having our search black box. But it turns out to be crucial to the quantum search algorithm that we get that clean behavior,∣x⟩∣0⟩→∣x⟩∣s(x)⟩|x\rangle|0\rangle \rightarrow |x\rangle|s(x)\rangle∣x⟩∣0⟩→∣x⟩∣s(x)⟩.We’ll discuss later why this clean form for the computation is needed. For right now, though, let’s figure out how to do it.

Fortunately, there’s a simple trick calleduncomputationwhich works. It involves three steps. The first is more or less what you’d expect, but the second and third are quite clever:

At the end, we can ignore the∣0⟩∣0⟩|0\rangle|0\rangle∣0⟩∣0⟩state, which isn’t changed at all by the entire process. And so the net result of these steps is the desired transformation,∣x⟩∣0⟩→∣x⟩∣s(x)⟩|x\rangle|0\rangle \rightarrow |x\rangle|s(x)\rangle∣x⟩∣0⟩→∣x⟩∣s(x)⟩.

Summing up, if we have a classical circuit to compute a functions(⋅)s(\cdot)s(⋅),you can think of the three stages in the corresponding clean quantum circuit as: computes(⋅)s(\cdot)s(⋅),by converting classical gates to quantum; copy the answer using a CNOT; uncompute, by reversing the gates and inverting them.

So, for instance, it’s easy to convert a computation ofs(x)=x1∧x2∧x3s(x) = x_1 \wedge x_2 \wedge x_3s(x)=x1​∧x2​∧x3​into the clean form using uncomputation. We just literally follow the steps above, and remember that the inverse of a Toffoli gate is a Toffoli gate:





I’ve written the results of the clean computation as∣x⟩∣0⟩→∣x⟩∣s(x)⟩|x\rangle|0\rangle \rightarrow |x\rangle|s(x)\rangle∣x⟩∣0⟩→∣x⟩∣s(x)⟩.What would have happened if the second register had been in the state111(or, more generally, an unknown statez=0z = 0z=0or111), instead of000?You can easily trace through the above steps to see that the net result is

∣x⟩∣z⟩→∣x⟩∣z⊕s(x)⟩,|x\rangle|z\rangle \rightarrow |x\rangle|z \oplus s(x) \rangle,∣x⟩∣z⟩→∣x⟩∣z⊕s(x)⟩,

where the addition is done modulo222.This type of clean computation turns out to be useful in many quantum computations, not just quantum search, and the form just shown is the standard form in which it is presented. In particular, we can do a clean computation of any functionf(x)f(x)f(x)for which we have a classical circuit, not just search functions. In any case, we will assume that the form given in the equation just above is the effect of the search black boxCsC_sCs​.

It’s worth noting that there is a price to pay in converting a classical circuit to its equivalent clean form: the uncomputation step doubles the number of gates required, and the copying step adds an extra CNOT on top of that doubling. So there is a genuine overhead in getting to the clean form. Still, for the speedup we’ll get from the quantum search algorithm this is a tiny price to pay.

Exercise:Find a quantum circuit which computes∣x1,x2⟩∣0⟩→∣x1,x2⟩∣x1∨x2⟩|x_1, x_2\rangle|0\rangle \rightarrow |x_1, x_2\rangle |x_1 \vee x_2\rangle∣x1​,x2​⟩∣0⟩→∣x1​,x2​⟩∣x1​∨x2​⟩,where∨\vee∨denotes the logical OR.

Exercise:Find a quantum circuit which performs a clean computation of the classical functions(x1,x2,x3)=x1∨x2∨x3s(x_1, x_2, x_3) = x_1 \vee x_2 \vee x_3s(x1​,x2​,x3​)=x1​∨x2​∨x3​.

Let me finish the discussion of clean computation by introducing some extra pieces of quantum circuit notation that will come in handy later. The notation I’ll introduce generalizes the CNOT and Toffoli gates to involve more control qubits. For instance, here’s an example involving three control qubits:





It behaves as you’d expect, NOTting the target qubit when all three control qubits are set, and otherwise leaving it alone. We just saw how to implement this using Toffoli gates and uncomputation:





If we want to break this down even further, we can use techniques from thelast essayto break the Toffoli gates into one- and two-qubit quantum gates.

Very similar ideas can be used to synthesize even more complicated controlled gates, e.g. gates controlled by four qubits such as:





In this notation, an open circle on a control qubit means gates are applied conditional on those control qubits being set to000.In this case, it means the NOT on the target qubit is applied conditional on the first two qubits being set to000and the third and fourth being set to111.I’ll leave it to you to figure out the details of how to break this down into Toffoli and other standard quantum gates – it’s a good exercise in applying the ideas we’ve been learning.

Exercise:Find a way of breaking the controlled gate shown just above (with four control qubits) down into Toffoli and one- and two-qubit quantum gates.

Database search?The quantum search algorithm is sometimes described as adatabasesearch algorithm. This is often done in popular media accounts, and sometimes even in research papers. Unfortunately, it’s not a terribly helpful way of thinking about it. For one thing, databases are usually ordered, and that ordering makes them extremely fast to search. For instance, suppose you have an alphabetically ordered list of surnames:

To find out if a name is on the list you wouldn’t run through the entire list. Rather, you’d exploit the ordering to do some kind of binary search. The result is that instead of needing to examine the databaseNNNtimes, you only need to examine it on the order oflog⁡2(N)\log_2(N)log2​(N)times. That’s vastly faster than the orderN\sqrt{N}N​times required by the quantum search algorithm. If someone needs to examine a databaseNNNtimes in order to search it, it probably means they need to think harder about how they’re indexing their database.

Why is the notion of a quantum database search used so often in explanations? My guess is that it’s because searching a database is the most obvious really concrete way of thinking about search. But it’s that very concreteness which makes it easy to build database indices, which usually make database search a trivial problem in practice. Search is vastly more challenging when it’s hard to find or exploit any structure in the search space, in problems like decoding a code or the TSP or protein folding. It’s in such cases that the quantum search algorithm will shine. More precisely: the quantum search algorithm is useful when: (a) you’re doing a search where there’s little exploitable structure in the search space; but (b) you have an algorithm which lets you recognize solutions to the search problem, and so you can build the search black box.

Now that we have an overall picture, what quantum circuits actually make the quantum search algorithm work? Rather than simply present the final algorithm, I’m going to describe a line of thinking you might imagine using to discover the quantum search algorithm. That means we’ll be making guesses, and occasionally backtracking as we realize something doesn’t work. It has the disadvantage that the presentation is longer than if I just showed you the final algorithm. But it also makes it easier to understand where the quantum search algorithm comes from, and why it works. It’s often surprisingly instructive to see reasonable ideas tried (and fail), and how it’s possible to learn from those failures.

Now, we’re looking for a truly quantum algorithm, one that exploits quantum mechanics to operate faster than a classical computer. So even though we start in a computational basis state, we should quickly move out of that state. After all, if we stayed in the computational basis we could do everything on a classical computer, and there would be no possibility of an advantage for a quantum computer.

What state might we move into?

In our circuit model, one of the gates that produces non-classical states is the Hadamard gate. Remember that the Hadamard gate takes the state∣0⟩|0\rangle∣0⟩to∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​and∣1⟩|1\rangle∣1⟩to∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​.A nice thing about the state∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​is that it’s a truly quantum state which is as agnostic as it’s possible to be about the value of the bit. Suppose we applied a Hadamard gate to all the∣0⟩|0\rangle∣0⟩’s at the start:





Then we’d end up with the quantum state

∑x1,x2,…,xn=0,1∣x1,x2,…,xn⟩2n,\frac{\sum_{x_1, x_2, \ldots, x_n = 0, 1} |x_1, x_2, \ldots, x_n\rangle}{\sqrt 2^n},2​n∑x1​,x2​,…,xn​=0,1​∣x1​,x2​,…,xn​⟩​,

where we sum over both000and111for each qubit. Put another way, we end up with an equal superposition of all possible solutions to the search problem. It’s a starting state that’s completely agnostic about the solution. We can write this more compactly by settingN:=2nN := 2^nN:=2nto be the size of the search space, and writing the last state as an equal superposition over all possible search solutions,

∑x∣x⟩N.\frac{\sum_x |x\rangle}{\sqrt{N}}.N​∑x​∣x⟩​.

This state will appear often in what follows, and it’s helpful to have some notation for it: we’ll call it∣E⟩|E\rangle∣E⟩,forequal superposition of possible solutions,∣E⟩:=∑x∣x⟩/N|E\rangle := \sum_x |x\rangle/\sqrt{N}∣E⟩:=∑x​∣x⟩/N​.

Of course, this is just a guess as to how we might start out. In fact – spoiler alert! – we’ll eventually find that starting in pretty much any superposition state works. But the equal superposition∣E⟩|E\rangle∣E⟩is easy to prepare, and turns out to work well. It’s got the additional bonus that this state turns up in lots of quantum algorithms, so it’s good to get comfortable with it.

By the way, I said above thatN=2nN = 2^nN=2nis the size of the search space. This isn’t always literally true. For instance, if we’re usingx=x1x2…x = x_1 x_2 \ldotsx=x1​x2​…to describe routes in the traveling salesperson problem, it might be that some bit strings don’t represent valid routes, so the actual size of the search space may be smaller than2n2^n2n.I won’t consider that possibility in any detail, although the algorithm we’ll find is easily modified to cope with that possibility.

Now, suppose we introduce a check qubit and apply the search black box to our equal superposition state. We get the state:

∑x∣x⟩∣s(x)⟩N.\sum_x \frac{|x\rangle|s(x)\rangle}{\sqrt{N}}.x∑​N​∣x⟩∣s(x)⟩​.

That doesn’t immediately help much: if we were to do a measurement in the computational basis, we get a resultx,s(x)x, s(x)x,s(x)wheres(x)=1s(x) = 1s(x)=1(i.e., the solution to the search problem) with probability1/N1/N1/N.We’re essentially just guessing a solution.

What could we do instead if not a measurement? The most obvious thing is to apply the search black box again. Unfortunately, this addss(x)s(x)s(x)to itself, modulo222,and so we end up in the state:

∑x∣x⟩∣0⟩N.\sum_x \frac{|x\rangle|0\rangle}{\sqrt N}.x∑​N​∣x⟩∣0⟩​.

This isn’t progress – we’re back where we were earlier!

Another thing to try is using a new check qubit. The simplest thing would be to apply the search black box over and over, each time with a new check qubit, so you end up with the state:

∑x∣x⟩∣s(x)⟩∣s(x)⟩…N.\sum_x \frac{|x\rangle|s(x)\rangle|s(x)\rangle \ldots}{\sqrt N}.x∑​N​∣x⟩∣s(x)⟩∣s(x)⟩…​.

Again, this doesn’t seem all that promising. If you measured in the computational basis you’d again get a solution with probability1/N1/N1/N,which is too low to be useful.

What we want is to somehow increase the amplitudes in the terms with a111in the check qubit, and decrease the amplitudes when there is a000in the check qubit, a way of concentrating the amplitude in the right place. Imagine, for instance, we could do the following: if the check bit is000,then shrink the amplitude of the term by a factor222.And if the check bit is111,then double the amplitude by a factor222.

Actually, that can’t work – the state would quickly become unnormalized. But maybe something like this could work, shrinking the “bad” amplitudes and growing the ”good” amplitudes, balancing things so state normalization is preserved.

Unfortunately, this isn’t possible either, at least not directly! The trouble is that quantum gates are linear. That means they don’t directly “see” the amplitudes at all. For instance, for any gate described by a unitary matrixUUUand superposition of states,

U(α∣ψ⟩+β∣ϕ⟩)=αU∣ψ⟩+βU∣ϕ⟩.U (\alpha|\psi\rangle+\beta|\phi\rangle) = \alpha U|\psi\rangle + \beta U|\phi\rangle.U(α∣ψ⟩+β∣ϕ⟩)=αU∣ψ⟩+βU∣ϕ⟩.

That is, the gate doesn’t directly respond to the values of the amplitudesα\alphaαandβ\betaβat all, and so there’s no shrinking or growing of amplitudes.

Well, we haven't made much progress! Since we haven’t gotten very far with algebra, let’s instead try to visualize what we’re hoping for geometrically. We can think of ourselves as starting out in a state∣E⟩|E\rangle∣E⟩,and somehow trying to swing around to the solution∣s⟩|s\rangle∣s⟩,perhaps passing through some intermediate states∣ψ⟩|\psi\rangle∣ψ⟩along the way:





Of course, if only weknewthe identitysssof the search solution, we could simply swing around directly. Indeed, we could solve the problem in just a single step! But we don’t know∣s⟩|s\rangle∣s⟩.Instead, we’re hoping to use the search black box to somehow move closer.

I want to draw your attention to one particular feature of the above diagram. I’ve shown∣E⟩|E\rangle∣E⟩and∣s⟩|s\rangle∣s⟩as being nearly orthogonal. That’s actually a pretty accurate representation of reality, since no matter what the value of∣s⟩|s\rangle∣s⟩,its amplitude in the equal superposition∣E⟩|E\rangle∣E⟩is1/N1/\sqrt{N}1/N​.It’ll be useful later to have a name for the corresponding angle, so let me draw it here:





In particular, observe that the component of∣E⟩|E\rangle∣E⟩in the∣s⟩|s\rangle∣s⟩direction is justsin⁡(Δ)=1/N\sin(\Delta) = 1/\sqrt{N}sin(Δ)=1/N​,and soΔ=arcsin⁡(1/N)≈1/N\Delta = \arcsin(1/\sqrt{N}) \approx 1/\sqrt{N}Δ=arcsin(1/N​)≈1/N​.

As an aside, I’ll be expressing all angles in radians, not degrees. So a right angle isπ/2\pi/2π/2,a half rotation isπ\piπ,a full rotation is2π2\pi2π,and so on. I know some people prefer to think about angles in degrees, and using radians may frustrate them. On the other hand, if I worked in degrees, that’d be equally frustrating for people who prefer radians. Actually, it’d be more frustrating (and make the presentation more complex), because certain facts about trigonometry are simpler when angles are expressed in radians. An example, which I used in the last paragraph, is thatarcsin⁡(x)≈x\arcsin(x) \approx xarcsin(x)≈xfor smallxxx.That becomes the much uglierarcsin⁡(x)≈180x/π\arcsin(x) \approx 180\, x/\piarcsin(x)≈180x/πif we work in degrees. So it’s better just to work in radians. End of aside.

At this point, I’m going to engage in somedeus ex machina, and ask a question: what if we could somehowreflectabout the solution vector∣s⟩|s\rangle∣s⟩?

In fact, that turns out to be possible, and I’ll show you in a bit how to do it. For now though let’s just assume we can do it. Here’s what happens:





In this diagram,θ\thetaθis the angle between∣ψ⟩|\psi\rangle∣ψ⟩and∣s⟩|s\rangle∣s⟩,so2θ2\theta2θis the total angle between∣ψ⟩|\psi\rangle∣ψ⟩and its reflection.

You may recall from elementary plane geometry that if we do two consecutive reflections of the plane about different axes, the net result is a rotation of the plane. That seems encouraging. The obvious other vector to try reflecting about is the equal superposition∣E⟩|E\rangle∣E⟩.It seems plausible that if we could reflect about∣s⟩|s\rangle∣s⟩then we could also figure out how to reflect about∣E⟩|E\rangle∣E⟩.For now let’s just assume we can. The result is:





We can see from the above diagram that we’ve rotated from the original∣ψ⟩|\psi\rangle∣ψ⟩by an angle2θ+2ϕ2\theta + 2\phi2θ+2ϕ,whereϕ\phiϕis the angle between the equal superposition∣E⟩|E\rangle∣E⟩and the vector∣ψ⟩|\psi\rangle∣ψ⟩.

Looking at the diagram, after the two reflections the quantum state is pointing in almost the opposite direction to where we started, i.e., it’s close to−∣ψ⟩-|\psi\rangle−∣ψ⟩,but with a slight extra rotation. To see why this is true, imagine you’re in a plane, and reflect a vector about two exactly orthogonal axes – say, the usualxxxandyyyaxes. Of course, the result is just that the vector ends up pointing in the opposite direction.

In this case, we’re not reflecting about exactly orthogonal axes, but rather about two almost-orthogonal axes. So we’d expect the net rotation to be approximatelyπ\piπ,but with a small deviation. What’s more, we’d expect that deviation to be related to the angleΔ\DeltaΔby which the axes failed to be orthogonal. And that’s exactly right: we haveΔ=π2−θ−ϕ\Delta = \frac{\pi}{2}-\theta-\phiΔ=2π​−θ−ϕ,and so a little algebra shows that the rotation is2θ+2ϕ=π−2Δ2\theta + 2\phi = \pi-2\Delta2θ+2ϕ=π−2Δ.

This rotation ofπ−2Δ\pi-2\Deltaπ−2Δis almost what we’re looking for. One thing that makes it a little hard to think about is theπ\piπ.In fact, a rotation byπ\piπjust flips a vector in the plane back and forth about the origin, effectively multiplying it by−1-1−1.But in theprevious essaywe saw that such global phase factors make no difference whatsoever to outcomes at the end of a quantum computation. So after the double reflection it's exactly as though we're working with the state∣ψ′⟩|\psi'\rangle∣ψ′⟩shown belowIgnoring such global phase factors sometimes bother people getting into quantum computing. If it bugs you, just insert a single-qubit gate−I-I−Ion one of the qubits.:





We can now see what’s going on very clearly: flipping about∣s⟩|s\rangle∣s⟩and then∣E⟩|E\rangle∣E⟩is the same as doing a rotation by2Δ2\Delta2Δ(up to the global phase factor, which can be ignored). Summing up the result in one diagram, and omitting the intermediate states we have:





This is exciting news! It means we have a way of rotating from the starting state∣E⟩|E\rangle∣E⟩an angle2Δ2 \Delta2Δcloser to the search solution∣s⟩|s\rangle∣s⟩.What’s more, we can just keep repeating this operation. Maybe if we repeat it enough times we can rotate close to∣s⟩|s\rangle∣s⟩?

How many times do we need to rotate to get close to∣s⟩|s\rangle∣s⟩?And how close can we get?

Well, we’re rotating each time by2Δ2\Delta2Δ,and ideally we’d like to rotate by a total angle ofπ/2−Δ\pi/2-\Deltaπ/2−Δ.To get as close as possible to that total angle, the number of times we should rotate is just the integer closest to the ratio of the total angleπ/2−Δ\pi/2-\Deltaπ/2−Δwith the angle of each rotation2Δ2\Delta2Δ,i.e.:

round(π4Δ−1/2)\text{round}\left( \frac{\pi}{4 \Delta} - 1/2 \right)round(4Δπ​−1/2)

When we do so, we end up within an angleΔ\DeltaΔof∣s⟩|s\rangle∣s⟩.Remember thatΔ\DeltaΔis small, so we’re very near the state∣s⟩|s\rangle∣s⟩.It should be plausible that if you measure the quantum system you’ll get the resultssswith pretty high probability. We’ll figure out just how high that probability is shortly, but intuitively the overall picture is encouraging.

The expression above for the number of times to do the rotation has many details in it, which makes it hard to think about. The key behavior to focus on is that the number of rotations required scales with1/Δ1/\Delta1/Δ.But we saw earlier thatΔ≈1/N\Delta \approx 1/\sqrt{N}Δ≈1/N​,so1/Δ1/\Delta1/Δscales withN\sqrt{N}N​.The result is that if you perform roughlyπN/4\pi \sqrt{N}/4πN​/4rotations, you’ll end up very near to the desired search solution.

(By the way, I’ve used the phrase “roughly” there because to getΔ≈1/N\Delta \approx 1/\sqrt{N}Δ≈1/N​we used the approximationarcsin⁡(x)≈x\arcsin(x) \approx xarcsin(x)≈xfor smallxxx.In fact, a bit of fiddling around with trigonometry and algebra shows that more thanπN/4+1\pi \sqrt{N}/4 + 1πN​/4+1rotations are never required. In practice, you’d use the exact formula with the arcsine in it. But that formula is a little complicated and somewhat opaque – the kind of thing you’d be unlikely to memorize, but would instead look up, unless for some reason you needed it often. On the other hand,πN/4\pi \sqrt{N}/4πN​/4is a good shorthand, capturing the essential behavior, and worth remembering, along with the caveat that the actual expression is a little more complex.)

That’s the essence of the quantum search algorithm! There are still details to be filled in, but the basic outline is as follows:

When you consider the remarkable feat this algorithm accomplishes – searching anNNN-item search using∼N\sim\sqrt{N}∼N​examinations of that search space(!) – this is really quite simple and beautiful.

The algorithm is due to Lov Grover, who introduced it in 1996, and it’s often called Grover’s quantum search algorithm in his honor. And, as mentioned above, the two steps at the core of the algorithm are sometimes called theGrover iteration.

Before filling in the remaining details in the quantum search algorithm, let’s go through a few more spaced-repetition questions. These will help you remember many of the core elements of the algorithm. Note that a few details of the algorithm are still to be filled in, and we’ll discuss those in later sections. But we've got the core ideas now.

Exercise:At several points in this essay I ask you to ignore global phase factors. If that makes you uncomfortable, I invite you to repeat the analysis at each place I’ve made the request, not ignoring global phase factors. Show that the states output from the computation only ever change by a factor−1-1−1,raised to some power, and argue that measurement probabilities for the computation are not changed at all.

How should we achieve the desired reflections about the∣s⟩|s\rangle∣s⟩and∣E⟩|E\rangle∣E⟩states? To answer this question, we’ll start by focusing on the∣s⟩|s\rangle∣s⟩state, since computational basis states are closer to our everyday way of thinking about the world. And to make it even more concrete, let’s focus on the all000state,∣00…0⟩|00\ldots 0\rangle∣00…0⟩.

What would such a reflection actually do? It would mean leaving the∣00…0⟩|00\ldots 0\rangle∣00…0⟩state alone, and taking every other computational basis state∣x⟩|x\rangle∣x⟩to−∣x⟩-|x\rangle−∣x⟩.In terms of pseudocode, if the input state is∣x⟩|x\rangle∣x⟩:

It’s pretty easy to translate this into the quantum circuit model. You simply introduce an extra qubit that’s used as a sort of workspace for theifstatement (this working qubit is often called anancillaqubit – an unusual word in everyday speech, but easy to remember if you notice that it’s the word root for “ancillary”):





This looks different to the pseudocode, but it’s really just the quantum circuit version of the pseudocode. The first controlled gate checks to see whetherxxxis equal to00…000\ldots 000…0,as in theifcondition, flipping the ancilla qubit to111if so, and otherwise leaving it as000.The−Z-Z−Zgate on the ancilla then does exactly what we want, doing nothing if the ancilla is set to111(i.e., theifclause), and applying a factor−1-1−1if the ancilla is set to000(theelseclause). So the overall state is now∣x⟩∣1⟩|x\rangle|1\rangle∣x⟩∣1⟩whenxxxis00…000 \ldots 000…0,and−∣x⟩∣0⟩-|x\rangle|0\rangle−∣x⟩∣0⟩otherwise.

We’re almost done. The final controlled gate is there so we can clean up the ancilla qubit, and subsequently ignore it. To do that, we apply the same controlled gate again, resetting the ancilla to000,no matter what the initial computational basis state was. The result is the state∣x⟩∣0⟩|x\rangle|0\rangle∣x⟩∣0⟩whenxxxis00…000\ldots 000…0,and−∣x⟩∣0⟩-|x\rangle|0\rangle−∣x⟩∣0⟩whenxxxis anything else. So no matter the value ofxxxthe circuit leaves the ancilla in the fixed state∣0⟩|0\rangle∣0⟩,and that ancilla can be ignored through subsequent computations. Ignoring the ancilla, we see that the∣x⟩|x\rangle∣x⟩register has been reflected about the∣00…⟩|00\ldots\rangle∣00…⟩state, just as we wanted.

There’s a rough heuristic worth noting here, which is that you can often convertif-thenstyle thinking into quantum circuits. You introduce an ancilla qubit to store the outcome of evaluating theifcondition. And then depending on the state of the ancilla, you perform the appropriate state manipulation. Finally, when possible you reverse the initial computation, resetting the ancilla to its original state so you can subsequently ignore it.

For the reflection about∣00…0⟩|00\ldots 0\rangle∣00…0⟩there’s a clever trick which can be used to simplify the circuit shown above. Instead of using an ancilla in the∣0⟩|0\rangle∣0⟩state, start the ancilla in the∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​state (you do this using a NOT gate followed by a Hadamard gate on∣0⟩|0\rangle∣0⟩), and then use the following circuit:





Why does this work? Ifx≠00…x \neq 00\ldotsx​=00…,then nothing happens, and we end up in the state∣x⟩∣0⟩−∣1⟩2|x\rangle\frac{|0\rangle-|1\rangle}{\sqrt 2}∣x⟩2​∣0⟩−∣1⟩​.Ifx=00…x = 00\ldotsx=00…the ancilla qubit is NOTted, changing it from∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​to∣1⟩−∣0⟩2\frac{|1\rangle-|0\rangle}{\sqrt 2}2​∣1⟩−∣0⟩​,which is, of course, just−∣0⟩−∣1⟩2-\frac{|0\rangle-|1\rangle}{\sqrt 2}−2​∣0⟩−∣1⟩​.In both cases this is exactly what we wanted, except for a global phase factor of−1-1−1,which we can ignore. Furthermore, no matter the value ofxxxthe circuit leaves the ancilla in the fixed state∣0⟩−∣1⟩2\frac{|0\rangle-|1\rangle}{\sqrt 2}2​∣0⟩−∣1⟩​,and so the ancilla can be ignored through subsequent computations.

This is a nice trick, which I sometimes call the “phase trick”. I must admit, it seems a little like magic. It’s one of those things that’s easy to verify works, but it’s not so obvious how you would have discovered it in the first place. I don’t actually know the history of the trick (the earliest mention I know is in this1997 paper), but here’s how you might have discovered it. Suppose you’d been working hard on the original circuit I showed, thinking about each element:





I don’t necessarily mean you were trying to simplify the circuit, I just mean you were messing around trying to better understand how the circuit works. And then suppose in some other context someone mentioned to you (or you noticed) thatX∣0⟩−∣1⟩2=−∣0⟩−∣1⟩2X\frac{|0\rangle-|1\rangle}{\sqrt 2} = -\frac{|0\rangle-|1\rangle}{\sqrt 2}X2​∣0⟩−∣1⟩​=−2​∣0⟩−∣1⟩​.If you’d been sufficiently deep into thinking about the original circuit, a lightbulb might go on and you’d think “Hey, the NOT gate can be used to generate a factor−1-1−1,without otherwise changing the state of the qubit its being applied to. That kind of factor is just what we needed in our reflections. I wonder if I can somehow use that in my original circuit?”

Having made the connection you’d eventually figure the second circuit out, though it might have required a fair bit more work before you got the circuit just right.

Reflection about the∣s⟩|s\rangle∣s⟩state:Having figured out how to do the reflection for the all000state, it’s easy to do it for the∣s⟩|s\rangle∣s⟩state. We just use the search black box, in exactly the same style as the circuit just shown above:





It works for exactly the same reasons as the earlier circuit: the search black box is effectively applying a NOT gate to the ancilla, conditional onxxxbeing equal tosss.You’ll notice, by the way, that the phase trick buys us something nice here. If we’d used the original circuit, without the phase trick, we’d need two applications of the search black box to do the reflection about∣s⟩|s\rangle∣s⟩.So the phase trick decreases the cost of the quantum search algorithm by a factor two, a nice win.

Reflection about the equal superposition state,∣E⟩|E\rangle∣E⟩:The first time I thought about how to do this, I got a little paralyzed, thinking in essence: “Ooh, the∣E⟩|E\rangle∣E⟩state is strange and quantum, how could we possible reflect about it?”

Actually, it’s straightforward: just move the∣E⟩|E\rangle∣E⟩state to∣00…0⟩|00\ldots 0\rangle∣00…0⟩,reflect about∣00…0⟩|00\ldots 0\rangle∣00…0⟩,and then move the∣00…0⟩|00\ldots 0\rangle∣00…0⟩state back to∣E⟩|E\rangle∣E⟩.Here’s a circuit which does it:





This circuit works because the product of Hadamard gates both moves∣00…0⟩|00\ldots 0\rangle∣00…0⟩to∣E⟩|E\rangle∣E⟩,as we saw earlier, and also moves∣E⟩|E\rangle∣E⟩back to∣00…0⟩|00\ldots 0\rangle∣00…0⟩,since the Hadamard gate is its own inverse.

I’m not sure what lesson to draw from my initial fear of this problem, and its actual ease of solution – perhaps that sometimes things sound scary because they’re unfamiliar, but in fact they’re simple.

Exercise:Prove that the circuit shown above does, indeed, reflect about∣E⟩|E\rangle∣E⟩.To do the proof, suppose the input to the circuit isα∣E⟩+β∣E⊥⟩\alpha|E\rangle + \beta |E_\perp\rangleα∣E⟩+β∣E⊥​⟩,where∣E⊥⟩|E_\perp\rangle∣E⊥​⟩is some state orthogonal to∣E⟩|E\rangle∣E⟩.Then argue that the effect of the circuit is to take this to−(α∣E⟩−β∣E⊥⟩)-(\alpha|E\rangle-\beta |E_\perp\rangle)−(α∣E⟩−β∣E⊥​⟩).Up to a global phase factor this is the desired reflection.

As we saw earlier, the quantum search algorithm doesn’t produce the state∣s⟩|s\rangle∣s⟩exactly as output. Instead it produces a quantum state∣ψ⟩|\psi\rangle∣ψ⟩which is within an angleΔ\DeltaΔof∣s⟩|s\rangle∣s⟩,as shown below (in this example∣ψ⟩|\psi\rangle∣ψ⟩has slightly over-rotated past∣s⟩|s\rangle∣s⟩):





Now, the angleΔ\DeltaΔis small (particularly for a large search space, i.e., largeNNN,which is when we’re most interested in search), which means∣ψ⟩|\psi\rangle∣ψ⟩must be very close to∣s⟩|s\rangle∣s⟩.Intuitively, you’d expect a measurement in the computational basis would producessswith high probability.

That intuition is correct.

In particular, the probability a computational basis measurement gives the resultsssis just the square of the amplitude for∣s⟩|s\rangle∣s⟩in∣ψ⟩|\psi\rangle∣ψ⟩.That’s at least equal tocos⁡2(Δ)=1−sin⁡2(Δ)\cos^2(\Delta) = 1-\sin^2(\Delta)cos2(Δ)=1−sin2(Δ),which is just1−1/N1-1/N1−1/N.

Summing up: the probability that a computational basis state measurement gives the outcomesssis at least1−1/N1-1/N1−1/N.

So, for instance, if your search space hasN=1,000N = 1,000N=1,000or more elements, then the probability the search algorithm will find the correct outcomesssis at least1−1/10001-1/10001−1/1000,i.e., at least99.999.999.9percent. It works even more reliably for larger search spaces.

Now, even with this high probability you might still reasonably worry about what happens if the measurement gives the wrong outcome. Fortunately, it’s possible to quickly check whether that’s happened – whatever the measurement outcome is, we can use the search black box to check whether it’s a genuine solution or not. If it’s not, we simply rerun the algorithm.

That, in turn, creates a worry that you’d need to rerun the algorithm many times. But for largeNNN– the case we usually care about when searching! – that’s extremely unlikely. A little probability calculation shows that on average the number of times needed to run the algorithm is never more than1/(1−1/N)1/(1-1/N)1/(1−1/N),which is very close to111.Unsurprisingly, but pleasingly, our initial intuition was good: the quantum search algorithm produces the right answer, with high probability.

Let’s sum up our completed understanding of the quantum search algorithm:









That’s it, the complete quantum search algorithm!

I’ve tried to explain quantum search using what I call discovery fiction, a mostly-plausible series of steps you could imagine having taken to discover it, complete with occasional wrong turns and backtracking. Despite my attempts to make it legible, I believe there’s still something almost shocking about the quantum search algorithm. It’s incredible that you need only examine anNNN-item search space on the order ofN\sqrt{N}N​times in order to find what you’re looking for. And, from a practical point of view, we so often use brute search algorithms that it’s exciting we can get this quadratic speedup. It seems almost like a free lunch. Of course, quantum computers still being theoretical, it’s not quite a free lunch – more like a multi-billion dollar, multi-decade lunch!

Variations on the basic quantum search algorithm:I’ve explained the quantum search algorithm in its simplest form. There are many variations on these ideas. Especially useful variations include extending the algorithm so it can cope with the case of multiple solutions, and extending the algorithm so it can be used to estimate the number of solutions if that number isn’t known in advance.

I won’t discuss these in any detail. But if you want a challenge, try attacking these problems yourself. A good starting point is to find a search algorithm for the case where there exactly222search solutions, says1s_1s1​ands2s_2s2​.You already have most of the ideas needed, but it’s still an instructive challenge to figure it out. If you’re looking for much more detail about variations on the quantum search algorithm, you can find it in Chapter 6 ofmy book with Ike Chuang.

What if we used a different starting state?We simply guessed that the state∣E⟩|E\rangle∣E⟩was a good starting state. Imagine we’d started in a different quantum state, let’s call it∣ϕ⟩|\phi\rangle∣ϕ⟩.And then we repeatedly reflected about∣s⟩|s\rangle∣s⟩and about∣ϕ⟩|\phi\rangle∣ϕ⟩.As before, the net result of such a double reflection is a rotation, with the angle equal toπ\piπminus double the angle between∣ϕ⟩|\phi\rangle∣ϕ⟩and∣s⟩|s\rangle∣s⟩.It’s fun to think about different things one can do with such a rotation. I won’t get into it here, except to quickly mention that this observation can be used to do a type of structured search. For instance, if we know some valuesxxxaren’t possible solutions to the search problem, we can actually speed the search algorithm up by making sure∣x⟩|x\rangle∣x⟩doesn’t appear in the initial superposition∣ϕ⟩|\phi\rangle∣ϕ⟩.

Can we improve the quantum search algorithm?A good question to ask is whether it’s possible to improve the quantum search algorithm? That is, is it possible to find a quantum algorithm which requires fewer applications of the search black box? Maybe, for instance, we could solve the search problem usingN3\sqrt[3]{N}3N​applications of the search black box. That would be a tremendously useful improvement.

If we were truly optimistic we might even hope to solve the search problem using on the order oflog⁡(N)\log(N)log(N)applications of the search black box. If that were possible, it would be revolutionary. We could use the resulting quantum algorithm to very rapidly solve problems like the traveling salesperson problem, and other NP-complete optimization problems, problems such as protein folding, satisfiability, and other famous hard problems. It would be a silver bullet, a way in which quantum computers were vastly superior to classical.

Unfortunately, it turns out that the quantum search algorithm as I’ve presented it is optimal. In particular, no search algorithm with faster than∼N\sim\sqrt{N}∼N​scaling is possible. This was proved in a remarkable1997 paper. While this is a real pity, the quantum search algorithm still provides a more limited butbona fidesilver bullet for speeding up a wide class of classical computations.

Exercise:Suppose that instead of performing a measurement, we instead continue performing Grover iterations. Argue that the quantum state will continue to rotate, and that we would expect the amplitude for∣s⟩|s\rangle∣s⟩to start todecrease.

Exercise:Argue that if we continue performing Grover iterations, as in the last question, we’d eventually expect the measurement probability forsssto be no more than1/N1/N1/N.

Are there any general lessons about quantum computers we can learn from the quantum search algorithm?

Although dozens or hundreds of quantum algorithms have been developed, most are for relatively specialized – indeed, often rather artificial – problems. Apart from simulating quantum systems, only a handful of inarguably extremely useful quantum algorithms are known (quantum search is one). In particular, there is as yet no good general-purpose recipe for saying when a problem can be fruitfully attacked using a quantum computer, or how. Quantum algorithm design is still bespoke.

For this reason, we should beware any too-pat explanation of why the quantum search algorithm works. If an explanation is really good, it should enable us to find interesting new algorithms, not merely provide eagle-eyed hindsight.

With that caveat in mind, I do want to make one observation. Below is an animation showing the amplitudes for all the computational basis states as the quantum search algorithm runs. In particular, it shows the amplitudes after each Grover iteration, starting at iteration000and running up to the final iteration – in this case, iteration number777:

You can see that the effect of the Grover iteration is to take amplitude from non-solutions and gradually concentrate it in the solution. This is just what I said earlier couldn’t be done directly. That was true, in the sense that all the gates in our circuit are still acting linearly through the amplitudes.

So what’s happening?

Well, you may remember in the last essay Iasked youto guess what would happen if you applied the Hadamard gate twice in a row to the∣0⟩|0\rangle∣0⟩state. Intuitively, the Hadamard gate mixes the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states, so you might guess the end result would be to thoroughly mix them up.

Only that’s not what happens. Instead, here’s the two steps:

∣0⟩→∣0⟩+∣1⟩2→∣0⟩+∣1⟩2+∣0⟩−∣1⟩22.|0\rangle \rightarrow \frac{|0\rangle+|1\rangle}{\sqrt 2} \rightarrow \frac{\frac{|0\rangle+|1\rangle}{\sqrt 2} + \frac{|0\rangle-|1\rangle}{\sqrt 2}}{\sqrt 2}.∣0⟩→2​∣0⟩+∣1⟩​→2​2​∣0⟩+∣1⟩​+2​∣0⟩−∣1⟩​​.

If you look closely at the final expression on the right-hand side you see that the opposite signs on the two∣1⟩|1\rangle∣1⟩states are canceling each other out, a phenomenon calleddestructive interference. Meanwhile, the two∣0⟩|0\rangle∣0⟩states add up, a phenomenon calledconstructive interference. The net result is to concentrate all the amplitude in the∣0⟩|0\rangle∣0⟩state, and so the outcome is just∣0⟩|0\rangle∣0⟩.

A similar (though more complicated) type of interference and sign cancellation is going on during the Grover iteration. Suppose we start out the iteration as follows:





We then reflect about the∣s⟩|s\rangle∣s⟩state, which inverts all the non-sssamplitudes:





The next step is to reflect about the∣E⟩|E\rangle∣E⟩state. The effect of this step is to achieve a cancellation similar (but more complicated) than was going on in the second stage of the double-Hadamard. In particular, this reflection reduces the∣s⟩|s\rangle∣s⟩amplitude a little, redistributing it over all the other computational basis states. At the same time, it takes the superposition over all the other states and reduces it slightly, redistributing it to the∣s⟩|s\rangle∣s⟩state. The net effect is to grow the∣s⟩|s\rangle∣s⟩amplitude and shrink the others, albeit “upside down”:





The−1-1−1global phase factor simply inverts everything, and the total effect is to grow the∣s⟩|s\rangle∣s⟩amplitude and shrink the others. In net, we’ve used the∣s⟩|s\rangle∣s⟩amplitude to cancel out some of the other amplitudes (destructive interference), and the other amplitudes to reinforce some of the∣s⟩|s\rangle∣s⟩amplitude (constructive interference).

This explanation is, alas, somewhat vague. I wish I could write it in a clearer way, but I can’t because I don’t really understand it in a clearer way. There’s more I could say – other perspectives, other calculations we could do. Going through all that would help, but only a little. At the core is still a clever way of using the∣s⟩|s\rangle∣s⟩-amplitude to cancel out non-∣s⟩|s\rangle∣s⟩amplitudes, and to use non-∣s⟩|s\rangle∣s⟩amplitudes to reinforce the∣s⟩|s\rangle∣s⟩-amplitude.

Quantum parallelism:One thing the quantum search algorithm has in common with many other quantum algorithms is the use of large superposition states. For instance, the equal superposition state∣E⟩=∑x∣x⟩/N|E\rangle = \sum_x |x\rangle/\sqrt{N}∣E⟩=∑x​∣x⟩/N​shows up in many quantum algorithms. It’s a pretty common pattern in those algorithms to then modify that state so each term∣x⟩|x\rangle∣x⟩picks up some information relevant to the solution of the overall problem, and then to trying to arrange cancellation of terms. This pattern is often known asquantum parallelism.

Upon first acquaintance, this seems much like a conventional classical computer running a randomized (i.e., Monte Carlo) algorithm. In particular, it’s a bit like trying a random solution, and then computing some information relevant to the overall problem you’re trying to solve. But what is very different is that in a classical computer there’s no way of getting cancellation between different possible solutions. The ability to get that kind of interference is crucial to quantum computing.

Why we use clean computation:Earlier, I promised you an explanation of why we used clean computation. In fact, for the interference to work, it’s essential that no other qubits are changed by the computation. Suppose we had a sum involving working qubits in lots of different states, something like (omitting factors)∑x∣x⟩∣w(x)⟩\sum_x |x\rangle|w(x)\rangle∑x​∣x⟩∣w(x)⟩,i.e., a non-clean computation. We couldn’t get any sort of cancellation (or reinforcement) between terms with different values ofw(x)w(x)w(x).Those other qubits would be storing information which prevented cancellation of terms. That’s why clean computation is helpful.

This helps explain why clean computation is useful, but may leave you wondering how you could ever have invented clean computation in the first place?

In fact, historically the uncomputation trick for clean computation was discovered for reasons having nothing to do with quantum algorithms or with interference. It was discovered by people who were trying to figure out how to make conventional classical computers more energy efficient. Those people had come up with an argument (which I won’t describe here) that working bits actually contributed to energy inefficiency. And so they discovered uncomputation as a way of minimizing that energy cost. It was only later that it was realized that clean computation was extremely useful in quantum computing, especially for getting interference effects.

This is a pattern which often occurs in creative work far beyond physics: ideas which arise in one context are often later reused for completely different reasons in another context. I believe that if that prior work on energy-efficient computing hadn’t been done, it might have taken quite a bit more effort to come up with the quantum search algorithm.

Concluding thoughts:You’ve now worked through the details of a powerful, widely-usable quantum algorithm. Other algorithms are known, some of which – notably, the quantum algorithm for factoring integers – offer even larger speedups over known classical algorithms. Still, if and when quantum computers are eventually built the quantum search algorithm is likely to be an extremely useful application. What’s more, many of the ideas used in the search algorithm are used in other quantum algorithms.

Thanks for reading this far. In the coming weeks, you’ll receive a notification containing a link to your first review session. In that review session you’ll be retested on the material you’ve learned, helping you further commit it to memory. It should only take a few minutes. In subsequent weeks you’ll receive more notifications linking you to re-review, gradually working toward genuine long-term memory of all the core material in the essay.

Thanks for reading this far. If you’d like to remember the core ideas of this essay durably, please set up an account below. We’ll track your review schedule and send you occasional reminders containing links that will take you to the review experience.

Michael Nielsen is supported byY Combinator Research.

In academic work, please cite this as:

Authors are listed in alphabetical order.

This work is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported License. This means you’re free to copy, share, and build on this essay, but not to sell it. If you’re interested in commercial use, pleasecontact us.

April 16, 2019

See ourUser Agreement and Privacy Policy.


---

# How quantum teleportation works

Andy MatuschakandMichael Nielsen

Part of aseries of essaysin a mnemonic medium which makes it almost effortless to remember what you read.

byAndy MatuschakandMichael Nielsen

Presented in a new mnemonic medium which makes it almost effortless to remember what you read.

Our future projects are funded in part by readers like you.

Special thanks to our sponsor-level patrons,Adam Wiggins,Andrew Sutherland,Bert Muthalaly,Calvin French-Owen,Dwight Crow,fnnch,James Hill-Khurana,Lambda AI Hardware,Ludwig Petersson,Mickey McManus,Mintter,Patrick Collison, Paul Sutter,Peter Hartree,Sana Labs,Shripriya Mahesh,Tim O'Reilly.

According to an old Mexican folk story, on October 24, 1593 a Spanish soldier named Gil Pérez was guarding the Governor's Palace in Manila, in what is today known as the Philippines. The Governor had been assassinated by pirates on the previous night, and the soldiers guarding the palace were exhausted. Tired, Pérez leaned against a wall, and shut his eyes.

When he opened his eyes, he was no longer in Manila. Somehow, miraculously, he'd been transported instantaneously across the Pacific Ocean. He was in the Zócalo, the great public square in Mexico City. He was found by guards, who suspected that he was a deserter, due to his uniform, and threw him in jail. But he had the presence of mind to tell the guards of the death of the Governor in Manila. Months later, Pérez's story was confirmed when news of the Governor's death arrived by boat, and he was releasedStory and text adapted fromWikipedia..

It's an entertaining story. For centuries, teleportation – especially the teleportation of humans! – has been a trope of folk stories, of magic shows, and of science fiction. But in 1993 a group of physicists discovered a genuine type ofquantum teleportation, which enables a quantum state to be transported across long distances, without any need to directly send the quantum stateThe original paper is by Charles H. Bennett, Gille Brassard, Claude Crépeau, Richard Jozsa, Asher Peres, and William K. Wootters,Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels(1993). An account of the discovery has been provided by one of the discoverers: Asher Peres,What is actually teleported?(2003)..

The initial quantum teleportation paper was theoretical, using the mathematical rules of quantum mechanics to predict the teleportation phenomenon. That prediction has since been followed by many experiments demonstrating the effect. Furthermore, it turns out that quantum teleportation isn't just a fun stunt. It underlies many other phenomena in quantum computing and, more broadly, in quantum information science. For instance, it's led to important ideas about reducing the effects of noise on quantum computers, and to new hardware ideas for building quantum computers. These connections were a surprise – it's not at all obvious that quantum teleportation should have such applications. But because of applications such as these, teleportation is today viewed as a core primitive in quantum information science.

In this essay I explainA note on pronouns: Michael wrote the text of the essay, and will use singular pronouns like “I” to denote the author, and “we” to mean the reader and the author jointly. Andy and Michael developed the mnemonic medium together.how quantum teleportation works. We'll delve deep into the details of the teleportation protocol, and discuss some of the implications of teleportation. To read the essay you need to be familiar with the quantum circuit model of computation. If you're not, you can learn the elements from the earlier essayQuantum Computing for the Very Curious, and you may wish to read that essay now. You shouldn't need any other prerequisites.

The essay is presented in an unusual style. It's an example of what Andy Matuschak and I have dubbed amnemonic medium, incorporating new user interface elements intended to make it almost effortless for you to remember the content of the essay. The motivator is that most people (myself included) quickly forget much of what we read in books and articles. But cognitive scientists know a lot about how human beings commit ideas to memory. The mnemonic medium takes advantage of this understanding, creating an interface which will make it easy to remember the material for the long term. That is, not only will you learn quantum teleportation now: with a little extra effort, you'll remember it near-permanently. More on how that works below.

If you look ahead, you'll see that the essay contains a lot of details, and perhaps seems like a lot of work to read. In fact, itisa lot of work to read! Why not just read some popular account of teleportation instead? Or do something else entirely? The payoff is that with less than an hour's work you can understand in full detail an astonishing fact about the way the universe works. And it won't be a handwavy explanation, the kind you find in popular science accounts. It'll be the full story. Furthermore, if you explore quantum information and computation further, you'll find teleportation pops up all over the place. It's a fundamental tool in the toolkit of quantum computing, well nigh as useful as a chef's knife in a kitchen. So let's get on with understanding it.

What might it mean to teleport a quantum state from one location to another?

For simplicity, we'll consider the case of teleporting the simplest possible quantum system – a qubit. We'll suppose an experimentalist, Alice, has in her laboratory a single qubit, in a quantum state∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha|0\rangle+\beta|1\rangle∣ψ⟩=α∣0⟩+β∣1⟩.Alice would like to send her quantum state to a distant laboratory operated by a colleague, Bob.

Of course, Alice could simply physically send the qubit. We're going to rule that out by fiat, as violating the desired spirit of teleportation.

Another approach would be for Alice to simply tell Bob the amplitudesα\alphaαandβ\betaβfor the quantum state∣ψ⟩|\psi\rangle∣ψ⟩.To do this she doesn't need to send a quantum state – she can simply send the complex numbersα\alphaαandβ\betaβto Bob, as ordinary classical information (perhaps over the internet). Bob could then re-create the state in his laboratory. But in general Alice won't know those amplitudes – there's no particular reason to suppose she knows the identity of her quantum state. It turns out that quantum teleportation works even when the identity of the state isn't known to Alice or Bob.

Yet another possible approach is for Alice to somehow measure the state of her qubit, figuring out the amplitudes, and then telling Bob so he can re-create the state. Unfortunately, as Iexplained elsewhere, in general Alice can get only very limited information about those amplitudes. There's certainly no way she can get anything like enough information for Bob to re-create∣ψ⟩|\psi\rangle∣ψ⟩or a state very close to it.

So what can Alice and Bob do?

The solution – the quantum teleportation protocol – is sufficiently simple that I'm just going to lay out the steps for you. After I've laid out the steps, it'll be pretty easy for us to verify that it works, and to discuss some implications. Note that youshouldn'texpect to immediately see why the protocol works, or why we're using these steps in particular. Indeed, it would be shocking if you could! Rather, the point right now is to begin getting familiar with the basic mechanics of teleportation – the gates and measurements involved. Only later in the essay will we verify that these work, and gradually understand in more depth how to think about the protocol.

For Alice and Bob to do the teleportation, in addition to Alice having∣ψ⟩|\psi\rangle∣ψ⟩in her possession, they also need to begin by sharing a special two-qubit state,

∣00⟩+∣11⟩2,\frac{|00\rangle+|11\rangle}{\sqrt 2},2​∣00⟩+∣11⟩​,

one qubit in Alice's possession, the other in Bob's possession. This can be arranged in many ways. One way, for instance, is for Bob to perform the following quantum circuit in his laboratory:



With that done, Bob sends one of the two qubits to Alice. It doesn't matter which qubit he sends, since the state is symmetric. We can now depict the three qubits as:



Here, the top two qubits belong to Alice. And the third qubit is in Bob's possession. This representation has the drawback that you've got to keep in mind which qubits belong to Alice, and which to Bob. We could make this easier by inserting some vertical space between the second and third qubits (and people sometimes do exactly this), but it's not that much work to remember, so we'll stick with the more compact representation.

The quantum circuit language is also a nice way to depict the rest of the quantum teleportation protocol. Here it is:



Most of this is pretty transparent. Alice starts with an unknown quantum state,∣ψ⟩|\psi\rangle∣ψ⟩,which is to be teleported. Alice and Bob share a quantum state∣00⟩+∣11⟩2\frac{|00\rangle+|11\rangle}{\sqrt 2}2​∣00⟩+∣11⟩​.Then Alice performs two gates on her qubits, followed by measuring both of her qubits in the computational basis, with outcomeszzzandxxx.These are just conventional classical bits, each taking the value000or111.

The next piece of the protocol is only implied in the circuit representation above. Having measured her qubits, Alice then sends the classical bitszzzandxxxover to Bob. She can do this however she likes – using the internet, or some other classical communication channel. Bob then applies the PauliXXXgate (i.e., the quantum NOT gate) to his qubit ifx=1x=1x=1,and otherwise does nothing. This is the meaning of theXxX^xXxnotationIt's just matrix exponentiation:X0=IX^0 = IX0=I,the identity matrix, andX1=XX^1 = XX1=X,the NOT gate.. Similarly, Bob applies the PauliZZZgate to his qubit ifz=1z = 1z=1,and otherwise does nothing.

The end result is that Bob's qubit is now in the same state∣ψ⟩|\psi\rangle∣ψ⟩that Alice started with. That is, Alice has successfully teleported her state to Bob.

There's a lot to unpack here. As I said above, you certainly shouldn't expect to immediately see why teleportation works! But as you can see at least the basic mechanics are pretty simple: it's just a few gates, a few measurements, and some classical communication. And, somehow, Bob ends up with the state∣ψ⟩|\psi\rangle∣ψ⟩.We'll spend the rest of the essay understanding why it's true, and what some of the implications are.

Before going through any of those details, I want to emphasize just how strange the result of the teleportation circuit is. Alice starts out with a state∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha|0\rangle+\beta|1\rangle∣ψ⟩=α∣0⟩+β∣1⟩.She does some stuff to her qubits, and then – without sending Bob any qubitat all– somehow Bob is able to recover∣ψ⟩|\psi\rangle∣ψ⟩,using just two bits of classical information,xxxandzzz.

This is quite remarkable. After all, Alice hasn't sent Bob a qubit, just two classical bits. You might say “Oh, well, those two bits must do the job of carrying the information from the qubit”. But that can't possibly be right: just to precisely specify the original amplitudesα\alphaαandβ\betaβwould require, in principle, an infinite amount of classical information. Obviously, neither Alice nor Bob receives that information. Yet Bob is somehow able to recover∣ψ⟩|\psi\rangle∣ψ⟩anyway.

This is, in my opinion, a most curious and surprising state of affairs. We'll understand more deeply how it works below.

In the introduction I said that this essay is in a new form, a mnemonic medium. That means the medium is designed to make it essentially effortless for you to remember what you read.

The way the mnemonic medium works is this: throughout the essay we'll occasionally pause to ask you a few simple questions, testing you on the material just explained. In the weeks ahead we'll re-test you in followup review sessions. By expanding the review schedule, we can ensure you consolidate the answers into your long-term memory, while minimizing the study time required. In particular, the expanding review schedule means that each extra minute spent studying provides more and more benefit, a kind of exponential return. The review sessions take no more than a few minutes, and we'll notify you when you need to review. The benefit is that instead of remembering how quantum teleportation works for a few hours or days, you'll remember for years; it'll become a much more deeply internalized part of your thinking. That may sound a strange aspiration. But if you're genuinely interested in understanding quantum computing, then having teleportation down cold is necessary.

To give you a more concrete flavor of how the mnemonic medium works, let's take a look at three questions reviewing part of what you've just learned. Please indulge me by answering these questions – it'll take just a few seconds. For each question, think about what you believe the answer to be, click to reveal the actual answer, and then mark whether you remembered or not. If you can recall, that's great. But if not – and most readers don't get the answers to these questions correct(!) – I'll have some comments on how to think about it below.

I said above that most readers don't recall the answers to these questions. It's worth thinking about what this means. The questions ask about some of the most absolutely basic things about the quantum teleportation protocol. If someone is not getting these questions correct, what are they really learning about quantum teleportation? If you're in this boat, I challenge you to name threespecificthings that you've learned about quantum teleportation so far. Genuine learning requires paying close attention to what you're reading. In fact, it's not difficult to learn any of the three things tested in the questions above, if you're paying attention.

I don't mean to be a downer. But I also think it's important to be realistic. Most people (myself included) learn very little from most of what we read, unless we're paying close attention. The reading may be entertaining, or produce a brief illusion of understanding. But you can only learn if you pay attention. The questions are good way of monitoring whether that's the case. And reviewing them again in the future will help you internalize this understanding for the long term.

You may object that there's not much point in knowing “unimportant details” like the circuit used to generate Alice and Bob's shared state. It's tempting to take refuge in a belief that what you're looking for is a broad, conceptual understanding. Unfortunately, I've never met someone knowledgeable about quantum computing who didn't know the details of teleportation. So I don't buy the “unimportant details” argument.

Imagine meeting someone who told you that they “had a broad conceptual understanding” of how to speak Spanish, but it turned out they didn't know the meanings of hola, adiós, or bien. You'd think their claim to a broad conceptual understanding of Spanish was hilarious. If you want to understand quantum computing and related subjects, you need to know the details of how the teleportation protocol works. That means knowing things like what state Alice and Bob initially share. What's more, it means not just knowing them immediately after reading. It means internalizing them for the long term.

If you're interested in doing that, then I invite you to set up an account by signing in below. If you do so, your review schedule for each question in the essay will be tracked, and you'll receive periodic reminders, containing a link which takes you to an online review session. That review session isn't this full essay – rather, it looks just like the question set you answered above, but contains insteadallthe questions which are due, so you can quickly run through them. The time commitment is no more than a few minutes per session. You can study on your phone while grabbing coffee, or standing in line, or going for a walk, or in transit. The return for that small time commitment is an internalized understanding of quantum teleportation, retained for years instead of days.

To keep this promise, we'll track your review schedule for each question, and send you occasional reminders to check in, and to run through the questions which are due. You can review on your phone while grabbing coffee, or standing in line, or going for a walk, or on transit. The return for that small time commitment is an internalized understanding of quantum teleportation; it'll become a part of who you are, retained for years instead of days.

Before we verify that the teleportation circuit works, let's briefly discuss one of the most common questions about quantum teleportation: does it enable faster-than-light communication?

At first, it looks as though it may – after all, Alice is able to transmit her state∣ψ⟩|\psi\rangle∣ψ⟩to Bob, even if he's very distant from her. It'd be quite marvelous if it enabled faster-than-light communication, since that in turn would give rise to many incredible phenomena, including the ability to send information backward in time.

But while it would be marvelous, it is not possible. You can see the trouble if you think closely about the protocol. Remember, for Bob to recover the state∣ψ⟩|\psi\rangle∣ψ⟩,Alice must send Bob two bits of classical information. The speed of that transmission is limited by the speed of light. Without that classical information, Bob can't guarantee that he recovers∣ψ⟩|\psi\rangle∣ψ⟩.Instead, what he has is a distribution over four different possible states. And while I won't prove it here, it turns out to be possible to prove that with only that distribution over states, no information is transferred from Alice to Bob. It's a pity, but that's the way the world seems to work.

Let's pause to quickly review a few more questions about teleportation:

Notice that the second question is a more qualitative style of question than the earlier questions. Your answer may not exactly match the answer given. It's up to you to decide whether you want to mark yourself correct or not. Ask yourself: have Ireallyunderstood the core point? If so, mark yourself correct. If not, don't! The point of all the questions is to serve you, and it's up to you to decide how best they can do that.

To verify that the teleportation protocol works, we'll mostly use tools already introduced in the earlier essayQuantum Computing for the Very Curious. But there's one missing piece of background knowledge we need to fill in first.

In the earlier essay I explained how to do computational basis measurements for multi-qubit systems. But I didn't explain what happens if you measure just some (but not all) of the qubits. This is relevant to quantum teleportation, since we're going to be measuring just two of three qubits.

The rule for describing such partial measurements is simple, though slightly cumbersome to describe. First, I'll describe it for a two-qubit system, and then explain how it generalizes. Suppose we have a two-qubit system in the state

a∣00⟩+b∣01⟩+c∣10⟩+d∣11⟩.a|00\rangle+b|01\rangle+c|10\rangle+d|11\rangle.a∣00⟩+b∣01⟩+c∣10⟩+d∣11⟩.

Suppose we measure just the first qubit in the computational basis. We'd like to know (i) what the probabilities for the two measurement outcomes are; and (ii) what the corresponding resulting state of the second qubit will be.

To answer these questions, we simply group terms corresponding to∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩on the first qubit, rewriting the state as

∣0⟩(a∣0⟩+b∣1⟩)+∣1⟩(c∣0⟩+d∣1⟩).|0\rangle(a|0\rangle+b|1\rangle)+ |1\rangle(c|0\rangle+d|1\rangle).∣0⟩(a∣0⟩+b∣1⟩)+∣1⟩(c∣0⟩+d∣1⟩).

Suppose we measure in the computational basis on the first qubit, and obtain the result000.It probably won't surprise you that the resulting state of the second qubit is just the corresponding piece from the above expression, namelya∣0⟩+b∣1⟩a|0\rangle+b|1\ranglea∣0⟩+b∣1⟩,normalized by dividing by∣a∣2+∣b∣2\sqrt{|a|^2+|b|^2}∣a∣2+∣b∣2​,so it's a properly normalized quantum state:

a∣0⟩+b∣1⟩∣a∣2+∣b∣2\frac{a|0\rangle+b|1\rangle}{\sqrt{|a|^2+|b|^2}}∣a∣2+∣b∣2​a∣0⟩+b∣1⟩​

This result occurs with probability∣a∣2+∣b∣2|a|^2+|b|^2∣a∣2+∣b∣2.The resulting state of the first qubit is, of course,∣0⟩|0\rangle∣0⟩.

Similarly, if the result from the computational basis measurement is111,then the corresponding conditional state for the second qubit is

c∣0⟩+d∣1⟩∣c∣2+∣d∣2,\frac{c|0\rangle+d|1\rangle}{\sqrt{|c|^2+|d|^2}},∣c∣2+∣d∣2​c∣0⟩+d∣1⟩​,

and this occurs with probability∣c∣2+∣d∣2|c|^2+|d|^2∣c∣2+∣d∣2.The resulting state of the first qubit is, of course,∣1⟩|1\rangle∣1⟩.

I won't write the general rule out in absolutely full generality, but hopefully it's pretty clear what the rule is. For instance, suppose we measure the first two qubits of a many-qubit system in the computational basis. To figure out the result, we express the state immediately prior to measurement as

∣00⟩∣ψ00⟩+∣01⟩∣ψ01⟩+∣10⟩∣ψ10⟩+∣11⟩∣ψ11⟩.|00\rangle|\psi_{00}\rangle + |01\rangle|\psi_{01}\rangle +|10\rangle|\psi_{10}\rangle + |11\rangle|\psi_{11}\rangle.∣00⟩∣ψ00​⟩+∣01⟩∣ψ01​⟩+∣10⟩∣ψ10​⟩+∣11⟩∣ψ11​⟩.

The result of measuring the first two qubits in the computational basis is000000with probability∥∣ψ00⟩∥2\| |\psi_{00}\rangle \|^2∥∣ψ00​⟩∥2,and the resulting state of the other qubits in the system is the normalized state∣ψ00⟩/∥∣ψ00⟩∥|\psi_{00}\rangle/\||\psi_{00}\rangle\|∣ψ00​⟩/∥∣ψ00​⟩∥.The resulting state of the first two qubits is∣00⟩|00\rangle∣00⟩.

It works similarly for the other possible outcomes.

As I said above, this rule is a little bit cumbersome, but with some practice it becomes easy to use fluently. We'll get an opportunity very shortly, as we verify the teleportation protocol.

To help you get used to the rule, it's worth taking a few minutes to work through the exercise immediately below. Unlike the review questions, the point of the exercise isn't as an aid to memory. Rather, it's here because it will help you better understand the material just introduced. Note that even if you don't work through the exercise, it's worth at least reading through it, since some of the results will be tested in the review questions.

Exercise:Suppose we have a quantum state0.8∣01⟩+0.2∣10⟩\sqrt{0.8} |01\rangle+\sqrt{0.2}|10\rangle0.8​∣01⟩+0.2​∣10⟩and measure the first qubit in the computational basis. What is the probability the measurement gives000as outcome? What is the corresponding state of the second qubit? What is the probability the measurement gives111as the outcome? What is the corresponding state of the second qubit?

Answer / spoilers:It's worth your time taking a shot at the exercise, since even if you get stuck, learning to cope with being stuck is a much-needed superpower in quantum computing. But after you've done that, here are the answers: the probability of the outcome000is0.80.80.8and the corresponding state of the second qubit is∣1⟩|1\rangle∣1⟩;the probability of the outcome111is0.20.20.2and the corresponding state of the second qubit is∣0⟩|0\rangle∣0⟩.

Some of these questions perhaps seem peculiar. Obviously, there's little long-term value in remembering thespecificprobability of getting outcome000when we measure the first qubit of0.8∣01⟩+0.2∣10⟩\sqrt{0.8}|01\rangle+\sqrt{0.2}|10\rangle0.8​∣01⟩+0.2​∣10⟩in the computational basis. Rather, you should think of this question (and similar questions) as really implicitly asking if you rememberhowto compute the probability. And marking your answer appropriately. That procedural knowledge really is valuable to remember.

We now have all the tools necessary to verify that teleportation works. In fact, if you're feeling enthusiastic, you can do the verification yourself. I won't pretend that it's not some work. On the other hand, if you push through the calculation you can take away a lot of confidence that you can do nontrivial calculations in quantum mechanics.

With that said, let me show you one approach to doing the verification.

(By the way, none of the in-essay review questions will be on the details of the verification. So while you should follow along, you don't need to remember every detail. There wouldn't be much point – there are many ways of doing the verification, and what's important is that you are able to do it somehow, not that you remember any particular approach.)

Let's start by recalling the circuit depicting the protocol:



Writing∣ψ⟩|\psi\rangle∣ψ⟩explicitly in terms of its amplitudes,∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha|0\rangle+\beta|1\rangle∣ψ⟩=α∣0⟩+β∣1⟩,we see that the initial state at the start of the teleportation protocol is:

(α∣0⟩+β∣1⟩)∣00⟩+∣11⟩2.(\alpha|0\rangle+\beta|1\rangle) \frac{|00\rangle+|11\rangle}{\sqrt 2}.(α∣0⟩+β∣1⟩)2​∣00⟩+∣11⟩​.

We can expand this out as

α∣000⟩+α∣011⟩+β∣100⟩+β∣111⟩2.\frac{\alpha|000\rangle+\alpha|011\rangle+\beta|100\rangle+\beta|111\rangle}{\sqrt 2}.2​α∣000⟩+α∣011⟩+β∣100⟩+β∣111⟩​.

We apply the CNOT to the first two qubits to obtain

α∣000⟩+α∣011⟩+β∣110⟩+β∣101⟩2.\frac{\alpha|000\rangle+\alpha|011\rangle+\beta|110\rangle+\beta|101\rangle}{\sqrt 2}.2​α∣000⟩+α∣011⟩+β∣110⟩+β∣101⟩​.

Then we apply the Hadamard gate to the first qubit. Recall from theearlier essaythatH∣0⟩=∣0⟩+∣1⟩2H|0\rangle = \frac{|0\rangle+|1\rangle}{\sqrt 2}H∣0⟩=2​∣0⟩+∣1⟩​andH∣1⟩=∣0⟩−∣1⟩2H|1\rangle = \frac{|0\rangle-|1\rangle}{\sqrt 2}H∣1⟩=2​∣0⟩−∣1⟩​.So after the Hadamard gate on the first qubit the state is

α∣000⟩+α∣100⟩+α∣011⟩+α∣111⟩+β∣010⟩−β∣110⟩+β∣001⟩−β∣101⟩2.\frac{\alpha|000\rangle+\alpha|100\rangle+\alpha|011\rangle+\alpha|111\rangle+\beta|010\rangle-\beta|110\rangle+\beta|001\rangle-\beta|101\rangle}{2}.2α∣000⟩+α∣100⟩+α∣011⟩+α∣111⟩+β∣010⟩−β∣110⟩+β∣001⟩−β∣101⟩​.

To analyze the computational basis measurement on the first two qubits, we group terms corresponding to each computational basis state for those qubits. The state above can be rewritten

∣00⟩(α∣0⟩+β∣1⟩)+∣01⟩(α∣1⟩+β∣0⟩)+∣10⟩(α∣0⟩−β∣1⟩)+∣11⟩(α∣1⟩−β∣0⟩)2.\frac{|00\rangle(\alpha|0\rangle+\beta|1\rangle)+ |01\rangle(\alpha|1\rangle+\beta|0\rangle)+ |10\rangle(\alpha|0\rangle-\beta|1\rangle)+ |11\rangle(\alpha|1\rangle-\beta|0\rangle) }{2}.2∣00⟩(α∣0⟩+β∣1⟩)+∣01⟩(α∣1⟩+β∣0⟩)+∣10⟩(α∣0⟩−β∣1⟩)+∣11⟩(α∣1⟩−β∣0⟩)​.

When Alice measures in the computational basis, the outcome is000000with probability given by∣α∣2/4+∣β∣2/4=14|\alpha|^2/4+|\beta|^2/4 = \frac{1}{4}∣α∣2/4+∣β∣2/4=41​,since∣α∣2+∣β∣2=1|\alpha|^2+|\beta|^2=1∣α∣2+∣β∣2=1(normalization condition for the original state). And the resulting conditional state for Bob isα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩,that is, just the original state to be teleported.

We can run through similar calculations for all four outcomes of the measurement in Alice's computational basis. The results are:

This is good news: in each case Bob's state is very similar to the original state∣ψ⟩|\psi\rangle∣ψ⟩to be teleported. The only thing wrong is the extra Pauli matrices in Bob's conditional states. But Bob can easily fix those.

To do the fix, recall that the Pauli matrices are self-inverse,XX=IXX = IXX=IandZZ=IZZ = IZZ=I.If we simply run through the four possibilities in the table above, we see that Bob can recover the original state by (in the respective cases): doing nothing; applying theXXXgate; applying theZZZgate; applyingZXZXZX.This is exactly what's done in the circuit described earlier.

That completes the verification that teleportation works.

Intuitively, one story you might tell yourself about why teleportation works is that somehow the measurement outcomes are “telling us something about the identity of the state to be teleported”, something that helps Bob put the state back together again.

While such a story seems appealing, it's wrong. Consider that the probabilities for the computational basis measurements are14\frac{1}{4}41​,no matter what the identity of the state wasContrast to a computational basis measurement of a state such asα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩,where the probabilities of the outcomes very strongly depend on the amplitudesα\alphaαandβ\betaβ,and so on the identity of the state.. Imagine a third party, Carol, eavesdropped on Alice and Bob's classical communication, and learned the results of Alice's measurements. Because the distribution of those measurement results doesn't depend in any way on the identity of the state∣ψ⟩|\psi\rangle∣ψ⟩,Carol would still be completely in the dark about the identity of∣ψ⟩|\psi\rangle∣ψ⟩.

Even after years of familiarity with teleportation, I still find this marvelous and surprising. What the measurement results are saying is purely how the state has been changed – to∣ψ⟩,X∣ψ⟩,Z∣ψ⟩|\psi\rangle, X|\psi\rangle, Z|\psi\rangle∣ψ⟩,X∣ψ⟩,Z∣ψ⟩,orXZ∣ψ⟩XZ|\psi\rangleXZ∣ψ⟩– without giving any information at all about the identity of∣ψ⟩|\psi\rangle∣ψ⟩.

There's no immediate further moral to this story. I'm mentioning it merely to help flesh out your appreciation for the teleportation protocol. (We'll do more in this vein a little later in the essay). Although the protocol is technically simple, it's very deep. Indeed, I believe there are still unsuspected depths in the protocol, ideas that no-one has yet fathomed.

One further fun fact about teleportation is that it doesn't matter where Bob is. In fact, Alice may not evenknowwhere Bob is – she can simply broadcast the classical bits out into the world, perhaps using a public address on the internet. Provided Bob can see those bits, he can recover the state∣ψ⟩|\psi\rangle∣ψ⟩.So teleportation is a kind of broadcast protocol.

We now have a basic picture of quantum teleportation, and have verified that it works. Let me summarize the key elements, followed by some questions reviewing those elements of the protocol not covered by earlier questions. The quantum circuit representation for teleportation is as follows:



In more descriptive prose, teleportation is achieved in four steps:

One final point: at the end of the teleportation protocol, Alice no longer possesses the quantum state∣ψ⟩|\psi\rangle∣ψ⟩.In particular, her computational basis measurement leaves her qubits in one of the four states,∣00⟩|00\rangle∣00⟩,∣01⟩|01\rangle∣01⟩,∣10⟩|10\rangle∣10⟩,or∣11⟩|11\rangle∣11⟩,corresponding to the result of her computational basis measurement. And so you shouldn't think of teleportation as copying the state∣ψ⟩|\psi\rangle∣ψ⟩,but rather as a way of moving the state.

Let's now review some questions covering those details of teleportation not covered by earlier questions. Note that I will ask several of the questions in closely related ways. This may seem redundant, but it's done because research on memory shows that encoding information in multiple related ways results in deeper and better memories being formed. This is the biggest batch of questions in the essay, and may take a couple of minutes to work through.

Quantum teleportation is different in several ways from what people ordinarily think of as teleportation, the kind of thing made famous byStar Trek.

For one thing, it's not about teleporting complex objects, like human beings. Rather, it's about teleporting elementary quantum systems. Although in principle it is possible to teleport much more complex objects, it seems extremely unlikely in the foreseeable future.

Another difference is that quantum teleportation is not about an object vanishing in one location and then reappearing instantaneously in another. It's essential that the classical information be sent, and that Bob performs the corresponding operations. This makes some people feel cheated: “it's not real teleportation!” While the name “quantum teleportation” is great marketing, it genuinely is a little misleading.

On the other hand, quantum teleportation is still astonishing. It's impossible to measure a quantum state to determine its amplitudes. Intuitively, that ought to make anything like quantum teleportation impossible. Yet, somehow, it is still possible to use measurement to transport a state from one location to another.

One of the originators of quantum teleportation, Asher Peres, was once asked by a reporter whether it is possible to teleport not only the [human] body but also the soul. Peres captured the essence of quantum teleportation beautifully when he replied “only the soul”Asher Peres,What is actually teleported?(2003).. Teleportation isn't really about transmitting objects over long distances. Rather, it's about a counter-intuitive way of disassembling an unknown quantum state into classical information, using a fixed shared state and measurement, and then later recovering the original quantum state. In lectures, another of the originators of teleportation, Charles Bennett, has sometimes illustrated this using an elegant informal inequality:





What this means, informally, is that one shared “ebit” (meaning the entangled state∣00⟩+∣11⟩2\frac{|00\rangle+|11\rangle}{\sqrt 2}2​∣00⟩+∣11⟩​)together with two classical bits of communication is enough to enable one quantum bit of communication. It's teleportation-expressed-as-an-inequality. Bennett sometimes combines this with inequalities expressing other quantum information processing protocols, and is able to develop a kind of algebra of what's possible. Not everyone finds this to their taste, but personally I find it a fun and stimulating way of thinking about what's going on.

Teleportation has been experimentally demonstrated in many systems, beginning in the late 1990s. The experiments have been somewhat contentious, with four separate teams claiming to be the first to “really” do teleportationD. Boschi, S. Branca, F. De Martini, L. Hardy, and S. Popescu,Experimental Realization of Teleporting an Unknown Pure Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels(1997); Dik Bouwmeester, Jian-Wei Pan, Klaus Mattle, Manfred Eibl, Harald Weinfurter, and Anton Zeilinger,Experimental Quantum Teleportation(1997); A. Furusawa, J. L. Sørensen, S. L. Braunstein, C. A. Fuchs, H. J. Kimble, and E. S. Polzik,Unconditional Quantum Teleportation(1998); M. A. Nielsen, E. Knill, and R. Laflamme,Complete quantum teleportation using nuclear magnetic resonance(1998).; each team adopted a somewhat different criterion for what it means to succeed. I'm not a disinterested observer: I was on one of the teams, and unsurprisingly I think our criterion was the best; others have different opinions. In the years since many more experiments have been done, improving the quality of the implementation, and also using teleportation as part of more complex quantum information processing protocols.

There are many variations of the quantum teleportation protocol. I've described the simplest version, one that works to teleport qubits. But it's worth knowing that it's possible to extend the protocol to more complex quantum systems. There are also variations which use a different state shared between Alice and Bob, different operations performed by Alice and Bob, and so on. The version of teleportation I've described is, however, the one people are usually referring to when they say “quantum teleportation”. If you want a fun challenge, you might try to find some variations on the protocol. For instance, can you find a way of teleporting a qubit using the shared state∣01⟩+∣10⟩2\frac{|01\rangle+|10\rangle}{\sqrt 2}2​∣01⟩+∣10⟩​?And are there other shared states you can find which can be used to do teleportation?

I've described how teleportation works, and we've verified that it does work. But it's still somewhat mysterious. How could you have come to discover teleportation in the first place? Why would you even suspect it's possible? Quantum mechanics took its near-modern form in the 1920s, and teleportation could have been discovered then. Certainly, more technically complex discoveries were made by physicists at the time. Yet, despite that, it wasn't discovered until 1993. Although technically rather simple, I believe teleportation wasn't discovered in part because it was conceptually unexpected. While I won't give a detailed answer to the question “what could lead you to discover teleportation”, if you're interested you may enjoythis Twitter thread, which provides a partial answer, and which should be possible to follow with the background in this essay.

Why does teleportation matter? While it's a simple protocol it opens up a world of questions, leading to new ideas and new applications. You could write a fun book containing nothing but ideas inspired by or building on teleportation. I won't survey all those here, but just to give you the flavor I will mention one line of development. I hope you pardon me, but it's something I played a small role in.

In 1997, Ike Chuang and IM. A. Nielsen and Isaac L. Chuang,Programmable Quantum Gate Arrays(1997).showed that it's not only possible to teleport quantum states, but by modifying the protocol it's possible to teleport quantumgatesfrom one location to another. Our gate teleportation protocol was stochastic, meaning it only worked some of the time, but in 1999, Chuang and Daniel GottesmanDaniel Gottesman and Isaac L. Chuang,Demonstrating the viability of universal quantum computation using teleportation and single-qubit operations(1999).pointed out that for some gates quantum gate teleportation could be made to work all the time.

This perhaps seems nice, but of mostly theoretical interest. However, in 2001 the scientists Manny Knill, Ray Laflamme, and Gerard MilburnE. Knill, R. Laflamme, and G. J. Milburn,A scheme for efficient quantum computation with linear optics(2001)., used quantum gate teleportation to show something unexpected. At the time, experts thought particles of light (photons) were likely to be a bad choice for use as qubits in quantum computers. While photons are in many ways excellent candidates to be qubits – it's easy to do many types of manipulation, and they're quite resistant to noise – there seemed to be no way of getting photons to interact to do a CNOT gate. But Knill, Laflamme, and Milburn found a beautiful way of teleporting the CNOT gate onto photons. This provided an in-principle (though initially very complex) way of building an optical quantum computer. That construction has since been simplified by many orders of magnitude, using yet more ideas related to teleportation. Today, there arestartup companiesworking toward optical quantum computers that build on this approach. Back in 1993, when teleportation was discovered, I doubt anyone anticipated that it would one day lead to new approaches to quantum computing. But teleportation is such a deep and powerful primitive that it keeps giving rise to new ideas, of which this is merely one example.

Thanks for reading. In the coming weeks, you’ll receive a notification containing a link to your first review session for this essay. In that review session you’ll be retested on the material you’ve learned, helping you further commit it to memory. It should only take a few minutes. In subsequent weeks you’ll receive more notifications linking you to re-review, gradually working toward genuine long-term memory of all the core material in the essay.

Concluding thought:Thanks for reading this account of quantum teleportation. If you’d like to remember the core ideas durably, please set up an account below. We’ll track your review schedule and send you occasional reminders containing links that will take you to the review experience.

Andy and Michael are supported in part through the generous contributions of ourPatreon supporters. Early work on this essay was supported byY Combinator Research. This essay is based in part on Michael’'s earlier lecture series onQuantum Computing for the Determined.

In academic work, please cite this as:

Authors are listed in alphabetical order.

This work is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported License. This means you’re free to copy, share, and build on this essay, but not to sell it. If you’re interested in commercial use, pleasecontact us.

November 12, 2019

See ourUser Agreement and Privacy Policy.


---

# Quantum mechanics distilled

Andy MatuschakandMichael Nielsen

Part of aseries of essaysin a mnemonic medium which makes it almost effortless to remember and apply what you read.

byAndy MatuschakandMichael Nielsen

Presented in a new mnemonic medium which makes it almost effortless to remember and apply what you read.

Our future projects are funded in part by readers like you.

Special thanks to our sponsor-level patrons,Adam Wiggins,Andrew Sutherland,Bert Muthalaly,Calvin French-Owen,Dwight Crow,fnnch,James Hill-Khurana,Lambda AI Hardware,Ludwig Petersson,Mickey McManus,Mintter,Patrick Collison, Paul Sutter,Peter Hartree,Sana Labs,Shripriya Mahesh,Tim O'Reilly.

— Albert Einstein, writing to a colleague in 1925

In fairy tales, a wizard will say the magic words of a spell, or inscribe a set of magic symbols, and the world will change. Fireballs shoot from their hands; the hero is revived from an endless slumber; a couple falls in love. We smile when we hear such stories. They seem quaint but implausible. Common sense tells us that merely speaking certain words, or inscribing certain symbols, cannot cause such changes in the world. And yet our scientific theories are not so different. By speaking the words or inscribing the symbols of such a theory, we can greatly deepen our understanding of the world. That new understanding then enables us to change the world in ways that formerly seemed impossible, even inconceivable. Consider quantum mechanics, one of our deepest theories. It has helped us create lasers, semiconductor chips, and magnetic resonance imaging. One day it will likely help us create quantum computers, perhaps even quantum intelligences. Quantum mechanics is magic that actually works.

In this essay, we explain quantum mechanics in detail. We will describe all the principles of quantum mechanics in depth, nothing held back. It's not a handy-wavy treatment, of the kind often found in articles written for a general audience. While such articles can be entertaining, trying to learn quantum mechanics by reading them is like learning to play basketball by merely watching basketball being played. This essay will get you out on the mathematical court of quantum mechanics. Of course, you won't learn to slam dunk, at least not yet. But the essay will ground you in an understanding of the fundamentals of quantum mechanics, which you can later build upon and extend.

To read the essay, you must first understand the quantum circuit model of quantum computation. If you're not familiar with quantum circuits, you can learn about them from our earlier essay,Quantum Computing for the Very Curious. You may wish to pause to read that essay now, if you haven't already. Once you've understood that material you shouldn't need any other prerequisites. Indeed, when you learned quantum computing, you learned in passing almost all of quantum mechanics. InPart Iof this essay we distill those past ideas, collecting them up into the package known as quantum mechanics.

Although quantum mechanics is not so difficult to learn, it's a theory which has disturbed many people. Here's a few classic quotes on this puzzlement:

I think I can safely say that nobody understands quantum mechanics … Do not keep saying to yourself, if you can possibly avoid it, “But how can it be like that?” because you will get “down the drain”, into a blind alley from which nobody has yet escaped. Nobody knows how it can be like that.– Richard Feynman

I have thought a hundred times as much about the quantum problems as I have about general relativity theory.– Albert Einstein

If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet.– Niels Bohr

If quantum mechanics is not so difficult to learn, why has it so disturbed many great physicists? What do they mean when they say they don't understand it, or are shocked by it? How can a scientific theory be both beautiful and disturbing? InPart IIof this essay we'll explore these questions. As we'll see, despite its simplicity quantum mechanics raises striking conceptual problems, problems which are among the most exciting open problems in science today.

The essay is presented in an unusual form. It's an example of what we call amnemonic essay, written in themnemonic medium. That means it incorporates new user interface elements intended to make it almost effortless for you to remember and apply the ideas in the essay. The motivator is that most people (ourselves included) quickly forget much of what we read in books and articles. The mnemonic medium takes advantage of what cognitive scientists know about how humans learn, creating an interface which ensures you'll remember the ideas and how to apply them near permanently. More on how that works below.

So, what is quantum mechanics? It's fun to wax poetic about it being magic that actually works, or to quote eminent scientists saying no-one really understands it. But while fun, those statements give no direct enlightenment. What is quantum mechanics, really?

Quantum mechanics is simply this: it's a set of four postulates that provide a mathematical framework for describing the universe and everything in it. These postulates reflect ideas you've already seen in the quantum circuit model: how to describe a quantum state; how to describe the dynamics of a quantum system; and so on. But rather than talk abstractly, it's better to just see the first postulate:

This may seem densely written, but you already know most of it. In particular, we've been working extensively with qubits, and we've seen this postulate in action. For a qubit the state space is, as you know, a two-dimensional complex vector space. The state is a unit vector in that state space (i.e., has length111). And the condition that the state vector is a unit vector expresses the idea that the probabilities for the outcomes of a computational basis measurement add up to111.

It's not just qubits that have a state space. The first postulate of quantum mechanics tells us thateveryphysical system has a state space. An atom has a state space; a human being has a state space; even the universe as a whole has a state space. Admittedly, the first postulate doesn't tell us what the state space is, for any given physical system. That needs to be figured out on a case-by-case basis. Different types of atoms have different state spaces; a human being has a different (and much more complicated) state space; the universe has a more complicated state space still.

As an example, suppose you're interested in what happens when you shine light on an atom. To give a quantum mechanical description, you'd need a state space to describe atoms and the electromagnetic field (i.e., light).A prioriit's not obvious what that state space should be. How many dimensions should the state space have? How do particular physical configurations of atoms and light correspond to states in that state space? By itself, quantum mechanics doesn't answer these questions. It merely does the subtle-but-important job of instructing you to look for answers to these questions. Fortunately, there is a theory, known as quantum electrodynamics (often shortened to QED), which describes how atoms and light interact. Among other things, QED tells us which states and state spaces to use to give quantum descriptions of atoms and light.

In a similar way, suppose we're trying to describe particles like quarks or the Higgs boson. Just as with the atoms-and-light example, quantum mechanics tells us we need figure out the right state spaces and state vectors. But it doesn't tell us what those are. In this case, the additional theory needed is the standard model of particle physics. Like QED, the standard model sits on top of basic quantum mechanics, fleshing it out, telling us things which aren't in the four postulates of quantum mechanics.

More generally, quantum mechanics alone isn't a fully specified physical theory. Rather, it's a framework to use to construct physical theories (like QED). It's helpful to think of quantum mechanics as analogous to an operating system for a computer. On its own, the operating system doesn't do all the user needs. Rather, it's a framework that accomplishes important housekeeping functions, creating a file system, a graphical display and interface, and so on. But users need another layer of application software on top of those basic functions. That application layer is analogous to physical theories like QED and the standard model. The application layer runs within the framework provided by the operating system, but isn't itself part of the operating systemThis analogy was popularized in Scott Aaronson's book “Quantum Computing Since Democritus”; MN believes Scott first heard it in atalkMN gave at the Fields Institute in Toronto in 2001. This wouldn't warrant mention, except when MN uses the analogy, people often respond “oh yes, that's Scott Aaronson's way of thinking about quantum mechanics”. MN doesn't recall where he first heard it, or if the description is original..

In this essay, we won't get deeply into QED or the standard model or the other theories physicists have developed to describe particular physical systems. Rather, our focus is on quantum mechanics itself – the four postulates. For examples, we'll mostly draw on the quantum circuit model, which makes simple and reasonable assumptions about state spaces and state vectors. This model is already an extremely rich arena for studying quantum mechanics. If you wish, you can learn later about QED, the standard model, and so on.

Of course, this means there is still much more to learn, beyond the scope of this essay. Each physical system requires learning its own particular set of recipes for state spaces and state vectors. You already know some such recipes: if we say “let's consider a 3-qubit system”, then we know the state space is just the 8-dimensional complex vector space spanned by the computational basis states∣0⟩∣0⟩∣0⟩|0\rangle|0\rangle|0\rangle∣0⟩∣0⟩∣0⟩,∣0⟩∣0⟩∣1⟩,…|0\rangle|0\rangle|1\rangle, \ldots∣0⟩∣0⟩∣1⟩,….By contrast, you probably don't know the recipe QED gives telling us how to construct the state space for a couple of hydrogen atoms interacting with the electromagnetic fieldA little more strictly speaking, QED tells us how charged elementary particles like electrons interact with the electromagnetic field. After QED was invented, atomic physicists and quantum opticians figured out how to use it to describe atoms and electromagnetic fields. And so the recipe you'd use would likely come from atomic physics or quantum optics.. While that recipe is different than in the three-qubit example, it's really much the same kind of thing. You learn the rules of the recipe, and then you can figure out the state spaces and quantum states.

Where do the recipes for things like the state space of an atom (or the electromagnetic field) come from? The unglamorous answer is that figuring those things out for the first time was incredibly hard. As in: Nobel prize hard, or even multiple Nobel prize hard. People made lots of guesses, tried lots of different things, trying to figure out states and state spaces (and all the other things), constructed lots of bad theories, and lots of good-but-not-good-enough theories along the way. And, eventually, they came up with some great recipes. Most of the time today we can use one of those recipes off-the-shelf. You go pick up a book about atomic physics, say, and it'll just tell you: use such-and-such a state space, and away you go. But in the background is thousands of instances of trial-and-error by often-frustrated physicists.

A point we've glossed over is the use of the termisolatedin the first postulate. In particular, the first postulate tells us thateveryphysical system has a state space, but inserts the qualifierisolatedwhen saying which physical systems have a state vector. By isolated we mean a system that's not interacting with any other system. Of course, most physical systems aren't isolated. An atom will interact with its surroundings (for instance, it may be hit by a photon, or perhaps be affected by the charge of a nearby electron). A human being isn't an isolated physical system either – we're constantly being bombarded by light, cosmic rays, and all sorts of other things.

In general such non-isolated systems don't have their own quantum state! In fact, we saw an example in theearlier essay. Suppose we use the following quantum circuit:





The output is the state:

∣00⟩+∣11⟩2.\frac{|00\rangle+|11\rangle}{\sqrt 2}.2​∣00⟩+∣11⟩​.

A good question to ask is: what is the state of the first qubit? But as discussed in theearlier essay, this is an entangled state of the two qubits, and there is no sensible way to assign a quantum state to the first qubitIn more advanced treatments you'll learn about an idea called the reduced density matrix, which can be used to describe part of an entangled quantum system. This is a useful mathematical tool derived from the four postulates we describe, but is not an essentially new idea. It's worth being aware of as a calculational convenience to learn about in the future, but discussing it is beyond our immediate scope..

Now, you might be bothered by this. Doesn't the circuit above start with the first qubit “in” the state∣0⟩|0\rangle∣0⟩?How does that square with the idea that a non-isolated system doesn't have a state? This is a good question, one we'll see how to address later, in the discussion of the fourth postulate.

Okay, that's the first postulate covered! Hopefully, you found it pretty easy. Perhaps you're wondering if that's all there is to it? Or perhaps some element of the postulate is bothering you because you feel we haven't unpacked it sufficiently and played it out.

It's fine if that's where you're at. Deeply understanding the consequences of the postulates is a lifetime's work. It is not, for instance, obvious from the postulates that phenomena such as quantum teleportation and quantum search are already implicit inside them. You have to work hard to see that! Indeed, if you believe the universe is quantum mechanical – as we do – then everything around you is implicit in the postulates: the colors of the rainbow; the shape of a mountain; the touch of the wind. And so in learning the postulates you are learning the starting rules of an extraordinarily complex game. But unlike an ordinary game, the stakes are not winning or losing; rather, they are about how the universe actually is.

This essay is an example of what we call a mnemonic essay. That means it incorporates new interface elements intended to make it almost effortless for you to remember and apply the content of the essay, over the long term. The idea is this: throughout the essay we occasionally pause to ask a few simple questions, testing you on the material just explained. In the weeks ahead we'll re-test you in followup review sessions. By carefully expanding the testing schedule, we can ensure you consolidate the answers into your long-term memory, while minimizing the review time required. The review sessions take no more than a few minutes per session, and we'll notify you when you need to review. The benefit is that instead of remembering how quantum mechanics works for a few hours or days, you'll remember for years. It'll become a much more deeply internalized part of your thinking. This long-term internalization is particularly valuable for the core ideas of quantum mechanics, which are at the foundation of many other subjects.

Of course, you can just read this as a conventional essay. But we hope you’ll try out the mnemonic medium. To do so please sign up below. This will enable us to track the best review schedule for each question, and to remind you to sign in for occasional short review sessions. And if you’d like to learn more about how the mnemonic medium works, please seeA medium which makes memory a choice,How to approach this [earlier] essay?, andHow to use (or not use!) the questions.

To give you a more concrete flavor of how the mnemonic medium works, let's look at three questions reviewing part of what you've just learned. Please indulge us by answering these questions – it'll take just a few seconds. For each question, think about what you believe the answer to be, click to reveal the actual answer, and then mark whether you remembered or not. If you can recall, that's great. But if not, that's fine, just mentally note the correct answer, and continue.

The first postulate of quantum mechanics told us how we describe states. What about how states change, that is, the dynamics of a quantum system? That's where the second postulate comes in. In theearlier essaywe saw that quantum gates are described by unitary matrices acting on the state space of a quantum system. The second postulate tells us that something very similar is true for any isolated quantum system:

Our quantum gates demonstrate this postulate in action. So, for instance, the PauliXXXgate, also known as the quantum NOT gate, is an example. Here it is shown in the quantum circuit and matrix representations, as well as the explicit action on states:





So too is the Hadamard gate,HHH:





And so on, through the controlled-NOT gate, the Toffoli gate, and all the other quantum gates we met earlier.

Why is it unitary matrices which appear in the second postulate? If you try writing a few matrices down on paper, you quickly find that most matrices aren't unitary, or even close to it. Why can't we have a general matrix in the second postulate? One partial explanation, discussed indepthin the earlier essay, is that unitary matrices are the only matrices which preserve length. If we want the quantum state to remain normalized, then unitary matrices are the only matrices which do the trick, since any other matrix will result in the norm changing. That normalization is in turn connected to the requirement that the probabilities of measurement outcomes sum to one. In this sense, the postulates of quantum mechanics form a tightly interconnected web, with requirements like unitarity from one postulate reflecting requirements elsewhere, like normalization of the state vector, or probabilities summing to one.

How to figure out which unitary transformation is needed to describe any particular physical situation? As you might guess from our discussion of the first postulate, the second postulate is silent on this question. It needs to be figured out case by case. Theories like QED and the standard model supply additional rules specifying the exact (unitary) dynamics of the systems they describe. It's as before: quantum mechanics is a framework, not a complete physical theory in its own right. But being told that the correct way to describe dynamics is using unitary transformations on state space is already an incredibly prescriptive statement. And, as before, the quantum circuit model is a useful source of examples, and working with it is a good way to build intuition.

More broadly: although quantum mechanics reached its final form in the 1920s, physicists spent much of the remainder of the twentieth century figuring out what unitary dynamics, state spaces, and quantum states are needed to describe this or that system. You can't just solve this problem once: optical physicists had to do it for light, atomic physicists for atoms, particle physicists have been doing it for the entire pantheon of particles described in the standard model of particle physics. Still, although there's much more to learn about the application of these two postulates, already they give us a remarkably constraining framework for thinking about what the worldisand how it canchange.

Let's pause and run through some more questions:

If you've read earlier essays in this series, you may recall that we described the mnemonic medium as making it almost effortless to remember the essay contents. We believed this would make it much easier to deeply understand the material. To figure out how well or poorly the medium was working, we interviewed many users. Many of the conversations started out encouragingly: “Yeah, I can remember the content for a long time. And it's weird and fun that it's almost effortless”. So far, so good. But when we dig into how well people understand the material, a pretty common line is: “Before using the mnemonic medium, I didn't think memory was all that important to understanding. I've changed my mind about that: it helps much more than I thought. But it's not a panaceaOf course, this isn't a real quote, just a synthesis. No-one actually said “panacea”!either. For instance, I'm not sure I really understand the Hadamard gate. Yeah, I know quite a bit about the gate, and it's remarkable to remember all that. But I'm not sure I coulduseit in another context. And I'm not sure I could explain it to someone else. It somehow falls short of a full understanding.”

They're right that memory is only part of understanding. Understanding also involves many other skills, among them the ability to use what you've learned in new contexts. And so in this essay we're extending the mnemonic medium to include questions where we ask you to apply what you've learned. Here's an example question:

At first glance that looks much like earlier cards. But in important ways it's different. When you do review sessions in the future youwon'tsee that particular question again. Instead, you'll see variation questions that are similar, but not quite the same. We'll cheat a bit now, and show you two variants that you'll see in future review sessions. We won't ask you to work these out here – in fact, it's probably best if you actively refrain from thinking too hard about these questions! Just take a look, and notice that they're asking you to solve the same kind of very simple problem as in the question above:

So this is different to the earlier cards, in that we're not asking you to remember the answer to the question. Rather, we're asking you to work out an answer to the question, which is very different. That is, we're asking you to use the understanding that you've gained. Furthermore, it's not just these three variations: you'll be asked a whole sequence of variations.

Our hope and expectation is that this will enable you to gradually internalize not just declarative knowledge, but also procedural knowledge. In this way, you'll learn to reliably transfer your understanding to new contexts.

If you're familiar with conventional spaced repetition flashcard software, then you know that this kind of process knowledge isn't something it's designed to support. Such systems are certainly not designed for multiple variations on a question, testing the ability to fluently apply understanding in new contexts. This is a small design change, but we believe it greatly expands the type of learning the mnemonic medium supports, and will result in a qualitative jump in what you get from the medium.

Over the longer term, there are umpteen ways the medium could be greatly improved, or radically changed. We think of these experiments as part of developing an answer to the question: what's an ideal, very high-growth personal environment? Of course, we're a long way from having developed such an environment! When we talk with people about the mnemonic medium, they sometimes described it as an educational experiment. This is a limited ambition, as education is commonly conceived. Imagine taking a month of public speaking lessons in school. Now compare that to a situation where you've been asked to present onstage at a major Apple product launch, and will have a team of people from Apple helping you practice for a month. Which do you think would be a higher growth environment? This is a fanciful example, but illustrates the point: there's tremendous scope to develop extraordinarily high-growth environments. This medium is one (tiny) experiment in exploring that scope, and we hope to develop many more such ideas in the future. But for now we'll explore the limits of the current medium.

Alright, let's get back to quantum stuff. Here's a couple more examples:

To reiterate, in future review sessions you'll be asked small variations on the questions above. You can't simply memorize the answers, since you won't be shown the questions again. Rather, you must work them out.

You may notice that in the second of the above questions there was an explanation available. You aren't being tested on these explanations, they're just intended to help out if you get stuck. In particular, it doesn't matter if you use the same approach as described in the explanation – anything which gives the correct answer is good.

Let's return to the details of the second postulate. You probably noticed that, like the first postulate, it contained a caveat about describing the dynamics ofisolatedsystems using unitary matrices. Of course, in nature most physical systems aren't isolated or even near-isolated. Suppose, for instance, you're trying to build a quantum computer, using atoms to store the states of your qubits. For instance, we could use two different orbital shells for an electron to correspond to the∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩states. And suppose you effect a quantum gate by briefly shining laser light on the atom, causing the electron to move between the shells.

Such an atom is not isolated: it's interacting strongly with the laser. But it turns out the dynamics of the atom are still closely described by a unitary transformation, even when laser light is being shone on it. This isn't obvious; it requires detailed investigation. But the upshot is that while the second postulate only directly applies to isolated systems, surprisingly often it's possible to describe the dynamics of non-isolated systems by unitary dynamics. Indeed, when we said above that quantum gates are examples of the second postulate, that's not quite right. Usually, quantum gates involve non-isolated systems. But with careful design they implement unitary operations anyway.

Let's also work through a few questions where you're asked to apply what you've learned. For these questions we'll return to the first postulate, since we didn't have any questions in that style in our earlier discussion, and it's useful being able to apply those ideas.

We presented the second postulate in the form most often used in quantum circuit contexts, with discrete gates being applied to cause discrete changes in the quantum state. We'll now briefly show you an alternate form, in which the evolution of the quantum state varies smoothly in continuous time, with the change described by a differential equation. We're not going to use this much, and so you don't need to understand all the details in depth – this is just so you get the gist. Here's the equation controlling the time rate of change of the quantum state:

id∣ψ⟩dt=H∣ψ⟩.i \frac{d|\psi\rangle}{dt} = H |\psi\rangle.idtd∣ψ⟩​=H∣ψ⟩.

This equation is known as theSchroedinger equation. The matrixHHHis a (fixed) hermitian matrix known as theHamiltonianof the system. (This isnotthe same as the Hadamard gate, it's merely an unfortunate notational coincidence). You can think of the HamiltonianHHHas telling the quantum state how to change. The Schroedinger equation thus provides a continuous-time description of the dynamics of the quantum state, whereas the second postulate was focused on a discrete time description.

By solving the Schroedinger equation we can relate the state of the system at timet2t_2t2​to the state at timet1t_1t1​.The solution is:

∣ψt2⟩=e−iH(t2−t1)∣ψt1⟩.|\psi_{t_2}\rangle = e^{-iH(t_2-t_1)} |\psi_{t_1}\rangle.∣ψt2​​⟩=e−iH(t2​−t1​)∣ψt1​​⟩.

Of course, while it's easy enough to write down the matrix exponential, it is often quite a bit of work to compute in practice!

Traditional treatments of quantum mechanics spend a lot of time discussing Hamiltonians used to describe different physical systems, and figuring out (often rather tediously) the value of the matrix exponential. These are important and worthy technical problems, but not necessary for understanding the fundamentals of quantum mechanics. Still, it's worth noting that the above solution is consistent with the second postulate: in particular, it can be shown thate−iH(t2−t1)e^{-iH(t_2-t_1)}e−iH(t2​−t1​)is a unitary matrix. Indeed, if you're wondering about questions like “where does that factoriiicome from in the Schroedinger equation” or “why is the HamiltonianHHHrequired to be Hermitian”, they turn out to be required to get unitary evolution. So it all hangs together nicely. In fact, there's also an informal argument which lets you turn the second postulate around and (with a few extra assumptions) derive the Schroedinger equation. We won't get into details here, but it seems worth being aware this is possible.

What is worth taking away from this discussion is a few basics: the term Hamiltonian, what the Schroedinger equation does, qualitatively, and a broad feel for how the Schroedinger equation relates to the second postulate. We won't ask you to remember the details of the Schroedinger equation – those really need to be unpacked in more depth, and with some detailed examples. On the other hand, it is valuable to know what the Schroedinger equation does: it describes the time rate of change of the quantum state of an isolated physical system. The questions below are somewhat outside the main scope of this essay. But they're included here so that if in later reading you come across terms like “Hamiltonian”, you'll have a basic understanding to build upon.

The third postulate is the strangest of the postulates of quantum mechanics. To explain its content, it helps to recap fromQuantum Computing for the Very Curious:

In the earlier essay we describedmeasurement in the computational basis. That process governs how you get information out of a quantum computer. Recall the simplest version, measuring just a single qubit in the computational basis. In that process, if you measure a qubit in the stateα∣0⟩+β∣1⟩\alpha|0\rangle+\beta|1\rangleα∣0⟩+β∣1⟩then you get the outcome000with probability∣α∣2|\alpha|^2∣α∣2and the outcome111with probability∣β∣2|\beta|^2∣β∣2.The posterior state in the two cases is∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩,respectively.

The third postulate generalizes this idea of measurement:

There's a lot going on in this postulate. But again it mostly expresses ideas we've already seen, albeit disguised. We'll give a concrete example in a moment, but first want to address the meaning of the completeness relation. It simply expresses the idea that probabilities sum to111.We can see this by pre-multiplying the completeness relation by⟨ψ∣\langle \psi|⟨ψ∣and post-multiplying by∣ψ⟩|\psi\rangle∣ψ⟩.Comparing with the equation for the probabilityp(m)p(m)p(m)we see this gives

∑mp(m)=∑m⟨ψ∣Mm†Mm∣ψ⟩=⟨ψ∣I∣ψ⟩=⟨ψ∣ψ⟩=1,\sum_m p(m) = \sum_m \langle \psi|M_m^\dagger M_m|\psi\rangle = \langle \psi| I |\psi\rangle = \langle \psi|\psi\rangle = 1,m∑​p(m)=m∑​⟨ψ∣Mm†​Mm​∣ψ⟩=⟨ψ∣I∣ψ⟩=⟨ψ∣ψ⟩=1,

where we assumed∣ψ⟩|\psi\rangle∣ψ⟩is a quantum state, and thus normalized to have length111.

To understand the meaning of the third postulate, it helps to work through the particular case of measuring a single qubit in the computational basis. In that case, the measurement operators areM0=∣0⟩⟨0∣M_0 = |0\rangle \langle 0|M0​=∣0⟩⟨0∣andM1=∣1⟩⟨1∣M_1 = |1\rangle \langle 1|M1​=∣1⟩⟨1∣.It's easiest to apply the third postulate if we write out explicit amplitudes for the quantum state,∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha|0\rangle + \beta|1\rangle∣ψ⟩=α∣0⟩+β∣1⟩.According to the third postulate, the probability for result000is:

p(0)=⟨ψ∣M0†M0∣ψ⟩=⟨ψ∣0⟩⟨0∣0⟩⟨0∣ψ⟩.\begin{aligned} p(0) & = \langle \psi| M_0^\dagger M_0 |\psi\rangle \\ & = \langle \psi|0\rangle \langle 0| 0\rangle \langle 0| \psi\rangle. \end{aligned}p(0)​=⟨ψ∣M0†​M0​∣ψ⟩=⟨ψ∣0⟩⟨0∣0⟩⟨0∣ψ⟩.​

Of course,∣0⟩|0\rangle∣0⟩is normalized and so⟨0∣0⟩=1\langle 0|0\rangle = 1⟨0∣0⟩=1,and this becomes:

p(0)=⟨ψ∣0⟩⟨0∣ψ⟩=∣⟨0∣ψ⟩∣2.\begin{aligned} p(0) & = \langle \psi|0\rangle \langle 0| \psi\rangle = |\langle 0|\psi\rangle|^2. \end{aligned}p(0)​=⟨ψ∣0⟩⟨0∣ψ⟩=∣⟨0∣ψ⟩∣2.​

But⟨0∣ψ⟩=α\langle 0|\psi\rangle = \alpha⟨0∣ψ⟩=α,and so this tells us the probability of measurement outcome000isp(0)=∣α∣2p(0) = |\alpha|^2p(0)=∣α∣2,just as we expected. The exact same calculation, but with000sreplaced by111s, shows us thatp(1)=∣β∣2p(1) = |\beta|^2p(1)=∣β∣2,also as expected.

What about the posterior states? Let's consider the case of measurement resultm=0m = 0m=0.In that case the third postulate tells us the posterior state is

∣0⟩⟨0∣ψ⟩p(0).\frac{|0\rangle \langle 0|\psi\rangle}{\sqrt{p(0)}}.p(0)​∣0⟩⟨0∣ψ⟩​.

We've already seenp(0)=∣α∣2p(0) = |\alpha|^2p(0)=∣α∣2.And, of course,⟨0∣ψ⟩=α\langle 0|\psi\rangle = \alpha⟨0∣ψ⟩=α.And so the posterior state is:

α∣α∣∣0⟩.\frac{\alpha}{|\alpha|} |0\rangle.∣α∣α​∣0⟩.

This is a peculiar looking state! The pre-factorα/∣α∣\alpha/|\alpha|α/∣α∣appears complicated, but it's just a global phase factor. Back inQuantum Computing for the Very Curiouswe observed that such global phase factors never affect measurement probabilities, and as a result it's conventional to regard quantum states which differ only by a global phase factor as identical. And so the state above can be regarded as equivalent to the quantum state∣0⟩|0\rangle∣0⟩,just as we expected for a measurement in the computational basis. In a similar fashion, we can show that the posterior state if the measurement result was111is∣1⟩|1\rangle∣1⟩(again, up to a global phase factor, which we ignore).

The argument for ignoring global phase factors inQuantum Computing for the Very Curiouswas hand wavy. In fact, the postulates can be used to make the argument watertight. Suppose we have two quantum states related by a global phase factor,∣ψ′⟩=eiθ∣ψ⟩|\psi'\rangle = e^{i\theta}|\psi\rangle∣ψ′⟩=eiθ∣ψ⟩.Then the measurement probabilities for the two states are always identical:

p′(m)=⟨ψ′∣Mm†Mm∣ψ′⟩=⟨ψ∣Mm†Mm∣ψ⟩=p(m).p'(m) = \langle \psi'| M_m^{\dagger} M_m |\psi'\rangle = \langle \psi|M_m^\dagger M_m |\psi\rangle = p(m).p′(m)=⟨ψ′∣Mm†​Mm​∣ψ′⟩=⟨ψ∣Mm†​Mm​∣ψ⟩=p(m).

And, although we won't show it explicitly, the global phase factor also propagates unchanged through both unitary dynamics and posterior state calculations. And so such a phase factor makes no difference at all to anything observable. In fact, people sometimes re-state the postulates using a different formulation which entirely eliminates such global phase factors. The reason we haven't done this is that it significantly complicates the presentation. It's easier and also more conventional to just use the informal argument we've made.

Incidentally, you may wonder what happens in the third postulate when the denominator⟨ψ∣Mm†Mm∣ψ⟩\sqrt{\langle \psi|M_m^\dagger M_m|\psi\rangle}⟨ψ∣Mm†​Mm​∣ψ⟩​in the posterior state vanishes. Wouldn't that make the posterior state undefined? Fortunately, that can only happen if the probability of the measurement outcome is zero. That also means the measurement outcome will never occur, so we don't need to worry about it.

We've gone through a lot of work just to analyze a single quantum measurement! The good news is that we rarely need to go through such work. Instead, you build up a library of common patterns for measurement operators. Indeed, in quantum computing you'll mainly be interested in measurements in the computational basis. And there are a few other common measurements as well, some of which we'll talk about later in the essay. In practice, you only rarely need to do calculations like those above.

Let's run through a few questions testing your memory of the third postulate. These may be more challenging than earlier questions, and you may find it helpful to first return to the statement of the third postulate, and check that you understand it. This is the most detailed part of the essay – if you can get past it, you're over the main hump.

Let's also work through a couple of cards giving you practice computing the outcomes of measurements in the computational basis:

Let's introduce a new type of measurement, one we haven't seen in any earlier essays. It's a single-qubit measurement, but not a measurement in the computational basis. Recall the equal superposition states:

∣+⟩=∣0⟩+∣1⟩2;∣−⟩=∣0⟩−∣1⟩2.|+\rangle = \frac{|0\rangle+|1\rangle}{\sqrt 2}; \,\,\,\,\,\, |-\rangle = \frac{|0\rangle-|1\rangle}{\sqrt 2}.∣+⟩=2​∣0⟩+∣1⟩​;∣−⟩=2​∣0⟩−∣1⟩​.

The measurement we'll now define is what people call “measuring in the∣+⟩,∣−⟩|+\rangle, |-\rangle∣+⟩,∣−⟩basis”. In particular, we define measurement operatorsM+=∣+⟩⟨+∣M_+ = |+\rangle\langle +|M+​=∣+⟩⟨+∣andM−=∣−⟩⟨−∣M_- = |-\rangle \langle -|M−​=∣−⟩⟨−∣.We won't work through the details of the calculation, but if you wish you can check the completeness relationM+†M++M−†M−=IM_+^\dagger M_+ + M_-^\dagger M_- = IM+†​M+​+M−†​M−​=I.Making this check is just a little matrix calculation. What we're going to focus on is understanding the measurement probabilities and posterior states.

It's tempting – in fact, it's a good idea! – to begin by expanding the state being measured as∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha |0\rangle+\beta |1\rangle∣ψ⟩=α∣0⟩+β∣1⟩.If you do this, you can push through and figure out the measurement probabilities and posterior states. But there's a trick you can use to simplify matters. It's worth pausing a moment, and seeing if you can think of what that trick might be. Any ideas?

The trick is this: it's to observe that we could equally well have expanded∣ψ⟩|\psi\rangle∣ψ⟩in terms of the∣+⟩|+\rangle∣+⟩and∣−⟩|-\rangle∣−⟩states, as∣ψ⟩=γ∣+⟩+δ∣−⟩|\psi\rangle = \gamma|+\rangle + \delta|-\rangle∣ψ⟩=γ∣+⟩+δ∣−⟩.We can certainly do this, since∣+⟩|+\rangle∣+⟩and∣−⟩|-\rangle∣−⟩are linearly independent (in fact, orthonormal) states in a two-dimensional vector space. Can you now guess what the measurement probabilities and posterior states are, by analogy with measurement in the computational basis?

We'll work through the explicit calculation in a moment, but it's worth stating the result up front: the probability of the+++outcome is∣γ∣2|\gamma|^2∣γ∣2,with posterior state∣+⟩|+\rangle∣+⟩,and the probability of the−-−outcome is∣δ∣2|\delta|^2∣δ∣2,with posterior state∣−⟩|-\rangle∣−⟩.This is much like the computational basis measurement, and the calculation showing it is much like the calculation earlier for the computational basis measurement. In particular, for the+++measurement we have:

p(+)=⟨ψ∣M+†M+∣ψ⟩=(γ∗⟨+∣+δ∗⟨−∣)∣+⟩⟨+∣+⟩⟨+∣(γ∣+⟩+δ∣−⟩).p(+) = \langle \psi| M_+^\dagger M_+ |\psi\rangle = (\gamma^* \langle +|+\delta^*\langle -|) |+\rangle \langle +|+\rangle \langle +|(\gamma |+\rangle+\delta|-\rangle).p(+)=⟨ψ∣M+†​M+​∣ψ⟩=(γ∗⟨+∣+δ∗⟨−∣)∣+⟩⟨+∣+⟩⟨+∣(γ∣+⟩+δ∣−⟩).

Of course,⟨+∣+⟩=1\langle +|+\rangle = 1⟨+∣+⟩=1.And, in case you've forgotten, a quick calculation shows⟨+∣−⟩=0\langle +|-\rangle = 0⟨+∣−⟩=0,i.e., the∣+⟩|+\rangle∣+⟩and∣−⟩|-\rangle∣−⟩states are orthogonal. So the above becomes:

p(+)=(γ∗⟨+∣+δ∗⟨−∣)∣+⟩⟨+∣(γ∣+⟩+δ∣−⟩)=∣γ∣2.\begin{aligned} p(+) & = (\gamma^* \langle +|+\delta^*\langle -|) |+\rangle\langle +| (\gamma |+\rangle+\delta |-\rangle) \\ & = |\gamma|^2. \end{aligned}p(+)​=(γ∗⟨+∣+δ∗⟨−∣)∣+⟩⟨+∣(γ∣+⟩+δ∣−⟩)=∣γ∣2.​

A similar but simpler calculation showsM+∣ψ⟩=γ∣+⟩M_+ |\psi\rangle = \gamma|+\rangleM+​∣ψ⟩=γ∣+⟩,and so the corresponding posterior state isγ/∣γ∣∣+⟩\gamma/|\gamma| |+\rangleγ/∣γ∣∣+⟩,which up to a global phase factor is the∣+⟩|+\rangle∣+⟩state. Similar calculations show that the probability of a−-−outcome is∣δ∣2|\delta|^2∣δ∣2,with posterior state∣−⟩|-\rangle∣−⟩(up to a global phase). In practice we just say the posterior states are∣+⟩|+\rangle∣+⟩and∣−⟩|-\rangle∣−⟩,respectively.

What would have happened if instead we'd stuck with∣ψ⟩=α∣0⟩+β∣1⟩|\psi\rangle = \alpha|0\rangle+\beta|1\rangle∣ψ⟩=α∣0⟩+β∣1⟩?The calculation would have been a little more complicated, but of course we would have gotten the same result in the end, albeit expressed in terms ofα\alphaαandβ\betaβinstead ofγ\gammaγandδ\deltaδ.

We've been asking you to guess or intuit many results. If you successfully guessed the answers that may have been fun, but if not it may have been frustrating. If you'll allow us to generalize, people who've been raised in a culture that values “quick” and “smart” sometimes feel bad if they can't solve this kind of problem. This is unfortunate. Much of getting good at mathematics or physics is how you respond to this kind of stuckness. Superb mathematicians get stuck in similar ways, sometimes on things which later may seem headslappingly obvious. But they develop lots of heuristics for trying new things, even when stuck; and for keeping morale up. Developing that ability to continue when stuck is a crucial part of learning to do mathematics or physics.

There's an alternate way of looking at the third postulate where it appears almost to be a generalization of the second postulate. Suppose we were to do a measurement with just a single measurement outcome. That sounds peculiar – if a measuring device always showed the same answer you'd think it was broken – but it at least makes logical sense. According to the third postulate such a measurement would be described by a single measurement operator, which we can just callMMM(no label needed, since the outcome is always the same).

In this situation the completeness relation becomesM†M=IM^\dagger M = IM†M=I.That's just the condition thatMMMbe unitary. And, of course, the probability of the outcome would be⟨ψ∣M†M∣ψ⟩=⟨ψ∣I∣ψ⟩=1\langle \psi|M^\dagger M |\psi\rangle = \langle \psi|I|\psi\rangle = 1⟨ψ∣M†M∣ψ⟩=⟨ψ∣I∣ψ⟩=1,so that outcome would occur with probability111,i.e., all the time. This is as we'd expect, given that there is only one possible outcome! So the second postulate appears to be a special case of the third postulate where there is just a single outcome.

We say “appears”. It's not quite as simple as that. After all, the third postulate is talking about a system which is being measured, presumably by interacting with some measuring device, while the second postulate is talking about the dynamics of isolated physical systems. So the two postulates are talking about quite distinct physical situations. To say the second postulate is a special case of the third it's not enough for the mathematics to check out: you need a unified and conceptually sensible physical picture too. Still, you can imagine trying to reformulate the postulates so that the second and third postulates are unified aspects of a single postulate. It's fun to try to find conceptual unifications making that work. We don't do it here, but you may enjoy pondering how to do it.

We're almost done! The fourth postulate is the final postulate of quantum mechanics. It's also the easiest to understand. Remember that the first postulate told us that quantum systems have state spaces. Suppose we take two quantum systems,AAAandBBB.What's the state space of the combined system containing bothAAAandBBB?The fourth postulate tells us the answer to this question. It involves the use of an idea from linear algebra known as thetensor product, which we haven't explicitly met before. We'll discuss the tensor product more below; for now, let's see the postulate.

We've already met many examples of this postulate, when we worked with many-qubit systems in the earlier essays. For instance, we dealt with two-qubit states like:

∣00⟩+∣11⟩2.\frac{|00\rangle+|11\rangle}{\sqrt 2}.2​∣00⟩+∣11⟩​.

If you read thequantum search essay, then in that essay we dealt withnnn-qubit systems. So, implicitly we've already worked quite a bit with the tensor product. Sometimes people will write states like∣00⟩|00\rangle∣00⟩as∣0⟩⊗∣0⟩|0\rangle \otimes |0\rangle∣0⟩⊗∣0⟩,and speak of “the tensor product of∣0⟩|0\rangle∣0⟩and∣0⟩|0\rangle∣0⟩”. (The symbol⊗\otimes⊗is known as the tensor product symbol.) In fact,∣00⟩,∣0⟩∣0⟩|00\rangle, |0\rangle|0\rangle∣00⟩,∣0⟩∣0⟩and∣0⟩⊗∣0⟩|0\rangle \otimes |0\rangle∣0⟩⊗∣0⟩are all just different notations for exactly the same thing. This proliferation of notations can seem a little confusing at first, but it's worth remembering that∣00⟩=∣0⟩∣0⟩=∣0⟩⊗∣0⟩|00\rangle = |0\rangle|0\rangle = |0\rangle \otimes |0\rangle∣00⟩=∣0⟩∣0⟩=∣0⟩⊗∣0⟩.

There is, of course, a formal definition for the tensor product of two vector spaces. We thought about including that formal definition here, but decided against it. If you're bothered, you might pause for a moment to consider how comfortable you feel with the natural numbers1,2,3,…1, 2, 3, \ldots1,2,3,….Chances are you didn't begin your acquaintance with the natural numbers with a rigorous definition. Rather, you probably used the numbers for years before ever seeing a definition (if you ever saw such a definition). In the same way: we believe you learn more about the tensor product by working through things like quantum circuits, the quantum search algorithm, and quantum teleportation than by working through a formal definition.

There are a couple of additional elements left implicit in the fourth postulate – physicists sometimes regard these elements as so obvious as to not merit mentioning. We'd like to mention them here. They're best illustrated concretely. Suppose we apply a quantum gate like the Hadamard gateHHHto the first qubit in a quantum circuit:





Usually, we think of the Hadamard gate as a2×22 \times 22×2unitary matrix,

H=12[111−1].H = \frac{1}{\sqrt 2} \left[ \begin{array}{cc} 1 & 1 \\ 1 & -1 \end{array} \right].H=2​1​[11​1−1​].

But in the context of a two-qubit circuit like that shown above, the gate must somehow be acting on the entire four-dimensional state space. Mathematically, we define thetensor productoperationH⊗IH \otimes IH⊗I.This does what you'd guess: it acts on tensor product states∣ψ⟩⊗∣ϕ⟩|\psi\rangle \otimes |\phi\rangle∣ψ⟩⊗∣ϕ⟩by lettingHHHact on the∣ψ⟩|\psi\rangle∣ψ⟩piece, and the2×22 \times 22×2identityIIIact on∣ϕ⟩|\phi\rangle∣ϕ⟩.Writing this all out very explicitly, it just means that the Hadamard gate acts on the two-qubit system exactly as we expect:

(H⊗I)(∣ψ⟩⊗∣ϕ⟩)=(H∣ψ⟩⊗∣ϕ⟩).(H \otimes I)(|\psi\rangle \otimes |\phi\rangle) = (H|\psi\rangle \otimes |\phi\rangle).(H⊗I)(∣ψ⟩⊗∣ϕ⟩)=(H∣ψ⟩⊗∣ϕ⟩).

Similar ideas apply more generally. For instance, if the Hadamard gate had acted on the second qubit instead, the operation on the entire state space would have beenI⊗HI \otimes HI⊗H,and we're sure you can figure out how that would be defined!

Much more generally still, when we apply unitary matrices or measurement operators to a system which is part of a larger quantum system, we extend the relevant unitary matrices and measurement operators by tensoring with the identity matrix acting on the state space for the rest of the system. It's worth knowing that this is implicitly (and sometimes explicitly) what's going on.

You've now seen quantum mechanics in its entirety! Let's briefly sum up what it does and does not do.

It does a few things: it tells us what a quantum state is, it tells us where quantum states live (state space), it tells us how they change, both when the system is isolated (unitary dynamics) and when it's measured (measurement operators). And it tells us how the state space of a composite physical system relates to the component systems. The exact details – what state, what state space, what unitary dynamics or measurement operators – need to be figured out case by case. That's additional to the core content of quantum mechanics. Here's that core content in a single diagram:



All the mathematical ideas are simple. But they're nota prioriobvious. Still, once the framework has been discovered, it's easy to use. If you're confident you understand all the elements of that diagram, then you're confident you understand quantum mechanics.

In a similar vein, it's possible to summarize in just a few lines thequantum computing model,the quantum search algorithm, andquantum teleportation. If you understand all those summaries, then you've got a good mastery of the core of quantum computing, quantum mechanics, and two deep applications of those subjects. It's worth examining the summaries, and asking yourself where you're comfortable – pausing to appreciate your achievement – and also to identify spots where you're uncomfortable, and to think about how you might improve your understanding, perhaps through re-reading.

We'll conclude Part I with a few questions that integrate what we've covered. In Part II we finish offQuantum Countryby discussing what makes quantum mechanics such a strange theory, and some major open scientific challenges it reveals.

If quantum mechanics is just four easily-understood postulates, then why did Richard Feynman say “nobody understands quantum mechanics”? What was Einstein referring to when he said he'd thought “a hundred times” as much about the quantum problems as about general relativity? What had them so upset?

On the one hand, no matter what Feynman says, tens of thousands of people genuinely understand quantum mechanics. They understand it well enough to use it to design and build new devices – for instance, quantum mechanics played a crucial role in developing the first transistor, and nowadays is a working tool for anyone thinking seriously about semiconductors. Or consider the tens of thousands of people who understand quantum search and quantum teleportation. All these people certainly understand quantum mechanics.

On the other hand, Feynman wasn't a yo-yo. When people say no-one understands quantum mechanics, they're using “understand” in an unconventional but meaningful sense. In particular, there are a few fundamental puzzles about the meaning of the theory that have never been entirely resolved, despite decades of thought. In Part II of this essay, we explain one of these puzzles in detail, the Bell inequality. And we'll briefly survey some of the other puzzles about quantum mechanics, and consider what would be entailed by a deeper understanding of the theory.

— Henry Stapp

— Albert Einstein

Suppose someone flips a coin, letting it land on their arm, but covers it up before you have a chance to see it. You will, naturally, model the state of the coin as being either heads or tails. And while that state is not immediately accessible to you (at least, not until they move their hand), you certainly assume that the coin has an objective state which could in principle be measured.

This all sounds rather trite. But it's actually not obvious that the same thing is true in quantum mechanics. Suppose you have a qubit in some state, and perform a measurement in the computational basis, with outcome000or111.What is being revealed by such a measurement? Is it revealing some objective, independent property of the qubit, a property that existed inside the qubit prior to the measurement? Or is it doing something else? In fact, does the qubit have any objective, independent properties at all?

These may seem like amusing philosophical questions, good for late-night conversation, but not of much importance. But in a remarkable 1964 paper, the physicist John Bell sharpened the questions up a very great deal. Indeed, it's not going too far to say Bell's results show a need to completely revise our thinking about what reality is.

In this section, we explain Bell's result. In fact, we'll explain a slightly stronger result, usually attributed to a 1969 paper of John Clauser, Michael Horne, Abner Shimony, and Richard Holt (CHSH)John Bell,On the Einstein Podolsky Rosen Paradox(1964), and John Clauser, Michael Horne, Abner Shimony, and Richard Holt,Proposed Experiment to Test Local Hidden-Variable Theories(1969).. This result is sometimes called the CHSH inequality, but we'll call it the Bell inequality (even though it's not quite the same as Bell's), since Bell had the core underlying insight.

To explain the Bell inequality, we first have to get ourselves out of the headspace of quantum mechanics. Nothing we say through the remainder of this section will have anything directly to do with quantum mechanics. There will be no qubits, no state vectors, no unitary dynamics, and certainly no measurement operators. Instead, we're going to consider a real-world experimental setup, and we'll think about what happens in that setup from (more or less) first principlesThe material that follows in this section is adapted from MN's essayWhy the world needs quantum mechanics(2008)..

In particular, we're going to think about light, and about photons, the elementary particles making up light. Photons have many physical properties – things like position, color, and so on. One property that may be a little less familiar to you is something calledpolarization. We say “less familiar”, but chances are you've at least met polarization, though you may not have realized it. If you take a pair of sunglasses, and hold them up toward the surface of the ocean or a pool on a sunny day, you'll notice that different amounts of light come through, depending on which angle you hold the sunglasses at. What this means is that depending on the angle, different numbers of photons are coming throughNot all sunglasses are polarizing in this way. But many are. You can check whether your sunglasses are polarizing by holding them up toward pretty much any surface that reflects glare. The ocean or a pool on a sunny day work well. If the surface appearance changes as you rotate the sunglasses, they're polarizing; if not, they're not..

Imagine, for example, that you hold the sunglasses horizontally:





The photons that make it through the sunglasses have what is calledhorizontal polarization. Not all photons coming toward the sunglasses have this polarization, which is why not all the photons make it through.

There are other physical properties that can be measured in a similar way. For example, imagine holding the sunglasses at 45 degrees to horizontal:





The photons that make it through the sunglasses have a polarization at 45 degrees to horizontal. You may wonder: is there any relationship between a photon having a horizontal polarization and having polarization at 45 degrees (or some other angle) to horizontal? The answer is that there is a relationship, but it's a little complicated to get into now: we'll come back to it.

Physicists routinely measure photon polarization in their laboratories. They don't use sunglasses; they use polarization-sensitive photodetectors instead. Despite that intimidating sounding name, these are essentially just like sunglasses, but have a more convenient shape and size for laboratory use, are more accurate, less fashionable, and far more expensive.

We'll now describe an experiment involving photon polarization that physicists can do in their laboratories. We'll build up the description of the experiment piece by piece. Along the way there's a few details that may seemad hoc– some angles of polarization measurement, and things like that. Don't worry too much about thosead hocdetails, just try to get the basic picture straight.

Let's begin by imagining an experimentalist named Alice. Alice is measuring a single photon to determine whether or not it has horizontal polarization. Alice will recordA=1A = 1A=1when it has horizontal polarization, andA=−1A = -1A=−1when it does not.

Of course, Alice might have decided to measure a different polarization, say at an angle of 45 degrees to the horizontal. Alice will recordB=1B = 1B=1when it has a polarization at 45 degrees to the horizontal, andB=−1B = -1B=−1when it does not. Here's a diagram summarizing the different things we want you to imagine Alice doing. By the way, we haven't put the photon she's measuring into the diagram, but you should imagine it coming into the screen, toward the sunglasses:





Now, remember what we were saying earlier – about our everyday assumption that objects have objective, intrinsic properties that can be measured. By analogy, you'd expect that a photon intrinsically “knows” whether it has a horizontal polarization or not. And it should also know whether it has a polarization at 45 degrees to horizontal or not.

It turns out the world doesn't work that way! What we'll now explain is that there are fundamental physical properties that don't have an independent existence like this. In particular, we'll see that prior to Alice measuring theAAAorBBBpolarization, the photon itself actually doesn't know what the value forAAAorBBBis going to be. This is utterly unlike our everyday experience. It's as though a coin doesn't decide whether to be heads or tails until we've measured it. Or, in terms of the epigraph with which we began this section, that the moon isn't really there when nobody looks.

(That last paragraph may have sounded like gobbledygook. If it didn't give you pause, you should reread it. It's difficult to understand because it's really a declaration of non-understanding, a declaration that the world is radically different from our ordinary, intuitive understanding.)

To see why this is the case, we'll first proceed on the assumption that our everyday view of the world is correct. That is, we'll assume photons really do know whether they have horizontal polarization or not, i.e., they have intrinsic valuesA=1A = 1A=1orA=−1A = -1A=−1,and alsoB=1B = 1B=1orB=−1B = -1B=−1.We'll find that this assumption leads us to a conclusion that is contradicted by real experiments. The only way this could be the case was if our original assumption was in fact wrong, i.e., photons don't have intrinsic properties in this way.

This strategy may sound complicated, but it's a common approach to everyday reasoning. Imagine your Uncle has shown you how to bake a cake. You decide to bake it on your own, but realize partway through that you've forgotten whether he said to put one or two cups of flour into the cake. You decide to proceed on the assumption that it was one cup of flour. Unfortunately, the cake falls and is a disaster; you conclude that your original assumption was wrong, and the recipe must have called for two cups. In a similar way, if we proceed on the assumption that photons do have intrinsic, objective values forAAAandBBB,but then arrive at a conclusion which is contradicted by experiment, we'll know our original assumptions must have been wrong.

Alright, let's finish describing the experiment. In addition to Alice, the experiment involves another experimentalist, Bob, and a third person, Eve, who prepares two photons and then sends one to Alice and one to Bob. When the photon gets to Alice, she measures either theAAAor theBBBpolarization, as described above. She makes the choice of which polarization to measure at random (e.g., by flipping a coin), for reasons which we'll understand later. When the photon gets to Bob, he decides at random to measure either a polarizationCCCat 22.5 degrees to horizontal, orDDD,at67.567.567.5degrees to horizontal. Here's a picture summarizing most of what's going on, although it leaves out Eve:





To make this all more concrete, let's think about what might happen in a typical instance of the experiment. Over on Alice's side, she decides to measure theBBBpolarization of her photon, and gets the result111,i.e., the photon is polarized at454545degrees to horizontal. Over on Bob's side, he decides to measure theCCCpolarization of his photon, and gets the result−1-1−1,i.e., the photon does not have polarization at22.522.522.5degrees to horizontal.

You might imagine Alice, Bob, and Eve doing this experiment many times. If they did, then you could conveniently represent the sequence of runs of the experiment in a table:







Each row of the table shows the results from a single run of the experiment, so this table shows a case where the experiment was done four times. Looking at the first row of the table, we see that in the first run of the experiment Alice chose to measureAAA,and got the result111,while Bob chose to measureDDD,and also got the result111.Running further down the table we can see for each experimental run which polarization directions Alice and Bob chose, and what result they got.

Now that we've understood the basic experimental setup, let's move onto the analysis leading to the Bell inequality. Remember, we're starting from the assumption that both photons in the experiment have independently existing and well-defined values forAAA,BBB,CCC,andDDD.Two of these four values are revealed in any given instance of the experiment, depending on what Alice and Bob choose to measure. However, because all four quantities have (by assumption) an independent existence, we can consider quantities which involve all four, like the quantityQQQdefined by the equation:

Q:=AC+BC+BD–AD.Q := AC + BC + BD – AD.Q:=AC+BC+BD–AD.

(To be really explicit, quantities likeACACACmeanA×CA \times CA×C,i.e., we're omitting the multiplication sign.)

AlthoughQQQ's definition appears to have come from out of the blue, it's at least easy to calculate for any given set of values forAAA,BBB,CCC,andDDD.For example, whenA=1A = 1A=1,B=−1B = -1B=−1,C=1C = 1C=1,andD=1D = 1D=1,we get:

Q=1×1+(−1)×1+(−1)×1−1×1=−2.Q = 1 \times 1 + (-1) \times 1 + (-1) \times 1 - 1 \times 1 = -2.Q=1×1+(−1)×1+(−1)×1−1×1=−2.

In fact, it turns out that no matter what valueAAA,BBB,CCC,andDDDhave, the value ofQQQis always equal to either222or−2-2−2.Perhaps the easiest way to see this is simply to run through all161616sets of possible values forAAA,BBB,CCC,andDDD,and verify thatQQQis indeed always either222or−2-2−2.Of course, it's a little tedious to run through all161616cases, and we don't think there's much point in writing them all out here (though you may wish to run through the cases).

A slicker way of seeingQQQis always222or−2-2−2is to rewriteQ=(A+B)C+(B−A)DQ = (A+B)C + (B-A)DQ=(A+B)C+(B−A)D.We can then split our analysis up into two cases. In the first caseA=BA = BA=B,causing the(B−A)(B-A)(B−A)terms inQQQto vanish, leaving just the(A+B)C(A+B)C(A+B)Cterm. A bit of thought and experimentation should convince you this is either222or−2-2−2.In the second case,A=−BA = -BA=−B,causing the(A+B)(A+B)(A+B)terms inQQQto vanish, and leaving just the(B−A)D(B-A)D(B−A)Dterm. Again, a bit of thought should convince you this is either222or−2-2−2.

Now, when Alice and Bob actually do an experiment, Alice chooses to measure just one ofAAAorBBB,and Bob chooses to measure just one ofCCCorDDD.This means they have no way of measuringQQQdirectly, although on any given run they can determine one of the four terms that make upQQQ,that is, they can always determine one ofACACAC,BCBCBC,BDBDBD,or−AD-AD−AD.

But if they repeat the experiment many times, Alice and Bob can estimate average values for each of the four quantities,ACACAC,BCBCBC,BDBDBD,and−AD-AD−AD.Because the sum of these four quantities is always222or−2-2−2,as we've seen, the sum of their averages over multiple runs of the experiment can not possibly be more than222:

Avg(AC)+Avg(BC)+Avg(BD)−Avg(AD)≤2.\text{Avg}(AC)+\text{Avg}(BC)+\text{Avg}(BD)-\text{Avg}(AD) \leq 2.Avg(AC)+Avg(BC)+Avg(BD)−Avg(AD)≤2.

This result is the Bell inequality (sometimes also called the Clauser-Horne-Shimony-Holt or CHSH inequality).

You might wonder why we need averages in the Bell inequality. Why can't Alice measure bothAAAandBBB,and Bob measure bothCCCandDDD,so they can determineQQQdirectly?

To understand this, remember that the idea we're exploring is the idea that the photon has an actual intrinsic value forAAA,and an actual intrinsic value forBBB,each of which is merely revealed by the measurement. A single photon is quite delicate, and if Alice measured bothAAAandBBB,there's a good chance the measurement ofAAAwould interfere with the measurement ofBBB,and vice versa, and so mess up the measurement ofQQQ.To keep things clean we force Alice to choose which one she wants to measure in any given run of the experiment, and stick to it. Similarly for Bob and choosing betweenCCCandDDD.That's why we have to work with averages over many experiments.

If you're a bit more paranoid, you might wonder if maybe Alice's measurement could interfere with what Bob sees. This may seem unlikely, but it's at least plausible. But Einstein's relativity tells us that no influence can travel faster than the speed of light. If Alice and Bob do their measurements near-simultaneously and very quickly, nothing Alice does can possibly affect what Bob sees.

As a result, if Alice and Bob do the experiment many times, they can estimate the averagesAvg(AC)\text{Avg}(AC)Avg(AC),Avg(BC)\text{Avg}(BC)Avg(BC),and so on, and check that the Bell inequality does, in fact, hold.

In the early 1980s, Alain Aspect did a series of experiments to determine whether the Bell inequality holds in nature. And Aspect found that if Eve prepares the two photons in just the right way, then what Alice and Bob see after many runs of the experiment isAspect and his collaborators published a series of papers on the subject in 1981 and 1982. We will simply link to the final paper: Alain Aspect, Jean Dalibard, and Gerard Roger,Experimental Test of Bell's Inequalities Using Time-Varying Analyzers(1982). Note that the paper considers a slight variation on the Bell inequality we have considered here. In particular, it considers a quantitySSSwhich is related to ourQQQbyQ=2+4SQ = 2+4SQ=2+4S,and the Bell inequality and its violations are rewritten in terms ofSSS.:

Avg(AC)+Avg(BC)+Avg(BD)−Avg(AD)≈2.4.\text{Avg}(AC)+\text{Avg}(BC)+\text{Avg}(BD)-\text{Avg}(AD) \approx 2.4.Avg(AC)+Avg(BC)+Avg(BD)−Avg(AD)≈2.4.

That is, Aspect and collaborators found that the Bell inequality fails to hold in the real world! And since it doesn't hold in the real world, there must be some assumption we made in deriving the Bell inequality that fails to be true in the real world.

Perhaps most obviously, our argument for the Bell inequality relies on a two-part set of assumptions often known aslocal realism. The first part is the idea that the universe is local, that is, influences can't propagate instantaneously. And second, as we've mentionedad nauseum, the idea that the universe is realistic, meaning that properties of physical systems like polarization have an intrinsic, independent existence, an existence which is merely revealed by the results of measurement.

Physicists thus often summarize the experimental violation of the Bell inequality as proving that the universe cannot be locally realistic.

This is an astonishing conclusion! In our opinion, the Aspect 1981/1982 experiments are crucial experiments in the history of science. They show the universe violates human intuition about reality in some extraordinarily strong sense.

Indeed, if you accept locality – as most physicists do – then the violation of the Bell inequalities by nature forces you to give up the idea of an independent, objective reality.

Of course, people have torn apart every piece of both the experiments where the Bell inequality is violated, and also every implicit assumption underlying the proof. Every assumption is fair game: you can go as deep as you like, ultimately asking questions about whether you accept ideas like the independence of different runs of the experiment, or whether it is possible for Alice and Bob to truly choose which polarization to measure.

That said, the conventional (though not universal) wisdom among physicists who have studied the Bell inequality is that: (a) the Bell inequality is violated in nature; and (b) this forces you to abandon realism. Although there are ways of escaping these conclusions, most people feel the proposed cures are worse than the disease. We don't want to go all New Age woo on you, but it's only a slight exaggeration to say the moral is that reality isn't real; it's not reality which needs an update, it's our notion of what is real.

It's an unfortunate fact that Einstein died in 1955, 9 years before Bell obtained the Bell inequalities, and 27 years before the Aspect experiment. So we don't know what he would have thought about all this. The physicist David Mermin has a nice account of asking a colleague

To conclude, it's worth re-emphasizing that the Bell inequalitydoes notdirectly involve quantum mechanics in any way – it's quite a common confusion that it's a result of quantum mechanics. Nothing could be further from the truth! The Bell inequality is, rather, a consequence of adopting a local realistic view of the world. But since that view has been rebutted by nature, we are forced to seek an alternate way of understanding the world, a way radically different from our conventional way of thinking. As we'll see in the next section, one solution is to use quantum mechanics.

In this section, we develop an example where quantum mechanics violates the Bell inequality. This implies that quantum mechanics isnota locally realistic theory, and also means that it has some chance of describing experimental results like the Aspect experiment. To develop this example, we're going to use our familiar language of qubits, computational basis measurements, and so on, instead of photons and polarization. It can all be mapped back onto the photon experiments, but explaining that mapping up front is more trouble than it's worth, given the experience we already have with qubits.

To do all this, we need to compute the average values associated to certain quantum measurements. There are quite a few details, so we'll just sketch the calculation. It's fine to follow along in more or less detail, to your own taste: you can drill down into details if you wish, or you can simply read quickly and focus on the conclusions, if that's your preference. The questions at the end of the section will thus be more conceptual in nature, and not about the details of the calculation.

As background, it helps to first explain a mathematical trick which makes it easier to compute the average outcome from a quantum measurement. As a concrete example, suppose we consider a measurement on a single qubit with two possible outcomes,+1+1+1and−1-1−1.The+1+1+1outcome will be associated to a measurement operatorM1=∣0⟩⟨0∣M_1 = |0\rangle \langle 0|M1​=∣0⟩⟨0∣,while the−1-1−1outcome has measurement operatorM−1=∣1⟩⟨1∣M_{-1} = |1\rangle \langle 1|M−1​=∣1⟩⟨1∣.Imagine you prepare a state∣ψ⟩|\psi\rangle∣ψ⟩repeatedly, and perform this measurement over and over. What is the average outcome?

By definition, the average is justp(1)∗1+p(−1)∗(−1)p(1)*1+p(-1)*(-1)p(1)∗1+p(−1)∗(−1).More generally, if we have a set of measurement operators{Mm}\{M_m\}{Mm​}then the average outcome is

∑mp(m)m=∑m⟨ψ∣Mm†Mm∣ψ⟩m,\sum_m p(m) m = \sum_m \langle \psi| M_m^\dagger M_m |\psi\rangle m,m∑​p(m)m=m∑​⟨ψ∣Mm†​Mm​∣ψ⟩m,

where the term on the left is just the definition of the average, and the term on the right comes from the third postulate. But we can take the sum inside and we see that the average is just⟨ψ∣M∣ψ⟩\langle \psi| M | \psi\rangle⟨ψ∣M∣ψ⟩where

M:=∑mmMm†Mm.M := \sum_m m M_m^\dagger M_m.M:=m∑​mMm†​Mm​.

MMMis known as theobservablecorresponding to the measurement{Mm}\{ M_m \}{Mm​}.This observable is a single, fixed operator which depends only on the measurement outcomesmmmand measurement operatorsMmM_mMm​.Yet if you know the observable then it is often easy to compute the average measurement outcome: it's just⟨ψ∣M∣ψ⟩\langle \psi| M |\psi\rangle⟨ψ∣M∣ψ⟩.Indeed, this is so convenient that it's often written in an abbreviated form as⟨M⟩:=⟨ψ∣M∣ψ⟩\langle M \rangle := \langle \psi| M |\psi\rangle⟨M⟩:=⟨ψ∣M∣ψ⟩.And so people often use⟨M⟩\langle M \rangle⟨M⟩as the notation for an average in quantum mechanics.

Let's come back to the example mentioned above, with measurement operatorsM1=∣0⟩⟨0∣M_1 = |0\rangle \langle 0|M1​=∣0⟩⟨0∣,andM−1=∣1⟩⟨1∣M_{-1} = |1\rangle \langle 1|M−1​=∣1⟩⟨1∣.The corresponding observable is then:

M=∣0⟩⟨0∣0⟩⟨0∣−∣1⟩⟨1∣1⟩⟨1∣=∣0⟩⟨0∣−∣1⟩⟨1∣.\begin{aligned} M & = |0\rangle\langle 0|0\rangle \langle 0| -|1\rangle\langle 1|1\rangle\langle 1| \\ & = |0\rangle \langle 0| -|1\rangle \langle 1|. \end{aligned}M​=∣0⟩⟨0∣0⟩⟨0∣−∣1⟩⟨1∣1⟩⟨1∣=∣0⟩⟨0∣−∣1⟩⟨1∣.​

Rewriting in matrix form, this is:

M=[100−1].M = \left[ \begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array} \right].M=[10​0−1​].

This is just the PauliZZZmatrix. And so if we want to compute the average value from such a measurement, it's just⟨ψ∣Z∣ψ⟩\langle \psi|Z|\psi\rangle⟨ψ∣Z∣ψ⟩.

More generally, we can tip this process upside down, using an observable to define a quantum measurement. In particular, supposeMMMis a Hermitian matrix acting on the quantum system's state space. Then a result known as the spectral theorem from linear algebraA somewhat peculiar but enlightening account may be foundhere. Unfortunately, the treatment on Wikipedia buries many of the key ideas in a mass of detail.guarantees thatMMMcan be decomposed as:

M=∑λλ∣λ⟩⟨λ∣,M = \sum_{\lambda} \lambda |\lambda\rangle \langle \lambda|,M=λ∑​λ∣λ⟩⟨λ∣,

where the sum is over all eigenvaluesλ\lambdaλand corresponding (normalized) eigenvectors∣λ⟩|\lambda\rangle∣λ⟩ofMMM.We can then define a quantum measurement with measurement operatorsMλ=∣λ⟩⟨λ∣M_\lambda = |\lambda\rangle \langle \lambda|Mλ​=∣λ⟩⟨λ∣.The completeness relation is easily checked to be true, and so this is a valid quantum measurement. What's more, you can check thatMMMis the observable corresponding to those choices.

This perhaps seems rather abstract and indirect. It's done because sometimes it's easier to specify a quantum measurement simply by specifying the observable. This can be particularly convenient when we're most interested in the average outcome from a measurement, as in the case of the Bell inequality. Indeed, in the case of the Bell inequality violations, the four observables we'll choose will correspond to:

A=ZB=X+Z2C=XD=X−Z2\begin{aligned} A & = Z \\ B & = \frac{X+Z}{\sqrt 2} \\ C & = X \\ D & = \frac{X-Z}{\sqrt 2} \end{aligned}ABCD​=Z=2​X+Z​=X=2​X−Z​​

It's simple to check that all these are Hermitian matrices, with eigenvalues+1+1+1and−1-1−1,and so define corresponding quantum measurements. You can, if you like, explicitly work out the corresponding eigenvectors and measurement operators. Doing so is likely good for your quantum mechanical soul (or at least your quantum mechanical work ethic)If you do so you'll discover that theXXXobservable corresponds to measuring in the∣+⟩,∣−⟩|+\rangle, |-\rangle∣+⟩,∣−⟩basis, as we discussed earlier.. But there's also a sense in which it's good practice to leave those things undetermined. After all, we're only going to be computing averages: we don't need to explicitly know the individual measurement operators!

To get a Bell inequality violation in quantum mechanics, we're going to imagine that our two experimental parties, Alice and Bob, are sharing a two-qubit state. In fact, it's an entangled state we met both inQuantum computing for the very curiousand (if you read it)How quantum teleportation works:

∣ψ⟩=∣00⟩+∣11⟩2.|\psi\rangle = \frac{|00\rangle+|11\rangle}{\sqrt 2}.∣ψ⟩=2​∣00⟩+∣11⟩​.

To reiterate, we suppose the quantum measurements Alice and Bob do correspond to the observables defined above:

A=ZB=X+Z2C=XD=X−Z2\begin{aligned} A & = Z \\ B & = \frac{X+Z}{\sqrt 2} \\ C & = X \\ D & = \frac{X-Z}{\sqrt 2} \end{aligned}ABCD​=Z=2​X+Z​=X=2​X−Z​​

To check whether the Bell inequalities hold or are violated, we want to compute:

Avg(AB)+Avg(CB)+Avg(CD)−Avg(AD).\text{Avg}(AB)+\text{Avg}(CB)+\text{Avg}(CD)-\text{Avg}(AD).Avg(AB)+Avg(CB)+Avg(CD)−Avg(AD).

With our choices forA,B,C,DA, B, C, DA,B,C,Dthis average can be shown to beWe're skipping over some plausible-but-need-to-be-checked steps here. In particular, we need to show that if Alice does the measurement corresponding to the observableAAA,then immediately afterward Bob does the measurement corresponding to the measurementBBB,the average of the product of the measurement results will just be⟨ψ∣A⊗B∣ψ⟩\langle \psi| A \otimes B |\psi\rangle⟨ψ∣A⊗B∣ψ⟩.Proving this is a good exercise.:

⟨Z⊗X+Z2⟩+⟨X⊗X+Z2⟩+⟨X⊗X−Z2⟩−⟨Z⊗X−Z2⟩.\langle Z \otimes \frac{X+Z}{\sqrt 2} \rangle + \langle X \otimes \frac{X+Z}{\sqrt 2} \rangle + \langle X \otimes \frac{X-Z}{\sqrt 2} \rangle - \langle Z \otimes \frac{X-Z}{\sqrt 2} \rangle.⟨Z⊗2​X+Z​⟩+⟨X⊗2​X+Z​⟩+⟨X⊗2​X−Z​⟩−⟨Z⊗2​X−Z​⟩.

To figure this out, let's start with the first term:

⟨Z⊗X+Z2⟩=⟨ψ∣Z⊗X∣ψ⟩+⟨ψ∣Z⊗Z∣ψ⟩2.\begin{aligned} \langle Z \otimes \frac{X+Z}{\sqrt 2} \rangle & = \frac{\langle \psi| Z \otimes X |\psi\rangle+\langle \psi|Z \otimes Z|\psi\rangle}{\sqrt 2}. \end{aligned}⟨Z⊗2​X+Z​⟩​=2​⟨ψ∣Z⊗X∣ψ⟩+⟨ψ∣Z⊗Z∣ψ⟩​.​

We can see that determining the averages is going to involve many computations that look like⟨ψ∣⋅⊗⋅∣ψ⟩\langle \psi| \cdot \otimes \cdot |\psi\rangle⟨ψ∣⋅⊗⋅∣ψ⟩,where the missing bits are Pauli operators. This is tedious to compute, but not especially difficult. If you are fluent with the Pauli operators it can be done pretty quickly. If you're less fluent, you can treat it as an exercise in becoming more fluent (the Pauli matrices are excellent things to become fluent with, but you should stop before you get bored).

Let's compute a few such terms. We'll start with⟨ψ∣Z⊗X∣ψ⟩\langle \psi|Z \otimes X |\psi\rangle⟨ψ∣Z⊗X∣ψ⟩.Substituting in∣ψ⟩=∣00⟩+∣11⟩2|\psi\rangle = \frac{|00\rangle+|11\rangle}{\sqrt 2}∣ψ⟩=2​∣00⟩+∣11⟩​this becomes:

⟨Z⊗X⟩=(⟨00∣+⟨11∣)(Z⊗X)(∣00⟩+∣11⟩)2.\begin{aligned} \langle Z \otimes X \rangle & = \frac{(\langle 00|+\langle 11|)(Z \otimes X) (|00\rangle+|11\rangle)}{2}. \end{aligned}⟨Z⊗X⟩​=2(⟨00∣+⟨11∣)(Z⊗X)(∣00⟩+∣11⟩)​.​

But(Z⊗X)∣00⟩=∣01⟩(Z \otimes X)|00\rangle = |01\rangle(Z⊗X)∣00⟩=∣01⟩,since theZZZleaves the∣0⟩|0\rangle∣0⟩state alone, andXXXflips∣0⟩|0\rangle∣0⟩to∣1⟩|1\rangle∣1⟩.Similarly,(Z⊗X)∣11⟩=−∣10⟩(Z\otimes X) |11\rangle = -|10\rangle(Z⊗X)∣11⟩=−∣10⟩.And so:

⟨Z⊗X⟩=(⟨00∣+⟨11∣)(∣01⟩−∣10⟩)2.\begin{aligned} \langle Z \otimes X \rangle & = \frac{(\langle 00|+\langle 11|)(|01\rangle-|10\rangle)}{2}. \end{aligned}⟨Z⊗X⟩​=2(⟨00∣+⟨11∣)(∣01⟩−∣10⟩)​.​

Of course, all the inner products vanish, and so⟨Z⊗X⟩=0\langle Z \otimes X \rangle = 0⟨Z⊗X⟩=0.

What about⟨Z⊗Z⟩\langle Z \otimes Z \rangle⟨Z⊗Z⟩?The calculation is very similar. Going through it with a little less explanation we obtain:

⟨Z⊗Z⟩=(⟨00∣+⟨11∣)(Z⊗Z)(∣00⟩+∣11⟩)2=(⟨00∣+⟨11∣)(∣00⟩+∣11⟩)2=22=1.\begin{aligned} \langle Z \otimes Z \rangle & = \frac{(\langle 00|+\langle 11|) (Z \otimes Z) (|00\rangle+|11\rangle)}{2} \\ & = \frac{(\langle 00|+\langle 11|)(|00\rangle+|11\rangle)}{2} \\ & = \frac{2}{2} \\ & = 1. \end{aligned}⟨Z⊗Z⟩​=2(⟨00∣+⟨11∣)(Z⊗Z)(∣00⟩+∣11⟩)​=2(⟨00∣+⟨11∣)(∣00⟩+∣11⟩)​=22​=1.​

So we see⟨Z⊗Z⟩=1\langle Z \otimes Z \rangle = 1⟨Z⊗Z⟩=1,and as a result⟨A⊗B⟩=12\langle A \otimes B \rangle = \frac{1}{\sqrt 2}⟨A⊗B⟩=2​1​.

All the remaining terms on the left-hand side of the Bell inequality can be computed very similarly. We won't explicitly work through them here. When you do, you learn thatAvg(CB)=12\text{Avg}(CB) = \frac{1}{\sqrt 2}Avg(CB)=2​1​,Avg(CD)=12\text{Avg}(CD) = \frac{1}{\sqrt 2}Avg(CD)=2​1​,andAvg(AD)=−12\text{Avg}(AD) = -\frac{1}{\sqrt 2}Avg(AD)=−2​1​.And so:

Avg(AB)+Avg(CB)+Avg(BD)−Avg(AD)=12+12+12−−12=42=22≈2.8.\begin{aligned} \text{Avg}(AB)+\text{Avg}(CB)+\text{Avg}(BD)-\text{Avg}(AD) & = \frac{1}{\sqrt 2}+\frac{1}{\sqrt 2}+\frac{1}{\sqrt 2}-\frac{-1}{\sqrt 2} \\ & = \frac{4}{\sqrt 2} \\ & = 2\sqrt{2}\\ & \approx 2.8. \end{aligned}Avg(AB)+Avg(CB)+Avg(BD)−Avg(AD)​=2​1​+2​1​+2​1​−2​−1​=2​4​=22​≈2.8.​

In other words, just as we claimed, quantum mechanics violates the Bell inequality! And thus quantum mechanics is not a locally realistic theory.

This is all for qubits. In fact, in quantum optics a photon's polarization is modeled essentially as a qubit, with horizontal polarization corresponding to the∣0⟩|0\rangle∣0⟩state, the454545degree polarization to the∣0⟩+∣1⟩2\frac{|0\rangle+|1\rangle}{\sqrt 2}2​∣0⟩+∣1⟩​state, and so on. We won't go through the detailed correspondence, but our quantum mechanical calculation above really does correspond to a calculation about a photon polarization experiment.

You may recall that the Aspect experiment gave a value for the sum of averages of2.42.42.4,not2.82.82.8.The reason is that the photodetectors in the Aspect experiment aren't perfectly efficient, and so don't capture all photons involved; the Aspect paper claims a quantum calculation with all the detector efficiencies accounted for gives a prediction just a little higher than the2.42.42.4observed, well within experimental errorUnfortunately, the paper is unclear on these points, mostly making claims without much detailed explanation or calculation; our comments are based on what seems a reasonable read, and deserve further checking.. More recent experiments have used much better photodetectors, and more closely approximate the2.82.82.8value. And so, not only does the Bell inequality and Aspect experiment lead us to reject the intuitive local realistic view of the world, it also confirms the predictions of quantum mechanics.

Why care about the Bell inequality, and its violation by quantum mechanics? Sure, it's weird. It's the kind of thing which provokes a “Whoah!” response. But astonishment aside, there's lots of weird things in the world. So what?

One reason to care is that fundamental physics is still incomplete. For instance, there's still no accepted, well-developed quantum theory of gravity. In fact, general relativity – our best current theory of gravity – is a local realistic theory: the Bell inequalityisn'tviolated in general relativity. So in order to develop a full quantum theory of gravitation, among many other challenges we'd need to reproduce the existing (local realistic) predictions where general relativity has been well tested, while also reproducing the (not always local realistic) predictions of quantum mechanics where that has been well tested. Doing both is not trivial!

Another way of looking at this is that Bell inequality violations tell you there's not going to be any way to get a quantum theory of gravity that is locally realistic. This straight away rules out many possible extensions of general relativity. Indeed, over the past decade much work on quantum gravity has focused on understanding the role entangled states play in quantum gravityA fun overview is thispopular essay.. This focus is natural, in the light of Bell inequality violations.

How would you ever have come up with the Bell inequality and with the quantityQQQ?In our presentation, it appeared out of nowhere. As did the particular experimental construction – all those polarization angles(!) – violating the Bell inequality.

Of course, the Bell inequality didn't come out of nowhere. It was motivated by the desire to find a sharp criterion separating the local realistic view of the world from the quantum mechanical view of the world. It's instructive to think about possible variations and simplifications.

For instance, in the Bell inequality we've described it's important that Alice and Bob each make a choice of what to measure. This gives rise to four possible combinations of measurement. What would happen if Alice and Bob each make a fixed measurement, sayAAAandBBB?Is it possible to find some Bell-like inequality satisfied by the productABABAB,but violated by a prediction of quantum mechanics?

If you try this, you quickly discover it's surprisingly difficult. And so you might decide to allow Bob two choices of possible measurement, sayBBBorCCC,and perhaps consider a quantity likeAB+ACAB+ACAB+AC,and whether there's a Bell-like inequality which can be violated by quantum mechanics. We actually don't know the answer here – it's fun to think about, and to try playing with examples.

Indeed, professional physicists have done quite a bit of work in this vein – trying to simplify and better understand different variations of the Bell inequalities. Of course, it's quite time-intensive: you need to try lots of things, and mostly it's hard to see how they might work. But it's good fun, and good for deepening your understanding of both quantum mechanics and the Bell inequality. Indeed, you're not so very far from the research frontier here. Of course, physicists have pushed on from the early Bell inequalities and the Aspect experiment. But there's certainly still more to discover.

The Bell inequality is just one of many phenomena that bother people about quantum mechanics. We'll now briefly describe a couple more, to give you a flavor for why people are bothered. If you'd like more depth a good introduction is Asher Peres's superb book “Quantum Theory: Concepts and Methods”. The book is now somewhat dated (it's from 1995), but still provides a clear account of many foundational issues, and is good preparation for understanding more recent work.

Why are there two types of dynamics?One oddity of quantum mechanics is that it has two different ways of describing the way states change: unitary dynamics, and the dynamics associated to measurement. This gives rise to a striking set of puzzles. Suppose we have a quantum system – let's call itQQQ– that's being measured. The measuring device is, of course, itself a quantum system. It seems therefore that it should be possible to find some larger quantum system which is isolated and that includes bothQQQand the measuring device. According to the second postulate, that larger system is undergoing unitary evolution.

What this means is that quantum mechanics now offers two seemingly different ways of describing the evolution of the system being measured: either through measurement operators and probabilities, as in the third postulate. Or in a completely deterministic way, under the unitary evolution of the larger system.

Having two different ways of describing the same situation prompts many questions: Can we guarantee the two descriptions are always consistent with one another? Is it possible to derive one description from the other? How can probabilities arise out of what seems like a deterministic description of the larger system? In particular, doesn't it seem strange that the quantum state for the combined system is evolving in a purely deterministic fashion, while the quantum state for the measured system changes at random? Shouldn't there be some way for us to derive the measurement probabilities from the deterministic evolution of the state of the combined system? In short: how can we reconcile these two points of view?

These are good questions. Together, these and other related questions are often known as themeasurement problemin quantum mechanics. Many resolutions of the measurement problem have been published by individual physicists. Unfortunately, the physics community as a whole has not agreed upon a complete resolution. We've heard variations on: “this has all been solved by Bohr; by von Neumann; by Everett; by Bohm;etc”. Unfortunately, for all the dozens or hundreds of resolutions which have been published there are also standard counterarguments. Indeed, a fun idea for a (very large!) project is to gather up the entire argument tree, containing all the strongest arguments and counterarguments, and cruxes of disagreement.

What does the quantum state mean? The interpretation of quantum mechanics:We've learned much about what you can do with quantum states, but never quite said what a quantum statemeans. We've been using it as a calculational device, a sort of ghost which helps us predict the probability distribution for results of measurements, and which can be used to solve problems like rapidly searching a large search space. But how should we think about the state? What does it mean? This is the problem ofinterpretationof the quantum state, and, more generally, of quantum mechanics.

As with the measurement problem, it's not difficult to find physicists who will confidently tell you how to correctly interpret the quantum state. Often they will follow up by telling you how their interpretation resolves the measurement problem, throws light on the violation of the Bell inequality, and how it will clean your living room as well. Again, the trouble is: there's a lot of disagreement between experts, standard arguments and counterarguments.

With all that said, many people have thought long and well about the meaning of the quantum state. As a starting point, we recommend readingHugh EverettandDavid Deutschon the many-worlds interpretation of quantum mechanics;Chris Fuchson the idea that the quantum state is a state of knowledge;David Bohmon the idea that it's a sort of pilot wave, guiding particles in the system; andRob Spekkens'sbroad, thoughtful work on what quantum mechanics means. Going further back in time, there is also much earlier work, some of it by physicists such as Einstein and Bohr who were deeply involved in creating quantum mechanics. A taste may be found in theexcellent collectionof papers curated by Wheeler and Zurek. Many of these papers are accessible and extremely stimulating, dealing with fundamental questions about the nature of reality. Finally, although it's not exactly an interpretation of the quantum state, we like Richard Feynman'spaperrecasting quantum mechanics in terms of (sometimes negative!) probability distributions, rather than quantum states.

This is just a tiny sample of the many ideas out there. Be aware that many of these people disagree (or disagreed, while alive) strongly with one another. But in controversy there is opportunity, and perhaps exploring that melange of ideas will even get you working on the problem yourself.

Why do any of these questions matter? After all, with our existing understanding of quantum mechanics we can develop ideas like quantum search and quantum teleportation. And, although we haven't gone through the details, it can also be used to make predictions about superconductors and lasers and semiconductors and so on. None of these is directly affected by concerns about the quantum measurement problem, about the meaning of the quantum state, or whether the world is locally realistic.

This returns us to the question from the introduction: what does it mean to understand quantum mechanics? If the purpose of a scientific theory is merely to predict the results of experiments, then quantum mechanics is doing an outstanding job. Not just in a practical sense, as with lasers and superconductors, but also with predicting unexpected phenomena like the violation of the Bell inequality, or quantum teleportation and quantum search. Put another way: in some very practical sense you havealreadyunderstood this Real Black Magic calculus. You know how to work the symbols, you can make astonishing predictions about the world. You really do understand quantum mechanics.

But while that's true, we demand more of our scientific theories. Consider Darwin's theory of evolution by natural selection. It's an astonishingly powerful theory, and explained much about the world that had hitherto been incomprehensible. But, as formulated by Darwin, it was not yet complete. It did not provide a detailed understanding of how variation arose in a population, and thus provided a limited understanding of selection. Genetics and successor ideas – from molecular biology to our still-nascent ideas about morphogenesis – have helped address many questions that Darwin left open.

In a similar way, while quantum mechanics is an astonishingly successful theory, it still leaves open fundamental questions such as the measurement problem and the interpretation of the quantum state. One day we'll know how to convincingly address those questions, and improve upon our existing understanding of quantum mechanics, in much the same way as modern biology has improved upon Darwin. Furthermore, it may be that solving such problems will help resolve problems such as the search for a quantum theory of gravity.

Concluding thought:This essay concludes a series of four essays. It's worth pausing to consider what the complete series gives you: not only an understanding of all the basic principles of quantum mechanics andquantum computing, but also of two major applications (searchandteleportation). If you've worked through the details, then you're well placed to understand more; you're no longer a beginner, but rather a person who understands the fundamentals of quantum mechanics and quantum computing.

Along the way, we've developed the mnemonic medium. If you've used the medium then you've participated in a small experiment in changing the way human beings understand new subjects. Of course, the medium has many limitations: it is by no means a silver bullet for understanding! But we believe it shows promise for changing the role of memory in understanding, and for developing fluency in the application of new skills. And that challenges us to ask: how much more powerful can we make such a medium?

Andy and Michael are supported in part through the generous contributions of ourPatreon supporters. Andy is supported in part by a grant from Emergent Ventures.

In academic work, please cite this as:

Authors are listed in alphabetical order.

This work is licensed under aCreative Commons Attribution-NonCommercial 3.0 Unported License. This means you’re free to copy, share, and build on this essay, but not to sell it. If you’re interested in commercial use, pleasecontact us.

March 15, 2020

See ourUser Agreement and Privacy Policy.


---

# Introduction to Qiskit







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The name "Qiskit" is a general term referring to a collection of software for executing programs on quantum computers. Most notably among these software tools is the open-source Qiskit SDK, and the runtime environment (accessed using Qiskit Runtime) through which you can execute workloads on IBM® quantum processing units (QPUs). As quantum technology evolves, so does Qiskit, with new capabilities released every year that expand this core collection of quantum software.

In addition, many open-source projects are part of the broader Qiskit ecosystem. These software tools are not part of Qiskit itself, but rather interface with Qiskit and can provide valuable additional functionality.

IBM is committed to the responsible development of quantum computing. Learn more and review our responsible quantum principles in theResponsible quantum computingtopic.

The Qiskit SDK (package nameqiskit) is an open-source SDK for working with quantum computers at the level of extended (static, dynamic, and scheduled) quantum circuits, operators, and primitives. This library is the core component of Qiskit; it is the largest package under the Qiskit name with the broadest suite of tools for quantum computation, and many other components interface with it.

Some of the most useful features of the Qiskit SDK include:

Circuit-building tools(qiskit.circuit) - For initializing and manipulating registers, circuits, instructions, gates, parameters, and control flow objects.

Circuit library(qiskit.circuit.library) - A vast range of circuits, instructions, and gates - key building blocks for circuit-based quantum computations.

Quantum info library(qiskit.quantum_info) - A toolkit for working with quantum states, operators and channels, using exact calculations (no sampling noise). Use this module to specify input observables and analyze fidelity of outputs from primitives queries.

Transpiler(qiskit.transpiler) - For transforming and adapting quantum circuits to suit specific device topology, and optimizing for execution on real quantum processing units (QPUs).

Primitives(qiskit.primitives) - The module that contains the base definitions and reference implementations of the Sampler and Estimator primitives, from which different quantum hardware providers can derive their own implementations. See more information about the Qiskit Runtime primitivesin the documentation.

For a more detailed introduction to installing the Qiskit SDK, check out theinstallation page. If you're ready to install it now, simply run:

Benchmarking is important for comparing the relative performance of quantum software across different stages of a development workflow. Benchmarking tests for quantum software might, for example, look at the speed and quality of building, manipulating, and transpiling circuits. IBM Quantum is committed to delivering the most performant SDK possible, and to that end, the Qiskit SDK is benchmarked using over 1,000 tests developed by leading universities, national labs, and researchers at IBM. The benchmarking suite used for these tests, named Benchpress, is now available asan open-source package. You can now use the Benchpress package to perform your own analysis of quantum SDK performance.

Qiskit Runtime is a cloud-based service for executing quantum computations on IBM Quantum® hardware. Theqiskit-ibm-runtimepackage is a client for that service, and is the successor to the Qiskit IBM Provider. The Qiskit Runtime service streamlines quantum computations and provides optimal implementations of the Qiskit primitives for IBM Quantum hardware. To get started with Qiskit Runtime primitives, visit thedocumentation.

With Qiskit Runtime you can choose to run your quantum programs on IBM Quantum hardware through the IBM Quantum Platform or IBM Cloud®. See more information on selecting an IBM Quantum channelin the documentation.

Qiskit Runtime is designed to use additional classical and quantum compute resources, including techniques such as error suppression and error mitigation, to return a higher-quality result from executing quantum circuits on quantum processors. Examples include dynamical decoupling for error suppression, and readout mitigation and zero-noise extrapolation (ZNE) for error mitigation. Learn how to configure these options on theConfigure error mitigationpage.

Qiskit Runtime also includes three types of execution modes for running your quantum program on IBM hardware:Job,Session, andBatch,each of which have different use cases and implications for the quantum job queue. A Job is a single query to a primitive that can be run over a specified number of shots. Sessions allow you to efficiently run multiple jobs in iterative workloads on quantum computers. Batch mode allows you to submit all your jobs at once for parallel processing.

To quickly install Qiskit Runtime, run the following command:

More details on setting up a development environment for building quantum programs can be found in theinstallation page.

The short answer is,not all of it. The Qiskit Runtime service software that handles the technicalities of running your quantum program on an IBM Quantum device (including any error mitigation and suppression) isnotopen-source. However, the Qiskit Runtime client (the interface for users to access the Qiskit Runtime service), the Qiskit SDK running on the server side, and some of the software used for error mitigation,areopen-source.  To get involved with the Qiskit open-source efforts, visit our GitHub organization atgithub.com/Qiskitandgithub.com/Qiskit-Extensions.

Creating utility-scale quantum applications generally requires a variety of compute resource requirements. Qiskit Serverless (qiskit-ibm-catalog.QiskitServerless) provides a simple interface to run workloads across quantum-classical resources. This includes deploying programs to IBM Quantum Platform and running workloads remotely, as well as easy resource management for multi-cloud and quantum-centric supercomputing use cases. See more information in theQiskit Serverless documentationabout how to use this collection of tools to:

To start using Qiskit Serverless right away, install it with pip:

Qiskit Functions (qiskit-ibm-catalog.QiskitFunctionsCatalog) are abstracted services designed to accelerate algorithm discovery and application prototyping. Explore theQiskit Functions Catalog, including:

Premium Plan members can access IBM-provided functions right away, or purchase licenses for the partner-provided functions directly from those partners.

The catalog can be installed with pip:

The Qiskit Transpiler Service (package nameqiskit-ibm-transpiler) is a new experimental service that provides remote transpilation capabilities on the cloud to IBM Quantum Premium Plan users. In addition to the local Qiskit SDK transpiler capabilities, your transpilation tasks can benefit from both IBM Quantum cloud resources and AI-powered transpiler passes using this service. To learn more about how to integrate cloud-based transpilation into your Qiskit workflow you cancheck out the documentation.

The transpiler service can be installed with pip:

Qiskit addons are a collection of research capabilities for utility-scale algorithm discovery. These capabilities build upon Qiskit’s performant foundation of tools for creating and running quantum algorithms. Addons are modular software components that plug into a workflow to scale or design new quantum algorithms. To learn more about the set of available Qiskit addons and how to get started using them, visit thedocumentation.

There are a number of addons depending on what research capability you are interested in. Each of them can be installed with pip.

Sample-based quantum diagonalization (SQD):

Approximate quantum compilation (AQC):

Operator backpropagation (OBP):

Multi-product formulas (MPF):

Beyond Qiskit there are many open-source projects that use the "Qiskit" name but are not part of Qiskit itself; rather, they interface with Qiskit and can provide valuable additional functionality to supplement the core Qiskit workflow. Some of these projects are maintained by IBM Quantum teams, whereas others are supported by the broader open-source community. The Qiskit SDK is designed in a modular, extensible way to make it easy for developers to create projects like these that extend its capabilities.

Some popular projects in the Qiskit ecosystem include:

You can find a catalog of projects in theQiskit ecosystem page, as well as information about how to nominate your own project.

On this page

© IBM Corp., 2017-2025


---

# Install Qiskit







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Whether you will work locally or in a cloud environment, the first step for all users is to install Qiskit.For those wanting to run on a real quantum processing unit (QPU), your next step is to choose one of two channels in order to access IBM® QPUs: IBM Quantum Platform or IBM Cloud®.

(If you are installing Qiskit for the first time, skip ahead to theInstall and set upsection. This notice is relevant only to users who have installed Qiskit previously.)

For those upgrading from version 0.x to 1.0 or later: note that because Qiskit v1.0 uses a new packaging structure, youcannotusepip install -U qiskitto upgrade from any Qiskit 0.x version to 1.0.

See theQiskit 1.0 migration guidefor details and instructions.

Future updates starting with Qiskit 1.0 will allow for in-place upgrades.

Install Python. Check the "Programming Language" section on theQiskit PyPI project pageto determine which Python versions are supported by the most recent release. For download instructions, see thePython Beginners Guide.

It is recommended that you usePython virtual environmentsto separate Qiskit from other applications.

These instructions use the standard Python distribution frompypi.org. However, you can use other Python distributions, such asAnacondaorminiconda, along with other dependency management workflows likePoetry.

If you're new to virtual environments, click here for more information.

A virtual Python environment is an isolated space to work with Python for a specific purpose — so you can install whatever packages you wish, and set up libraries, dependencies, and so on, without affecting the "base" Python environment on your machine.

One important advantage of a virtual environment is that if your Python environment becomes corrupted somewhere along the way, you can easily delete the virtual environment and start over!

Choose a preferred location in which to store information about your virtual environments. Typically they're stored in a directory named.venvwithin each project directory you're working in.

First, navigate to your project directory and create a minimal environment with only Python installed in it.

Next, activate your new environment.

If using PowerShell:

If using Git Bash:

If using command prompt:

Install pipif it's not already installed in your environment. Pip is a Python package manager that you use to install Qiskit and other Python packages. Usepip listto see what is in your virtual environment. In most Python environments, pip is already installed.

Install the Qiskit SDK. If you plan to run jobs on quantum hardware, also install Qiskit Runtime.

If you intend to use visualization functionality or Jupyter notebooks, it is recommended to install Qiskit with the extra visualization support ('qiskit[visualization]').

If you want to run a Jupyter notebook with the Qiskit packages you just installed, you need to install Jupyter in your environment.

Then open your notebook as follows:

If you are planning to work locally and use simulators built into Qiskit, then your installation is done. If you want to run jobs on IBM QPUs, nextselect an access channeland finish your setup.

Periodically check theQiskit release notesand theQiskit Runtime release notesto see new releases. We recommend frequently updating your requirements forqiskitandqiskit-ibm-runtimeby, for example, changing the versions inrequirements.txtto the latest versions, then runningpip install -r requirements.txtor the appropriate command for your dependency management workflow.

Need help? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

"No Module 'qiskit'" error with Jupyter Notebook

If you usedpip install qiskitand set up your virtual environment in
Anaconda, then you may get theNo Module 'qiskit'error when you run a tutorial
in Jupyter Notebook. If you have not installed Qiskit or set up your
virtual environment, you can follow theinstallationsteps.

The error is caused when trying to import the Qiskit package in an
environment where Qiskit is not installed. If you launched Jupyter Notebook
from the Anaconda-Navigator, it is possible that Jupyter Notebook is running
in the base (root) environment, instead of in your virtual
environment. Choose a virtual environment in the Anaconda-Navigator from theApplications ondropdown menu. In this menu, you can see
all of the virtual environments within Anaconda, and you can
select the environment where you have Qiskit installed to launch Jupyter
Notebook.

Compilation errors during installation

Qiskit depends on a number of other open-source Python packages, which
are automatically installed when doingpip install qiskit. Depending on
your system's platform and Python version, it is possible that a particular
package does not provide pre-built binaries for your system. You can refer
toOperating system supportfor a list of platforms supported by Qiskit, some
of which may need an extra compiler. In cases where there are
no precompiled binaries available,pipwill attempt to compile the package
from source, which in turn might require some extra dependencies that need to
be installed manually.

If the output ofpip install qiskitcontains similar lines to:

please check the documentation of the package that failed to install (in the
example code,SOME_PACKAGE) for information on how to install the libraries
needed for compiling from source.

Qiskit strives to support as many operating systems as possible, but due to limitations in available testing resources and operating system availability, not all operating systems can be supported. Operating system support for Qiskit is broken into three tiers with different levels of support for each tier. For platforms outside these, such as FreeBSD or WebAssembly (WASI), Qiskit may still be installable, but it is not tested and you will have to build Qiskit (and likely Qiskit’s dependencies) from source.

Additionally, Qiskit only supports the CPython implementation of the Python language. Running with other Python interpreters such as PyPy is not supported.

In the Qiskit v2.x release series, the supported platforms are:

Tier 1

Tier 1 operating systems are fully tested as part of the development processes to ensure any proposed change will function correctly. Pre-compiled binaries are built, tested, and published to PyPI as part of the release process. Typically, as long as there is a functioning Python environment installed, Qiskit can be installed on these operating systems without needing to install further dependencies.

Tier 1 operating systems:

Tier 2

There are no Tier 2 operating systems in the Qiskit v2.x release series.Tier 2 operating systems are not tested as part of development process. However, pre-compiled binaries are built, tested, and published to PyPI as part of the release process and these packages can be expected to be installed with only a functioning Python environment.

Tier 3

Tier 3 operating systems are not tested as part of the development process. Pre-compiled binaries are built and published to PyPI as part of the release process but are not tested. They may not be installable with only a functioning Python environment and might require a C/C++ compiler or additional programs to build dependencies from source as part of the installation process. Support for these operating systems are best effort only.

Tier 3 operating systems:

Starting in Qiskit v2.0.0, only 64-bit platforms are supported and 32-bit platforms are not supported. You will not be able to build from source
on 32-bit platforms either, as internally the Qiskit Rust code assumes a 64-bit pointer width.

In the Qiskit v1.x release series, the supported platforms are:

Tier 1

Tier 1 operating systems are fully tested as part of the development processes to ensure any proposed change will function correctly. Pre-compiled binaries are built, tested, and published to PyPI as part of the release process. Typically, as long as there is a functioning Python environment installed, Qiskit can be installed on these operating systems without needing to install further dependencies.

Tier 1 operating systems:

Tier 2

Tier 2 operating systems are not tested as part of development process. However, pre-compiled binaries are built, tested, and published to PyPI as part of the release process and these packages can be expected to be installed with just a functioning Python environment.

Tier 2 operating systems:

Tier 3

Tier 3 operating systems are not tested as part of the development process. Pre-compiled binaries are built and published to PyPI as part of the release process but are not tested. They may not be installable with just a functioning Python environment and might require a C/C++ compiler or additional programs to build dependencies from source as part of the installation process. Support for these operating systems are best effort only.

Tier 3 operating systems:

On this page

© IBM Corp., 2017-2025


---

# Set up an IBM Quantum channel







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

You can access IBM® quantum processing units (QPUs) by using the IBM Quantum Platform or IBM Cloud® channel.Channelis the term used to describe the method you use to access IBM Quantum services.

You have the option to access IBM Quantum hardware through eitherIBM Quantum PlatformorIBM Cloud.

IBM Quantum Platform has Open (free access) and Premium (enterprise subscription) plans. SeeIBM Quantum access plansfor details.

Before setting up with IBM Quantum Platform, make sure you have theQiskit SDK and Qiskit Runtime installed.

Available plans:

Open Plan- Run your quantum circuits on the world's best QPUs for free (up to 10 minutes quantum time per month).

Premium Plan- Run quantum circuits on the world's best QPUs using an enterprise quantum time subscription.

IBM Cloud offers pay-as-you-go access plans. SeeIBM Quantum access plansfor details.

IBM Cloud has Lite (free access - deprecated) and Standard (pay-as-you-go access) plans. SeeQiskit Runtime planson IBM Cloud for details.

This channel does not support a cloud-based development environment. Therefore, you will need toinstall and set up Qiskit and Qiskit Runtimeandset up to use IBM Cloud.

Available plans:

Standard (Pay-as-you-go) Plan- Run quantum circuits on the world's best QPUs and pay only for the quantum time you use.

Lite plan: Debug and learn about quantum circuits using free simulators.

Before setting up with IBM Quantum Platform, ensure you are working in an active Python environment with theQiskit SDK and Qiskit Runtime installed.

If you do not already have a user account, get one at theIBM Quantum login page.Your user account is associated with one or moreinstances(in the form hub / group / project) that give access to IBM Quantum services. Additionally, a unique token is assigned to each account, allowing for IBM Quantum access from Qiskit. The instructions in this section use our default instance.  For instructions to choose a specific instance, seeConnect to an instance.

The Instances section in yourIBM Quantum account pagelists the instances that you can access.

Protect your API key!Never include your key in source code, Python script, or notebook file. If you are working in a trusted Python environment (such as on a personal laptop or workstation), use thesave_account()method described in the next step to store your credentials, keeping in mind that your key will still be stored as plain text on your local drive. If you are executing code in a Python environment that is not trusted, see theinstructions in step 4.

Retrieve your API key from theIBM Quantum account page, and activate your Python virtual environment.  See theinstallation instructionsif you do not already have a virtual environment set up.

If you are working in a trusted Python environment (such as on a personal laptop or workstation),use thesave_account()method to save your credentials locally. (Skip to the next stepif you are not using a trusted environment, such as a shared or public computer, to authenticate to IBM Quantum Platform.) To usesave_account(), runpythonin your shell, then enter the following:

Alternatively, you can copy the code for accessing a specific instance, then paste it into your code. Go to the Instances section of yourIBM Quantum accountpage and click the vertical ellipses at the end of an instance's column to copy the code.

Typeexit(). From now on, whenever you need to authenticate to the service, you can load your credentials withQiskitRuntimeService().

Avoid executing code on an untrusted machine or an external cloud Python environment to minimize security risks.If you must use an untrusted environment (on, for example, a public computer), change your API key after each use by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk. To initialize the service in this situation, you can use code like the following:

When sharing code with others, ensure that your API key is not embedded directly within the Python script. Instead, share the script without the token and provide instructions for securely setting it up.

If you accidentally share your key with someone or include it in version control like Git, immediately revoke your key by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk.

Test your setup.  Run a simple circuit using Sampler to ensure that your environment is set up properly:

Alternatively, you can also access quantum processors with REST APIs, enabling you to work with QPUs using any programming language or framework.

If you do not already have a user account, get one at theIBM Quantum login page.Your user account is associated with one or moreinstances(in the form hub / group / project) that give access to IBM Quantum services. Additionally, a unique token is assigned to each account, allowing for IBM Quantum access from Qiskit. The instructions in this section use our default instance.  For instructions to choose a specific instance, seeConnect to an instance.

The Instances section in yourIBM Quantum account pagelists the instances that you can access.

Retrieve your API key from theIBM Quantum account page.

Because of the security risks posed by executing code that contains your API key, the recommended authentication method is to first create an environment variable for your API key, but only do soif you are working in a trusted Python environment (such as on a personal laptop or workstation).Skip to the next stepif you are not using a trusted environment, such as a shared or public computer.

To set the IQP_API_TOKEN environment variable in your system, you can add the following line to your shell profile (for example, .bashrc or .zshrc) or by setting it directly in your terminal:

When you invoke the environment variable in your code, includeimport os, as in this example request:

Note that when creating an environment variable, your API key is still stored locally in plain text, and should be safeguarded.

Avoid executing code on an untrusted machine or an external cloud Python environment to minimize security risks.If you must use an untrusted environment (on, for example, a public computer), change your API key after each use by rotating it on theIBM Quantum Platform dashboard(click the refresh button in the API key field). To initialize the service in this situation, use your API key directly:

When sharing code with others, ensure that your API key is not embedded directly within the Python script. Instead, share the script without the token and provide instructions for securely setting it up.

If you accidentally share your key with someone or include it in version control like Git, immediately revoke your key by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk.

Optionally obtain a temporary access token by supplying your API key. This is especially useful if you would like control over tokens, such as token invalidation. Follow the same precautions previously mentioned about securely using the environment variable.

View your available backends:

You can thentranspile circuits using REST APIand run them using either theSampler or the Estimator primitives.

After your experiments are complete, you can proceed to invalidate your key and then test its invalidation.

This should yield an error (Error 401) once the access token is invalidated.

Output

Before setting up with IBM Cloud, ensure you are working in an active Python environment with theQiskit SDK and Qiskit Runtime installed.

If you do not already have one, set up an IBM Cloud account from theIBM Cloud Registration page.

Create a service instance, if necessary. Open yourIBM Cloud Instances page. If you have one or more instances shown, continue to the next step. Otherwise, clickCreate instance. When creating your instance you can name it, tag it, select a resource group for it, and select a performance strategy. Next, agree to the license agreements by checking the box in the bottom right corner of the page, and clickCreate.

If you are an administrator who needs to set up Qiskit Runtime on Cloud for your organization, refer toPlan Qiskit Runtime for an organization.

Find your access credentials.

If you are working in a trusted Python environment (such as on a personal laptop or workstation),use thesave_account()method to save your credentials locally. (Skip to the next stepif you are not using a trusted environment, such as a shared or public computer, to authenticate to IBM Cloud.) To usesave_account(), activate a Python virtual environment (see theinstallation instructionsif you do not already have a virtual environment set up). Then, run Python in your virtual environment and enter the following:

Typeexit(). From now on, whenever you need to authenticate to the service, you can load your credentials withQiskitRuntimeService().  Test your setup and ensure that you can connect to the service:

Avoid executing code on an untrusted machine or an external cloud Python environment to minimize security risks.If you must use an untrusted environment (on, for example, a public computer), change your API key after each use by deleting it on theAPI keys pageand creating a new one.

Protect your API key!Never include your key in source code, Python script, or notebook file. When sharing code with others, ensure that your API key is not embedded directly within the Python script. Instead, share the script without the token and provide instructions for securely setting it up.

If you accidentally share your key with someone or include it in version control like Git, immediately revoke your key by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk.

To initialize the service in this situation, you can use code like the following:

On this page

© IBM Corp., 2017-2025


---

# Online lab environments







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

In addition to downloading and installing Qiskit to work on your local machine, there are several options available for those who prefer to work in an online development environment.

Several providers offer online Jupyter environments with Qiskit preinstalled for fast and convenient onboarding. These recommended providers include the cloud service provider OVHcloud and the quantum software development cloud platform qBraid.

Additional online Jupyter notebook environments like IBM Watson® Studio, Google Colab, and Microsoft Azure Machine Learning Studio can be used to work with Qiskit by following the appropriate instructions.

OVHcloud Public Cloud and OVHcloud Startup users can use their OVHcloud quantum notebooks to access Qiskit and submit jobs to IBM® QPUs with their IBM Quantum® or IBM Cloud® account. To learn more, visit theOVHcloud Documentation and tutorialspage.

OVHcloud AI notebooks are not available in some regions, such as the United States. Additionally, user interfaces might look different in different regions.

Follow these steps to get started:

Qiskit users can use qBraid’s preconfigured Python environments by following these instructions. For more information, see theqBraid Docs.

For platforms without Qiskit preconfigured, the setup instructions are similar, except that you must install Qiskit manually. You will create an account, start a new project (or notebook or workspace, depending on the platform), and install Qiskit.

On this page

© IBM Corp., 2017-2025


---

# Install the Qiskit SDK and Qiskit Runtime from source







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Installing the Qiskit SDK from source allows you to access the current development version, instead of using the version in the Python Package Index (PyPI) repository. This lets you inspect and extend the latest version of the Qiskit code more efficiently.

Navigate to your project directory and create a minimal environment with only Python installed in it.

Activate your new environment.

A Rust compiler must be installed on your system to compile Qiskit. To install the Rust compiler, use the cross-platform Rust installerrustuporanother install method.

Follow these steps to install Qiskit:

Standard install:

Editable mode: In this mode, you don't need to reinstall Qiskit when there are code changes to the project.

In editable mode, the compiled extensions are built indebug modewithout optimizations. This affects the runtime performance of the compiled code. To build the compiled extensions with optimizations enabled, run the following command to rebuild the binary inrelease mode:

If you are working on Rust code in Qiskit, you need to rebuild the extension code every time you make a local change. In editable mode, the Rust extension is only built when the install command is run, so local changes you make to the Rust code are not reflected in the installed package unless you rebuild the extension by rerunningbuild_rust(with or without--release, depending on whether you want to build in release or debug mode).

Follow these steps if you want to install Qiskit Runtime:

Standard install:

Editable mode: In this mode, you don't need to reinstall Qiskit when there are code changes to the project.

In editable mode, the compiled extensions are built indebug modewithout optimizations.

On this page

© IBM Corp., 2017-2025


---

# Configure the Qiskit SDK locally







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

After the Qiskit SDK is installed and running, there are some optional steps you can take to change the default Qiskit behavior.

The main location for local configuration of Qiskit is the user configuration file. This is an .ini-format file that can be used to change Qiskit default settings.

Example:

By default, this file is in~/.qiskit/settings.confbut the path can be overridden with theQISKIT_SETTINGSenvironment variable.

Set these environment variables to alter the default behavior of Qiskit:

On this page

© IBM Corp., 2017-2025


---

# Install the Qiskit C API







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This guide describes how to install and use the Qiskit C API. To see how to extend your
Qiskit Python workflow with C, readExtend Python with the Qiskit C API.

The following example builds an observable with C:

This section provides build instructions for UNIX-like systems.

Compilation requires the following tools:

This code verifies that everything has been installed:

To build the C header and library, you can run the following Make command1in Qiskit root,

which will provide the compiled shared library indist/c/liband theqiskit.hheader with
all function declarations indist/c/include. Note that the precise library name depends
on the platform; for example,libqiskit.soon UNIX andlibqiskit.dylibon MacOS.
(Note that this step currently emits a lot of warnings, which is expected, and is no cause for alarm. Future versions will remove the warnings.)

You can then compile a C program using the Qiskit C header and library:

To ensure the library is found during execution, set the runtime library path to
include/path/to/dist/c/lib. This depends on the platform. On Linux:

On MacOS:

Alternatively, you can set the runtime library path during compilation by adding

to the compiler flags.

Now you can execute the binary:

which, if using the example snippet shown previously, should print

This section provides build instructions for Windows systems.

Compilation requires the following tools:

First, compile theqiskit_cextdynamic library, by running the following in Qiskit root

This will generate the.dlldynamic library and associated.dll.libfile intarget/release.
Next, generate the header with

This will write the MSVC-compatible header indist\c\include.

Now you can useclto compile the C program. To ensure the compiler finds the qiskit library,
we includetarget\releasein thePATHvariable.

Before running, you have to include the path to yourpython3.dll.

should then print

If you did not install Make, check theMakefilein Qiskit root for the required commands - or simply install Make; it's not too late.)↩

On this page

© IBM Corp., 2017-2025


---

# Extend Qiskit in Python with C







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

To accelerate your Qiskit Python programs with C, you can use the Qiskit C extension for Python.
This requires additional steps to the standalone C usage; for more details, see theInstall the Qiskit C API guide.

The Qiskit C API is still experimental, and has not yet committed to a fully stable programming or
binary interface.  Extension modules built against Qiskit are only guaranteed to work against
the version of Qiskit used in the build.

These instructions have only been tested on UNIX-like systems. Windows instructions are in progress._

Start by ensuring you have installed theQiskit C API. Next, install the Qiskit Python interface, as follows:

There are various options to write a C extension for Python. For simplicity, this guide starts with an approach that uses Python's built-inctypesmodule.  In the next section, thethe Manual C extensionsection provides an example of building the C extension using Python's C API to reduce runtime overhead.

As an example, assume you write a C function to build an observable and would like to return
it to Python. You can convert a C-sideQkObs*to a Python-sideSparseObservableobject, using the provided converterqk_obs_to_python:

The following demonstrates how to compile this into a shared library - for example,qiskit_cextension.so.
Once this is done, you can call the C program from Python:

First, you have to build the Qiskit Python extension. This includes the C symbols so you can access both interfaces via the same shared library. This is important to ensure data can be passed
correctly across C and Python.

The shared library is called_accelerate.<platform-specific-part>. Find its location and name as follows:

You will need to know the location of the environments Python includes (Python.h) and libraries (libpython.<suffix>).
These can, for example, be identified with

(If you already know these locations and names, you can also just set them directly.)

Linking can differ among platforms and linkers. The following describes a solution for linkers
supporting libraries with arbitrary names, using the-l:flag (such as GNU'sldlinker).
See below if your linker requires the library to be calledlib<something>(such as thelddlinker common on MacOS).

You can build the extension specifying the full name of the_acceleratelibrary:

Then,  simply enterpython main.pyto run the Python program.

An alternative to using the exact library name with-l:is to symlink the_acceleratelibrary
to the desired name.
To include the_accelerateshared library, symlink it to the linker's expected format oflib<library name>.<suffix>:

where<suffix>is e.g.soon Linux ordylibon MacOS. This allows to useqiskitas library name:

Then, simply enterpython main.pyto run the Python program.

Instead of usingctypes, it is possible to manually build an extension for Python usingPython's
C APIdirectly. This has the potential to be
faster than usingctypes, though it requires more effort to implement.
The following code is a brief example on how to achieve this.

To compile a shared library, link both the Python and Qiskit libraries, as described in
theBuildsection above. The Python script then does not needctypesbut can directly importcextensionmodule (ensure it is on your Python path):

On this page

© IBM Corp., 2017-2025


---

# Hello world







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This example contains two parts. You will first create a simple quantum program and run it on a quantum processing unit (QPU).  Because actual quantum research requires much more robust programs, in the second section (Scale to large numbers of qubits), you will scale the simple program up to utility level.  You can also follow along with the Hello World episode of the Coding with Qiskit 1.0 video series.

This video uses theQiskitRuntimeService.get_backendmethod, which has since been deprecated. UseQiskitRuntimeService.backendinstead.

Follow theInstall and set upinstructions if you haven't already, including the steps toSet up to use IBM Quantum® Platform.

The code examples found in the IBM Quantum Platform documentation were developed by usingJupyternotebooks.  To follow along with the examples, it is recommended that you set up an environment to run Jupyter notebookslocallyoronline.Be sure to install the recommended extra visualization support ('qiskit[visualization]'). You'll also need thematplotlibpackage for the second part of this example.

To learn about quantum computing in general, visit theBasics of quantum information coursein IBM Quantum Learning.

IBM® is committed to the responsible development of quantum computing. Learn more about responsible quantum at IBM and review our responsible quantum principles in theResponsible quantum computing and inclusive techtopic.

The four steps to writing a quantum program using Qiskit patterns are:

Map the problem to a quantum-native format.

Optimize the circuits and operators.

Execute using a quantum primitive function.

Analyze the results.

In a quantum program,quantum circuitsare the native format in which to represent quantum instructions, andoperatorsrepresent the observables to be measured. When creating a circuit, you'll usually create a newQuantumCircuitobject, then add instructions to it in sequence.

The following code cell creates a circuit that produces aBell state,which is a state wherein two qubits are fully entangled with each other.

The Qiskit SDK uses the LSb 0 bit numbering where thenthn^{th}nthdigit has value1≪n1 \ll n1≪nor2n2^n2n. For more details, see theBit-ordering in the Qiskit SDKtopic.

Output:

SeeQuantumCircuitin the documentation for all available operations.

When creating quantum circuits, you must also consider what type of data you want returned after execution. Qiskit provides two ways to return data: you can obtain a probability distribution for a set of qubits you choose to measure, or you can obtain the expectation value of an observable. Prepare your workload to measure your circuit in one of these two ways withQiskit primitives(explained in detail inStep 3).

This example measures expectation values by using theqiskit.quantum_infosubmodule, which is specified by using operators (mathematical objects used to represent an action or process that changes a quantum state). The following code cell creates six two-qubit Pauli operators:IZ,IX,ZI,XI,ZZ, andXX.

Here, something like theZZoperator is a shorthand for the tensor productZ⊗ZZ\otimes ZZ⊗Z, which means measuring Z on qubit 1 and Z on qubit 0 together, and obtaining information about the correlation between qubit 1 and qubit 0. Expectation values like this are also typically written as⟨Z1Z0⟩\langle Z_1 Z_0 \rangle⟨Z1​Z0​⟩.

If the state is entangled, then the measurement of⟨Z1Z0⟩\langle Z_1 Z_0 \rangle⟨Z1​Z0​⟩should be different from the measurement of⟨I1⊗Z0⟩⟨Z1⊗I0⟩\langle I_1 \otimes Z_0 \rangle \langle Z_1 \otimes I_0 \rangle⟨I1​⊗Z0​⟩⟨Z1​⊗I0​⟩. For the specific entangled state created by our circuit described above, the measurement of⟨Z1Z0⟩\langle Z_1 Z_0 \rangle⟨Z1​Z0​⟩should be 1 and the measurement of⟨I1⊗Z0⟩⟨Z1⊗I0⟩\langle I_1 \otimes Z_0 \rangle \langle Z_1 \otimes I_0 \rangle⟨I1​⊗Z0​⟩⟨Z1​⊗I0​⟩should be zero.

When executing circuits on a device, it is important to optimize the set of instructions that the circuit contains and minimize the overall depth (roughly the number of instructions) of the circuit. This ensures that you obtain the best results possible by reducing the effects of error and noise. Additionally, the circuit's instructions must conform to a backend device'sInstruction Set Architecture (ISA)and must consider the device's basis gates and qubit connectivity.

The following code instantiates a real device to submit a job to and transforms the circuit and observables to match that backend's ISA. It requires that you have alreadysaved your credentials

Output:

Quantum computers can produce random results, so you usually collect a sample of the outputs by running the circuit many times. You can estimate the value of the observable by using theEstimatorclass.Estimatoris one of twoprimitives; the other isSampler, which can be used to get data from a quantum computer.  These objects possess arun()method that executes the selection of circuits, observables, and parameters (if applicable), using aprimitive unified bloc (PUB).

Output:

After a job is submitted, you can wait until either the job is completed within your current python instance, or use thejob_idto retrieve the data at a later time.  (See thesection on retrieving jobsfor details.)

After the job completes, examine its output through the job'sresult()attribute.

When you run your quantum program on a real device, your workload must wait in a queue before it runs. To save time, you can instead use the following code to run this small workload on thefake_providerwith the Qiskit Runtime local testing mode. Note that this is only possible for a small circuit. When you scale up in the next section, you will need to use a real device.

The analyze step is typically where you might postprocess your results using, for example, measurement error mitigation or zero noise extrapolation (ZNE). You might feed these results into another workflow for further analysis or prepare a plot of the key values and data. In general, this step is specific to your problem.  For this example, plot each of the expectation values that were measured for our circuit.

The expectation values and standard deviations for the observables you specified to Estimator are accessed through the job result'sPubResult.data.evsandPubResult.data.stdsattributes. To obtain the results from Sampler, use thePubResult.data.meas.get_counts()function, which will return adictof measurements in the form of bitstrings as keys and counts as their corresponding values. For more information, seeGet started with Sampler.

Output:

Notice that for qubits 0 and 1, the independent expectation values of both X and Z are 0, while the correlations (XXandZZ) are 1. This is a hallmark of quantum entanglement.

In quantum computing, utility-scale work is crucial for making progress in the field. Such work requires computations to be done on a much larger scale; working with circuits that might use over 100 qubits and over 1000 gates. This example demonstrates how you can accomplish utility-scale work on IBM® QPUs by creating and analyzing a 100-qubit GHZ state.  It uses the Qiskit patterns workflow and ends by measuring the expectation value⟨Z0Zi⟩\langle Z_0 Z_i \rangle⟨Z0​Zi​⟩for each qubit.

Write a function that returns aQuantumCircuitthat prepares annnn-qubit GHZ state (essentially an extended Bell state), then use that function to prepare a 100-qubit GHZ state and collect the observables to be measured.

Next, map to the operators of interest. This example uses theZZoperators between qubits to examine the behavior as they get farther apart.  Increasingly inaccurate (corrupted) expectation values between distant qubits would reveal the level of noise present.

Output:

The following code transforms the circuit and observables to match the backend's ISA. It requires that you have alreadysaved your credentials

Submit the job and enable error suppression by using a technique to reduce errors calleddynamical decoupling.The resilience level specifies how much resilience to build against errors. Higher levels generate more accurate results, at the expense of longer processing times.  For further explanation of the options set in the following code, seeConfigure error mitigation for Qiskit Runtime.

Output:

After the job completes, plot the results and notice that⟨Z0Zi⟩\langle Z_0 Z_i \rangle⟨Z0​Zi​⟩decreases with increasingiii, even though in an ideal simulation all⟨Z0Zi⟩\langle Z_0 Z_i \rangle⟨Z0​Zi​⟩should be 1.

Output:

The previous plot shows that as the distance between qubits increases, the signal decays because of the presence of noise.

On this page

© IBM Corp., 2017-2025


---

# Introduction to Qiskit patterns







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

A Qiskit pattern is a general framework for breaking down domain-specific problems and contextualizing required capabilities in stages. This allows for the seamless composability of new capabilities developed by IBM Quantum® researchers (and others) and enables a future in which quantum computing tasks are performed by powerful heterogenous (CPU/GPU/QPU) computing infrastructure. Blocks or groups of blocks perform the steps of a pattern, with the Qiskit SDK providing an important foundational layer, supported by other tools or services developed by IBM Quantum or the quantum open-source community. Qiskit patterns allow domain experts to specify a problem and compose the tooling (blocks) that achieves a Qiskit pattern. That pattern can then be executed locally, through cloud services, or deployed with Qiskit Serverless.

The four steps of a Qiskit pattern are as follows:

Each step is detailed in the sections below.

This step describes how a user starts with a classical problem and figures out how to map it to a quantum computer. For example, in applications such as chemistry and quantum simulation, this step generally involves constructing a quantum circuit representing the Hamiltonian you are attempting to solve. During this step, for certain problems, it might also be desirable to specify the mapping of the problem onto qubits in the heavy-hex (or gross) lattice of IBM® hardware from the outset if the structure of the problem lends itself to optimization earlier. It is also worth considering at this point what the outcome of the particular algorithm will be in preparation for the later execute step - for example, if the desired outcome involves inferring correlation functions using Hadamard tests, you might prepare to use Sampler, whereas specifying observables would use the Estimator and could provide many error mitigation options.

The output of this step is normally a collection of circuits or quantum operators that can be optimized for hardware in the next step.

In this step you take the abstract circuits (or operators) produced from the map step and perform a series of optimizations on them. This can include mapping the route and layout of the circuit to physical qubit hardware, converting to basis gates of the hardware, and reducing the number of operations, all designed to optimize the likelihood of success in the later execute step. At this point you might also wish to test out your circuits with a simulator before executing on real hardware in the next step.

During this step, abstract circuits must be transpiled to Instruction Set Architecture (ISA) circuits. An ISA circuit is one that only consists of gates understood by the target hardware (basis gates), and any multi-qubit gates needed to obey any connectivity constraints (coupling map). Only ISA circuits can be run on IBM hardware using IBM Qiskit Runtime.

This step involves running your circuits on hardware and produces the outputs of the quantum computation. The ISA circuits produced in the previous step can be executed using either a Sampler or Estimator primitive from Qiskit Runtime, initialized locally on your computer or from a cluster or other heterogeneous compute environment. These can be executed in a Batch, which allows parallel transpilation for classical computational efficiency - or a Session, which allows iterative tasks to be implemented efficiently without queuing delays. During this step, there is also the option to configure certain error suppression and mitigation techniques provided by Qiskit Runtime.

Depending on whether you are using the Sampler or Estimator primitive, the outcome of this step will be different. If using the Sampler, the output will be per-shot measurements in the form of bitstrings. If using the Estimator, the output will be expectation values of observables corresponding to physical quantities or cost functions.

This final step involves stitching the outputs from the prior step back together to obtain the desired result. This can involve a range of classical data-processing steps such as visualizing results, readout error mitigation techniques, marginalizing quasi-probability distributions to ascertain results on smaller sets of qubits, or post-selection on inherent properties of the problem, such as total spin, parity, or particle conservation by removing unphysical observables.

As the field moves from bespoke circuit construction to utility-scale workflows, the flexibility and ease with which Qiskit patterns allow users to compose the different steps of the pattern opens quantum computing to a wide variety of applications and techniques for easy use by quantum computational scientists.

Qiskit Serverless

Qiskit Functions

On this page

© IBM Corp., 2017-2025


---

# Map the problem to quantum circuits and operators







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The "map the problem to quantum circuits and operators" step of a Qiskit pattern describes how a user starts with a classical
problem and figures out how to map it to a quantum computer.

For example, in applications such as chemistry and quantum simulation, this step generally involves
constructing a quantum circuit representing the Hamiltonian you are attempting to solve.
During this step, for certain problems, it might also be desirable to specify the mapping of
the problem onto qubits in the heavy-hex (or gross) lattice of IBM® hardware from the
outset if the structure of the problem lends itself to optimization earlier.

It is also worth considering at this point what the outcome of the particular algorithm will be
in preparation for the later execute step - for example, if the desired outcome involves
inferring correlation functions using Hadamard tests, you might prepare to use Sampler, whereas
specifying observables would use Estimator and could provide many error mitigation options.

The output of this step in a Qiskit pattern is normally a collection of circuits or quantum operators.

On this page

© IBM Corp., 2017-2025


---

# Optimize for target hardware







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

In the "optimize for target hardware" step of a Qiskit pattern, you take the abstract circuits
(or operators) produced from the map step and perform a series of optimizations on them. This
can include mapping the route and layout of the circuit to physical qubit hardware, converting
to basis gates of the hardware, and reducing the number of operations, all designed to optimize
the likelihood of success in the later execute step. At this point you might also wish to debug
your circuits with a simulator before executing on real hardware in the next step.

During this step, abstract circuits must be transpiled to Instruction Set Architecture (ISA) circuits.
An ISA circuit is one that only consists of gates understood by the target hardware (basis gates), and
any multi-qubit gates needed to obey any connectivity constraints (coupling map). Only ISA circuits
can be run on IBM® hardware using IBM Qiskit Runtime.

On this page

© IBM Corp., 2017-2025


---

# Execute on target hardware







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The "execute on hardware" step of a Qiskit pattern involves running your circuits on hardware
and produces the outputs of the quantum computation. The ISA circuits produced in
the previous step can be executed using either a Sampler or Estimator primitive from
Qiskit Runtime, initialized locally on your computer or from a cluster or other
heterogeneous compute environment. These can be executed in a Batch, which allows
parallel transpilation for classical computational efficiency - or a Session,
which allows iterative tasks to be implemented efficiently without queuing delays.

During this step, there is also the option to configure certain error suppression and
mitigation techniques provided by Qiskit Runtime.

Depending on whether you are using the Sampler or Estimator primitive, the outcome of this step
will be different. If using the Sampler, the output will be per-shot measurements
in the form of bitstrings. If using the Estimator, the output will be
expectation values of observables corresponding to physical quantities or cost functions.

On this page

© IBM Corp., 2017-2025


---

# Post-process results







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This final "post-process results" step of a Qiskit pattern involves stitching the outputs from
the prior step back together to obtain the desired result. This can involve a range of classical
data-processing steps such as visualizing results, readout error mitigation techniques, marginalizing
quasi-probability distributions to ascertain results on smaller sets of qubits, or post-selection on inherent
properties of the problem, such as total spin, parity, or particle conservation by removing
unphysical observables.

On this page

© IBM Corp., 2017-2025


---

# Latest updates







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Last updated 9 June 2025

Keep up with the latest and greatest from Qiskit and IBM Quantum®!

For all product announcements, visit theAnnouncementspage on IBM Quantum Platform Classic.

Jump toQiskit SDK|Qiskit Runtime client|Qiskit Runtime service|Qiskit Transpiler service|Qiskit Serverless|Qiskit Functions|Qiskit Code Assistant|Documentation

31 Mar 2025

Qiskit SDK v2.0 introduces significant performance improvements over its predecessor, and lays the groundwork for powerful new tools and capabilities that we plan to share in the coming months. Highlights include:

Wondering what has changed? Read thechangelogand thev2.0 release notes.

To see the release notes for all versions, visit theQiskit SDK release notes.

28 May 2025

The following changes were made to support the upcomingIBM Quantum platform migration:

A new channel type,ibm_quantum_platform, has been introduced for service initialization (QiskitRuntimeService()). It joins the existingibm_quantum(now deprecated) andibm_cloudchannels. Bydefault,ibm_quantum_platformis selected when no channel is specified. This new channel connects to the new IBM Quantum Platform API and is intended to replaceibm_cloud. In the meantime, theibm_cloudchannel will redirect to the new API, but its continued use is discouraged.

Aninstancevalue isno longer requiredfor saving (QiskitRuntimeService.save_account()) or initializing (QiskitRuntimeService()) an account on the new platform (ibm_quantum_platform, and temporarily,ibm_cloudchannels). If an instance is not passed in, all instances will be checked when a backend is retrieved, (service.backend("backend_name")). If an instance is passed intoQiskitRuntimeService.save_account(), or passed in during initialization, it will be used as thedefault instancewhen retrieving backends. The instance passed in at initialization will takeprecedenceover the one saved in the account.

Note that the IBM Cloud API Token (token) is required for saving (QiskitRuntimeService.save_account()) or initializing (QiskitRuntimeService()) an account on the new platform. It’s treated as the account identifier and will unlock the resources associated with the account the token was created in. A list of tokens per account can be foundhere. Only one account per API token can be used. If you want to use multiple accounts, you must create multiple API tokens.

TheQiskitRuntimeService.backend()andQiskitRuntimeService.backends()methods have been updated to accept aninstancepassed in explicitly when retrieving backends:service.backend(name="...", instance="...").

New parameters,regionandplans_preference, have been added to theQiskitRuntimeServiceinitializer andQiskitRuntimeService.save_account()method. These can be used toprioritizecertain instances on the new platform (ibm_quantum_platform, and temporarily,ibm_cloudchannels) without explicitly providing the CRN. In more detail:

For example, ifregionis saved asus-east, only instances fromus-eastwill be checked. Ifplans_preferenceis set, the instances will be prioritized in the order given, so['Open', 'Premium']would prioritize all Open Plan instances, then all Premium Plan instances, and then the rest. Note that the plan names inplans_preferencemust exactly match the API names (case insensitive).

Theinstanceinput parameter ofQiskitRuntimeServicehas been extended to accept new input types for theibm_quantum_platformandibm_cloudchannels. In addition to the IBM Cloud Resource Name (CRN), the instancenamecan now be passed in as the instance value.

Theinstances()method has been extended to show all available instances associated to an account for theibm_quantum_platformandibm_cloudchannels, in addition to the already enabledibm_quantumchannel.

The following code snippets show the new usage patterns enabled by the changes described above (2239):

Theprivateoption underEnvironmentOptionsis now supported on theibm_cloudandibm_quantum_platformchannels (new IBM Quantum Platform). When this option is set toTrue, the job will be returned without parameters, and results can only be retrieved once.

There is also a newprivate()property that returns whether or not a job is private. (2263)

To see the release notes for all versions, visit theQiskit Runtime client release notes.

This summary of the latest changes to the Qiskit Runtime service applies to anyone using Qiskit Runtime, regardless of how you communicate with the service (by usingqiskit-ibm-runtimeor otherwise), or which version of the client SDK you use.

5 June 2025

3 February 2025

2 February 2025

Starting 2 June 2025 and continuing through the year, IBM Quantum will begin a gradual rollout of new features todynamic circuitsthat will enable them at the utility scale.
Improvements include the following:

To accelerate the rollout, the following capabilities are now deprecated and will be no longer supported on or around 2 June 2025:

7 January 2025

15 October 2024

1 October 2024

15 August 2024

3 July 2024

The following endpoints are deprecated and will be removed on or after 3 October 2024:GET /stream/jobsandGET /stream/jobs/{id}. This removal has the following impacts:

18 June 2024

3 June 2024

28 March 2024

25 March 2025

To see the release notes for all versions, visit theQiskit Transpiler Service client release notes.

Qiskit Transpiler Service client v0.3.0

16 May 2025

Developers can set detailed statuses and track what's happening across a workflow.

Serverless workloads have several stages across a workflow. By default, the following statuses are viewable withjob.status():

Now, you can also set custom statuses that further describe the specific workflow stage, as in the following example.

5 June 2025

QUICK-PDEby ColibriTD allows users to solve certain differential equations for material deformation and computational fluid dynamics problems. For example, one team of researchers has already begun using the QUICK-PDE function to study the dynamics of novel reactive fluids developed to transfer heat more efficiently in a type of nuclear reactor known as Small Modular Reactors.

Quantum Portfolio Optimizerby Global Data Quantum enables quantitative finance researchers to back-test portfolio optimization strategies. Running on over 100 qubits, this function calculates a portfolio’s Sharpe ratio versus return across a specified time period. Early users are exploring the optimizer’s ability to evaluate historical performance of an investment strategy and to enable comparisons of different portfolios under similar conditions.

Check out theQiskit Functions Catalogto request a free trial today.

4 June 2025

New updates

16 May 2025

Over the coming weeks, every function will give detailed information to help you run, debug, and analyze your workflows. This includes:

We're hoping these changes make it easier to use Qiskit Functions, andyou can get started with free trials in the catalog today.

10 March 2025

Latest additions to the Qiskit Functions Catalog

To get started, explore theQiskit Functions documentation.

16 September 2024

Introducing the Qiskit Functions preview, for IBM Quantum Premium Plan users. To get started,pip install qiskit-ibm-catalogand explore theQiskit Functions documentation.With the Qiskit Functions Catalog client, you can submit workloads to abstracted services designed to accelerate your research. Sign in with your existing IBM Quantum Platform credentials.

The Qiskit Functions Catalog preview provides access to Premium Plan users to explore the available functions, including those written by IBM and those written by other members of our ecosystem. The catalog contains two kinds of functions: circuit functions and application functions.

Circuit functionsprovide a simplified interface for running circuits. They receive user-provided abstract circuits and observables as input, then manage synthesis, optimization, and execution of the representative ISA circuit. Circuit functions bring together the latest capabilities in transpilation, error suppression, and error mitigation to make utility-grade performance accessible out of the box. This allows computational scientists to focus on mapping their problems to circuits, rather than building the pattern for each problem from scratch.

Application functionscover higher-level tasks, like exploring algorithms and domain-specific use cases. Enterprise developers and data scientists may not have the background quantum information science knowledge for working with circuits, and instead hope to bring their domain knowledge to advance quantum computing algorithms and applications. With application functions, users can enter their classical inputs and receive solutions so they can more easily experiment with plugging quantum into their domain-specific workflows.

With the launch of the Qiskit Functions Catalog, Premium Plan developers can explore the IBM Circuit function. The IBM Circuit function includes the latest AI-powered extensions to Qiskit for circuit synthesis, optimization, and scheduling, as well as advanced error mitigation methods to return the most accurate estimations possible with today's hardware.

Users can purchase licenses for the following functions contributed by our partners at Q-CTRL, QEDMA, Algorithmiq, and Qunasys.

Circuit functions

Application functions

5 June 2025

We have updated the model available in the service to the newer granite-3.3-8b-qiskit model

We have open-sourced three new models for local inference in Hugging Face:

For more details on Qiskit Code Assistant, see thedocumentation.

IBM Quantum documentation recently added a number of user-facing improvements, including content updates and new features. Many of these changes are a result of specific user requests! Check out the highlights below.

18 December 2024

New pages

Introductory and get-started material for theseQiskit addons:SQD|AQC-Tensor|OBP|MPF

Debug Qiskit Runtime jobswith the NEAT class.

Integrate external quantum resources with Qiskitguide in Open-source resources.

New migration guide:Migrate from Qiskit Pulse to fractional gates.

New Qiskit Functions guide:Singularity Machine Learning - Classification.

Use Qiskit Code Assistant in local mode.

Content additions and improvements

Revisions by Qunasys to the Qiskit FunctionsQURI Chemistryguide

Updated code examples to fix a bug inGet started with primitives

Updates toIntroduction to optionsto include the newgen3-turbooptions

Copyediting and typo fixes across the documentation, including bugs reported by open-source contributors - thank you!

New API reference documentation

User experience improvements

A huge thank you goes out to everyone in the open-source community who contributed and gave feedback!Pleaseopen an issueif you find a bug, have a suggestion, or want to share your experience.

On this page

© IBM Corp., 2017-2025


---

# Introduction to Qiskit Functions







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Qiskit Functions simplify and accelerate utility-scale algorithm discovery and application development, by abstracting away parts of the quantum software development workflow. In this way, Qiskit Functions free up time normally spent hand-writing code and fine-tuning experiments.

Functions come in two forms:

Functions are provided by IBM® and third-party partners. Each is performant for specific workload characteristics and have unique performance-tuning options. Premium Plan users can get started with IBM Qiskit Functions for free, or procure a license from one of the partners who have contributed a function to the catalog.

To start using Qiskit Functions, install the IBM Qiskit Functions Catalog client:

Retrieve your API key from theIBM Quantum account page, and activate your Python virtual environment.  See theinstallation instructionsif you do not already have a virtual environment set up.

If you are working in a trusted Python environment (such as on a personal laptop or workstation),use thesave_account()method to save your credentials locally. (Skip to the next stepif you are not using a trusted environment, such as a shared or public computer, to authenticate to IBM Quantum Platform.)

To usesave_account(), runpythonin your shell, then enter the following:

Typeexit(). From now on, whenever you need to authenticate to the service, you can load your credentials withQiskitFunctionsCatalog().

Avoid executing code on an untrusted machine or an external cloud Python environment to minimize security risks.If you must use an untrusted environment (on, for example, a public computer), change your API key after each use by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk. To initialize the service in this situation, expand the following section to view code you can use:

Protect your API key!Never include your key in source code, Python script, or notebook file. When sharing code with others, ensure that your API key is not embedded directly within the Python script. Instead, share the script without the key and provide instructions for securely setting it up.

If you accidentally share your key with someone or include it in version control like Git, immediately revoke your key by expiring it on theIBM Quantum Platform dashboard(click the refresh button in the API key field) to reduce risk.

Output:

After a catalog object has been instantiated, you can select a function usingcatalog.load(provider/function-name):

Each Qiskit Function has custom inputs, options, and outputs. Check the specific documentation pages for the function you want to run for more information. By default, all users can only run one function job at a time:

Output:

Currently, the IBM Quantum workloads table only reflects Qiskit Runtime workloads. Usejob.status()to see your Qiskit Function workload's current status.

With your Qiskit Functionjob_id, you can check the status of running jobs. This includes the following statuses:

Output:

After a program isDONE, you can usejob.results()to fetch the result. This output format varies with each function, so be sure to follow the specific documentation:

Output:

You can also cancel a job at any time:

Output:

You can usejobs()to list all jobs submitted to Qiskit Functions:

Output:

If you already have the job ID for a certain job, you can retrieve the job withcatalog.get_job_by_id():

If a program status isERROR, usejob.result()to fetch the error message as follows:

Output:

On this page

© IBM Corp., 2017-2025


---

# IBM Circuit function







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The IBM® Circuit function takesabstract PUBsas inputs, and returns mitigated expectation values as outputs. This circuit function includes an automated and customized pipeline to enable researchers to focus on algorithm and application discovery.

After submitting your PUB, your abstract circuits and observables are automatically transpiled, executed on hardware, and post-processed to return mitigated expectation values. To do so, this combines the following tools:

Authenticate using yourAPI keyand select the Qiskit Function as follows:

To get started, try this basic example:

Check your Qiskit Function workload'sstatusor returnresultsas follows:

Output:

The results have the same format as anEstimator result:

Output:

See the following table for all input parameters the IBM Circuit function accepts. The subsequentOptionssection goes into more details about the availableoptions.

Similar to Qiskit Runtime primitives, options for IBM Circuit function can be specified as a nested dictionary. Commonly used options, such asoptimization_levelandmitigation_level, are at the first level. Other, more advanced options are grouped into different categories, such asresilience.

If you do not specify a value for an option, the default value specified by the service is used.

IBM Circuit function also supportsmitigation_level. The mitigation level specifies how much error suppression and mitigation to apply to the job. Higher levels generate more accurate results, at the expense of longer processing times. The degree of error reduction depends on the method applied. The mitigation level abstracts the detailed choice of error mitigation and suppression methods to allow users to reason about the cost/accuracy trade-off appropriate to their application. The following table shows the corresponding methods for each level.

While the names are similar,mitigation_levelapplies different techniques than the ones used by Estimator’sresilience_level.

Similar toresilience_levelin Qiskit Runtime Estimator,mitigation_levelspecifies a base set of curated options. Any options you manually specify in addition to the mitigation level are applied on top of the base set of options defined by the mitigation level. Therefore, in principle, you could set the mitigation level to 1, but then turn off measurement mitigation, although this is not advised.

The following example demonstrates setting the mitigation level:

In addition tomitigation_level, the IBM Circuit function also provides a select number of advanced options that allow you to fine-tune the cost/accuracy trade-off. The following table shows all the available options:

In the following example, setting the mitigation level to 1 initially turns off ZNE mitigation, but settingzne_mitigationtoTrueoverrides the relevant setup frommitigation_level.

The output of a Circuit function is aPrimitiveResult, which contains two fields:

One or morePubResultobjects. These can be indexed directly from thePrimitiveResult.

Job-level metadata.

EachPubResultcontains adataand ametadatafield.

Thedatafield contains at least an array of expectation values (PubResult.data.evs) and an array of standard errors (PubResult.data.stds). It can also contain more data, depending on the options used.

Themetadatafield contains PUB-level metadata (PubResult.metadata).

The following code snippet describes thePrimitiveResult(and associatedPubResult) format.

Output:

If your workload status isERROR, usejob.result()to fetch the error message to help debug as follows:

Output:

Reach out toIBM Quantum support, and include the following information:

On this page

© IBM Corp., 2017-2025


---

# Tensor-network error mitigation (TEM): A Qiskit Function by Algorithmiq







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Algorithmiq’s Tensor-network Error Mitigation (TEM) method is a hybrid
quantum-classical algorithm designed for performing noise mitigation entirely at
the classical post-processing stage. With TEM, the user can compute the
expectation values of observables mitigating the inevitable noise-induced errors
that occur on quantum hardware with increased accuracy and cost efficiency,
making it a highly attractive option for quantum researchers and industry
practitioners alike.

The method consists of constructing a tensor network representing the inverse of
the global noise channel affecting the state of the quantum processor and then
applying the map to informationally complete measurement outcomes acquired from
the noisy state to obtain unbiased estimators for the observables.

As an advantage, TEM leverages informationally complete measurements to give
access to a vast set of mitigated expectation values of observables and has
optimal sampling overhead on the quantum hardware, as described in Filippov at
al. (2023),arXiv:2307.11740, and  Filippov
at al. (2024),arXiv:2403.13542. The
measurement overhead refers to the number of additional measurements required to
perform efficient error mitigation, a critical factor in the feasibility of
quantum computations. Therefore, TEM has the potential to enable quantum
advantage in complex scenarios, such as applications in the fields of quantum
chaos, many-body physics, Hubbard dynamics, and small molecule chemistry
simulations.

The main features and benefits of TEM can be summarized as:

The TEM function allows you to obtain error-mitigated expectation values for
multiple observables on a quantum circuit with minimal sampling overhead. The
circuit is measured with an informationally complete positive operator-valued
measure (IC-POVM), and the collected measurement outcomes are processed on a
classical computer. This measurement is used to perform the tensor network
methods and build a noise-inversion map. The function applies a map that fully
inverts the whole noisy circuit using tensor networks to represent the noisy
layers.

Once the circuits are submitted to the function, they are transpiled and
optimized to minimize the number of layers with two-qubit gates (the noisier
gates on quantum devices). The noise affecting the layers is learned throughQiskit Runtimeusing a sparse Pauli-Lindblad noise model as described in E. van den Berg, Z.
Minev, A. Kandala, K. Temme, Nat. Phys. (2023).arXiv:2201.09866.

The noise model is an accurate description of the noise on the device able to
capture subtle features, including qubit cross-talk. However, noise on the
devices can fluctuate and drift and the learned noise might not be accurate at
the point at which the estimation is done. This might result in inaccurate
results.

Authenticate using yourIBM Quantum Platform API key, and select the TEM function as follows:

The following snippet shows an example where TEM is used to compute the expectation values of an observable given a simple quantum circuit.

Use the Qiskit Serverless APIs to check your Qiskit Function workload's status:

Output:

You can return the results as:

The expected value for the noiseless circuit for the given operator should be around0.18409094298943401.

Parameters

TEM currently has the following limitations:

A dictionary containing the advanced options for the TEM. The dictionary may contain the keys in the following table. If any of the options are not provided, the default value listed in the table will be used. The default values are good for typical use of TEM.

A QiskitPrimitiveResultscontaining the TEM-mitigated result. The result for each PUB is returned as aPubResultcontaining the following fields:

If your workload status is ERROR, use job.result() to fetch the error message as follows:

Output:

Reach out to[email protected]

Be sure to include the following information:

On this page

© IBM Corp., 2017-2025


---

# Performance Management: A Qiskit Function by Q-CTRL Fire Opal







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Fire Opal Performance Management makes it simple for anyone to achieve meaningful results from quantum computers at scale without needing to be quantum hardware experts. When running circuits with Fire Opal Performance Management, AI-driven error suppression techniques are automatically applied, enabling the scaling of larger problems with more gates and qubits. This approach reduces the number of shots required to reach the correct answer, with no added overhead — resulting in significant savings in both compute time and cost.

Performance Management suppresses errors and increases the probability of getting the correct answer on noisy hardware. In other words, it increases the signal-to-noise ratio. The following image shows how increased accuracy enabled by Performance Management can reduce the need for additional shots in the case of a 10-qubit Quantum Fourier Transform algorithm. With only 30 shots, Q-CTRL reaches the 99% confidence threshold, whereas the default (QiskitRuntimeSampler,optimization_level=3 andresilience_level=1,ibm_sherbrooke) requires 170,000 shots. By getting the right answer faster, you save significant compute runtime.

The Performance Management function can be used with any algorithm, and you can easily use it in place of the standardQiskit Runtime primitives. Behind the scenes, multiple error suppression techniques work together to prevent errors from happening at runtime. All Fire Opal pipeline methods are pre-configured and algorithm-agnostic, meaning you always get the best performance out of the box.

To get access to Performance Management,contact Q-CTRL.

Fire Opal Performance Management has two options for execution that are similar to the Qiskit Runtime primitives, so you can easily swap in the Q-CTRL Sampler and Estimator. The general workflow for using the Performance Management function is:

To reduce hardware noise, Fire Opal employs a range of AI-driven error suppression techniques depicted in the following image. With Fire Opal, the entire pipeline is completely automated with zero need for configuration.

Fire Opal's pipeline eliminates the need for additional overhead, such as increased quantum runtime or extra physical qubits. Note that classical processing time remains a factor (refer to theBenchmarkssection for estimates, where "Total time" reflects both classical and quantum processing). In contrast to error mitigation, which requires overhead in the form of sampling, Fire Opal's error suppression works at both the gate and pulse levels to address various sources of noise and to prevent the likelihood of an error occurring. By preventing errors, the need for expensive post-processing is eliminated.

The following image depicts the error suppression methods automated by Fire Opal Performance Management.

The function offers two primitives, Sampler and Estimator, and the inputs and outputs of both extend the implemented spec forQiskit Runtime V2 primitives.

Published algorithmic benchmarkingresults demonstrate significant performance improvement across various algorithms, including Bernstein-Vazirani, quantum Fourier transform, Grover’s search, quantum approximate optimization algorithm, and variational quantum eigensolver. The rest of this section provides more details about types of algorithms you can run, as well as the expected performance and runtimes.

The following independent studies demonstrate how Q-CTRL's Performance Management enables algorithmic research at record-breaking scale:

The following table provides a rough guide on accuracy and runtimes from prior benchmarking runs onibm_fez. Performance on other devices may vary. The usage time is based on an assumption of 10,000 shots per circuit. The "Number of qubits" indicated is not a hard limitation but represents rough thresholds where you can expect extremely consistent solution accuracy. Larger problem sizes have been successfully solved, and testing beyond these limits is encouraged.

Defining the accuracy of the measurement of an expectation value - the metricAAAis defined as follows:

whereϵideal\epsilon^{ideal}ϵideal= ideal expectation value,ϵmeas\epsilon^{meas}ϵmeas= measured expectation value,ϵmaxideal\epsilon^{ideal}_{max}ϵmaxideal​= ideal maximum value, andϵminideal\epsilon^{ideal}_{min}ϵminideal​= ideal minimum value.AmeanA_{mean}Amean​is simply the average of the value ofAAAacross multiple measurements.

This metric is used because it is invariant to global shifts and scaling in the range of attainable values. In other words, regardless of whether you shift the range of possible expectation values higher or lower or increase the spread, the value ofAAAshould remain consistent.

Authenticate using yourIBM Quantum Platform API key, and select the Qiskit Function as follows:

Use Fire Opal Performance Management's Estimator primitive to determine the expectation value of a single circuit-observable pair.

In addition to theqiskit-ibm-catalogandqiskitpackages, you will also use thenumpypackage to run this example. You can install this package by uncommenting the following cell if you are running this example in a notebook using the IPython kernel.

1. Create the circuit

As an example, generate a random Hermitian operator and an observable to input to the Performance Management function.

2. Run the circuit

Run the circuit and optionally define the backend and number of shots.

You can use the familiarQiskit Serverless APIsto check your Qiskit Function workload's status:

Output:

3. Retrieve the result

The results have the same format as anEstimator result:

Output:

QctrlEstimatorPubLikecomponents (derived from theQiskit Runtime PUB definition):

Supported observables formats:

Supported backends:The following list of backends are currently supported. If your device is not listed,reach out to Q-CTRLto add support.

Options:

Use Fire Opal Performance Management's Sampler primitive to run a Bernstein–Vazirani circuit. This algorithm, used to find a hidden string from the outputs of a black box function, is a common benchmarking algorithm because there is a single correct answer.

1. Create the circuit

Define the correct answer to the algorithm, the hidden bitstring, and the Bernstein–Vazirani circuit. You can adjust the width of the circuit by simply changing thecircuit_width.

2. Run the circuit

Run the circuit and optionally define the backend and number of shots.

Check your Qiskit Function workload'sstatusor returnresultsas follows:

Output:

3. Retrieve the result

Output:

3. Plot the top bitstrings

Plot the bitstring with the highest counts to see if the hidden bitstring was the mode.

The hidden bitstring is highlighted in purple, and it should be the bitstring with the highest number of counts.

Output:

QctrlSamplerPubLikecomponents (derived from theQiskit Runtime PUB definition):

Supported backends:The following list of backends are currently supported. If your device is not listed,reach out to Q-CTRLto add support.

Options:

For any questions or issues,contact Q-CTRL.

On this page

© IBM Corp., 2017-2025


---

# QESEM: A Qiskit Function by Qedma







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

While quantum processing units have vastly improved in recent years, errors due to noise and imperfections in existing hardware remain a central challenge for quantum algorithm developers. As the field approaches utility-scale quantum computations that cannot be verified classically, solutions for canceling noise with guaranteed accuracy are becoming increasingly important. To overcome this challenge, Qedma has developed Quantum Error Suppression and Error Mitigation (QESEM), seamlessly integrated on IBM Quantum Platform as aQiskit Function.

With QESEM, users can run their quantum circuits on noisy QPUs to obtain highly accurate error-free results with highly efficient QPU-time overheads, close to fundamental bounds. To achieve this, QESEM leverages a suite of propriety methods developed by Qedma, for the characterization and reduction of errors. Error reduction techniques include gate optimization, noise-aware transpilation, error suppression (ES), and unbiased error mitigation (EM). With this combination of these characterization-based methods, users can achieve reliable, error-free results for generic large-volume quantum circuits, unlocking applications that cannot be accomplished otherwise.

You can use the QESEM function by Qedma to easily estimate and execute your circuits with error suppression and mitigation, achieving larger circuit volumes and higher accuracies. To use QESEM, you provide a quantum circuit, a set of observables to measure, a target statistical accuracy for each observable, and a chosen QPU. Before you run the circuit to the target accuracy, you can estimate the required QPU time based on an analytical calculation that does not require circuit execution. Once you are satisfied with the QPU time estimation, you can execute the circuit with QESEM.

When you execute a circuit, QESEM runs a device characterization protocol tailored to your circuit, yielding a reliable noise model for the errors occurring in the circuit. Based on the characterization, QESEM first implements noise-aware transpilation to map the input circuit onto a set of physical qubits and gates, which minimizes the noise affecting the target observable. These include the natively available gates (CX/CZ on IBM® devices), as well as additional gates optimized by QESEM, forming QESEM’s extended gate set. QESEM then runs a set of characterization-based ES and EM circuits on the QPU and collects their measurement outcomes. These are then classically post-processed to provide an unbiased expectation value and an error bar for each observable, corresponding to the requested accuracy.

QESEM has been demonstrated to provide high-accuracy results for a variety of quantum applications and on the largest circuit volumes achievable today. QESEM offers the following user-facing features, demonstrated in the benchmarks section below:

QESEM has been tested on a wide variety of use cases and applications. The following examples can assist you with assessing which types of workloads you can run with QESEM.

A key figure of merit for quantifying the hardness of both error mitigation and classical simulation for a given circuit and observable isactive volume: the number of CNOT gates affecting the observable in the circuit. The active volume depends on the circuit depth and width, on the observable weight, and on the circuit structure, which determines the light cone of the observable. For further details, see the talk from the2024 IBM Quantum Summit. QESEM provides particularly large value in the high-volume regime, giving reliable results for generic circuits and observables.

Accuracy is measured here relative to the ideal value of the observable:⟨O⟩ideal−ϵ⟨O⟩ideal\frac{\langle O \rangle_{ideal} - \epsilon}{\langle O \rangle_{ideal}}⟨O⟩ideal​⟨O⟩ideal​−ϵ​, where 'ϵ\epsilonϵ' is the absolute precision of the mitigation (set by the user input), and⟨O⟩ideal\langle O \rangle_{ideal}⟨O⟩ideal​is the observable at the noiseless circuit.
'Runtime usage' measures the usage of the benchmark in batch mode (sum over usage of individual jobs), whereas 'total time' measures usage in session mode (experiment wall time), which includes additional classical and communication times. QESEM is available for execution in both modes, so that users can make the best use of their available resources.

The 28-qubit Kicked Ising circuits simulate the Discrete Time Quasicrystal studied by Shinjo et al. (seearXiv 2403.16718andQ2B24 Tokyo) on three connected loops of ibm_kawasaki. The circuit parameters taken here are(θx,θz)=(0.9π,0)(\theta_x, \theta_z) = (0.9 \pi, 0)(θx​,θz​)=(0.9π,0), with a ferromagnetic initial state∣ψ0⟩=∣0⟩⊗n| \psi_0 \rangle = | 0 \rangle ^{\otimes n}∣ψ0​⟩=∣0⟩⊗n. The measured observable is the absolute value of the magnetizationM=∣128∑i=027⟨Zi⟩∣M = |\frac{1}{28} \sum_{i=0}^{27} \langle Z_i \rangle|M=∣281​∑i=027​⟨Zi​⟩∣. The utility-scale Kicked Ising experiment was run on the 136 best qubits of ibm_fez; this particular benchmark was run at the Clifford angle(θx,θz)=(π,0)(\theta_x, \theta_z) = (\pi, 0)(θx​,θz​)=(π,0), at which the active volume grows slowly with circuit depth, which - together with the high device fidelities - enables high accuracy at a short runtime.

Trotterized Hamiltonian simulation circuits are for a Transverse-Field Ising model at fractional angles:(θzz,θx)=(π/4,π/8)(\theta_{zz}, \theta_x) = (\pi / 4, \pi /8)(θzz​,θx​)=(π/4,π/8)and(θzz,θx)=(π/6,π/8)(\theta_{zz}, \theta_x) = (\pi / 6, \pi / 8)(θzz​,θx​)=(π/6,π/8)correspondingly (seeQ2B24 Tokyo). The utility-scale circuit was run on the 119 best qubits of ibm_brisbane, whereas the 40-qubit experiment was run on the best available chain. The accuracy is reported for the magnetization; high-accuracy results were obtained for higher-weight observables as well.

The VQE circuit was developed together with researchers from the Center for Quantum Technology and Applications at the Deutsches Elektronen-Synchrotron (DESY). The target observable here was a Hamiltonian consisting of a large number of non-commuting Pauli strings, emphasizing QESEM's optimized performance for multi-basis observables. Mitigation was applied to a classically-optimized ansatz; although these results are still unpublished, results of the same quality will be obtained for different circuits with similar structural properties.

Authenticate using yourIBM Quantum Platform API token, and select the QESEM Qiskit Function as follows:

To get started, try this basic example of estimating the required QPU time to run QESEM for a givenpub:

The following example executes a QESEM job:

You can use the familiar Qiskit Serverless APIs to check your Qiskit Function workload's status or return results:

Output:

estimate_time_only- This flag enables users to obtain an estimate for the QPU time required to execute the circuit with QESEM.

max_execution_time: Allows you to limit the QPU time, specified in seconds, to be used for the entire QESEM process. Since the final QPU time required to reach the target accuracy is determined dynamically during the QESEM job, this parameter enables you to limit the cost of the experiment. If the dynamically-determined QPU time is shorter than the time allocated by the user, this parameter will not affect the experiment. Themax_execution_timeparameter is particularly useful in cases where the analytical time estimate provided by QESEM before the job starts is too pessimistic and the user wants to initiate a mitigation job anyway. After the time limit it reached, QESEM stops sending new circuits. Circuits that have already been sent continue running (so the total time may surpass the limit by up to 30 minutes), and the user receives the processed results from the circuits that ran up to that point. If you want to apply a QPU time limit shorter than the analytical time estimate, consult with Qedma to obtain an estimate for the accuracy achievable within the time limit.

transpilation_level: After a circuit is submitted to QESEM, it automatically prepares several alternative circuit transpilations and chooses the one that minimizes QPU time. For instance, alternative transpilations might utilize Qedma-optimized fractional RZZ gates to reduce the circuit depth. Of course, all transpilations are equivalent to the input circuit, in terms of their ideal output. To exert more control over the circuit transpilation, set the transpilation level in theoptions. While"transpilation_level": 1corresponds to the default behavior described above,"transpilation_level": 0includes only minimal modifications required to the original circuit; for example, ‘layerification’ - the organization of circuit operations into ‘layers’ of simultaneous two-qubit gates. Note that automatic hardware-mapping onto high-fidelity qubits is applied in any case.

Barrier operations are typically used to specify the layers of two-qubit gates in quantum circuits. In level 0, QESEM preserves the layers specified by the barriers. In level 1, the layers specified by the barriers are considered as one transpilation alternative when minimizing QPU time.

The output of a Circuit function is aPrimitiveResult, which contains two fields:

OnePubResultobject. It can be indexed directly from thePrimitiveResult.

Job-level metadata.

EachPubResultcontains adataand ametadatafield.

Thedatafield contains at least an array of expectation values (PubResult.data.evs) and an array of standard errors (PubResult.data.stds). It can also contain more data, depending on the options used.

Themetadatafield contains PUB-level metadata (PubResult.metadata).

The following code snippet describes how to retrieve the QPU time estimation (estimate_time_onlyis set):

Output:

The following code snippet describes how to retrieve the mitigation results (estimate_time_onlyis not set).

Output:

If your workload status is ERROR, use job.result() to fetch the error message to fetch the error message as follows:

Output:

The Qedma support team is here to help! If you encounter any issues or have questions about using the QESEM Qiskit Function, please don't hesitate to reach out. Our knowledgeable and friendly support staff are ready to assist you with any technical concerns or inquiries you may have.

You can email us at[email protected]for assistance. Please include as much detail as possible about the issue you're experiencing to help us provide a swift and accurate response. You can also contact your dedicated Qedma POC representative via email or phone.

To help us assist you more efficiently, please provide the following information when you contact us:

We are committed to providing you with prompt and effective support to ensure you have the best possible experience with our Qiskit Function.

We are always looking to improve our product and we welcome your suggestions! If you have ideas on how we can enhance our services or features you'd like to see, please send us your thoughts at[email protected]

On this page

© IBM Corp., 2017-2025


---

# Iskay Quantum Optimizer - A Qiskit Function by Kipu Quantum







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

With the Iskay Quantum Optimizer by Kipu Quantum, you can tackle complex optimization problems using IBM® quantum computers. This solver leverages Kipu's cutting-edgebf-DCQO algorithmrequiring only the objective function as input to automatically deliver problem solutions. It can handle optimization problems involving up to 156 qubits, enabling the use of all qubits of the IBM quantum devices. The Optimizer uses a 1-to-1 mapping between classical variables and qubits, which allows you to tackle optimization problems with up to 156 binary variables.

The Optimizer enables the solving of unconstrained binary optimization problems. In addition to the commonly used QUBO (Quadratic Unconstrained Binary Optimization) formulation, it also supports higher-order (HUBO) optimization problems. The solver utilizes a non-variational quantum algorithm, performing most of the computation on quantum devices.

The following provides more details about the used algorithm and a brief guide on how to use the function, as well as benchmarking results on various problem instances of different sizes and complexities.

The Optimizer is a ready-to-use implementation of cutting-edge quantum optimization algorithms. It solves optimization problems by running highly-compressed quantum circuits on quantum hardware. This compression is achieved by introducing counterdiabatic terms into the underlying time evolution of the quantum system. The algorithm executes several iterations of hardware runs to obtain the final solutions and combines it with post-processing. These steps are seamlessly integrated into the Optimizer's workflow and are executed automatically.

This section outlines the basics of the implemented bf-DCQO algorithm. An introduction to the algorithm can also be found on theQiskit YouTube channel.

The algorithm is based on the time evolution of a quantum system which is transformed over time, where the problem solution is encoded in the ground state of the quantum system at the end of the evolution. According to theadiabatic theorem, this evolution has to be slow to ensure the system remains in its ground state. Digitizing this evolution is the basis of digitized quantum adiabatic computation (DQA) and the infamous QAOA algorithm. However, the required slow evolution is not feasible for increasing problem sizes since it results in an increasing circuit depth. By using counterdiabatic protocols, you can suppress unwanted excitations occurring during short evolution times while remaining in the ground state. Here, digitizing this shorter evolution time results in quantum circuits with shorter depth and fewer entangling gates.

The circuits of the bf-DCQO algorithms typically use up to ten times fewer entangling gates than DQA, and three to four times fewer entangling gates than standard QAOA implementations. Because of the smaller number of gates, fewer errors occur during the circuit execution on hardware. Hence, the optimizer does not require using techniques like error suppression or error mitigation. Implementing them in future versions can enhance the solution quality even further.

Although the bf-DCQO algorithm uses iterations, it is non-variational. After each iteration of the algorithm, the distribution of states is measured. The obtained distribution is used to calculate a so-called bias-field. The bias-field allows starting the next iteration from an energy state near the previously found solution. In this way, the algorithm moves with each iteration to solutions of lower energy. Typically, approximately ten iterations are sufficient to converge to a solution, in total requiring a much lower number of iterations than variational algorithms, which is on the order of  approximately 100 iterations.

The optimizer combines the bf-DCQO algorithm with classical post-processing. After measuring the distribution of states, a local search is performed. During the local search, the bits of the measured solution are randomly flipped. After the flip, the energy of the new bitstring is evaluated. If the energy is lower, the bitstring is kept as the new solution. The local search only scales linearly with the number of qubits; hence, it is computationally cheap. Since the post-processing corrects local bitflips, it compensates for bit-flip errors that often are the result of hardware imperfections and readout errors.

A schematic of the workflow of the Quantum Optimizer follows.

By using the Quantum Optimizer, solving an optimization problem on quantum hardware can be reduced to

The benchmark metrics below show that the Optimizer effectively addresses problems involving up to 156 qubits and offer a general overview of the optimizer's accuracy and scalability across different problem types. Note that actual performance metrics may vary depending on specific problem characteristics, such as the number of variables, the density and locality of terms in the objective function, and the polynomial order.

The following table includes the approximation ratio (AR), a metric defined as follows:

whereCCCis the objective function,CminC_{\textrm{min}}Cmin​,CmaxC_{\textrm{max}}Cmax​are its minimum and maximum values, andC∗C^{*}C∗is the cost of the best solution found, respectively. Therefore, AR=100% means that the ground state of the problem has been obtained.

All the benchmark instances are accessible on GitHub (seeKipu benchmark instances). An example to run these instances can be found inExample 3: Benchmark instances.

See the following table for all input parameters the Quantum Optimizer accepts.  The subsequentOptionssection goes into more details about the availableoptions.

Theproblemandproblem_typearguments encode an optimization problem of the form

where

The coefficients of the problem should be encoded in a dictionary as follows:

The hyper-parameters of the algorithm are set automatically. However, you can fine-tune the algorithm by exposing parameters to the user. For example, you can select the number of iterations of the algorithm.

This is a dictionary containing the details of the solution found by the optimizer. It contains the following items:

Note that thesolutiondictionary is obtained from the solution bitstring, using themappingobject for indexing the variables. Whenproblem_type=spinwe use the assignment1→−1,0→11 \rightarrow -1, \quad 0 \rightarrow 11→−1,0→1.

Authenticate using yourIBM Quantum® Platform API token, and select the Qiskit Function as follows:

The following code assumes that you have saved your credentials. If you have not, follow the instructions inSet up an IBM Quantum channelto authenticate with your API key.

Consider the cost function in spin formulation:

where(x0,...,x4)∈{−1,1}5(x_0, ..., x_4) \in \{-1, 1\}^5(x0​,...,x4​)∈{−1,1}5.

The solution to this simple cost function is

with minimum valueC∗=−6C^{*} = -6C∗=−6

We start by creating a dictionary with the coefficients of the objective function as follows:

We solve the problem by running the optimizer. Since(x0,...,x4)∈{−1,1}5(x_0, ..., x_4) \in \{-1, 1\}^5(x0​,...,x4​)∈{−1,1}5we must setproblem_type=spin.

The solution of the optimization problem is provided directly from the optimizer.

This will show a dictionary of the form:

Notice that the dictionarysolutiondisplays the result vector(x0,x1,x2,x3,x4)=(−1,−1,−1,1,1)(x_0, x_1, x_2, x_3, x_4) = (-1, -1, -1, 1, 1)(x0​,x1​,x2​,x3​,x4​)=(−1,−1,−1,1,1).

Many graph problems like MaxCut or Maximum independent set are NP-hard problems and ideal candidates for testing quantum algorithms and hardware. This example demonstrates solving the MaxCut problem of a 3-regular graph with the Quantum Optimizer.

To run this example you must install thenetworkxpackage in addition to theqiskit-ibm-catalog. To install it, run the following command:

Start by generating a random 3-regular graph. For this graph, we define the objective function of the MaxCut problem.

Solve the problem by running the optimizer.

Retrieve the result and map the solution bitstring back to the original graph nodes.

The solution to the Maxcut problem is directly contained in thesolutionsub-dictionary of the result object

The benchmark instances are available on GitHub:Kipu benchmark instances.

The instances can be loaded using thepygithublibrary. To install it, run the following command:

The paths for the benchmark instances are:

Maxcut:

HUBO:

To reproduce the performance of the benchmark for the HUBO instances, select the backendibm_marrakeshand setdirect_qubit_mappingtoTruein theoptionssub-dictionary.

The following example runs the Maxcut instance with 32 nodes.

Typical use cases for the Optimization solver are combinatorial optimization problems. You can solve problems from many industries like finance, pharmaceutics, or logistics. Some examples follow.

If you are interested in tackling a specific use case and develop a dedicated mapping, we can assist you.Contact us.

For support, contact[email protected].

Request access to the Quantum Optimizer by Kipu Quantum

Iskay, like our company name Kipu Quantum, is a Peruvian word. Although we are a startup from Germany, these words come from the native country of one of our co-founders, where the Quipu was one of the very first calculation machines developed by mankind 2000 years BCE.

On this page

© IBM Corp., 2017-2025


---

# Singularity Machine Learning - Classification: A Qiskit Function by Multiverse Computing







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

With the "Singularity Machine Learning - Classification" function, you can solve real-world machine learning problems on quantum hardware without requiring quantum expertise. This Application function, based on ensemble methods, is a hybrid classifier. It leverages classical methods like boosting, bagging, and stacking for initial ensemble training. Subsequently, quantum algorithms such as variational quantum eigensolver (VQE) and quantum approximate optimization algorithm (QAOA) are employed to enhance the trained ensemble's diversity, generalization capabilities, and overall complexity.

Unlike other quantum machine learning solutions, this function is capable of handling large-scale datasets with millions of examples and features without being limited by the number of qubits in the target QPU. The number of qubits only determines the size of the ensemble that can be trained. It is also highly flexible, and can be used to solve classification problems across a wide range of domains, including finance, healthcare, and cybersecurity.

It consistently achieves high accuracies on classically challenging problems involving high-dimensional, noisy, and imbalanced datasets.

It is built for:

The following example showcases its various functionalities, includingcreate,list,fit, andpredict, and demonstrates its usage in a synthetic problem comprising two interleaving half circles, a notoriously challenging problem due to its nonlinear decision boundary.

This Qiskit Function allows users to solve binary classification problems using Singularity's quantum-enhanced ensemble classifier. Behind the scenes, it uses a hybrid approach to classically train an ensemble of classifiers on the labeled dataset, and then optimize it for maximum diversity and generalization using the Quantum Approximate Optimization Algorithm (QAOA) on IBM® QPUs. Through a user-friendly interface, users can configure a classifier according to their requirements, train it on the dataset of their choice, and use it to make predictions on a previously unseen dataset.

To solve a generic classification problem:

The function uses an action-based approach. You can think of it as a virtual environment where you use actions to perform tasks or change its state. Currently, it offers the following actions:list,create,delete,fit,predict,fit_predict, andcreate_fit_predict. The following example demonstrates thecreate_fit_predictaction.

Output:

Thelistaction retrieves all stored classifiers in*.pkl.tarformat from the shared data directory. You can also access the contents of this directory by using thecatalog.files()method. In general, the list action searches for files with the*.pkl.tarextension in the shared data directory and returns them in a list format.

Thecreateaction creates a classifier of the specifiedquantum_classifiertype by using the provided parameters, and saves it in the shared data directory.

The function currently supports only theQuantumEnhancedEnsembleClassifier.

Thedeleteaction removes a classifier from the shared data directory.

Thefitaction trains a classifier using the provided training data.

Thepredictaction is used to obtain hard and soft predictions (probabilities).

Thefit_predictaction trains a classifier using the training data and then uses it to obtain hard and soft predictions (probabilities).

name:

options["out"]:

Thecreate_fit_predictaction creates a classifier, trains it using the provided training data, and then uses it to obtain hard and soft predictions (probabilities).

name:

options["out"]:

Authenticate using yourIBM Quantum Platform API token, and select the Qiskit Function as follows:

In this example, you'll use the "Singularity Machine Learning - Classification" function to classify a dataset consisting of two interleaving, moon-shaped half-circles. The dataset is synthetic, two-dimensional, and labeled with binary labels. It is created to be challenging for algorithms such as centroid-based clustering and linear classification.

Through this process, you'll learn how to create the classifier, fit it to the training data, use it to predict on the test data, and delete the classifier when you're finished.

Before starting, you need to installscikit-learn. Install it using the following command:

Perform the following steps:

Step 1.Import the necessary modules and generate the synthetic dataset, then split it into training and test datasets.

Output:

Step 2.Save the labeled training and test datasets on your local disk, and then upload them to theshared data directory.

Output:

Step 3.Create a quantum-enhanced classifier using thecreateaction.

Output:

Output:

Step 4.Train the quantum-enhanced classifier using thefitaction.

Output:

Step 5.Obtain predictions and probabilities from the quantum-enhanced classifier using thepredictaction.

Output:

Step 6.Delete the quantum-enhanced classifier using thedeleteaction.

Output:

Step 7.Clean up local and shared data directories.

These benchmarks show that the classifier can achieve extremely high accuracies on challenging problems. They also show that increasing the number of learners in the ensemble (number of qubits) can lead to increased accuracy.

"Classical accuracy" refers to the accuracy obtained using corresponding classical state of the art which, in this case, is an AdaBoost classifier based on an ensemble of size 75. "Quantum accuracy", on the other hand, refers to the accuracy obtained using the "Singularity Machine Learning - Classification".

As quantum hardware evolves and scales, the implications for our quantum classifier become increasingly significant. While the number of qubits does impose limitations on the size of the ensemble that can be utilized, it does not restrict the volume of data that can be processed. This powerful capability enables the classifier to efficiently handle datasets containing millions of data points and thousands of features. Importantly, the constraints related to ensemble size can be addressed through the implementation of a large-scale version of the classifier. By leveraging an iterative outer-loop approach, the ensemble can be dynamically expanded, enhancing flexibility and overall performance. However, it's worth noting that this feature has not yet been implemented in the current version of the classifier.

For any questions,reach out to Multiverse Computing.

Be sure to include the following information:

On this page

© IBM Corp., 2017-2025


---

# Optimization Solver: A Qiskit Function by Q-CTRL Fire Opal







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Qiskit Functions are an experimental feature available only to IBM Quantum® Premium Plan users. They are in preview release status and subject to change.

With the Fire Opal Optimization Solver, you can solve utility-scale optimization problems on quantum hardware without requiring quantum expertise. Simply input the high-level problem definition, and the Solver takes care of the rest. The entire workflow is noise-aware and leveragesFire Opal's Performance Managementunder the hood. The Solver consistently delivers accurate solutions to classically challenging problems, even at full-device scale on the largest IBM® QPUs.

The Solver is flexible and can be used to solve combinatorial optimization problems defined as objective functions or arbitrary graphs. Problems do not have to be mapped to device topology. Both unconstrained and constrained problems are solvable, given that constraints can be formulated as penalty terms. The examples included in this guide demonstrate how to solve an unconstrained and a constrained utility-scale optimization problem using different Solver input types. The first example involves a Max-Cut problem defined on a 156-node, 3-Regular graph, while the second example tackles a 50-node Minimum Vertex Cover problem defined by a cost function.

To get access to the Optimization Solver,contact Q-CTRL.

The Solver fully optimizes and automates the entire algorithm, from error suppression at the hardware level to efficient problem mapping and closed-loop classical optimization. Behind the scenes, the Solver's pipeline reduces errors at every stage, enabling the enhanced performance required to meaningfully scale. The underlying workflow is inspired by the Quantum Approximate Optimization Algorithm (QAOA), which is a hybrid quantum-classical algorithm. For a detailed summary of the full Optimization Solver workflow, refer tothe published manuscript.

To solve a generic problem with the Optimization Solver:

Accepted problem formats:

Supported backends:The following list of backends are currently supported. If your device is not listed,reach out to Q-CTRLto add support.

Options:

Result dictionary contents:

Published benchmarking resultsshow that the Solver successfully solves problems with over 120 qubits, even outperforming previously published results on quantum annealing and trapped-ion devices. The following benchmark metrics provide a rough indication of the accuracy and scaling of problem types based on a few examples. Actual metrics may differ based on various problem features, such as the number of terms in the objective function (density) and their locality, number of variables, and polynomial order.

The "Number of qubits" indicated is not a hard limitation but represents rough thresholds where you can expect extremely consistent solution accuracy. Larger problem sizes have been successfully solved, and testing beyond these limits is encouraged.

Arbitrary qubit connectivity is supported across all problem types.

First, authenticate using yourIBM Quantum API token. Then, select the Qiskit Function as follows:

Run themaximum cut(Max-Cut) problem. The following example demonstrates the Solver's capabilities on a 156-node, 3-regular unweighted graph Max-Cut problem, but you can also solve weighted graph problems.

In addition toqiskit-ibm-catalog, you will also use the following packages to run this example:networkxandnumpy. You can install these packages by uncommenting the following cell if you are running this example in a notebook using the IPython kernel.

You can run a Max-Cut problem by defining a graph problem and specifyingproblem_type='maxcut'.

Output:

The Solver accepts a string as the problem definition input.

When using the graph-based input method, specify the problem type.

Check your Qiskit Function workload'sstatusor returnresultsas follows:

Output:

Retrieve the optimal cut value from the results dictionary.

Output:

You can verify the accuracy of the result by solving the problem classically with open-source solvers likePuLPif the graph is not densely connected. High density problems may require advanced classical solvers to validate the solution.

The prior Max-Cut example is a common quadratic unconstrained binary optimization problem. Q-CTRL's Optimization Solver can be used for various problem types, including constrained optimization. You can solve arbitrary problem types by inputting the problem definition represented as a polynomial where constraints are modeled as penalty terms.

The following example demonstrates how to construct a cost function for a constrained optimization problem,minimum vertex cover(MVC).

In addition to theqiskit-ibm-catalogandqiskitpackages, you will also use the following packages to run this example:numpy,networkx, andsympy. You can install these packages by uncommenting the following cell if you are running this example in a notebook using the IPython kernel.

Define a random MVC problem by generating a graph with randomly weighted nodes.

Output:

A standard optimization model for weighted MVC can be formulated as follows. First, a penalty must be added for any case where an edge is not connected to a vertex in the subset. Therefore, letni=1n_i = 1ni​=1if vertexiiiis in the cover (i.e., in the subset) andni=0n_i = 0ni​=0otherwise. Second, the goal is to minimize the total number of vertices in the subset, which can be represented by the following function:

Minimizey=∑i∈Vωini\textbf{Minimize}\qquad y = \sum_{i\in V} \omega_i n_iMinimizey=∑i∈V​ωi​ni​

Now every edge in the graph should include at least one end point from the cover, which can be expressed as the inequality:

ni+nj≥1forall(i,j)∈En_i + n_j \ge 1 \texttt{ for all } (i,j)\in Eni​+nj​≥1for all(i,j)∈E

Any case where an edge is not connected to the vertex of cover must be penalized. This can be represented in the cost function by adding a penalty of the formP(1−ni−nj+ninj)P(1-n_i-n_j+n_i n_j)P(1−ni​−nj​+ni​nj​)wherePPPis a positive penalty constant. Thus, an unconstrained alternative to the constrained inequality for weighted MVC is:

Minimizey=∑i∈Vωini+P(∑(i,j)∈E(1−ni−nj+ninj))\textbf{Minimize}\qquad y = \sum_{i\in V}\omega_i n_i + P(\sum_{(i,j)\in E}(1 - n_i - n_j + n_i n_j))Minimizey=∑i∈V​ωi​ni​+P(∑(i,j)∈E​(1−ni​−nj​+ni​nj​))

Check your Qiskit Function workload'sstatusor returnresultsas follows:

Retrieve the solution and analyze the results. Because this problem has weighted nodes, the solution is not simply the minimum number of nodes covered. Instead, the solution cost represents the sum of the weights of the vertices that are included in the vertex cover. It represents the total "cost" or "weight" of covering all the edges in the graph using the selected vertices.

Output:

For any questions or issues,reach out to Q-CTRL.

On this page

© IBM Corp., 2017-2025


---

# Quantum Portfolio Optimizer: A Qiskit Function by Global Data Quantum







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit Functions are an experimental feature available only to IBM Quantum® Premium Plan and Flex Plan users. They are in preview release status and subject to change.

The Quantum Portfolio Optimizer is a Qiskit Function that tackles the dynamic portfolio optimization problem, a standard problem in finance that aims to rebalance periodic investments across a set of assets, to maximize returns and minimize risks. By deploying cutting-edge quantum optimization techniques, this function simplifies the process so that users, with no expertise in quantum computing, can benefit from its advantages in finding optimal investment trajectories. Ideal for portfolio managers, researchers in quantitative finance, and individual investors, this tool enables back-testing of trading strategies in portfolio optimization.

The Quantum Portfolio Optimizer function uses the Variational Quantum Eigensolver (VQE) algorithm to solve a Quadratic Unconstrained Binary Optimization (QUBO) problem, addressing dynamic portfolio optimization problems. Users simply need to provide the asset price data and define the investment constraint, then the function runs the quantum optimization process that returns a set of optimized investment trajectories.

The process consists of four main stages. First, the input data is mapped to a quantum-compatible problem, constructing the QUBO of the dynamic portfolio optimization problem, and transforming it into a quantum operator (Ising Hamiltonian). Next, the input problem and the VQE algorithm are adapted to be run in the quantum hardware. The VQE algorithm is then run on the quantum hardware, and finally, the results are post-processed to provide the optimal investment trajectories. The system also includes a noise-aware (SQD-based) post-processing to maximize the quality of the output.

This Qiskit Function is based on thepublished manuscriptby Global Data Quantum.

The input arguments of the function are described in the following table. The assets data and other problem specifications must be provided; additionally, the VQE settings can be included to customize the optimization process.

*To resume an execution or retrieve jobs that were processed in one or more previous sessions, the list of session IDs must be passed in theprevious_session_idparameter. This is particularly useful in cases where an optimization task failed to complete due to any error in the process, and execution needs to finish. To achieve this, you must provide the same arguments used in the initial execution, along with theprevious_session_idlist as described.

Loading data for previous sessions (for resuming an optimization) can take up to one hour.

The data must be structured as a JSON object that stores information about the closing prices of financial assets on specific dates. The format is as follows:

Note that all dictionaries must have the same secondary key (dates). If a specific asset lacks a date that others have, the data must be filled to ensure consistency. For example, this can be done by using the last tracked closing price of that asset.

The asset data must contain, at least, the closing prices at(nt+1) * dt(see thequbo_settingsinput section) time stamps (for example, days).

The next table describes the keys of thequbo_settingsdictionary. Build the dictionary specifying the number of time stepsnt, the number of resolution qubitsnq, and themax_investment- or change other default values.

To modify the default options, create a dictionary for theansatz_settingsparameter with the following keys. By default, the ansatz is set to"real_amplitudes", and both extra options (see the following table) are set toFalse.

* Available ansatzes

** Ifmultiple_passmanageris set toFalse, the function uses the default Qiskit pass manager withoptimization_level=3. If set toTrue, themultiple_passmanagersubroutine compares three pass managers: the previous default Qiskit pass manager, a pass manager mapping qubits over the QPU first neighbors chain, and theAI transpilerservices. Then, the pass manager with the estimated lower cumulative error is selected.

This parameter is a dictionary with some tunable options of the optimizing process.

Currently, the only optimizer option available is"differential_evolution".

Underprimitive_optionsandoptimizer_optionskeys we set dictionaries with the following parameters:

The number of generations evaluated by the differential evolution isnum_generations+ 1 since the initial population is included.

The total number of circuits is calculated as(num_generations + 1) * population_size.

Using a larger population size and more generations generally improves the quality of the optimization results. However, it is not recommended to exceed a population size of 120 and a number of generations greater than 20 (for example,120 * 21 = 2520total circuits), as this would generate an excessive number of circuits, which can be computationally expensive and time-consuming to process.

The function allows you to resume previous optimization, and it is always possible to increase the number of generations (by providing the same input except forprevious_session_idand an increasednum_generations).

Ensure compliance with Qiskit Runtime job limits.

See theJob limitsguide for more information.

The function returns two dictionaries:"result"dictionary, containing the best optimization results, including the optimal solution and its associated minimum objective cost; and"metadata", with data from all results obtained during the optimization process, along with their respective metrics.

The first dictionary focuses on the best-performing solution, while the second provides detailed information about all solutions, including states, objective costs, and other relevant metrics.

Authenticate using yourAPI keyand select the Qiskit Function as follows:

This example demonstrates how to execute the dynamic portfolio optimization (DPO) function and adjust its settings for optimal performance. It includes detailed steps for fine-tuning the parameters to achieve the desired outcomes.

This case involves seven assets, four time steps, and four resolution qubits, resulting in a total requirement of 112 qubits.

If all the assets in the portfolio are stored in a folder at a specific path, you can load them into apandas.DataFrameand convert it to adictformat object using the following function.

For this example, we have used the assets8801.T,CLF,GBPJPY,ITX.MC,META,TMBMKDE-10Y, andXS2239553048. The following figure illustrates the data used in this example, showing the daily closing price evolution of the assets from 1 January to 1 September in 2023.

In this example, to ensure uniformity across dates, we have filled non-trading days with the closing price from the previous available date. We apply this step because the selected assets come from different markets with varying trading days, making it essential to standardize the dataset for consistency.

Define the specifications of the problem by configuring the parameters in thequbo_settingsdictionary.

Optionally define specific requirements for the optimization process, including the selection of the optimizer and its parameters, as well as the specification of the primitive and its configurations.

For the Tailored Ansatz, the chosen population size was based on previous experiments showing that this value yields stable and efficient optimization.

In the case of the Real Amplitudes Ansatz, you can follow a linear relationship between thepopulation_sizeand the number of qubits in the circuit. As an approximated rule of thumb, it is recommended to use aminimumpopulation_size ~ 0.8 * n_qubitsfor thereal_amplitudesansatz.

It is expected that the Optimized Real Amplitudes will have a better optimization performance than the Real Amplitudes ansatz. However, the number of variables to optimize in this ansatz increases much faster than in the Real Amplitudes case (see themanuscript). Thus, for large problems, the Optimized Real Amplitudes requires more circuit executions. The Optimized Real Amplitudes is likely to be useful for problems requiring up to 100 qubits, but it is recommended to be mindful when setting thepopulation_sizeparameters. As an example of this scale-up inpopulation_size, the previous table shows that for an 84-qubit problem, the Optimize Real Amplitudes requires 120population_size, while for a 56-qubit problem, apopulation_sizeof 40 is enough.

It is also possible to choose a specific ansatz. The following uses the'Tailored'ansatz.

As mentioned in theOutputsection, the function returns a dictionary with the investment trajectories ordered from lowest to highest according to their objective function value. This set of results allows for the identification of the trajectory with the lowest cost and its corresponding investment evaluations. Additionally, it provides for the analysis of different trajectories, facilitating the selection of those that best align with specific needs or objectives. This flexibility ensures that choices can be tailored to suit a variety of preferences or scenarios.

Begin by presenting the resulting strategy that achieved the lowest objective cost found during the process.

Output:

Afterwards, using the metadata, you can access the results of all the sampled strategies. You can thereby further analyze the alternative trajectories returned by the optimizer. To do this, read the dictionary stored indpo_result['metadata']['all_postprocessed_samples'], which contains not only additional information about the optimal strategy, but also details of the other candidate strategies evaluated during the optimization.

The following example shows how to read this information usingpandasto extract key metrics associated with the optimal strategy. These include the binary solution state, Restriction Deviation, Sharpe Ratio, and the corresponding investment return.

Output:

Last, analyze the performance of your optimization application. Specifically, compare your results, obtained in the previous example, against a random baseline to assess the effectiveness of our approach. If the quantum algorithm demonstrably and consistently produces results with lower cost values, it indicates an effective optimization process.

The figure presents the probability distributions of the objective costs. To generate these distributions, take the list of objective costs from the function result and count the occurrences of each cost value (values rounded to the second decimal place). Then, update the count column accordingly by joining counts of identical rounded values. Note that, for better visual comparison, the occurrence counts have been normalized so that each distribution is displayed between 0 and 1.

As shown in the figure (blue solid line), the cost distribution for our Variational Quantum Eigensolver (post-processed with SQD) approach is sharply concentrated at lower objective cost values, indicating good optimization performance. In contrast, the noisy baseline exhibits a broader distribution, centered around higher cost values. The gray dashed vertical line represents the mean value of the random distribution, further highlighting the consistency of the function in returning optimized investment strategies. For an additional comparison, the black dashed line in the figure corresponds to the solution obtained with the Gurobi optimizer (free version). All these results are further explored in the benchmarks below for the "Mixed Assets" example evaluated with the "Tailored" ansatz.

This function was tested under different configurations of resolution qubits, ansatz circuits, and groupings of assets from various sectors: a mix of different assets (Set 1), oil derivatives (Set 2), and IBEX35 (Set 3). See more details in the following table.

Two key metrics were used to evaluate solution quality.

Together, these metrics benchmark both computational and financial aspects of the quantum-generated portfolios.

Results show that the quantum optimizer, with problem-specific ansatzes, effectively identifies efficient investment strategies across various portfolio types.

Below we detail both the population size and the number of generations specified in theoptimizer_optionsdictionary. All other parameters were set to their default values.

The number of generations was set to 20, as this value was found to be sufficient to reach convergence. Additionally, the default values for the optimizer's internal parameters were left unchanged, as they consistently provided good performance and are generally recommended by the literature and implementation guidelines.

If you need help, you can send an email to[email protected]. In your message, provide the function job ID.

On this page

© IBM Corp., 2017-2025


---

# QURI Chemistry: a Qiskit Function by QunaSys







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This function helps you solve the quantum chemistry ground state estimation problem by using one of two algorithms based on theQuantum Selected Configuration Interaction (QSCI) algorithm:

The overall procedure for using this function is summarized in the following flow chart:

The QSCI algorithm samples from a specific ansatz on quantum computers. Each sampled bitstring corresponds to an electron configuration, and the number of times a bitstring is sampled represents the importance of that electron configuration. Choose a number,RRR, to select theRRRmost important electron configurations from the sample. The function constructs and diagonalizes the subspace Hamiltonian, depending on your choice ofRRR. The smallest eigenvalue is called "QSCI energy" and is the estimation of the QSCI algorithm's true ground state energy.

One important QSCI ingredient is its initial state preparations. Several possible initial state preparations are provided in this function. These include thehardware efficient,UCCSD,kUpCCGSD, andkuCJansatzes. A CCSD amplitude-based double excitation ansatz is provided specifically to be executed on near-term devices. Ansatz-specific settings are also provided for you to customize according to your needs.

In addition to returning the QSCI energy, the function also computes the estimated ground state wave function to help you identify the important electron configurations.

First, authenticate using yourIBM Quantum® API keyand select the Qiskit Function as follows:

The function is called with the following arguments:

Each argument is described in following table.

Refer to theSpecify an instance in your codeguide to learn more.

Specify the details about the molecule here. The input is the same as thepyscf.gto.Mwith an additionalactive_spaceoption. Detailed settings for configuring a molecule are summarized in the following table.

The active space settings are summarized below.

Thecircuit_optionsfield should be a dictionary containing detailed settings of the circuit for running the QSCI algorithm - for example, the state preparation settings. In general it should take this form:

Each field is explained in the subsequent sections.

Theansatzstring specifies the ansatz to use. This specifies a type of parametric circuit without specifying what the concrete circuit parameters are.state_prep_methodspecifies how the circuit parameter is prepared. Finally, theansatz_settinglets you  customize the ansatz.

Whenmethodis "QSCI", only the "CCSD" preparation method is supported. The "Random" preparation method is only supported when method = "OPT_QSCI".

Detailed settings for UCCSD ansatz can be found in theQURI Parts documentation. Thereduce_parameteroption is the same as thesinglet_excitationoption in the QURI Parts documentation.

Detailed settings for KUpCCGSD ansatz can be found in theQURI Parts documentation.

Usually, the problem at hand needs to respect some symmetry, especially particle number and spin conservation. To restore symmetry, use symmetry post-selection orconfiguration recoveryerror mitigation. You can choose either of them with themitigation_settingfield in either algorithm. Symmetry post-selection is the default value.

post-selectionremoves the erroneous states completely, leaving only the basis states to construct the subspace Hamiltonian. This usually saves classical resources, but might miss many states. Configuration recovery attempts to flip individual bits in erroneous basis states with respect to some probability distribution. Using configuration recovery increases the number of basis states to build a larger subspace Hamiltonian, but it uses a lot more classical resources.

The options are explained in the following table.

You cannot set spin symmetry to True when particle symmetry is False.

These keys control the symmetry post-selection:particle_number_symmetryandspin_symmetry. Settingparticle_number_symmetryto True selects those states that conserve the total electron numbers.  Settingspin_symmetryto True selects those states that conserve theszs_zsz​quantum number. Currently onlysz=0s_z = 0sz​=0is supported. The default is:

Instead of the symmetry post-selection, you can choose to do configuration recovery. To turn it on, set it toTrue, and optionally customize it with a dictionary containing the following parameters:

Other error mitigations are not allowed when configuration recovery is turned on.

The output of the function contains these fields:

Thestate_vectorfield is a dictionary containing these fields:

This example shows you how to compute the ground state energy of the water molecule using the QSCI algorithm.

First, configure the setting for aH2OH_2OH2​Omolecule in JSON format. The coordinates of the water molecule can be loaded fromOpenFermion.

All the function input is in JSON format. You will set up a JSON string that specifies the options for running an algorithm. As stated previously, the two types of algorithms provided are "QSCI" and "OPT_QSCI".

First, set up the number of shots and the maximum subspace Hamiltonian size with theqsci_settingfield.

Next, set up the ansatz. This example uses theDoubleExcitationas the ansatz because it carries the most non-trivial information with the lowest circuit depth. You can specify how many excitation amplitudes to include with then_amplitudeskey in theansatz_settingfield. The default value is 10. The function sorts the CCSD amplitudes according to their magnitude and chooses the largestn_amplitudesto construct the ansatz. An example JSON dictionary using this ansatz follows:

Turn on the configuration recovery algorithm for error mitigation.

Finally, execute the function.

Print out the result from the run:

Output:

Use the "qsci_energy" key to see the QSCI energy:

Output:

The returned ground state energy estimation of anH2O\text{H}_2 \text{O}H2​Omolecule is very close to the exact result!

Thestate_vectorfield contains three values:bits,reals, andimags. Thebitsvalue is a list of integers representing electron configurations. Theiii-th position of thereals(imags) field represents the real (imaginary) part of the amplitude of the electron configuration on positioniii. You can sort it by magnitude and print out the top 10 most important electron configurations.

Output:

If you don't want to use CCSD as the state preparation method, or if you want to optimize further from the CCSD initial state, you can use the optimization-based QSCI. This algorithm gives you access to more chemistry-inspired ansatz with random initial parameters. For this algorithm, the QSCI energy is used as the cost function for the COBYLA optimizer. In each iteration, the circuit parameters are updated and the QSCI energy is evaluated with the circuit carrying the new set of circuit parameters.

The JSON dictionary used to run this algorithm is similar to that of QSCI. It only contains one additional field, "max_iter", which lets you limit the resource usage. The default is 2000 iterations.

Example of running this algorithm with the 1-uCJ ansatz:

Print out the result.

Output:

The returned result has the same fields as the one in the QSCI example.

Output:

As a performance benchmark, the 20-qubitN2\text{N}_2N2​dissociation curve is shown.

The red curve in the plot is generated by the QSCI method with theDoubleExcitationansatz. You can reproduce it by using the following code with different choices ofd, the distance between the nitrogen atoms.

Note that each point typically takes about one minute of QPU usage. On the classical side, whereRRRis chosen to be 50000, it doesn't necessarily mean that diagonalization of a50000×5000050000 \times 5000050000×50000matrix is done. The number of samples after configuration recovery in this case is approximately 5000 - 7000, which sets the dimension of the subspace Hamiltonian. Thus, the classical diagonalization cost is much smaller than that of typical FCI computation.

The key takeaway of this result is that QSCI with suitable configuration recovery outperforms scalable classical methods such as Hartree-Fock (HF), CCSD, and CISD atallchoices ofd. This implies that at a scale where FCI energy is no longer available, QSCI serves as a reliable method to estimate the ground state energy at all distances. For example, using the 6-31g basis,
a 36-qubitN2\text{N}_2N2​dissociation curve produced by QURI Function QSCI is given by

Here, the FCI curve is not available on a typical laptop (M2 Pro Chip, 16G RAM). However, QSCI can produce a qualitatively correct dissociation curve compared to the classical methods on the same machine with the assistance of theibm_strasbourgquantum computer.

Azobenzene has two isomers, trans-azobenzene and cis-azobenzene. The energy difference between the ground states of the two isomers plays an important role in the photoisomerization of azobenzene. This example benchmarks the ground state energy difference between QSCI and FCI with different active space settings up to 28 qubits. With configuration recovery, QURI Function QSCI yields error less than 5 mHa with only10510^5105shots, 30 to 40 seconds of QPU usage, and under 10 minutes of classical post-processing time per point.

For running systems larger than 20 qubits, please contact[email protected].

On this page

© IBM Corp., 2017-2025


---

# QUICK-PDE: A Qiskit Function by ColibriTD







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Qiskit Functions are an experimental feature available to IBM Quantum® Premium Plan and Flex Plan users. They are in preview release status and subject to change.

The Partial Differential Equation (PDE) solver presented here is part of our Quantum Innovative Computing Kit (QUICK) platform (QUICK-PDE), and is packaged as a Qiskit Function. With the QUICK-PDE function, you can solve domain-specific partial differential equations on IBM Quantum QPUs. This function is based on the algorithm described inColibriTD's H-DES description paper.This algorithm can solve complex multi-physics problems, starting with Computational Fluid Dynamics (CFD) and Materials Deformation (MD), and other use cases coming soon.

To tackle the differential equations, the trial solutions are encoded as linear combinations of orthogonal functions (typically Chebyshev polynomials, and more specifically2n2^n2nof them wherennnis the number of qubits encoding your function), parametrized by the angles of a Variable Quantum Circuit (VQC). The ansatz generates a state encoding the function, which is evaluated by observables whose combinations allow for evaluating the function at all points. You can then evaluate the loss function in which the differential equations are encoded, and fine-tune the angles in a hybrid loop, as shown in the following. The trial solutions get gradually closer to the actual solutions until you reach a satisfactory result.

In addition to this hybrid loop, you can also chain together different optimizers. This is useful when you want a global optimizer to find a good set of angles, and then a more fine-tuned optimizer to follow a gradient to the best set of neighboring angles. In the case of computational fluid dynamics (CFD), the default optimization sequence produces the best results - but in the case of material deformation (MD), while the default provides good results, you can configure it further for problem-specific benefits.

Note for each variable of the function, we specify number of qubits (which you can play with). By stacking 10 identical circuits and evaluating the 10 identical observables on different qubits throughout one big circuit, you can noise-mitigate within the CMA optimization process, relying on the noise learner method, and significantly reduce the number of shots needed.

The inviscid Burgers' equation, models flowing non-viscous fluids as follows:

∂u∂t+u∂u∂x=0,\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = 0,∂t∂u​+u∂x∂u​=0,

uuurepresents the fluid speed field. This use-case has a temporal boundary condition: you can select the initial condition and then allow the system to relax. Currently, the only accepted initial conditions are linear functions:ax+bax + bax+b.

The arguments for CFD's differential equations are on a fixed grid, as follows:

tttis between 0 and 0.95 with 30 sample points.xxxis between 0 and 0.95 with a step size of 0.2375.

This use case focuses on hypoelastic deformation with the one-dimensional tensile test, in which a bar fixed in space is pulled at its other extremity. We describe the problem as follows:

u′−σ3K−23ϵ0(σ′σ03)n=0u' - \frac{\sigma}{3K} - \frac{2}{\sqrt{3}}\epsilon_0\left(\frac{\sigma'}{\sigma_0\sqrt{3}}\right)^n = 0u′−3Kσ​−3​2​ϵ0​(σ0​3​σ′​)n=0

σ′−b=0,\sigma' - b = 0,σ′−b=0,

KKKrepresents the bulk modulus of the material being stretched,nnnthe exponent of a power law,bbbthe force per unit mass,ϵ0\epsilon_0ϵ0​the proportional stress limit,σ0\sigma_0σ0​the proportional strain limit,uuuthe stress function, andσ\sigmaσthe strain function.

The considered bar is of unitary length. This use-case has a boundary condition for surface stressttt, or the amount of work needed to stretch the bar.

The arguments for MD's differential equations are on a fixed grid, as follows:

xxxis between 0 and 1 with a step size of 0.04.

In order to run the QUICK-PDE Qiskit Function, you can adjust the following parameters:

The parameters of the differential equation (physical parameters and boundary condition) should follow the given format:

The output is a dictionary with the list of sample points, as well as the values of the functions at each of these points:

The shape of a solution array depends on the variables' samples:

The mapping between the function variables' sample points and the solution array's dimension is done in alphanumeric order of the variable's name. For example, if the variables are"t"and"x", a row ofsolution["functions"]["u"]represents the values of the solution for a fixed"t", and a column ofsolution["functions"]["u"]represents the values of the solution for a fixed"x".

The following is an example of how to get the value of the function for a specific set of coordinate:

The following table presents statistics on various runs of our function.

Fill out theform to request access to the QUICK-PDE function.Then, authenticate using yourAPI keyand select the function as follows:

To get started, try one of the following examples:

When initial conditions are set tou(0,x)=xu(0,x) = xu(0,x)=x, the results are as follows:

Check your Qiskit Function workload'sstatusor returnresultsas follows:

The material deformation use case requires the physical parameters of your material and the applied force, as follows:

If your workload status isERROR, usejob.result()to fetch the error message to help debug, as follows:

For support, contact[email protected].

On this page

© IBM Corp., 2017-2025


---

# HI-VQE Chemistry - A Qiskit Function by Qunova Computing







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Qiskit Functions are an experimental feature available only to IBM Quantum® Premium Plan users. They are in preview release status and subject to change.

In quantum chemistry, the electronic structure problem focuses on finding the solutions to the electronic Schrödinger equation - the quantum wave functions describing the behavior of the system's electrons. These wave functions are vectors of complex amplitudes, with each amplitude corresponding to the contribution of a possible electron configuration.

The ground state is the lowest energy wave function of the system and has a special importance in the study of molecular systems. The most accurate approach for computing the ground state considers all possible electron configurations, but this becomes intractable for larger systems since the number of configurations grows exponentially with system size.

The Handover Iterative Variational Quantum Eigensolver (HI-VQE) is an innovative hybrid quantum-classical method for accurately estimating the ground state of molecular systems. It integrates quantum hardware with classical computing, using quantum processors to efficiently explore candidate electron configurations and calculating the resulting wave function on classical computers. By generating compact yet chemically accurate wave functions, HI-VQE enhances research and discovery in quantum chemistry and materials science.

HI-VQE reduces the computational complexity of the electronic structure problem by efficiently estimating the ground state with high accuracy. It focuses on a carefully selected subset of the most relevant electron configurations, optimizing both accuracy and efficiency.

Combining the strengths of both classical and quantum computers, HI-VQE iteratively refines and improves the current estimate wave function. Its unique subspace construction techniques help make configuration selection more efficient, so that users have greater computational control and improved accuracy in quantum chemistry simulations.

If you would like to learn about the algorithm in more depth, you canread the associated research paper.

The number of electron configurations for a molecular system grows exponentially with system size. However, for certain electronic states, such as the ground state, it is common that only a small fraction of configurations significantly contribute to the state’s energy. Selected configuration interaction (SCI) methods exploit this sparsity to reduce computational costs by identifying and focusing on the most relevant configurations. This subset of configurations is referred to as a subspace.

HI-VQE leverages the inherent efficiency of quantum computers for representing molecular systems to aid the subspace search. It integrates classical and quantum subroutines to solve the electronic structure problem with high accuracy. Unlike existing quantum SCI methods, HI-VQE combines variational training, iterative subspace construction, and pre-diagonalization configuration screening to enhance efficiency by reducing quantum measurements, iterations, and classical diagonalization costs. HI-VQE can therefore be applied to larger molecular systems which require more qubits, and reduces the cost to solve a problem of a given size to the same degree of accuracy.

To compute a system's ground state, HI-VQE first uses the classical chemistry package PySCF to generate a molecular representation from user-provided inputs, such as the molecular geometry and other molecular information. It then enters a hybrid quantum-classical optimization loop, iteratively refining a subspace to optimally represent the ground state while minimizing the number of configurations included. The loop continues until convergence criteria, such as subspace size or energy stability, are met, after which the computed ground state wave function and energy are output. These results can be used to construct accurate potential energy surfaces and perform further analysis of the system.

The optimization loop focuses on adjusting a quantum circuit’s parameters to generate a high-quality subspace. HI-VQE offers three quantum circuit options:excitation_preserving,efficient_su2, andLUCJ. The optimization is initialized close to the Hartree-Fock reference state due to its general suitability. The circuit is then executed on a quantum device and configurations are sampled from the resulting quantum state before being returned as binary strings. Due to quantum device noise, some sampled configurations may be physically invalid, failing to conserve electron number or spin. HI-VQE addresses this using the configuration recovery process from theqiskit-addon-sqdpackage, so that users can either correct invalid configurations or discard them.

The valid configurations then undergo an optional screening step to remove those predicted to contribute minimally. This reduces the dimension of the subspace, thereby lowering the cost of the diagonalization step. If the screening is enabled, then a preliminary subspace Hamiltonian is constructed from the valid configurations and a diagonalization is performed with very loose termination critieria. Though the accuracy of the resulting amplitudes for each configuration is low, it is effective for predicting which configurations to leave out of the subspace this iteration, and it is fast to compute.

The selected configurations are added to the subspace, and the system's Hamiltonian is projected into this subspace. The subspace updates iteratively, preserving the most relevant configurations across iterations. This approach contrasts with alternative methods because the quantum circuit does not need to approximate the full ground state at each step.

Next, the subspace Hamiltonian is classically diagonalized to obtain the lowest eigenvalue and its corresponding eigenvector, representing an approximation of the ground state and its energy. As the subspace quality improves through iterations, the computed ground state better approximates the true ground state. An additional screening step can be performed at this point to remove any configurations from the subspace that don't have a substantial contribution to the computed ground state. This step ensures that the subspace carried into the next iteration is as compact as possible. This is evaluated based on the amplitudes that are returned by the diagonalization, as these represent each configuration's importance contribution to the computed ground state.

A convergence check then determines whether further training would improve results. If so, then an optional classical expansion step is performed, the quantum circuit parameters are updated to further minimize the computed energy, and the process repeats. The classical expansion step generates additional configurations for the subspace, supplementing the configurations sampled from the quantum device. It first identifies the configuration with the largest amplitude in the diagonalization results, before generating new configurations with single and double excitations from the identified configuration. The desired number of these configurations are then added to the subspace.

Once it is determined that the iterations have converged, HI-VQE returns the computed ground state (in the form of the states in the subspace and their amplitudes in the ground state wave function), its energy, and an energy variance measure that gives an indication of whether the computed state forms an eigenstate of the system's Hamiltonian.

Users are able to decide the quantum circuit used and the number of shots taken for each quantum circuit, as well as control the subspace size or enable the classical generation of additional configurations to assist the quantum generated configurations. In this way users can tailor the behavior of HI-VQE to suit their desired applications.

First,request access to the function.

Then, authenticate using yourIBM Quantum® API keyand select the Qiskit Function as follows:

See the following table for all input parameters the function accepts. The subsequentMolecule optionsandHI-VQE optionssections go into more details about those arguments.

The following table details all keys and values that can be set in themolecule_optionsdictionary, as well as their data types and default values. All keys are optional.

The following table details all keys and values that can be set in thehivqe_optionsdictionary, as well as their data types and default values. All keys are optional.

The function returns a dictionary with four keys and values. The keys and values are documented in the following table:

The first example shows how to compute the ground state energy for an NH3 molecule using the HI-VQE algorithm.

The molecular geometry of NH3 is provided with Cartesian coordinates separated with ";" for each atom.

Additional options can be defined and provided for molecular system in the following dictionary format.

Execute the function with geometry and option inputs.

It is a good idea to print the Function job ID so that it can be provided in support requests if something goes wrong.

Output:

This example then utilizes 16 qubits with 8 orbitals of sto3g basis for an NH3 molecule.

Check your Qiskit Function workload'sstatusor returnresultsas follows:

Output:

After the job is completed, the results can be obtained withresult()instance.

Output:

To access the ground state energy, use the "energy" key. The "eigenvector" key provides the CI coefficients with corresponding bitstring notation of electron configuration stored with "states" of the results.

Output:

Output:

|Exact Energy - HI-VQE Energy|: 0.077237504 mHa
Sampled Number of States: 1936

This section shows the demonstrated benchmark calculations of HI-VQE with a 24-qubit case for Li2S, a 40-qubit case for an N2 molecule, and a 44-qubit case for an FeP-NO system.

The PES curve is shown with the FCI reference and initial guess from RHF, together with the energy error from the FCI reference.

The calculations have been conducted with the following geometries and options.

The red dots represent the HI-VQE calculation results for six different geometries, and three geometries corresponding to 1.51, 2.40, and 3.80 Angstrom are provided as input in the above cell.

The nitrogen molecule has been identified as a multireference system with large correlation energy contributions beyond the Hartree-Fock state. We conducted a benchmark calculation for the N2 molecule with cc-pvdz basis, (20o,14e) using the homo-lumo active orbital selection. The complete active space (CAS) number to represent this problem is 6,009,350,400. It is not possible to obtain the eigenvalue problem solution (for energy and electronic structure) with this number of states using a powerful desktop (16cpu/64GB). With HI-VQE, users can efficiently search the subspace of CAS states to find chemically accurate results while saving computation resources significantly. The following plots show the PES curve of 40 qubits HI-VQE calculation of the N2 molecule dissociation.

Another interesting chemical system is an iron(II)-porphyrin (FeP) complex with a coordinated nitric oxide (NO) ligand, which represents a biologically relevant metalloporphyrin system that plays crucial roles in various physiological processes. In this example, HI-VQE has been utilized to estimate the accurate potential energy surface curve of the intermolecular interaction between FeP and NO (ground state energy for differently separated geometries). The combined system has 450 orbitals and 202 electrons (450o,202e) with 6-31g(d) basis in total. The homo-lumo active orbital selection was utilized to calculate the smaller case from the real case with (22o,22e). From the following benchmark results, we were able to achieve the chemical accuracy (> 1.6 mHa) with a state-of-the-art classical computer chemistry calculation of CASCI(DMRG) (22o,22e) reference.

If your workload fails, the status will beERRORand callingjob.result()will raise an exception:

Output:

Output:

You can send an email to[email protected]for help with this function.

If you want help with troubleshooting a specific error, please provide the Function job ID of the job that encountered the error.

On this page

© IBM Corp., 2017-2025


---

# Circuit library







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The Qiskit SDK includes a library of popular circuits to use as building blocks in your own programs. Using pre-defined circuits saves time researching, writing code, and debugging. The library includes popular circuits in quantum computing, circuits that are difficult to simulate classically, and circuits useful for quantum hardware benchmarking.

This page lists the different circuit categories the library provides. For a full list of circuits, see thecircuit library API documentation.

The circuit library also includes standard quantum gates. Some are more fundamental gates (such as theUGate), and others are multi-qubit gates that usually need building from single- and two-qubit gates. To add imported gates to your circuit, use theappendmethod; the first argument is the gate, and the next argument is a list of qubits to apply the gate to.

For example, the following code cell creates a circuit with a Hadamard gate and a multi-controlled-X gate.

Output:

SeeStandard gatesin the circuit library API documentation.

Not sure what your gate's called? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

These circuits alternate layers of single-qubit rotation gates with layers of multi-qubit entangling gates.

This family of circuits is popular in variational quantum algorithms because they can produce a wide range of quantum states. Variational algorithms adjust the gate parameters to find states that have certain properties (such as states that represent a good solution to an optimization problem). For this purpose, many circuits in the library areparameterized, which means you can define them without fixed values.

The following code cell imports an_localcircuit, in which the entangling gates are two-qubit gates. This circuit interleaves blocks of parameterized single-qubit gates, followed by entangling blocks of two-qubit gates. The following code creates a three-qubit circuit, with single-qubit RX-gates and two-qubit CZ-gates.

Output:

You can get a list-like object of the circuit's parameters from theparametersattribute.

Output:

You can also use this to assign these parameters to real values using a dictionary of the form{ Parameter: number }. To demonstrate, the following code cell assigns each parameter in the circuit to0.

Output:

For more information, seeN-local gatesin the circuit library API documentation or take ourVariational algorithm design course.

These parameterized circuits encode data onto quantum states for processing by quantum machine learning algorithms. Some circuits supported by Qiskit are:

The best approach depends upon the specifics of your application. On current quantum computers, however, we often use angle-encoding circuits such as thezz_feature_map.

Output:

SeeData encoding circuitsin the circuit library API documentation.

These circuits simulate a quantum state evolving in time. Use time-evolution circuits to investigate physical effects such as heat transfer or phase transitions in a system. Time-evolution circuits are also a fundamental building block of chemistry wave functions (such as unitary coupled-cluster trial states) and of the QAOA algorithm we use for optimization problems.

Output:

Read thePauliEvolutionGateAPI documentation.

Benchmarking circuits give us a sense of how well our hardware is actually working, and complexity-theory circuits help us understand how difficult the problems we want to solve are.

For example, the "quantum volume" benchmark measures how accurately a quantum computer executes a type of random quantum circuit. The score of the quantum computer increases with the size of the circuit it can reliably run. This takes into account all aspects of the computer, including qubit count, instruction fidelity, qubit connectivity, and the software stack transpiling and post-processing results. Read more about quantum volume in the originalquantum volume paper.

The following code shows an example of a quantum volume circuit built in Qiskit that runs on four qubits (theunitaryblocks are randomized two-qubit gates).

Output:

The circuit library also includes circuits believed to be hard to simulate classically, such as instantaneous quantum polynomial (iqp) circuits. These circuits sandwich certain diagonal gates (in the computational basis) between blocks of Hadamard gates.

Other circuits includegrover_operatorfor use in Grover's algorithm, and thefourier_checkingcircuit for the Fourier checking problem. See these circuits inParticular quantum circuitsin the circuit library API documentation.

Arithmetic operations are classical functions, such as adding integers and bit-wise operations. These may be useful with algorithms such as amplitude estimation for finance applications, and in algorithms like the HHL algorithm, which solves linear systems of equations.

As an example, let’s try adding two three-bit numbers using a "ripple-carry" circuit to perform in-place addition (FullAdderGate). This adder adds two numbers (we'll call them "A" and "B") and writes the result to the register that held B. In the following example, A=2 and B=3.

Output:

Simulating the circuit shows that it outputs5for all1024shots (i.e. is measured with probability1.0).

Output:

SeeArithmeticin the circuit library API documentation.

On this page

© IBM Corp., 2017-2025


---

# Classical feedforward and control flow







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Starting 2 June 2025 and continuing through the year, IBM Quantum® will begin a gradual rollout of new features to dynamic circuits that will enable them at the utility scale. See theannouncementfor more details.

To accelerate the rollout, the following have been deprecated:

New QPUs released after this deprecation will not support dynamic circuits until the updated features are released. Additionally, after the release, QPUs with older control electronics will not support dynamic circuits. To check whether a specific QPU supports dynamic circuits, use this code:

This guide demonstrates the functionality available in the Qiskit SDK for performing classical feedforward and control flow. These features are sometimes referred to collectively as "dynamic circuits." Classical feedforward refers to the ability to measure qubits in the middle of a circuit and perform additional quantum operations that depend on the measurement outcome. Qiskit supports four control flow constructs for classical feedforward, each implemented as a method onQuantumCircuit. The constructs and their corresponding methods are:

Each of these methods returns acontext managerand is typically used in awithstatement. In the rest of this guide, we will explain each of these constructs and how to use them.

There are some limitations of classical feedforward and control flow operations on quantum hardware that might impact your program. For more information, seeHardware considerations and limitations for classical feedforward and control flow.

The if statement is used to conditionally perform operations based on the value of a classical bit or register.

In the example below, we apply a Hadamard gate to a qubit and measure it. If the result is 1, then we apply an X gate on the qubit, which has the effect of flipping it back to the 0 state. We then measure the qubit again. The resulting measurement outcome should be 0 with 100% probability.

Output:

Thewithstatement can be given an assignment target which is itself a context manager that can be stored and subsequently used to create an else block, which is executed whenever the contents of the if block arenotexecuted.

In the example below, we initialize registers with two qubits and two classical bits. We apply a Hadamard gate to the first qubit and measure it. If the result is 1, then we apply a Hadamard gate on the second qubit; otherwise, we apply an X gate on the second qubit. Finally, we measure the second qubit as well.

Output:

In addition to conditioning on a single classical bit, it's also possible to condition on the value of a classical register composed of multiple bits.

In the example below, we apply Hadamard gates to two qubits and measure them. If the result is01, that is, the first qubit is 1 and the second qubit is 0, then we apply an X gate to a third qubit. Finally, we measure the third qubit. Note that for clarity, we chose to specify the state of the third classical bit, which is 0, in the if condition. In the circuit drawing, the condition is indicated by the circles on the classical bits being conditioned on. A black circle indicates conditioning on 1, while a white circle indicates conditioning on 0.

Output:

The switch statement is used to select actions based on the value of a classical bit or register. It is similar to an if statement, but allows one to specify more cases for the branching logic. In the example below, we apply a Hadamard gate to a qubit and measure it. If the result is 0, we apply an X gate on the qubit, and if the result is 1, we apply a Z gate. The resulting measurement outcome should be 1 with 100% probability.

Output:

Because the example above used a single classical bit, there were only two possible cases, so we could have achieved the same result using an if-else statement. The switch case is mainly useful when branching on the value of a classical register composed of multiple bits, as demonstrated in the following example. Here, we also show how to construct a default case, which is executed if none of the preceding cases are. Note that in a switch statement, only one of the blocks are ever executed. There is no fallthrough.

In the example below, we apply Hadamard gates to two qubits and measure them. If the result is either 00 or 11, we apply a Z gate to the third qubit. If the result is 01, we apply a Y gate. If none of the preceding cases matched, we apply an X gate. Finally, measure the third qubit.

Output:

A for loop is used to iterate over a sequence of classical values and perform some operations during each iteration.

In the example below, we use a for loop to apply 5 X gates to a qubit and then measure it. Because we perform an odd number of X gates, the overall effect is to flip the qubit from the 0 state to the 1 state.

Output:

A while loop is used to repeat instructions while some condition is satisfied.

In the example below, we apply Hadamard gates to two qubits and measure them. Then, we create a while loop that repeats this procedure while the measurement outcome is 11. As a result, the final measurement should never be 11, with the remaining possibilities appearing with approximately equal frequency.

Output:

On this page

© IBM Corp., 2017-2025


---

# Fractional gates







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page introduces two newly supported gate types on the IBM Quantum® fleet of QPUs. Thesefractionalgates are supported onHeron QPUsin the form of:

This page discusses the use cases where implementing fractional gates can improve the efficiency of your workflows, as well as how to use these gates on IBM Quantum QPUs.

Internally, these fractional gates work by directly executing anRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)andRX(θ)R_X(\theta)RX​(θ)rotation for an arbitrary angle. Use of theRX(θ)R_X(\theta)RX​(θ)gate can reduce the duration and error for single-qubit rotations of arbitrary angle by up to a factor of two. The direct execution of theRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)gate rotation avoids decomposition into multipleCZGates, similarly reducing a circuit's duration and error. This is especially useful for circuits that contain many single- and two-qubit rotations, such as when simulating the dynamics of a quantum system or when using a variational ansatz with many parameters.

While these types of gates are in thelibrary of standard gateswhich aQuantumCircuitcan possess, they can only be used on specific IBM Quantum QPUs, and which must be loaded with the flaguse_fractional_gatesset toTrue(shown below). This flag will ensure that fractional gates are included in the backend'sTargetfor the transpiler.

This code example demonstrates how to use fractional gates in the context of a workflow that simulates the dynamics of an Ising chain using fractional gates. The circuit duration is then compared against a backend that does not use fractional gates.

The error value reported in theTargetof a backend with fractional gates enabled is just a copy of the non-fractional gate's counterpart (which may not be the same). This is because the reporting of error rates on the fractional gates is not yet supported.

However, since the gate time of fractional versus non-fractional gates are the same, it is a reasonable assumption that their error rates are comparable -- especially when the dominant source of error in a circuit is due to relaxation.

Output:

Specify two backend objects: one with fractional gates enabled, and the other with them disabled, then transpile them both.

Display the timeline of the circuit using the two types of gates.

Output:

Output:

For the two-qubitRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)gate, only angles between000andπ/2\pi/2π/2can be executed on IBM Quantum hardware. If a circuit contains anyRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)gates with an angle outside of this range, then the standard transpilation pipeline will generally correct this with an appropriate circuit transformation (through theFoldRzzAnglepass).  However, for anyRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)gate containing one or moreParameters, the transpiler will assume these parameters will be assigned angles within this range at runtime. The job will fail if any of the parameter values specified in the PUB submitted to Qiskit Runtime are outside of this range.

Historically, the basis gates available on IBM Quantum QPUs have beenCZ,X,RZ,SX, andID, which can not efficiently represent circuits with single- and two-qubit rotations that are not multiples ofπ/2\pi / 2π/2. For example, anRX(θ)R_X(\theta)RX​(θ)gate, when transpiled, must decompose into a series ofRZRZRZandX\sqrt{X}X​gates, which creates a circuit with two gates of finite duration instead of one.

Similarly, when two-qubit rotations such as anRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)gate are transpiled, the decomposition requires twoCZgates and several single-qubit gates, which increases the circuit depth. These decompositions are shown in the following code.

Output:

Output:

Output:

Output:

For workflows that require many single-qubitRX(θ)R_X(\theta)RX​(θ)or two-qubit rotations (such as in a variational ansatz or when simulating the time evolution of quantum systems), this constraint causes the circuit depth to grow rapidly. However, fractional gates remove this requirement, because the single- and two-qubit rotations are executed directly, and create a more efficient (and thus error-suppressed) quantum circuit.

It is important to note that fractional gates are anexperimentalfeature and the behavior of theuse_fractional_gatesflag may change in the future. Look to therelease notesfor new versions of Qiskit Runtime for more information. See also the API reference documentation forQiskitRuntimeService.backend, which describesuse_fractional_gates.

Additionally, the Qiskit transpiler has limited capability to useRZZ(θ)R_{ZZ}(\theta)RZZ​(θ)in its optimization passes. This requires you to take more care in crafting and optimizing circuits that contain these instructions.

Lastly, using fractional gates is not supported for:

Read the guide onprimitive optionsto learn more about customizing the error mitigation and suppression techniques for a given quantum workload.

On this page

© IBM Corp., 2017-2025


---

# Construct circuits







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page takes a closer look at theQuantumCircuitclass in the Qiskit SDK, including some more advanced methods you can use to create quantum circuits.

A simple quantum circuit is a collection of qubits and a list of instructions that act on those qubits. To demonstrate, the following cell creates a new circuit with two new qubits, then displays the circuit'squbitsattribute.

Output:

Adding an instruction to the circuit appends the instruction to the circuit'sdataattribute. The following cell output showsdatais a list ofCircuitInstructionobjects, each of which has anoperationattribute, and aqubitsattribute.

Output:

The easiest way to view this information is through thedrawmethod, which returns a visualization of a circuit. SeeVisualize circuitsfor different ways of displaying quantum circuits.

Output:

Circuit instruction objects can contain "definition" circuits that describe the instruction in terms of more fundamental instructions. For example, theX-gateis defined as a specific case of theU3-gate, a more general single-qubit gate.

Output:

Instructions and circuits are similar in that they both describe operations on bits and qubits, but they have different purposes:

Thedepth()of a quantum circuit is a measure of the number of “layers” of quantum gates, executed in parallel, it takes to complete the computation defined by the circuit. Because quantum gates take time to implement, the depth of a circuit roughly corresponds to the amount of time it takes the quantum computer to execute the circuit. Thus, the depth of a circuit is one important quantity used to measure if a quantum circuit can be run on a device.

The rest of this page illustrates how to manipulate quantum circuits.

Methods such asQuantumCircuit.handQuantumCircuit.cxadd specific instructions to circuits. To add instructions to a circuit more generally, use theappendmethod. This takes an instruction and a list of qubits to apply the instruction to. See theCircuit Library API documentationfor a list of supported instructions.

Output:

To combine two circuits, use thecomposemethod. This accepts anotherQuantumCircuitand an optional list of qubit mappings.

Thecomposemethod returns a new circuit and doesnotmutate either circuit it acts on. To mutate the circuit on which you're calling thecomposemethod, use the argumentinplace=True.

Output:

You might also want to compile circuits into instructions to keep your circuits organized. You can convert a circuit to an instruction by using theto_instructionmethod, then append this to another circuit as you would any other instruction. The circuit drawn in the following cell is functionally equivalent to the circuit drawn in the previous cell.

Output:

If your circuit is unitary, you can convert it to aGateby using theto_gatemethod.Gateobjects are specific types of instructions that have some extra features, such as thecontrolmethod, which adds a quantum control.

Output:

To see what's going on, you can use thedecomposemethod to expand each instruction into its definition.

Thedecomposemethod returns a new circuit and doesnotmutate the circuit it acts on.

Output:

Many near-term quantum algorithms involve executing many variations of a quantum circuit. Since constructing and optimizing large circuits can be computationally expensive, Qiskit supportsparameterizedcircuits. These circuits have undefined parameters, and their values do not need to be defined until just before executing the circuit. This lets you move circuit construction and optimization out of the main program loop.  The following cell creates and displays a parameterized circuit.

Output:

The following cell creates many variations of this circuit and displays one of the variations.

Output:

You can find a list of a circuit's undefined parameters in itsparametersattribute.

Output:

Forgotten the method name? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

On this page

© IBM Corp., 2017-2025


---

# Measure qubits







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

To get information about a qubit's state, you canmeasureit onto aclassical bit. In Qiskit, measurements are performed in the computational basis, that is, the single-qubit Pauli-ZZZbasis. Therefore, a measurement yields 0 or 1, depending on the overlap with the Pauli-ZZZeigenstates∣0⟩|0\rangle∣0⟩and∣1⟩|1\rangle∣1⟩:

There are several ways to apply measurements to a circuit:

Use themeasuremethod to measure aQuantumCircuit.

Examples:

Output:

Output:

The QiskitMeasureclass measures the specified qubits.

Output:

To measure all qubits into the corresponding classical bits, use themeasure_allmethod. By default, this method adds new classical bits in aClassicalRegisterto store these measurements.

To measure all qubits that are not idle, use themeasure_activemethod. This method creates a newClassicalRegisterwith a size equal to the number of non-idle qubits being measured.

On this page

© IBM Corp., 2017-2025


---

# Synthesize unitary operations







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

A unitary operation describes a norm-preserving change to a quantum system.
Fornnnqubits this change is described by a2n×2n2^n \times 2^n2n×2ndimensional, complex matrixUUUwhose adjoint equals the inverse, that isU†U=1U^\dagger U = \mathbb{1}U†U=1.

Synthesizing specific unitary operations into a set of quantum gates is a fundamental task used, for example, in the design and application of quantum algorithms or in compiling quantum circuits.

While efficient synthesis is possible for certain classes of unitaries – like those composed of Clifford gates or having a tensor product structure – most unitaries do not fall into these categories.
For general unitary matrices, synthesis is a complex task with computational costs that increase exponentially with the number of qubits.
Therefore, if you know an efficient decomposition for the unitary you would like to implement, it will likely be better than a general synthesis.

If no decomposition is available, the Qiskit SDK provides you with the tools to find one.
However, note that this generally generates deep circuits that may be unsuitable to run on noisy quantum computers.

Output:

Sometimes it is beneficial to re-synthesize a long series of single- and two-qubit gates, if the length can be reduced. For example, the following circuit uses three two-qubit gates.

Output:

However, after re-synthesizing with the following code, it only needs a single CX gate. (Here we use theQuantumCircuit.decompose()method to better visualize the gates used to re-synthesize the unitary.)

Output:

Qiskit'stranspilefunction automatically performs this re-synthesis for a sufficiently high optimization level.

On this page

© IBM Corp., 2017-2025


---

# Bit-ordering in the Qiskit SDK







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

If you have a set ofnnnbits (or qubits), you'll usually label each bit0→n−10
\rightarrow n-10→n−1. Different softwares and resources must choose how they order
these bits both in computer memory and when displayed on-screen.

Here's how the Qiskit SDK orders bits in different scenarios.

TheQuantumCircuitclass stores its qubits in a list
(QuantumCircuit.qubits). The index of a qubit in this list defines the
qubit's label.

Output:

On a circuit diagram, qubit000is the topmost qubit, and qubitn−1n-1n−1the
bottommost qubit. You can change this with thereverse_bitsargument ofQuantumCircuit.draw(seeChange ordering in
Qiskit).

Output:

When interpreting bits as a number, bit000is the least significant bit, and
bitn−1n-1n−1the most significant. This is helpful when coding because each bit has
the value2label2^\text{label}2label(label being the qubit's index inQuantumCircuit.qubits). For example, the following circuit execution ends
with bit000being0, and bit111being1. This is interpreted as the
decimal integer2(measured with probability1.0).

Output:

When displaying or interpreting a list of bits (or qubits) as a string, bitn−1n-1n−1is the leftmost bit, and bit000is the rightmost bit. This is because we
usually write numbers with the most significant digit on the left, and in
Qiskit, bitn−1n-1n−1is interpreted as the most significant bit.

For example, the following cell defines aStatevectorfrom a string of
single-qubit states. In this case, qubit000is in state∣+⟩|+\rangle∣+⟩, and
qubit111in state∣0⟩|0\rangle∣0⟩.

Output:

This occasionally causes confusion when interpreting a string of bits, as you
might expect the leftmost bit to be bit000, whereas it usually represents bitn−1n-1n−1.

When representing a statevector as a list of complex numbers (amplitudes),
Qiskit orders these amplitudes such that the amplitude at indexxxxrepresents
the computational basis state∣x⟩|x\rangle∣x⟩.

Output:

Each gate in Qiskit can interpret a list of qubits in its own way, but
controlled gates usually follow the convention(control, target).

For example, the following cell adds a controlled-X gate where qubit000is
the control and qubit111is the target.

Output:

Following all the previously mentioned conventions in Qiskit, this CX-gate
performs the transformation∣01⟩↔∣11⟩|01\rangle \leftrightarrow |11\rangle∣01⟩↔∣11⟩, so has the
following matrix.

To draw a circuit with qubits in reversed order (that is, qubit000at the
bottom), use thereverse_bitsargument. This only affects the generated
diagram and does not affect the circuit; the X-gate still acts on qubit000.

Output:

You can use thereverse_bitsmethod to return a new circuit with the
qubits' labels reversed (this does not mutate the original circuit).

Output:

Note that in this new circuit, the X-gate acts on qubit111.

On this page

© IBM Corp., 2017-2025


---

# Save circuits to disk







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

UseQPY serializationto save your circuit to file. QPY files store the full Qiskit circuit object and will be compatible with newer versions of Qiskit (although not necessarily with older versions of Qiskit).

To demonstrate, the following cell creates a simple quantum circuit.

To save this file to disk, use theqpy.dumpfunction. You can also save a list of circuits.

This circuit is now saved to the filetest.qpy. If you restart your Python kernel, you can re-load the circuit using theqpy.loadfunction. Note that this always returns a list of circuits, even if you only serialized one circuit.

Output:

© IBM Corp., 2017-2025


---

# Overview of operator classes







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

In Qiskit, quantum operators are represented using classes from thequantum_infomodule. The most important operator class isSparsePauliOp, which represents a general quantum operator as a linear combination of Pauli strings.SparsePauliOpis the class most commonly used to represent quantum observables. The rest of this page explains how to useSparsePauliOpand other operator classes.

TheSparsePauliOpclass represents a linear combination of Pauli strings. There are several ways to initialize aSparsePauliOp, but the most flexible way is to use thefrom_sparse_listmethod, as demonstrated in the following code cell. Thefrom_sparse_listaccepts a list of(pauli_string, qubit_indices, coefficient)triplets.

Output:

SparsePauliOpsupports arithmetic operations, as demonstrated in the following code cell.

Output:

ThePauliclass represents a single Pauli string with an optional phase coefficient from the set{+1,i,−1,−i}\set{+1, i, -1, -i}{+1,i,−1,−i}. APaulican be initialized by passing a string of characters from the set{"I", "X", "Y", "Z"}, optionally prefixed by one of{"", "i", "-", "-i"}to represent the phase coefficient.

Output:

The following code cell demonstrates the use of some attributes and methods.

Output:

Pauliobjects possess a number of other methods to manipulate the operators such as determining its adjoint, whether it (anti)commutes with anotherPauli, and computing the dot product with anotherPauli. Refer to theAPI documentationfor more info.

TheOperatorclass represents a general linear operator. UnlikeSparsePauliOp,Operatorstores the linear operator as a dense matrix. Because the memory required to store a dense matrix scales exponentially with the number of qubits, theOperatorclass is only suitable for use with a small number of qubits.

You can initialize anOperatorby directly passing a Numpy array storing the matrix of the operator. For example, the following code cell creates a two-qubit Pauli XX operator:

Output:

The operator object stores the underlying matrix, and the input and output dimension of subsystems.

Output:

Output:

The operator class also keeps track of subsystem dimensions, which can be used for composing operators together. These can be accessed using theinput_dimsandoutput_dimsfunctions.

For2N2^N2Nby2M2^M2Moperators, the input and output dimensions are automatically assumed to be M-qubit and N-qubit:

Output:

If the input matrix is not divisible into qubit subsystems, then it will be stored as a single-qubit operator. For example, for a6×66\times66×6matrix:

Output:

The input and output dimension can also be manually specified when initializing a new operator:

Output:

Output:

You can also extract just the input or output dimensions of a subset of subsystems using theinput_dimsandoutput_dimsfunctions:

Output:

On this page

© IBM Corp., 2017-2025


---

# Specify observables in the Pauli basis







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

In quantum mechanics, observables correspond to physical properties that can be measured.
When considering a system of spins, for example, you could be interested in measuring the system's energy or obtaining information about the alignment of the spins, such as the magnetization or the correlations between spins.

To measure annnn-qubit observableOOOon a quantum computer, you must represent it as a sum of tensor products of Pauli operators, that is

where

and you use the fact that an observable is Hermitian, as in,O†=OO^\dagger = OO†=O. IfOOOis not Hermitian it can still be decomposed as a sum of Paulis, but the coefficientαk\alpha_kαk​becomes complex.

In many cases, the observable is naturally specified in this representation after mapping the system of interest to qubits.
For example, a spin-1/2 system can be mapped to an Ising Hamiltonian

where the indices⟨i,j⟩\langle i, j\rangle⟨i,j⟩run over interacting spins and the spins are subject to a transversal field inXXX.
The subscript index indicates which qubit the Pauli operator acts on, i.e.XiX_iXi​applies anXXXoperator on qubitiiiand leaves the rest unchanged.

In the Qiskit SDK, this Hamiltonian could be constructed with the following code.

Output:

If we would like to measure the energy the observable is the Hamiltonian itself. Alternatively, we could be
interested in measuring system properties like the average magnetization by counting the number of spins
aligned in theZZZ-direction with the observable

For observables that are not given in terms of Pauli operators but in a matrix form, we first have to reformulate them
in the Pauli basis in order to evaluate them on a quantum computer.
We are always able to find such a representation as the Pauli matrices form a basis for the Hermitian2n×2n2^n \times 2^n2n×2nmatrices.
We expand the observableOOOas

where the sum runs over all possiblennn-qubit Pauli terms andTr(⋅)\mathrm{Tr}(\cdot)Tr(⋅)is the trace of a matrix, which acts as inner product.
You can implement this decomposition  from a matrix to Pauli terms using theSparsePauliOp.from_operatormethod, like so:

Output:

This means the matrix can be written as Pauli terms asO=−Z1+0.5X2+Y2Y1O = -Z_1 + 0.5 X_2 + Y_2 Y_1O=−Z1​+0.5X2​+Y2​Y1​.

Remember the tensor product order maps to qubits asqn⊗qn−1⊗⋯⊗q1q_n \otimes q_{n-1} \otimes \cdots \otimes q_1qn​⊗qn−1​⊗⋯⊗q1​.

If the observable is Hermitian (meaningO†=OO^\dagger = OO†=O), the Pauli coefficients are real numbers.
We can, however, also decompose any other complex matrix in terms of Paulis, if we allow for complex-valued coefficients.

A measurement projects the qubit state to the computational basis{∣0⟩,∣1⟩}\{|0\rangle, |1\rangle\}{∣0⟩,∣1⟩}. This implies that you can only measure observables that are diagonal in this basis, such as Paulis consisting only ofIIIandZZZterms.
Measuring arbitrary Pauli terms therefore requires a change of basis to diagonalize them. To do this, perform the following transformations,

whereHHHis the Hadamard gate andS=ZS = \sqrt{Z}S=Z​is sometimes referred to as the phase gate.
If you are using anEstimatorto compute expectation values, the basis transformations are automatically performed.

Below is an example demonstrating how to prepare a quantum circuit and manually measure the qubit 0 in the X basis,
qubit 1 in the Y basis and qubit 2 in the Z basis.
We apply the transformations shown in the previous equation and obtain the following circuit:

Output:

On this page

© IBM Corp., 2017-2025


---

# The Operator class







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page shows how to use theOperatorclass. For a high-level overview of operator representations in Qiskit, including theOperatorclass and others, seeOverview of operator classes.

Several other classes in Qiskit can be directly converted to anOperatorobject using the operator initialization method. For example:

Note that the last point means you can use theOperatorclass as a unitary simulator to compute the final unitary matrix for a quantum circuit, without having to call a simulator backend. If the circuit contains any unsupported operations, an exception is raised. Unsupported operations are: measure, reset, conditional operations, or a gate that does not have a matrix definition or decomposition in terms of gate with matrix definitions.

Output:

Output:

Output:

Output:

UnitaryOperatorscan be directly inserted into aQuantumCircuitusing theQuantumCircuit.appendmethod. This converts theOperatorinto aUnitaryGateobject, which is added to the circuit.

If the operator is not unitary, an exception is raised. This can be checked using theOperator.is_unitary()function, which returnsTrueif the operator is unitary andFalseotherwise.

Output:

Note that in the above example the operator is initialized from aPauliobject. However, thePauliobject may also be directly inserted into the circuit itself and will be converted into a sequence of single-qubit Pauli gates:

Output:

Operators may be combined using several methods.

Two operatorsAAAandBBBcan be combined into a tensor product operatorA⊗BA\otimes BA⊗Busing theOperator.tensorfunction. Note that if bothAAAandBBBare single-qubit operators, thenA.tensor(B)=A⊗BA\otimes BA⊗Bwill have the subsystems indexed as matrixBBBon subsystem 0, and matrixAAAon subsystem 1.

Output:

A closely related operation isOperator.expand, which acts like a tensor product but in the reverse order. Hence, for two operatorsAAAandBBByou haveA.expand(B)=B⊗AB\otimes AB⊗Awhere the subsystems are indexed as matrixAAAon subsystem 0, and matrixBBBon subsystem 1.

Output:

You can also compose two operatorsAAAandBBBto implement matrix multiplication using theOperator.composemethod.A.compose(B)returns the operator with matrixB.AB.AB.A:

Output:

You can also compose in the reverse order by applyingBBBin front ofAAAusing thefrontkwarg ofcompose:A.compose(B, front=True)=A.BA.BA.B:

Output:

Note that the previous compose requires that the total output dimension of the first operatorAAAis equal to the total input dimension of the composed operatorBBB(and similarly, the output dimension ofBBBmust be equal to the input dimension ofAAAwhen composing withfront=True).

You can also compose a smaller operator with a selection of subsystems on a larger operator using theqargskwarg ofcompose, either with or withoutfront=True. In this case, the relevant input and output dimensions of the subsystems being composed must match.Note that the smaller operator must always be the argument of thecomposemethod.

For example, to compose a two-qubit gate with a three-qubit operator:

Output:

Output:

Operators may also be combined using standard linear operators for addition, subtraction, and scalar multiplication by complex numbers.

Output:

An important point is that whiletensor,expand, andcomposepreserves the unitarity of unitary operators, linear combinations do not; hence, adding two unitary operators will, in general, result in a non-unitary operator:

Output:

Note that for all the following methods, if the second object is not already anOperatorobject, it is implicitly converted into one by the method. This means that matrices can be passed in directly without being explicitly converted to anOperatorfirst. If the conversion is not possible, an exception is raised.

Output:

Operators implement an equality method that can be used to check if two operators are approximately equal.

Output:

Note that this checks that each matrix element of the operators is approximately equal; two unitaries that differ by a global phase are not considered equal:

Output:

You can also compare operators using theprocess_fidelityfunction from theQuantum Informationmodule. This is an information-theoretic quantity for how close two quantum channels are to each other, and in the case of unitary operators it does not depend on global phase.

Output:

Note that process fidelity is generally only a valid measure of closeness if the input operators are unitary (or CP in the case of quantum channels), and an exception is raised if the inputs are not CP.

On this page

© IBM Corp., 2017-2025


---

# Pulse schedules







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Pulse-level control onallIBM Quantum® processors has been removed and this tutorial willnot work correctlyusing these QPUs.

If you were using pulse schedules to execute single and two-qubit rotations, use the newfractional gatesfeature. Alternatively, if you would like to simulate pulse schedules for you work, check out theQiskit Dynamicspackage.

Additionally, theqiskit.pulsemodule has beenremovedas of the Qiskit SDK v2.0.0 (but is still supported under the Qiskit SDK v1.4 until September of 2025). See thepulse migration guidefor more information.

Most quantum algorithms can be described with circuit operations alone. When you need more control over the low-level program implementation, you can usepulse gates. Pulse gates remove the constraint of executing circuits with basis gates only and let you override the default implementation of any basis gate.

Pulse gates let you map a logical circuit gate (for example,X) to a Qiskit Pulse program, called aScheduleBlock. This mapping is referred to as acalibration. A high-fidelity calibration is one that faithfully implements the logical operation it is mapped from (for example, whether theXgate calibration drives∣0⟩|0\rangle∣0⟩to∣1⟩|1\rangle∣1⟩).

A schedule specifies the exact time dynamics of the input signals across all inputchannelsto the device. There are usually multiple channels per qubit, such as drive and measure. This interface is more powerful, and requires a deeper understanding of the underlying device physics.

It's important to note that pulse programs operate on physical qubits. A drive pulse on qubitaaadoes not enact the same logical operation on the state of qubitbbb.  In other words, gate calibrations are not interchangeable across qubits. This is in contrast to the circuit level, where anXgate is defined independently of its qubit operand.

This page shows you how to add a calibration to your circuit.

Note:Not all QPUs support pulse gates. To see which QPUs have pulse gate support, filter your view (click the funnel icon) on theCompute resources pageby checking thePulse gatesbox.

Let's start with a very simple example, a Bell state circuit.

Output:

Define a calibration for the Hadamard gate on qubit 0.

In practice, the pulse shape and its parameters would be optimized through a series of calibration experiments. For this demonstration, the Hadamard will be a Gaussian pulse. Youplaythe pulse on thedrivechannel of qubit 0.

For more information about calibrations, see thelegacy Qiskit Experiments tutorial in GitHub.

Output:

Let's draw the new schedule to see what we've built.

Output:

All that remains is to complete the registration. The circuit methodadd_calibrationneeds information about the gate and a reference to the schedule to complete the mapping:

QuantumCircuit.add_calibration(gate, qubits, schedule, parameters)

Thegatecan be either acircuit.Gateobject or the name of the gate. Usually, you'll need a different schedule for each unique set ofqubitsandparameters. Since the Hadamard gate doesn't have any parameters, there is no need to supply any.

Output:

Lastly, note that the transpiler will respect your calibrations. Use it as you normally would (our example is too simple for the transpiler to optimize, so the output is the same).

Output:

Notice thathis not a basis gate for the mock backendFakeHanoiV2. Since you added a calibration for it, the transpiler will treat the gate as a basis gate,but only on the qubits for which it was defined. A Hadamard applied to a different qubit would be unrolled to the basis gates.

This demonstrates the same process for nonstandard, completely custom gates, including a gate with parameters.

Output:

Output:

If you use theGateinstance variablecustom_gateto add the calibration, the parameters are derived from that instance. Remember that the order of parameters is significant.

Output:

Normally, if you tried to transpilecirc, you would get an error. There was no functional definition provided for"my_custom_gate", so the transpiler can't unroll it to the basis gate set of the target device. You can show this by trying to add"my_custom_gate"to another qubit that hasn't been calibrated.

Output:

To link a custom gate to your circuits, you can also add toTargetand transpile. A pass manager pass implicitly extracts calibration data from the target and callsadd_calibration. This is convenient if you need to attach a calibration to multiple circuits or manage multiple calibrations.

Output:

Pulse gates define a low-level, exact representation for a circuit gate. A single operation can be implemented with a pulse program, which is comprised of multiple low-level instructions.  Regardless of how the program is used, the syntax for building the program is the same.

Important:For IBM® devices, pulse programs are used as subroutines to describe gates. IBM devices do not accept full programs in this format.

A pulse program, which is called aScheduleBlock, describes instruction sequences for the control electronics. Use the Pulse Builder to build aScheduleBlock, then initialize a schedule:

Output:

You can see that there are no instructions yet. The next section explains each of the instructions you might add to a schedule, and the last section will describe variousalignment contexts, which determine how instructions are placed in time relative to one another.

Each instruction type has its own set of operands. As you can see above, they each include at least oneChannelto specify where the instruction will be applied.

Channelsare labels for signal lines from the control hardware to the quantum chip.

DriveChannels,ControlChannels, andMeasureChannels are allPulseChannels; this means that they supporttransmittingpulses, whereas theAcquireChannelis a receive channel only and cannot play waveforms.

In the following examples, you can create oneDriveChannelinstance for eachInstructionthat accepts aPulseChannel. Channels take one integerindexargument. Except forControlChannels, the index maps trivially to the qubit label.

Output:

The pulseScheduleBlockis independent of the backend it runs on. However, you can build your program in a context that is aware of the target backend by supplying it topulse.build. When possible you should supply a backend. By using the channel accessorspulse.<type>_channel(<idx>)you ensure you are only using available device resources.

Output:

One of the simplest instructions isdelay. This is a blocking instruction that tells the control electronics to output no signal on the given channel for the duration specified. It is useful for controlling the timing of other instructions.

The duration here and elsewhere is in terms of the backend's cycle time (1 / sample rate),dt. It must take an integer value.

To add adelayinstruction, pass a duration and a channel, wherechannelcan be any kind of channel, includingAcquireChannel. Usepulse.buildto begin a Pulse Builder context. This automatically schedules the delay into the scheduledelay_5dt.

Output:

Any instruction added after this delay on the same channel will execute five timesteps later than it would have without this delay.

Theplayinstruction is responsible for executingpulses. It's straightforward to add a play instruction:

Let's clarify what thepulseargument is and explore a few different ways to build one.

APulsespecifies an arbitrary pulseenvelope. The modulation frequency and phase of the output waveform are controlled by theset_frequencyandshift_phaseinstructions.

There are many methods available for building pulses, such as those available in the Qiskit Pulselibrary.  Take for example a simple Gaussian pulse -- a pulse with its envelope described by a sampled Gaussian function. We arbitrarily choose an amplitude of 1, standard deviationσ\sigmaσof 10, and 128 sample points.

Note: The amplitude norm is arbitrarily limited to1.0. Each backend may also impose further constraints.  For instance, a minimum pulse size of 64. Any additional constraints are provided throughTarget.

You can build a Gaussian pulse by using theGaussianparametric pulse. A parametric pulse sends the name of the function and its parameters to the backend, rather than every individual sample. Using parametric pulses makes the jobs much smaller to send. IBM Quantum backends limit the maximum job size that they accept, so parametric pulses might allow you to run larger programs.

Other parametric pulses in thelibraryincludeGaussianSquare,Drag, andConstant. See thefull list in the API reference.

Note: The backend is responsible for deciding how to sample the parametric pulses. It is possible to draw parametric pulses, but the samples displayed are not guaranteed to be the same as those executed on the backend.

Output:

AWaveformis a pulse signal specified as an array of time-ordered complex amplitudes, orsamples. Each sample is played for one cycle, a timestepdt, determined by the backend. You must know the value ofdtto determine a program's real-time dynamics. The (zero-indexed)ithi^{th}ithsample plays from timei*dtup to(i + 1)*dt, modulated by the qubit frequency.

Output:

Regardless of which method you use to specify yourpulse,playis added to your schedule the same way:

Output:

You may also supply a complex list or array directly toplay.

Output:

Theplayinstruction gets its duration from itsPulse: the duration of a parametrized pulse is an explicit argument, and the duration of aWaveformis the number of input samples.

As explained previously, the output pulse waveform envelope is also modulated by a frequency and phase. Each channel has a default frequency listed in thebackend.defaults.

A channel's frequency can be updated at any time within aScheduleBlockby theset_frequencyinstruction. It takes a floatfrequencyand aPulseChannelchannelas input. All pulses on a channel following aset_frequencyinstruction are modulated by the given frequency until anotherset_frequencyinstruction is encountered or until the program ends.

The instruction has an implicit duration of0.

Note: The frequencies that can be requested are limited by the total bandwidth and the instantaneous bandwidth of each hardware channel. In the future, these will be reported by thebackend.

Output:

Theshift_frequencyinstruction shifts thefrequencyof a pulsechannel.

Output:

Theshift_frequencyandset_frequencyinstructions change the frequency of following pulses and also change the channel's frame of reference. Because a qubit oscillates at its transition frequency, the controller needs to sync with its oscillation; otherwise, an unwanted Z drive is continuously applied. Usually, because the frame is matched with the drive's frequency, and drive matches with the transition's frequency, the Z drive is eliminated when the qubit frequency is calibrated properly. When you apply theshift_frequencyinstruction, it changes the drive frequency and impacts the frame. In other words, it accumulates the phase (Z) as a function of shifted frequency and duration of the program. Specifically, when you shift the frequency bydfand spenddton that frame, the qubit may experience a phase rotation ofdf * dt. The programmer needs to take this into account to control their qubits precisely.

Note also that these instructions are localized in the pulse gate in IBM devices. This means that accumulated phase and frequency shifts are not carried over. Each pulse gate always starts from the hardware default setting. This behavior is backend-dependent.

Theset_phaseinstruction sets the phase of a pulse channel.

Output:

Theshift_phaseinstruction will increase the phase of the frequency modulation byphase. Likeset_frequency, this phase shift will affect all following instructions on the same channel until the program ends. To undo the affect of ashift_phase, the negativephasecan be passed to a new instruction.

Likeset_frequency, the instruction has an implicit duration of0.

Output:

Theacquireinstruction triggers data acquisition for readout. It takes a duration, anAcquireChannel, which maps to the qubit being measured, and aMemorySlotor aRegisterSlot. TheMemorySlotis classical memory where the readout result will be stored. TheRegisterSlotmaps to a register in the control electronics that stores the readout result for fast feedback.

Theacquireinstruction can also take customDiscriminators andKernels as keyword arguments. TheKernelsubroutine integrates a time series of measurement responses and generates an IQ data point, which will be classified into a quantum state by the discriminator. This indicates that if you use a custom measurement stimulus, as in a measurement pulse, you might need to update the kernel setting to not deteriorate the measurement SNR.

Output:

After addingScheduleBlockinstructions, you need to understand how to control when they're played.

Below are the most important Pulse Builder features for learning how to build schedules. This is not an exhaustive list.  For more details about using the Pulse Builder, refer to thePulse API reference.

The builder has alignment contexts that influence how a schedule is built. Contexts can also be nested. Try them out, and use.draw()to see how the pulses are aligned.

Regardless of the alignment context, the duration of the resulting schedule is as short as it can be while including every instruction and following the alignment rules. This still allows some degrees of freedom for scheduling instructions off the "longest path". The examples below illustrate this.

The builder has alignment contexts that influence how a schedule is built. The default isalign_left.

Output:

Notice how there is no scheduling freedom for the pulses onD1. The second waveform begins immediately after the first. The pulse onD0can start at any time betweent=0andt=100without changing the duration of the overall schedule. Thealign_leftcontext sets the start time of this pulse tot=0. You can think of this like left-justification of a text document.

align_rightdoes the opposite ofalign_left. It choosest=100in the above example to begin the Gaussian pulse onD0. Left and right are also sometimes called "as soon as possible" and "as late as possible" scheduling, respectively.

Output:

If the duration of a particular block is known, you can also usealign_equispacedto insert equal duration delays between each instruction.

Output:

This alignment context does not schedule instructions in parallel. Each instruction will begin at the end of the previously added instruction.

Output:

The builder can help temporarily offset the frequency or phase of pulses on a channel.

Output:

On this page

© IBM Corp., 2017-2025


---

# Introduction to OpenQASM







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

OpenQASM (open quantum assembly language), a machine-independent programming interface compatible with IBM® QPUs, is an imperative programming language for describing quantum circuits. OpenQASM uses the quantum circuit model to express quantum programs as ordered sequences of parameterized operations (such as gates, measurements, and resets) and real-time classical computation. In addition to quantum algorithms, OpenQASM can describe circuits intended to characterize, validate, or debug quantum processors.

As the needs of QPU development have evolved, OpenQASM's feature list has expanded in response; the latest version,OpenQASM 3,incorporates extensions including classical feed-forward flow control, gate modifiers, and pulse implementations.

OpenQASM is the choice for a variety of audiences because of its versatility. The introduction to the OpenQASM 3 paper1gives examples:

"Although OpenQASM is not a high-level language, many users would like to write simple quantum circuits by hand using an expressive domain-specific language. Researchers who study circuit compiling need high-level information recorded in the intermediate representations to inform the optimization and synthesis algorithms. Experimentalists prefer the convenience of writing circuits at a relatively high level but often need to manually modify timing or pulse-level gate descriptions at various points in the circuit. Hardware engineers who design the classical controllers and waveform generators prefer languages that are practical to compile given the hardware constraints and make explicit circuit structure that the controllers can take advantage of."

OpenQASM is the common interchange format among independent quantum software tools. For developers that prefer one tool for circuit construction, another for transpilation, and so forth, OpenQASM is thelingua francathat acts as a bridge among them.

The Qiskit SDK provides ways to convert between OpenQASM and theQuantumCircuitclass (seeOpenQASM 2 and QiskitandOpenQASM 3 and Qiskitfor instructions).

For more information, view theOpenQASM live specification.

Andrew W. Cross et al. "OpenQASM 3: A broader and deeper quantum assembly language,"ACM Transactions on Quantum Computing, Volume 3, Issue 3 (2022).https://doi.org/10.48550/arXiv.2104.14722↩

On this page

© IBM Corp., 2017-2025


---

# OpenQASM 2 and the Qiskit SDK







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The Qiskit SDK provides some tools for converting between OpenQASM representations of quantum programs, and theQuantumCircuitclass.

Two functions import OpenQASM 2 programs into Qiskit.
These areqasm2.load(), which takes a filename, andqasm2.loads(), which takes the OpenQASM 2 program as a string.

See theOpenQASM 2 Qiskit APIfor more information.

For most OpenQASM 2 programs, you can simply useqasm2.loadandqasm2.loadswith a single argument.

Useqasm2.loads()to import an OpenQASM 2 program as a string into a QuantumCircuit:

Output:

Useload()to import an OpenQASM 2 program from a file into a QuantumCircuit:

By default, Qiskit's OpenQASM 2 importer treats the include file"qelib1.inc"as ade factostandard library.
The importer treats this file as containing precisely the gates it is described to contain inthe original paper defining OpenQASM 2.
Qiskit will use the built-in gates inthe circuit libraryto represent the gates in"qelib1.inc".
Gates defined in the program by manual OpenQASM 2gatestatements will, by default, be constructed as customQiskitGatesubclasses.

You can tell the importer to use specificGateclasses for the givengatestatements it encounters.
You can also use this mechanism to treat additional gate names as "built-in", that is, not requiring an explicit definition.
If you specify which gate classes to use forgatestatements outside of"qelib1.inc", the resulting circuit will typically be more efficient to work with.

As of Qiskit SDK 1.0, Qiskit's OpenQASM 2exporter(seeExport a Qiskit circuit to OpenQASM 2) still behaves as if"qelib1.inc"has more gates than it really does.
This means that the default settings of the importer might not be able to import a program exported by our importer.
Seethe specific example on working with the legacy exporterto resolve this problem.

This discrepancy is legacy behavior of Qiskit, andit will be resolved in a later release of Qiskit.

To pass information about a custom instruction to the OpenQASM 2 importer, usetheqasm2.CustomInstructionclass.
This has four required pieces of information, in order:

If the importer encounters agatedefinition that matches a given custom instruction, it will use that custom information to reconstruct the gate object.
If agatestatement is encountered that matches thenameof a custom instruction, but does not match both the number of parameters and the number of qubits, the importer will raise aQASM2ParseError, to indicate the mismatch between the supplied information and program.

In addition, a fifth argumentbuiltincan be optionally set toTrueto make the gate automatically available within the OpenQASM 2 program, even if it is not explicitly defined.
If the importer does encounter an explicitgatedefinition for a built-in custom instruction, it will accept it silently.
As before, if an explicit definition of the same name is not compatible with the provided custom instruction, aQASM2ParseErrorwill be raised.
This is useful for compatibility with older OpenQASM 2 exporters, and with certain other quantum platforms that treat the "basis gates" of their hardware as built-in instructions.

Qiskit provides a data attribute for working with OpenQASM 2 programs produced by legacy versions ofQiskit's OpenQASM 2 exporting capabilities.
This isqasm2.LEGACY_CUSTOM_INSTRUCTIONS, which can be given as thecustom_instructionsargument toqasm2.load()andqasm2.loads().

This OpenQASM 2 program uses gates that are not in the original version of"qelib1.inc"without declaring them, but are standard gates in Qiskit's library.
You can useqasm2.LEGACY_CUSTOM_INSTRUCTIONSto easily tell the importer to use the same set of gates that Qiskit's OpenQASM 2 exporter previously used.

Qiskit cannot, in general, verify if the definition in an OpenQASM 2gatestatement corresponds exactly to a Qiskit standard-library gate.
Instead, Qiskit chooses a custom gate using the precise definition supplied.
This can be less efficient that using one of the built-in standard gates, or a user-defined custom gate.
You can manually definegatestatements with particular classes.

If the argumentbuiltin=Trueis set, a custom gate does not need to have an associated definition.

OpenQASM 2 includes some built-in classical functions to use in gate arguments.
You can extend the language with more functions by using thecustom_classicalargument toqasm2.load()andqasm2.loads(), with theqasm2.CustomClassicalclass.

To define a custom classical function, you must supply:

All defined custom classical functions are treated as built-in to the OpenQASM 2 language by the importer.
There is no official way within the OpenQASM 2 language to define new functions; this is a Qiskit extension.

Here we provide two custom classical functions.
The first is simple, and just adds one to its input.
The second is the functionmath.atan2, which represents the mathematical operationarctan⁡(y/x)\arctan(y/x)arctan(y/x)in a quadrant-aware manner.

By default, this parser is more relaxed than the official specification.
It allows trailing commas in parameter lists; unnecessary (empty-statement) semicolons; omission of theOPENQASM 2.0;version statement; and several other quality-of-life improvements without emitting any errors.
However, you can use the "letter-of-the-spec" mode withstrict=True.

Qiskit can also export aQuantumCircuitto OpenQASM 2.
You use the functionqasm2.dump()to write to a file, andqasm2.dumps()to write to a string.
These functions currently have a very simple interface: they accept a circuit and, only in the case ofqasm2.dump(), a location to write the output to.

Qiskit's OpenQASM 2 exporter still assumes a legacy, non-standard version of the"qelib1.inc"include file.This will be resolved in a later release of Qiskit, but in the meantime, if you need to re-import an OpenQASM 2 program created with Qiskit, usethe example above for how to tell the importer about the legacy gates.

On this page

© IBM Corp., 2017-2025


---

# OpenQASM 3 and the Qiskit SDK







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The Qiskit SDK provides some tools for converting between OpenQASM representations of quantum programs, and the QuantumCircuit class. Note these tools are still in an exploratory phase of development and will continue to evolve as Qiskit's support for dynamic circuit capabilities expressed by OpenQASM 3 increases.

This function is still in the exploratory phase.  Therefore, it is likely that the syntax and capabilities will evolve.

You must install the packageqiskit_qasm3_importto use this function. Install using the following command.

Currently two high-level functions are available for importing from OpenQASM 3 into Qiskit. These functions areload(), which takes a file name, andloads(), which takes the program itself as a string:

In this example, we define a quantum program using OpenQASM 3, and useloads()to directly convert it into a QuantumCircuit:

Output:

You can export Qiskit code to OpenQASM 3 withdumps(), which exports to a string, ordump(), which exports to a file.

Output:

For more information, see theExporting to OpenQASM 3section of the API reference.

On this page

© IBM Corp., 2017-2025


---

# OpenQASM 3 feature table







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Below is a list of theOpenQASM 3language features.

For more details on these capabilities, see theOpenQASM 3.X Live Specification.

Key:

On this page

© IBM Corp., 2017-2025


---

# Introduction to transpilation







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Transpilation is the process of rewriting a given input circuit to match the topology of a specific quantum device, and optimize the circuit instructions for execution on noisy quantum computers.  This documentation covers the tooling and workflows for local transpilation available to all Qiskit users, as well as for the cloud-basedQiskit Transpiler Serviceavailable to Premium Plan users.  If you're using primitives and are only interested in the default transpilation options provided by the Qiskit Runtime service, read theConfigure runtime compilation for Qiskit Runtimetopic.

The process of transpilation takes a circuit that contains your instructions:

Transpilation then transforms it such that only instructions available on a chosen backend are used, and optimizes those instructions to minimize the effects of noise:

A central component of the Qiskit SDK, the transpiler is designed for modularity and extensibility. Its main use is to write new circuit transformations (known as transpilerpasses), and combine them with other existing passes, greatly reducing the depth and complexity of quantum circuits.  Which passes are chained together and in which order has a major effect on the final outcome. This pipeline is determined by thePassManagerandStagedPassManagerobjects.  TheStagedPassManagerorchestrates the execution of one or morePassManagersand determines the order in which they are executed, while thePassManagerobject is merely a collection of one or more passes.  Think of theStagedPassManageras the conductor in an orchestra, thePassManagersas the different instrument sections, and thePassobjects as the individual musicians.  In this way, you can compose hardware-efficient quantum circuits that let you execute utility-scale work while keeping noise manageable.

Find more information about the pass manager stages in theTranspiler stagestopic.

In addition to reducing the depth and complexity of quantum circuits, the transpiler is designed to transform the instructions contained in a givenQuantumCircuitto obey the Instruction Set Architecture (ISA) of a particular backend.  Circuits obeying the ISA consist only of instructions that are supported by the backend'sTarget, such as the hardware's available basis gates, measurements, resets, and control flow operations, and comply with the constraints specified by the connectivity of the hardware, that is, the target'sCouplingMap.  When submitting a job to an IBM Quantum® backend, the circuits must adhere to the backend's ISA.

Qiskit's prebuilt transpiler pipeline consists of six fundamental stages:

If you customize a transpilation workflow, use these stages as a guideline during development.

The recommended way to transpile a circuit is to create a staged pass manager and then execute itsrunmethod with your circuit as input. You can use thegenerate_preset_pass_managerfunction to generate a staged pass manager with reasonable defaults.

More advanced users can customize a set ofPassManagerandStagedPassManagerobjects and determine the order in which each stage is run.  This can dramatically change the final output circuit. In fact, a custom approach to transpiling a quantum algorithm often produces more efficient error suppression than the default approach.  A custom approach involves rewriting quantum circuits to match hardware constraints and suppress the effects of noise.  The flow of logic for this tool chain is customizable and need not be linear.  The transpilation process can prepare iterative loops, conditional branches, and other complex behaviors.  A good starting place when developing a set of custom passes is to examine the default sequence of transformations.

For an overview of transpiling using pass managers, seeTranspile with pass managers.

For a simpler, but less customizable, "out-of-the-box" way to use the transpiler, use theqiskit.compiler.transpilefunction.  This generates and runs one of the presetStagedPassManagers based on, among other options, anoptimization_levelflag that can be set to 0, 1, 2, or 3.  Higher levels generate more optimized circuits at the expense of longer transpilation times.

On this page

© IBM Corp., 2017-2025


---

# Transpile with pass managers







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The recommended way to transpile a circuit is to create a staged pass manager and then execute itsrunmethod with the circuit as input. This page explains how to transpile quantum circuits this way.

In the context of the Qiskit SDK, transpilation refers to the process of transforming an input circuit into a form that is suitable for execution on a quantum device. Transpilation typically occurs in a sequence of steps called transpiler passes. The circuit is processed by each transpiler pass in sequence, with the output of one pass becoming the input to the next. For example, one pass could go through the circuit and merge all consecutive sequences of single-qubit gates, and then the next pass could synthesize these gates into the basis set of the target device. The transpiler passes included with Qiskit are located in theqiskit.transpiler.passesmodule.

A pass manager is an object that stores a list of transpiler passes and can execute them on a circuit. Create a pass manager by initializing aPassManagerwith a list of transpiler passes. To run the transpilation on a circuit, call therunmethod with a circuit as input.

A staged pass manager is a special kind of pass manager that represents a level of abstraction above that of a normal pass manager. While a normal pass manager is composed of several transpiler passes, a staged pass manager is composed of severalpass managers. This is a useful abstraction because transpilation typically happens in discrete stages, as described inTranspiler stages, with each stage being represented by a pass manager. Staged pass managers are represented by theStagedPassManagerclass. The rest of this page describes how to create and customize (staged) pass managers.

To create a preset staged pass manager with reasonable defaults, use thegenerate_preset_pass_managerfunction:

To transpile a circuit or list of circuits with a pass manager, pass the circuit or list of circuits to therunmethod. Let's do this on a two-qubit circuit consisting of a Hadamard followed by two adjacent CX gates:

Output:

SeeTranspilation defaults and configuration optionsfor a description of the possible arguments to thegenerate_preset_pass_managerfunction. The arguments togenerate_preset_pass_managermatch the arguments to thetranspilefunction.

Having trouble remembering pass manager details? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

If the preset pass managers don't fulfill your needs, customize transpilation by creating (staged) pass managers or even transpilation passes. The rest of this page describes how to create pass managers. For instructions on how to create transpilation passes, seeWrite your own transpiler pass.

Theqiskit.transpiler.passesmodule includes many transpiler passes that can be used to create pass managers. To create a pass manager, initialize aPassManagerwith a list of passes. For example, the following code creates a transpiler pass that merges adjacent two-qubit gates and then synthesizes them into a basis ofRyR_yRy​,RzR_zRz​, andRxxR_{xx}Rxx​,  gates.

To demonstrate this pass manager in action, test it on a two-qubit circuit consisting of a Hadamard followed by two adjacent CX gates:

Output:

To run the pass manager on the circuit, call therunmethod.

Output:

For a more advanced example that shows how to create a pass manager to implement the error suppression technique known as dynamical decoupling, seeCreate a pass manager for dynamical decoupling.

AStagedPassManageris a pass manager that is composed of individual stages, where each stage is defined by aPassManagerinstance. You can create aStagedPassManagerby specifying the desired stages. For example, the following code creates a staged pass manager with two stages,initandtranslation. Thetranslationstage is defined by the pass manager that was created previously.

There is no limit on the number of stages you can put in a staged pass manager.

Another useful way to create a staged pass manager is to begin with a preset staged pass manager and then swap out some of the stages. For example, the following code generates a preset pass manager with optimization level 3, and then specifies a custompre_layoutstage.

Thestage generator functionsmight be useful for constructing custom pass managers.
They generate stages that provide common functionality used in many pass managers.
For example,generate_embed_passmanagercan be used to generate a stage
to "embed" a selected initialLayoutfrom a layout pass to the specified target device.

On this page

© IBM Corp., 2017-2025


---

# Create a pass manager for dynamical decoupling







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page demonstrates how to use thePadDynamicalDecouplingpass to add an error suppression technique calleddynamical decouplingto the circuit.

Dynamical decoupling works by adding pulse sequences (known asdynamical decoupling sequences) to idle qubits to flip them around the Bloch sphere, which cancels the effect of noise channels, thereby suppressing decoherence. These pulse sequences are similar to refocusing pulses used in nuclear magnetic resonance. For a full description, seeA Quantum Engineer's Guide to Superconducting Qubits.

Because thePadDynamicalDecouplingpass only operates on scheduled circuits and involves gates that are not necessarily basis gates of our target, you will need theALAPScheduleAnalysisandBasisTranslatorpasses as well.

This example usesibm_brisbane, which was initialized previously. Get thetargetinformation from thebackendand save the operation names asbasis_gatesbecause thetargetwill need to be modified to add timing information for the gates used in dynamical decoupling.

Create anefficient_su2circuit as an example. First, transpile the circuit to the backend because dynamical decoupling pulses need to be added after the circuit has been transpiled and scheduled. Dynamical decoupling often works best when there is a lot of idle time in the quantum circuits - that is, there are qubits that are not being used while others are active. This is the case in this circuit because the two-qubitecrgates are applied sequentially in this ansatz.

Output:

A dynamical decoupling sequence is a series of gates that compose to the identity and are spaced regularly in time. For example, start by creating a simple sequence called XY4 consisting of four gates.

Because of the regular timing of dynamical decoupling sequences, information about theYGatemust be added to thetargetbecause it isnota basis gate, whereas theXGateis. We knowa priorithat theYGatehas the same duration and error as theXGate, however, so we can just retrieve those properties from thetargetand add them back for theYGates. This is also why thebasis_gateswere saved separately, since we are adding theYGateinstruction to thetargetalthough it is not an actual basis gate ofibm_brisbane.

Ansatz circuits such asefficient_su2are parameterized, so they must have value bound to them before being sent to the backend. Here, assign random parameters.

Next, execute the custom passes. Instantiate thePassManagerwithALAPScheduleAnalysisandPadDynamicalDecoupling.  RunALAPScheduleAnalysisfirst to add timing information about the quantum circuit before the regularly-spaced dynamical decoupling sequences can be added. These passes are run on the circuit with.run().

Use the visualization tooltimeline_drawerto see the circuit's timing and confirm that a regularly-spaced sequence ofXGates andYGates appear in the circuit.

Output:

Lastly, because theYGateis not an actual basis gate of our backend, manually apply theBasisTranslatorpass (this is a default pass, but it is executed before scheduling, so it needs to be applied again). The session equivalence library is a library of circuit equivalences that allows the transpiler to decompose circuits into basis gates, as also specified as an argument.

Output:

Now,YGates are absent from our circuit, and there is explicit timing information in the form ofDelaygates. This transpiled circuit with dynamical decoupling is now ready to be sent to the backend.

On this page

© IBM Corp., 2017-2025


---

# Transpilation default settings and configuration options







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Abstract circuits need to be transpiled because QPUs have a limited set of basis gates and cannot execute arbitrary operations. The transpiler's function is to change arbitrary circuits so that they can run on a specified QPU.  This is done by translating the circuits to the supported basis gates, and by introducing SWAP gates as needed, so that the circuit's connectivity matches that of the QPU.

As explained inTranspile with pass managers, you can create apass managerusing thegenerate_preset_pass_managerfunction and pass a circuit or list of circuits to itsrunmethod to transpile them. You can callgenerate_preset_pass_managerpassing only the optimization level and backend, choosing to use the defaults for all other options, or you can pass additional arguments to the function to fine-tune the transpilation.

In this example, we pass a circuit and target QPU to the transpiler without specifying any further parameters.

Create a circuit and view the result:

Output:

Transpile the circuit and view the result:

Output:

Following are all of the available parameters for thegenerate_preset_pass_managerfunction.  There are two classes of arguments: those that describe the target of compilation, and those that influence how the transpiler works.

All parameters exceptoptimization_levelare optional.  For full details, see theTranspiler API documentation.

These arguments describe the target QPU for circuit execution, including information such as the coupling map of the QPU (which describes the connectivity of the qubits), the basis gates supported by the QPU, and the error rates of the gates.

Many of these parameters are described in detail inCommonly used parameters for transpilation.

QPU (Backend) parameters

Backend parameters- If you specifybackend, you don't need to specifytargetor any other backend options. Likewise, if you specifytarget, you don't need to specifybackendor any other backend options.

Layout and topology parameters

These parameters impact specific transpilation stages. Some of them might impact multiple stages, but have only been listed under one stage for simplicity. If you specify an argument, such asinitial_layoutfor the qubits you want to use, that value overrides all the passes that could change it. In other words, the transpiler won't change anything that you manually specify. For details about specific stages, seeTranspiler stages.

Initialization stage

Layout stage

Routing stage

Translation stage

Optimization stage

Scheduling stage

Transpiler execution

The following default values are used if you don't specify any of the above parameters. Refer to the method'sAPI reference pagefor more information:

Output:

On this page

© IBM Corp., 2017-2025


---

# Set transpiler optimization level







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Real quantum devices are subject to noise and gate errors, so optimizing the circuits to reduce their depth and gate count can significantly improve the results obtained from executing those circuits.
Thegenerate_preset_pass_managerfunction has one required positional argument,optimization_level, that controls how much effort the transpiler spends on optimizing circuits. This argument can be an integer taking one of the values 0, 1, 2, or 3.
Higher optimization levels generate more optimized circuits at the expense of longer compile times.
The following table explains the optimizations performed with each setting.

No optimization: typically used for hardware characterization

Light optimization:

Medium optimization:

High Optimization:

Since two-qubit gates are typically the most significant source of errors, we can approximately quantify the transpilation's "hardware efficiency" by counting the number of two-qubit gates in the resulting circuit.
Here, we'll try the different optimization levels on an input circuit consisting of a random unitary followed by a SWAP gate.

Output:

We'll use theFakeSherbrookemock backend in our examples. First, let's transpile using optimization level 0.

Output:

The transpiled circuit has six of the two-qubit ECR gates.

Repeat for optimization level 1:

Output:

The transpiled circuit still has six ECR gates, but the number of single-qubit gates has reduced.

Repeat for optimization level 2:

Output:

This yields the same results as optimization level 1. Note that increasing the level of optimization does not always make a difference.

Repeat again, with optimization level 3:

Output:

Now, there are only three ECR gates. We obtain this result because at optimization level 3, Qiskit tries to re-synthesize two-qubit blocks of gates, and any two-qubit gate can be implemented using at most three ECR gates. We can get even fewer ECR gates if we setapproximation_degreeto a value less than 1, allowing the transpiler to make approximations that may introduce some error in the gate decomposition (seeCommonly used parameters for transpilation):

Output:

This circuit has only two ECR gates, but it's an approximate circuit. To understand how its effect differs from the exact circuit, we can calculate the fidelity between the unitary operator this circuit implements, and the exact unitary. Before performing the computation, we first reduce the transpiled circuit, which contains 127 qubits, down to a circuit that only contains the active qubits, of which there are two.

Output:

Adjusting the optimization level can change other aspects of the circuit too, not just the number of ECR gates. For examples of how setting optimization level changes the layout, seeRepresenting quantum computers.

On this page

© IBM Corp., 2017-2025


---

# Commonly used parameters for transpilation







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page describes some of the more commonly used parameters for local transpilation. These parameters are configured using arguments togenerate_preset_pass_managerortranspile.

You can use the approximation degree to specify how closely you want the resultant circuit to match the desired (input) circuit.  This is a float in the range (0.0 - 1.0), where 0.0 is maximum approximation and 1.0 (default) is no approximation. Smaller values trade output accuracy for ease of execution (that is, fewer gates).  The default value is 1.0.

In two-qubit unitary synthesis (used in initial stages of all levels and for optimization stage with optimization level 3), this value specifies the target fidelity of the output decomposition. That is, how much error is introduced when a matrix representation of a circuit is converted to discrete gates. If the approximation degree is a lower value (more approximation), the output circuit from synthesis will differ more from the input matrix, but will also likely have fewer gates (because any arbitrary two-qubit operation can be decomposed perfectly with at most three CX gates) and is easier to run.

When the approximation degree is less than 1.0, circuits with one or two CX gates might be synthesized, leading to less error from the hardware, but more from the approximation. Since CX is the most expensive gate in terms of error, it might be beneficial to decrease the number of them at the cost of fidelity in synthesis (this technique was used to increase quantum volume on IBM® devices:Validating quantum computers using randomized model circuits).

As an example, we generate a random two-qubitUnitaryGatewhich will be synthesized in the initial stage. Setting theapproximation_degreeless than 1.0 might generate an approximate circuit. We must also specify thebasis_gatesto let the synthesis method know which gates it can use for the approximate synthesis.

Output:

This yields an output of2because the approximation requires fewer CX gates.

Some parts of the transpiler are stochastic, so repeated transpilation runs may return different results. To obtain a reproducible result, you can set the seed for the pseudorandom number generator using theseed_transpilerargument. Repeated runs using the same seed will return the same results.

Example:

Output:

Before transpilation, the qubits contained in your circuit are virtual qubits that don't necessarily correspond to physical qubits on the target backend. You can specify the initial mapping of virtual qubits to physical qubits using theinitial_layoutargument. Note that the final qubit layout may differ from the initial layout because the transpiler may permute qubits using swap gates or other means.

In the example below, we construct an initial layout for theFakeSherbrookemock backend by creating aLayoutobject. Our layout maps the first qubit of our circuit to qubit 5 of Sherbrooke, and it maps the second qubit of our circuit to qubit 6 of Sherbrooke. Note that physical qubits are always represented by integers.

Output:

In addition to specifying a Layout object, you can also pass a list of integers, where theiii-th element of the list contains the physical qubit that theiii-th qubit should be mapped to. For example:

Output:

You can use theplot_error_mapfunction to generate a diagram of the device graph with error information and with the physical qubits labeled. You can also view similar diagrams athttps://quantum.ibm.com/services/resources.

Output:

These options are suffixed with_method. They influence how the transpiler works and are used to try and get better, different, or specific output from the transpiler.

init_method(str) - The plugin to use for the initialization stage.

layout_method(str) - The layout selection pass (trivial,dense,sabre). This can also be the external plugin name to use for the layout stage.

optimization_method(str) - The plugin to use for the optimization stage.

routing_method(str) - Name of routing pass (basic,lookahead,default,sabre,none). This can also be the external plugin name to use for the routing stage.

scheduling_method(str) - Name of scheduling pass. This can also be the external plugin name to use for the scheduling stage.

translation_method(str) - Name of translation pass (unroller,translator,synthesis). This can also be the external plugin name to use for the translation stage.

unitary_synthesis_method(str) - The name of the unitary synthesis method to use. By defaultdefaultis used.

To see a list of all installed plugins for a given stage, runlist_stage_plugins("stage_name"). For example, if you want to see a list of all installed plugins for the routing stage, runlist_stage_plugins(routing).

On this page

© IBM Corp., 2017-2025


---

# Representing quantum computers for the transpiler







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

To convert an abstract circuit to an ISA circuit that can run on a specific QPU (quantum processing unit), the transpiler needs certain information about the QPU. This information is found in two places: theBackendV2(or legacyBackendV1) object you plan to submit jobs to, and the backend'sTargetattribute.

You can also explicitly provide information for the transpiler to use, for example, if you have a specific use case, or if you believe this information will help the transpiler generate a more optimized circuit.

The precision with which the transpiler produces the most appropriate circuit for specific hardware depends on how much information theTargetorBackendhas about its constraints.

Because many of the underlying transpilation algorithms are stochastic, there is no guarantee that a better circuit will be found.

This page shows several examples of passing QPU information to the transpiler. These examples use the target from theFakeSherbrookemock backend.

The simplest use of the transpiler is to provide all the QPU information by providing theBackendorTarget. To better understand how the transpiler works, construct a circuit and transpile it with different information, as follows.

Import the necessary libraries and instantiate the QPU:
In order to convert an abstract circuit to an ISA circuit that can run on a specific processor, the transpiler needs certain information about the processor.  Typically, this information is stored in theBackendorTargetprovided to the transpiler, and no further information is needed. However, you can also explicitly provide information for the transpiler to use, for example, if you have a specific use case, or if you believe this information will help the transpiler generate a more optimized circuit.

This topic shows several examples of passing information to the transpiler. These examples use the target from theFakeSherbrookemock backend.

The example circuit uses an instance ofefficient_su2from Qiskit's circuit library.

Output:

This example uses default settings to transpile to thebackend'starget, which provides all the information needed to convert the circuit to one that will run on the backend.

Output:

This example is used in later sections of this topic to illustrate that the coupling map and basis gates are the essential pieces of information to pass to the transpiler for optimal circuit construction. The QPU can usually select default settings for other information that is not passed in, such as timing and scheduling.

The coupling map is a graph that shows which qubits are connected and hence have two-qubit gates between them. Sometimes this graph is directional, meaning that the two-qubit gates can only go in one direction. However, the transpiler can always flip a gate's direction by adding additional single-qubit gates. An abstract quantum circuit can always be represented on this graph, even if its connectivity is limited, by introducing SWAP gates to move the quantum information around.

The qubits from our abstract circuits are calledvirtual qubitsand those on the coupling map arephysical qubits. The transpiler provides a mapping between virtual and physical qubits. One of the first steps in transpilation, thelayoutstage, performs this mapping.

Although the routing stage is intertwined with thelayoutstage — which selects the actual qubits — by default, this topic treats them as separate stages for simplicity. The combination of routing and layout is calledqubit mapping.  Learn more about these stages in theTranspiler stagestopic.

Pass thecoupling_mapkeyword argument to see its effect on the transpiler:

Output:

As shown above, several SWAP gates were inserted (each consisting of three CX gates), which will cause a lot of errors on current devices. To see which qubits are selected on the actual qubit topology, useplot_circuit_layoutfrom Qiskit Visualizations:

Output:

This shows that our virtual qubits 0-11 were trivially mapped to the line of physical qubits 0-11. Let's return to the default (optimization_level=1), which usesVF2Layoutif any routing is required.

Output:

Now there are no SWAP gates inserted and the physical qubits selected are the same when using thetargetclass.

Output:

Now the layout is in a ring.  Because this layout respects the circuit's connectivity, there are no SWAP gates, providing a much better circuit for execution.

Every quantum computer supports a limited instruction set, called itsbasis gates.  Every gate in the circuit must be translated to the elements of this set. This set should consist of single- and two-qubit gates that provide a universal gates set, meaning that any quantum operation can be decomposed into those gates.  This is done by theBasisTranslator, and the basis gates can be specified as a keyword argument to the transpiler to provide this information.

Output:

The default single-qubit gates onibm_sherbrookearerz,x, andsx, and the default two-qubit gate isecr(echoed cross-resonance). CX gates are constructed fromecrgates, so on some QPUsecris specified as the two-qubit basis gate, while on otherscxis the default. Theecrgate is theentanglingpart of thecxgate. To use a gate that is not in the basis gate set, follow instructions in the Qiskit SDK API documentation for custom gates usingpulse gates. In addition to the control gates, there are alsodelayandmeasurementinstructions.

QPUs have default basis gates, but you can choose whatever gates you want, as long as you provide the instruction or add pulse gates (seeCreate transpiler passes.) The default basis gates are those that calibrations have been done for on the QPU, so no further instruction/pulse gates need to be provided. For example, on some QPUscxis the default two-qubit gate andecron others. See theNative gates and operationstopic for more details.

Output:

Note that theCXGates have been decomposed toecrgates and single-qubit basis gates.

TheTargetclass can contain information about the error rates for operations on the device.
For example, the following code retrieves the properties for the echoed cross-resonance (ECR) gate between qubit 1 and 0 (note that the ECR gate is directional):

Output:

The output displays the duration of the gate (in seconds) and its error rate. To reveal error information to the transpiler, build a target model with thebasis_gatesandcoupling_mapfrom above and populate it with error values from the backendFakeSherbrooke.

Transpile with our new targeterr_targas the target:

Output:

Because the target includes error information, theVF2PostLayoutpass tries to find the optimal qubits to use, resulting in the same circuit that was originally found with the same physical qubits.

On this page

© IBM Corp., 2017-2025


---

# Transpile circuits remotely with the Qiskit Transpiler Service







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The Qiskit Transpiler Service provides transpilation capabilities on the cloud. In addition to the local Qiskit transpiler capabilities, your transpilation tasks can benefit from both IBM Quantum® cloud resources and AI-powered transpiler passes.

The Qiskit Transpiler Service offers a Python library to seamlessly integrate this service and its capabilities into your current Qiskit patterns and workflows.

This service is only available for IBM Quantum Premium Plan users.
The service is a beta release, subject to change.
If you have feedback or want to contact the developer team, please use thisQiskit Slack Workspace channel.

To use the Qiskit Transpiler Service, install theqiskit-ibm-transpilerpackage:

By default, the package tries to authenticate to IBM Quantum services with the defined Qiskit API key, and uses your token from theQISKIT_IBM_TOKENenvironment variable or from the file~/.qiskit/qiskit-ibm.json(under the sectiondefault-ibm-quantum).

Note: This package requires Qiskit SDK v1.X.

For more information about the availableqiskit-ibm-transpilermethods, see theqiskit-ibm-transpiler API reference. To learn more about the service API, see theQiskit Transpiler Service REST API documentation.

The following examples demonstrate how to transpile circuits using the Qiskit Transpiler Service with different parameters.

Note: you only can use backend_name devices you have access to with your IBM Quantum account. Apart from thebackend_name, theTranspilerServicealso allowscoupling_mapas parameter.

Following are the most relevant limitations of the service:

If you use any AI-powered feature from the Qiskit Transpiler Service in your research, use the following recommended citation:

On this page

© IBM Corp., 2017-2025


---

# AI transpiler passes







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The AI-powered transpiler passes are passes that work as a drop-in replacement of "traditional" Qiskit passes for some transpiling tasks. They often produce better results than existing heuristic algorithms (such as lower depth and CNOT count), but are also much faster than optimization algorithms such as Boolean satisfiability solvers. The AI transpiler passes can run on your local environment or on the cloud using the Qiskit Transpiler Service if you are part of the IBM Quantum® Premium Plan.

The AI-powered transpiler passes are in beta release status, subject to change.
If you have feedback or want to contact the developer team, please use thisQiskit Slack Workspace channel.

The following passes are currently available:

Routing passes

Circuit synthesis passes

To use the AI transpiler passes, firstinstall theqiskit-ibm-transpilerpackage. Visit theqiskit-ibm-transpiler API documentationto get more information about the different options available.

If you want to use the AI-powered transpiler passes in your local environment for free, installqiskit-ibm-transpilerwith some extra dependencies as follows:

Without these extra dependencies, the AI-powered transpiler passes run on the cloud through the Qiskit Transpiler Service (available only for IBM Quantum Premium Plan users). After installing the extra dependencies, the default mode to run the AI-powered transpiler passes is to use your local machine.

TheAIRoutingpass acts both as a layout stage and a routing stage. It can be used within aPassManageras follows:

Here, thebackenddetermines which coupling map to route for, theoptimization_level(1, 2, or 3) determines the computational effort to spend in the process (higher usually gives better results but takes longer), and thelayout_modespecifies how to handle the layout selection.
Thelayout_modeincludes the following options:

The AI circuit synthesis passes allow you to optimize pieces of different circuit types (Clifford,Linear Function,Permutation, Pauli Network) by re-synthesizing them. A typical way to use the synthesis pass is as follows:

The synthesis respects the coupling map of the device: it can be run safely after other routing passes without disturbing the circuit, so the overall circuit will still follow the device restrictions. By default, the synthesis will replace the original sub-circuit only if the synthesized sub-circuit improves the original (currently only checking CNOT count), but this can be forced to always replace the circuit by settingreplace_only_if_better=False.

The following synthesis passes are available fromqiskit_ibm_transpiler.ai.synthesis:

We expect to gradually increase the size of the supported blocks.

All passes use a thread pool to send several requests in parallel. By default, the number for max threads is the number of cores plus four (default values for theThreadPoolExecutorPython object). However, you can set your own value with themax_threadsargument at pass instantiation. For example, the following line instantiates theAILinearFunctionSynthesispass, which allows it to use a maximum of 20 threads.

You can also set the environment variableAI_TRANSPILER_MAX_THREADSto the desired number of maximum threads, and all synthesis passes instantiated after that will use that value.

For the AI synthesis passes to synthesize a sub-circuit, it must lay on a connected subgraph of the coupling map (one way to do this is with a routing pass before collecting the blocks, but this is not the only way to do it). The synthesis passes will automatically check that the specific subgraph is supported, and if not, it will raise a warning and leave the original sub-circuit unchanged.

The following custom collection passes for Cliffords, Linear Functions and Permutations that can be imported fromqiskit_ibm_transpiler.ai.collectionalso complement the synthesis passes:

These custom collection passes limit the sizes of the collected sub-circuits so they are supported by the AI-powered synthesis passes. Therefore, it is recommended to use them after the routing passes and before the synthesis passes for a better overall optimization.

Theqiskit-ibm-transpilerallows you to configure a hybrid pass manager that combines the best of Qiskit's heuristic and the AI-powered transpiler passes. This feature behaves similarly to the Qiskitgenerate_pass_managermethod. A typical way to usegenerate_ai_pass_manageris as follows:

The following options are used in this example:

Refer to theQiskit Transpiler Service documentationfor more information about the limits that apply to the AI-powered transpiler passes.

If you use any AI-powered feature from the Qiskit Transpiler Service in your research, usethe recommended citation.

On this page

© IBM Corp., 2017-2025


---

# Transpile using REST API







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation utilizes the Pythonrequestsmodule to demonstrate the Qiskit Transpiler Service API. However, this workflow can be executed using any language or framework that supports working with REST APIs. Refer to theAPI reference documentationfor details.

The process of rewriting a given input circuit to match the topology of a specific quantum device, and optimizing the circuit instructions for execution on noisy quantum QPUs, is known astranspilation.

You have two transpilation options:

Transpilelocally via Qiskitbefore generating the QASM string.

Use theQiskit Transpiler Service Python clientorQiskit Transpiler Service REST API.

Transpilation is necessaryprior to submitting a circuit to IBM® QPUs.

The steps in this topic describe how to transpile a given QASM circuit and obtain results using the Cloud Transpiler REST API, and include suggestions on how to submit the transpiled quantum circuit to IBM compute resources.  For an example that uses parameterized input, seeSampler primitive with REST API and parameterized circuits.

Query the Qiskit Transpiler Service REST API and provide your QASM string as input. See more details in theAPI reference documentation.

There are two ways to invoke the Qiskit Transpiler Service using REST API: with regular transpilation, and with AI-enhanced transpilation. The following demonstrates both ways to invoke the Qiskit Transpiler Service API.

This experimental service is only available to IBM Quantum® Premium Plan users.

Since there might be cases where it’s more effective not to use AI-enhanced passes, you can set theaiparameter toai="auto"to enable the QPU to decide automatically whether to apply the standard Qiskit heuristic passes or the new AI-powered passes, based on the particulars of your circuit.

Request the transpilation service results using thetask_id.

Output

On this page

© IBM Corp., 2017-2025


---

# Write a custom transpiler pass







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The Qiskit SDK lets you create custom transpilation passes and run them in thePassManagerobject or add them to aStagedPassManager. Here we will demonstrate how to write a  transpiler pass, focusing on building a pass that performsPauli twirlingon the noisy quantum gates in a quantum circuit. This example uses the DAG, which is the object manipulated by theTransformationPasstype of pass.

Background: DAG representation

Before building a pass, it is important to introduce the internal representation of quantum circuits in Qiskit, thedirected acyclic graph (DAG)(seethis tutorialfor an overview).  To follow these steps, install thegraphvizlibraryfor the DAG plotting functions.

In Qiskit, within the transpilation stages, circuits are represented using a DAG.  In general, a DAG is composed ofvertices(also known as "nodes") and directededgesthat connect pairs of vertices in a particular orientation.  This representation is stored usingqiskit.dagcircuit.DAGCircuitobjects that are composed of invididualDagNodeobjects.  The advantage of this representation over a pure list of gates (that is, anetlist) is that the flow of information between operations is explicit, making it easier to make transformation decisions.

This example illustrates the DAG by creating a simple circuit that prepares a Bell state and applies anRZR_ZRZ​rotation, depending on the measurement outcome.

Use theqiskit.tools.visualization.dag_drawer()function to view this circuit's DAG.  There are three kinds of graph nodes: qubit/clbit nodes (green), operation nodes (blue), and output nodes (red).  Each edge indicates data flow (or dependency) between two nodes.

Transpiler passes are classified either as anAnalysisPassor aTransformationPass. Passes in general work with theDAGand theproperty_set, a dictionary-like object for storing properties determined by analysis passes. Analysis passes work with both the DAG and itsproperty_set.  They cannot modify the DAG, but can modify theproperty_set.  This contrasts with transformation passes, which do modify the DAG, and can read (but not write to)property_set.  For example, transformation passes translate a circuit to itsISAor perform routing passes to insert SWAP gates where needed.

The following example constructs a transpiler pass that adds Pauli twirls.Pauli twirlingis an error suppression strategy that randomizes how qubits experience noisy channels, which we assume to be two-qubit gates in this example (because they are much more error-prone than single-qubit gates). The Pauli twirls do not affect the two-qubit gates' operation. They are chosen such that those appliedbeforethe two-qubit gate (to the left) are countered by those appliedafterthe two-qubit gate (to the right). In this sense, the two-qubit operations are identical, but the way they are performed is different. One benefit of Pauli twirling is that it turns coherent errors into stochastic errors, which can be improved by averaging more.

Transpiler passes act on theDAG, so the important method to override is.run(), which takes the DAG as input. Initializing pairs of Paulis as shown preserves the operation of each two-qubit gate. This is done with the helper methodbuild_twirl_set, which goes through each two-qubit Pauli (as obtained frompauli_basis(2)) and finds the other Pauli that preserves the operation.

From the DAG, use theop_nodes()method to return all of its nodes. The DAG can also be used to collect runs, which are sequences of nodes that run uninterrupted on a qubit. These can be collected as single-qubit runs withcollect_1q_runs, two-qubit runs withcollect_2q_runs, and runs of nodes where the instruction names are in a namelist withcollect_runs.  TheDAGCircuithas many methods for searching and traversing a graph.  One commonly used method istopological_op_nodes, which provides the nodes in a dependency ordering. Other methods such asbfs_successorsare used primarily to determine how nodes interact with subsequent operations on a DAG.

In the example, we want to replace each node, representing an instruction, with a subcircuit built as a mini DAG. The mini DAG has a two-qubit quantum register added to it.  Operations are added to the mini DAG by usingapply_operation_back, which places theInstructionon the mini DAG's output (whereasapply_operation_frontwould place it on the mini DAG's input). The node is then substituted by the mini DAG by usingsubstitute_node_with_dag, and the process continues over each instance ofCXGateandECRGatein the DAG (corresponding to the two-qubit basis gates on IBM® backends).

The following code uses the pass created above to transpile a circuit. Consider a simple circuit withcxs andecrs.

Output:

To apply the custom pass, build a pass manager using thePauliTwirlpass and run it on 50 circuits.

Each two-qubit gate is now sandwiched between two Paulis.

Output:

The operators are the same ifOperatorfromqiskit.quantum_infois used:

Output:

On this page

© IBM Corp., 2017-2025


---

# Transpile against custom backends







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

One of the more powerful features of Qiskit is the ability to support unique device configurations.  Qiskit is built to be agnostic to the provider of the quantum hardware you use, and providers can configure theBackendV2object to their own unique device properties.  This topic demonstrates how to configure your own backend and transpile quantum circuits against them.

You can create uniqueBackendV2objects with different geometries or basis gates and transpile your circuits with those configurations in mind.  The example below covers a backend with a disjoint qubit lattice, whose basis gates are different along the edges from within the bulk.

Before beginning, it is helpful to understand the usage and purpose of theProvider,BackendV2, andTargetobjects.

If you have a quantum device or simulator that you want to integrate into the Qiskit SDK, you need to write your ownProviderclass. This class serves a single purpose: to get backend objects that you provide. This is where any required credential and/or authentication tasks are handled. Once instantiated, the provider object will then provide a list of backends as well as the ability to acquire/instantiate backends.

Next, the backend classes provide the interface between the Qiskit SDK and the hardware or simulator that will execute circuits. They include all necessary information to describe a backend to the transpiler so that it can optimize any circuit according to its constraints. ABackendV2is built of four main parts:

TheBackendV2object is an abstract class used for all backend objects created by a provider (either withinqiskit.providersor another library such asqiskit_ibm_runtime.IBMBackend).  As mentioned above, these objects contain several attributes, including aTarget. TheTargetcontains information that specifies the backend's attributes - such as theCoupling Map, list ofInstructions, and others - to the transpiler.  In addition to theTarget, one can also define pulse-level details such as theDriveChannelorControlChannel.

The following example demonstrates this customization by creating a simulated multi-chip backend, where each chip possesses a heavy-hex connectivity.  The example specifies the backend's two-qubit gate set to beCZGateswithin each chip andCXGatesbetween chips.  First, create your ownBackendV2and customize itsTargetwith single and two-qubit gates according to the previously described constraints.

Plotting a coupling map requires thegraphvizlibrary to be installed.

You can view the connectivity graph of this new class with theplot_gate_map()method from theqiskit.visualizationmodule.  This method, along withplot_coupling_map()andplot_circuit_layout(), are helpful tools for visualizing the qubit arrangement of a backend, as well as how a circuit is laid out across the qubits of a backend.  This example creates a backend containing three small heavy-hex chips. It specifies a set of coordinates to arrange the qubits, as well as a set of custom colors for the differing two-qubit gates.

Output:

Each qubit is labeled, and colored arrows represent the two-qubit gates.  Gray arrows are the CZ gates and the black arrows are the inter-chip CX gates (these connect qubits6→216 \rightarrow 216→21and25→4025 \rightarrow 4025→40).  The direction of the arrow indicates the default direction in which these gates are executed; they specify which qubits are control/targets by default for each two-qubit channel.

Now that a custom backend with its own uniqueTargethas been defined, it is straightforward to transpile quantum circuits against this backend, since all the relevant constraints (basis gates, qubit connectivity, and so forth) needed for transpiler passes are contained within this attribute. The next example builds a circuit that creates a large GHZ state and transpiles it against the backend constructed above.

Output:

The transpiled circuit now contains a mixture ofCZandECRgates,which we specified as the basis gates in the backend'sTarget.  There are also quite a few more gates than you started with because of the need to insert SWAP instructions after choosing a layout.  Below, theplot_circuit_layout()visualization tool is used to specify which qubits and two-qubit channels were used in this circuit.

Output:

Therustworkxpackage contains a large library of different graphs and enables the creation of custom graphs.  The visually interesting code below creates a backend inspired by the toric code. You can then visualize the backend using the functions from theVisualize backendssection.

Output:

Output:

On this page

© IBM Corp., 2017-2025


---

# Install and use transpiler plugins







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

To facilitate the development and reuse of custom transpilation code by the wider community of Qiskit users, the Qiskit SDK supports a plugin interface that enables third-party Python packages to declare that they provide extended transpilation functionality accessible via Qiskit.

Currently, third-party plugins can provide extended transpilation functionality in three ways:

The rest of the page describes how to list available plugins, install new ones, and use them.

Qiskit already includes some built-in plugins for transpilation. To install more, you can use your Python package manager. For example, you might runpip install qiskit-toqmto install theQiskit TOQMrouting stage plugin. A number of third-party plugins are part of theQiskit ecosystem.

Use thelist_stage_pluginsfunction, passing the name of the stage whose plugins you want to list.

Output:

Output:

Ifqiskit-toqmwere installed, thentoqmwould appear in the list ofroutingplugins.

Use theunitary_synthesis_plugin_namesfunction.

Output:

Use thehigh_level_synthesis_plugin_namesfunction, passing the name of the type of "high-level object" to be synthesized. The name corresponds to thenameattribute of theOperationclass representing the type of object being synthesized.

Output:

You can use theHighLevelSynthesisPluginManagerclass to list the names of all high-level synthesis plugins:

Output:

In this section, we show how to use transpiler plugins. In the code examples, we use plugins that come with Qiskit, but plugins installed from third-party packages are used the same way.

To use a transpiler stage plugin, specify its name with the appropriate argument togenerate_preset_pass_managerortranspile. The argument is formed by appending_methodto the name of the transpilation stage. For example, to use thelookaheadrouting plugin, we would specifylookaheadfor therouting_methodargument:

To use a unitary synthesis plugin, specify its name as theunitary_synthesis_methodargument togenerate_preset_pass_managerortranspile:

Unitary synthesis is used in theinit,translation, andoptimizationstages of the staged pass manager returned bygenerate_preset_pass_manageror used intranspile. SeeTranspiler stagesfor a description of these stages.

Use theunitary_synthesis_plugin_configargument, a free-form dictionary, to pass options for the unitary synthesis method. The documentation of the synthesis method should explain the options it supports. Seethis listfor links to the documentation of the built-in unitary synthesis plugins.

First, create anHLSConfigto
store the names of the plugins to use for various high-level objects. For example:

This code cell creates a high-level synthesis configuration that uses thelayersplugin
for synthesizingCliffordobjects and thepmhplugin for synthesizingLinearFunctionobjects. The names of the keyword arguments correspond to thenameattribute of theOperationclass representing the type of object being synthesized.
For each high-level object, the list of given plugins are tried in sequence until one of them
succeeds (in the example above, each list only contains a single plugin).

In addition to specifying
a plugin by its name, you can instead pass a(name, options)tuple, where the second element of the tuple is a dictionary containing options for the plugin. The documentation of the synthesis method should explain the options it supports. Seethis listfor links to the documentation of the built-in high-level synthesis plugins.

Once you have created theHLSConfigobject, pass it as thehls_configargument togenerate_preset_pass_managerortranspile:

High-level synthesis is used in theinit,translation, andoptimizationstages of the staged pass manager returned bygenerate_preset_pass_manageror used intranspile. SeeTranspiler stagesfor a description of these stages.

On this page

© IBM Corp., 2017-2025


---

# Create a transpiler plugin







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Creating atranspiler pluginis a great way to share your transpilation code with the wider Qiskit community, allowing other users to benefit from the functionality you've developed. Thank you for your interest in contributing to the Qiskit community!

Before you create a transpiler plugin, you need to decide what kind of plugin is appropriate for your situation. There are three kinds of transpiler plugins:

Once you've determined which kind of plugin to create, follow these steps to create the plugin:

There is no limit to the number of plugins a single package can define, but each plugin must have a unique name. The Qiskit SDK itself includes a number of plugins, whose names are also reserved. The reserved names are:

In the next sections, we show examples of these steps for the different types of plugins. In these examples, we assume that we are creating a Python package calledmy_qiskit_plugin. For information on creating Python packages, you can check outthis tutorialfrom the Python website.

In this example, we create a transpiler stage plugin for thelayoutstage (seeTranspiler stagesfor a description of the 6 stages of Qiskit's built-in transpilation pipeline).
Our plugin simply runsVF2Layoutfor a number of trials that depends on the requested optimization level.

First, we create a subclass ofPassManagerStagePlugin. There is one method we need to implement, calledpass_manager. This method takes as input aPassManagerConfigand returns the pass manager that we are defining. The PassManagerConfig object stores information about the target backend, such as its coupling map and basis gates.

Now, we expose the plugin by adding an entry point in our Python package metadata.
Here, we assume that the class we defined is exposed in a module calledmy_qiskit_plugin, for example by being imported in the__init__.pyfile of themy_qiskit_pluginmodule.
We edit thepyproject.toml,setup.cfg, orsetup.pyfile of our package (depending on which kind of file you chose to store your Python project metadata):

See thetable of transpiler plugin stagesfor the entry points and expectations for each transpiler stage.

To check that your plugin is successfully detected by Qiskit, install your plugin package and follow the instructions atTranspiler pluginsfor listing installed plugins, and ensure that your plugin appears in the list:

Output:

If our example plugin were installed, then the namemy_layoutwould appear in this list.

If you want to use a built-in transpiler stage as the starting point for your transpiler stage plugin, you can obtain the pass manager for a built-in transpiler stage usingPassManagerStagePluginManager. The following code cell shows how to do this to obtain the built-in optimization stage for optimization level 3.

In this example, we'll create a unitary synthesis plugin that simply uses the built-inUnitarySynthesistranspilation pass to synthesize a gate. Of course, your own plugin will do something more interesting than that.

TheUnitarySynthesisPluginclass defines the interface and contract for unitary synthesis
plugins. The primary method isrun,
which takes as input a Numpy array storing a unitary matrix
and returns aDAGCircuitrepresenting the circuit synthesized from that unitary matrix.
In addition to therunmethod, there are a number of property methods that need to be defined.
SeeUnitarySynthesisPluginfor documentation of all required properties.

Let's create our UnitarySynthesisPlugin subclass:

If you find that the inputs available to therunmethod are insufficient for your purposes, pleaseopen an issueexplaining your requirements. Changes to the plugin interface, such as adding additional optional inputs, will be done in a backward compatible way so that they do not require changes from existing plugins.

All methods prefixed withsupports_are reserved on aUnitarySynthesisPluginderived class as part of the interface. You should not define any customsupports_*methods on a subclass that are not defined in the abstract class.

Now, we expose the plugin by adding an entry point in our Python package metadata.
Here, we assume that the class we defined is exposed in a module calledmy_qiskit_plugin, for example by being imported in the__init__.pyfile of themy_qiskit_pluginmodule.
We edit thepyproject.toml,setup.cfg, orsetup.pyfile of our package:

As before, if your project usessetup.cfgorsetup.pyinstead ofpyproject.toml, see thesetuptools documentationfor how to adapt these lines for your situation.

To check that your plugin is successfully detected by Qiskit, install your plugin package and follow the instructions atTranspiler pluginsfor listing installed plugins, and ensure that your plugin appears in the list:

Output:

If our example plugin were installed, then the namemy_unitary_synthesiswould appear in this list.

To accommodate unitary synthesis plugins that expose multiple options,
the plugin interface has an option for users to provide a free-form
configuration dictionary. This will be passed to therunmethod
via theoptionskeyword argument. If your plugin has these configuration options, you should clearly document them.

In this example, we'll create a high-level synthesis plugin that simply uses the built-insynth_clifford_bmfunction to synthesize a Clifford operator.

TheHighLevelSynthesisPluginclass defines the interface and contract for high-level synthesis plugins. The primary method isrun.
The positional argumenthigh_level_objectis anOperationrepresenting the "high-level" object to be synthesized. For example, it could be aLinearFunctionor aClifford.
The following keyword arguments are present:

Therunmethod returns aQuantumCircuitrepresenting the circuit synthesized from that high-level object.
It is also allowed to returnNone, indicating that the plugin is unable to synthesize the given high-level object.
The actual synthesis of high-level objects is performed by theHighLevelSynthesistranspiler pass.

In addition to therunmethod, there are a number of property methods that need to be defined.
SeeHighLevelSynthesisPluginfor documentation of all required properties.

Let's define our HighLevelSynthesisPlugin subclass:

This plugin synthesizes objects of typeCliffordthat have
at most 3 qubits, using thesynth_clifford_bmmethod.

Now, we expose the plugin by adding an entry point in our Python package metadata.
Here, we assume that the class we defined is exposed in a module calledmy_qiskit_plugin, for example by being imported in the__init__.pyfile of themy_qiskit_pluginmodule.
We edit thepyproject.toml,setup.cfg, orsetup.pyfile of our package:

Thenameconsists of two parts separated by a dot (.):

As before, if your project usessetup.cfgorsetup.pyinstead ofpyproject.toml, see thesetuptools documentationfor how to adapt these lines for your situation.

To check that your plugin is successfully detected by Qiskit, install your plugin package and follow the instructions atTranspiler pluginsfor listing installed plugins, and ensure that your plugin appears in the list:

Output:

If our example plugin were installed, then the namemy_clifford_synthesiswould appear in this list.

On this page

© IBM Corp., 2017-2025


---

# Work with DAGs in transpiler passes







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

In Qiskit, within the transpilation stages, circuits are represented using a DAG. In general, a DAG is composed of vertices (also known as "nodes") and directed edges that connect pairs of vertices in a particular orientation. This representation is stored usingqiskit.dagcircuit.DAGCircuitobjects that are composed of individualDagNodeobjects. The advantage of this representation over a pure list of gates (that is, a netlist) is that the flow of information between operations is explicit, making it easier to make transformation decisions.

This guide demonstrates how to work with DAGs and use them to write custom transpiler passes. It will start with building a simple circuit and examining its DAG representation, then explores basic DAG operations and implements a customBasicMapperpass.

The code snippet below illustrates the DAG by creating a simple circuit that prepares a Bell state and applies anRZR_ZRZ​rotation, depending on the measurement outcome.

In the DAG, there are three kinds of graph nodes: qubit/clbit input nodes (green), operation nodes (blue), and output nodes (red). Each edge indicates data flow (or dependency) between two nodes. Use the qiskit.tools.visualization.dag_drawer() function to view this circuit's DAG. (Install theGraphviz libraryto run this.)

The code examples below demonstrate common operations with DAGs, including accessing nodes, adding operations, and substituting subcircuits. These operations form the foundation for building transpiler passes.

Theop_nodes()method returns an iterable list ofDAGOpNodeobjects in the circuit:

Each node is an instance of theDAGOpNodeclass:

An operation is added to the end of the DAGCircuit using theapply_operation_back()method. This appends the specified gate to act on the given qubits after all existing operations in the circuit.

An operation is added to the beginning of the DAGCircuit using theapply_operation_front()method. This inserts the specified gate before all existing operations in the circuit, effectively making it the first operation executed.

A node representing a specific operation in the DAGCircuit is replaced with a subcircuit. First, a new sub-DAG is constructed with the desired sequence of gates, then the target node is substituted by this sub-DAG usingsubstitute_node_with_dag(), preserving the connections to the rest of the circuit.

After all transformations are completed, the DAG can be converted back into a regularQuantumCircuitobject. This is how the transpiler pipeline operates. A circuit is taken, processed in DAG form, and a transformed circuit is produced as output.

The DAG structure can be leveraged for writing transpiler passes. In the example below, aBasicMapperpass is implemented to map an arbitrary circuit onto a device with restricted qubit connectivity. For additional guidance, refer to the guide onwriting custom transpiler passes.

The pass is defined as aTransformationPass, meaning that it modifies the circuit. It does so by traversing the DAG layer-by-layer, checking whether each instruction satisfies the constraints imposed by the device's coupling map. If a violation is detected, a swap path is determined and the necessary SWAP gates are inserted accordingly.

When creating a transpiler pass, the first decision involves selecting whether the pass should inherit fromTransformationPassorAnalysisPass. Transformation passes are designed to modify the circuit, whereas analysis passes are intended only to extract information for use by subsequent passes. The main functionality is then implemented in therun(dag)method. Finally, the pass should be registered within theqiskit.transpiler.passesmodule.

In this specific pass, the DAG is traversed layer-by-layer (where each layer contains operations that act on disjoint sets of qubits and can thus be executed independently). For each operation, if the coupling map constraints are not met, a suitable swap path is identified, and the required swaps are inserted to bring the involved qubits into adjacency.

The pass can now be tested on a small example circuit. A pass manager is constructed with the newly defined pass included. The example circuit is then provided to this pass manager, and a new, transformed circuit is obtained as the output.

On this page

© IBM Corp., 2017-2025


---

# Introduction to debugging tools







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

You can test your quantum programs by running them on simulated devices and exploring their performance under realistic device noise models. This allows you to debug them before sending them to a quantum processing unit (QPU).

Quantum simulators can be used to help develop and test programs before fine-tuning them and sending them to quantum hardware. Local simulators can do this with good performance and efficiency.

Because the cost of classically simulating quantum circuits scales exponentially with the number of qubits, circuits that are larger than 50 qubits or so generally cannot run on simulators. For such circuits, you can:

Stabilizer circuits, also known as Clifford circuits, are a useful tool for accomplishing this latter goal. These are a restricted class of quantum circuits that can be efficiently simulated classically. Specialized simulators can easily simulate stabilizer circuits with thousands of qubits. SeeEfficient simulation of stabilizer circuits with Qiskit Aer primitivesfor more information.

For general quantum circuits, the following tools are available to test and debug your quantum programs:

Several factors impact how much memory quantum simulation requires, so there are no exact hardware requirements for simulation, but there are some guidelines you can follow.

On this page

© IBM Corp., 2017-2025


---

# Exact simulation with Qiskit SDK primitives







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The reference primitives in the Qiskit SDK perform local statevector simulations. These simulations do not support
modeling device noise, but are useful for quickly prototyping algorithms before looking into more advanced simulation
techniques (using Qiskit Aer) or running on real devices (Qiskit Runtime primitives).

The Estimator primitive can compute expectation values of circuits, and the Sampler primitive can sample
from output distributions of circuits.

The following sections show how to use the reference primitives to run your workflow locally.

The reference implementation ofEstimatorV2inqiskit.primitivesthat runs on a local statevector
simulators is theStatevectorEstimatorclass. It can take circuits, observables, and parameters as inputs and returns the locally computed expectation values.

The following code prepares the inputs that will be used in the examples that follow. The expected input type for the
observables isqiskit.quantum_info.SparsePauliOp. Note that
the circuit in the example is parametrized, but you can also run the Estimator on non-parametrized circuits.

Any circuit passed to an Estimator mustnotinclude anymeasurements.

Output:

The Qiskit Runtime primitives workflow requires circuits and observables to be transformed to only use instructions supported by the QPU (referred to asinstruction set architecture (ISA)circuits and observables). The reference primitives still accept abstract instructions, as they rely on local statevector simulations, but transpiling the circuit might still be beneficial in terms of circuit optimization.

Instantiate aqiskit.primitives.StatevectorEstimator.

This example only uses one circuit (of typeQuantumCircuit) and one
observable.

Run the estimation by calling theStatevectorEstimator.runmethod, which returns an instance of aPrimitiveJobobject. You can get the results from the job (as aqiskit.primitives.PrimitiveResultobject)
with theqiskit.primitives.PrimitiveJob.resultmethod.

Output:

The primitives result outputs an array ofPubResults, where each item of the array is aPubResultobject that contains in its data the array of evaluations corresponding to every circuit-observable combination in the PUB.

To retrieve the expectation values and metadata for the first (and in this case, only) circuit evaluation, we must access the evaluationdatafor PUB 0:

Output:

By default, the reference Estimator performs an exact statevector calculation based on thequantum_info.Statevectorclass.
However, this can be modified to introduce the effect of the sampling overhead (also known as "shot noise").

Estimator accepts aprecisionargument that expresses the error bars that the
primitive implementation should target for expectation values estimates.  This is the sampling overhead and is defined exclusively in the.run()method. This  lets you fine-tune the option all the way to the PUB level.

For a full example, see thePrimitives examplespage.

The reference implementations ofSamplerV2inqiskit.primitivesis theStatevectorSamplerclass. It takes circuits and parameters as inputs and returns the results from sampling from the output probability distributions as a quasi-probability distribution of output states.

The following code prepares the inputs used in the examples that follow. Note that
these examples run a single parametrized circuit, but you can also run the Sampler
on non-parametrized circuits.

Output:

Any quantum circuit passed to a Samplermustinclude measurements.

The Qiskit Runtime primitives workflow requires circuits to be transformed to only use instructions supported by the QPU (referred to as ISA circuits). The reference primitives still accept abstract instructions, as they rely on local statevector simulations, but transpiling the circuit might still be beneficial in terms of circuit optimization.

Instantiateqiskit.primitives.StatevectorSampler:

Output:

Primitives accept multiple PUBs as inputs, and each PUB gets its own result. Therefore, you can run different circuits with various parameter/observable combinations, and retrieve the PUB results:

Output:

Measurement outcome samples are returned asbitstringsorcounts. The bitstrings show the measurement outcomes, preserving the shot order in which they were measured. The Sampler result objects organize data in terms of their input circuits' classical register names, for compatibility with dynamic circuits.

The name of the classical register defaults to"meas". This name will be used later to access the measurement bitstrings.

Output:

Output:

By default, the reference Sampler performs an exact statevector calculation based on thequantum_info.Statevectorclass.
However, this can be modified to introduce the effect of the sampling overhead (also known as "shot noise"). To help manage this overhead, the Sampler interface accepts ashotsargument that can be defined at the PUB level.

This example assumes you have defined two circuits.

Output:

For a full example, see thePrimitives examplespage.

On this page

© IBM Corp., 2017-2025


---

# Exact and noisy simulation with Qiskit Aer primitives







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Exact simulation with Qiskit primitivesdemonstrates how to use the reference primitives included with Qiskit to perform exact simulation of quantum circuits. Currently existing quantum processors suffer from errors, or noise, so the results of an exact simulation do not necessarily reflect the results you would expect when running circuits on real hardware. While the reference primitives in Qiskit do not support modeling noise,Qiskit Aerincludes implementations of the primitives that do support modeling noise. Qiskit Aer is a high-performance quantum circuit simulator that you can use in place of the reference primitives for better performance and more features. It is part of theQiskit Ecosystem. In this article, we demonstrate the use of Qiskit Aer primitives for exact and noisy simulation.

To explore exact and noisy simulation, create an example circuit on eight qubits:

Output:

This circuit contains parameters to represent the rotation angles forRyR_yRy​andRzR_zRz​gates. When simulating this circuit, we need to specify explicit values for these parameters. In the next cell, we specify some values for these parameters and use the Estimator primitive from Qiskit Aer to compute the exact expectation value of the observableZZ⋯ZZZ \cdots ZZZ⋯Z.

Output:

Now, let's initialize a noise model that includes depolarizing error of 2% on every CX gate. In practice, the error arising from the two-qubit gates, which are CX gates here, are the dominant source of error when running a circuit. SeeBuild noise modelsfor an overview of constructing noise models in Qiskit Aer.

In the next cell, we construct an Estimator that incorporates this noise model and use it to compute the expectation value of the observable.

Output:

As you can see, the expectation value in the presence of the noise is quite far from the correct value. In practice, you can employ a variety of error mitigation techniques to counter the effects of the noise, but a discussion of these techniques is outside the scope of this article.

To get a very rough sense of how the noise affects the final result, consider our noise model, which adds a depolarizing error of 2% to each CX gate. Depolarizing error with probabilitypppis defined as a quantum channelEEEthat has the following action on a density matrixρ\rhoρ:

wherennnis the number of qubits, in this case, 2. That is, with probabilityppp, the state is replaced with the completely mixed state, and the state is preserved with probability1−p1 - p1−p. Aftermmmapplications of the depolarizing channel, the probability of the state being preserved would be(1−p)m(1 - p)^m(1−p)m. Therefore, we expect the probability of retaining the correct state at the end of the simulation to go down exponentially with the number of CX gates in our circuit.

Let's count the number of CX gates in our circuit and compute(1−p)m(1 - p)^m(1−p)m. We callcount_opsto get a dictionary that maps gate names to counts, and retrieve the entry for the CX gate.

Output:

This value, 65%, gives a rough estimate of the probability that our final state is correct. It is a conservative estimate because it does not take into account the initial state of the simulation.

The following code cell shows how to use the Sampler primitive from Qiskit Aer to sample from the noisy circuit. We need to add measurements to the circuit before running it with the Sampler primitive.

Output:

On this page

© IBM Corp., 2017-2025


---

# Qiskit Runtime local testing mode







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Local testing mode (available withqiskit-ibm-runtime0.22.0 or later) can be used to help develop and test programs before fine-tuning them and sending them to real quantum hardware.  After using local testing mode to verify your program, all you need to change is the backend name to run it on a QPU.

To use local testing mode, specify one of the fake backends fromqiskit_ibm_runtime.fake_provideror specify a Qiskit Aer backend when instantiating a Qiskit Runtime primitive or a session.

Example with sessions, without noise:

To simulate with noise, specify a QPU (quantum hardware) and submit it to Aer.  Aer builds a noise model based on the calibration data from that QPU, and instantiates an Aer backend with that model.  If you prefer, you canbuild a noise model.

Example with noise:

Because Clifford circuits can be simulated efficiently with verifiable results, Clifford simulation is a very useful tool. For an in-depth example, seeEfficient simulation of stabilizer circuits with Qiskit Aer primitives.

Example:

On this page

© IBM Corp., 2017-2025


---

# Debug Qiskit Runtime jobs







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Before submitting a resource-intensive Qiskit Runtime workload to execute on hardware, you can use the Qiskit RuntimeNeat(Noisy Estimator Analyzer Tool)class to verify that your Estimator workload is set up correctly, is likely to return  accurate results, uses the most appropriate options for the specified problem, and more.

NeatCliffordizes the input circuits for efficient simulation, while retaining its structure and depth. Clifford circuits suffer similar levels of noise and are a good proxy for studying the original circuit of interest.

The following examples illustrate situations whereNeatcan be a useful resource.

First, import the relevant packages andauthenticate to the Qiskit Runtime service.

Consider a six-qubit circuit that has the following properties:

Output:

Choose single-PauliZoperators as observables and use them to initialize the primitive unified blocs (PUBs).

Output:

The previously defined PUB circuits are not Clifford, which makes them difficult to simulate classically. However, you can use theNeatto_cliffordmethod to map them to Clifford circuits for more efficient simulation.  Theto_cliffordmethod is a wrapper around theConvertISAToCliffordtranspiler pass, which can also be used independently. In particular, it replaces non-Clifford single-qubit gates in the original circuit with Clifford single-qubit gates, but it does not mutate the two-qubit gates, number of qubits, or circuit depth.

SeeEfficient simulation of stabilizer circuits with Qiskit Aer primitivesfor more information about Clifford circuit simulation.

First, initializeNeat.

Next, Cliffordize the PUBs.

Output:

This example shows how to useNeatto study the impact of different noise models on PUBs as a function of circuit depth by running simulations in both ideal (ideal_sim) and noisy (noisy_sim) conditions. This can be useful to set up expectations on the quality of the experimental results before running a job on a QPU. To learn more about noise models, seeExact and noisy simulation with Qiskit Aer primitives.

The simulated results support mathematical operations, and can therefore be compared with each other (or with experimental results) to calculate figures of merit.

Begin by performing ideal and noisy classical simulations.

Output:

Next, apply mathematical operations to compute the absolute difference. The remainder of the guide uses the absolute difference as a figure of merit to compare ideal results with noisy or experimental results, but similar figures of merit can be set up.

The absolute difference shows that the impact of noise grows with the circuits' sizes.

Output:

You can follow these rough and simplified guidelines to improve circuits of this type:

Because all of the absolute differences above are less than 90%, applying PEA to the original circuit will hopefully improve the quality of its results.

You can specify different noise models in the analyzer. The following example performs the same test but adds a custom noise model.

Output:

As shown, given a noise model, you can try to quantify the impact of noise on the (Cliffordized version of the) PUBs of interest before running them on a QPU.

This example usesNeatto help identify the best options for your PUBs. To do so, consider running an estimation problem with PEA, which cannot be simulated withqiskit_aer. You can useNeatto help determine which noise amplification factors will work best, then use those factors when running the original experiment on a QPU.

Output:

The result with the smallest difference suggests which options to choose.

On this page

© IBM Corp., 2017-2025


---

# Build noise models







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page shows how to use the Qiskit Aernoisemodule to build noise models for simulating quantum circuits in the presence of errors. This is useful for emulating noisy quantum processors and for studying the effects of noise on the execution of quantum algorithms.

The Qiskit Aernoisemodule contains Python classes to build customized noise models for simulation. There are three key classes:

TheNoiseModelclass which stores a noise model used for noisy simulation.

TheQuantumErrorclass which describes CPTP gate errors. These can be applied:

TheReadoutErrorclass which describes classical readout errors.

You can initialize a noise model with parameters set from the latest calibration data for a physical backend:

This will yield a noise model that roughly approximates the errors one would encounter when using that backend. If you want to have more detailed control over the parameters of the noise model, then you'll need to create your own noise model, as described in the rest of this page.

Rather than deal with theQuantumErrorobject directly, many helper functions exist to automatically generate a specific type of parameterized quantum error. These are contained in thenoisemodule and include functions for many common errors types used in quantum computing research. The function names and the type of error they return are:

QuantumErrorinstances can be combined by using composition, tensor product, and tensor expansion (reversed order tensor product) to produce newQuantumErrorsas:

To construct a 5% single-qubit bit-flip error:

Output:

Output:

Output:

We can also convert back and forth betweenQuantumErrorobjects in Qiskit Aer andQuantumChannelobjects in Qiskit.

Output:

Output:

Output:

Classical readout errors are specified by a list of assignment probabilities vectorsP(A∣B)P(A|B)P(A∣B):

For example, for one qubit:P(A∣B)=[P(A∣0),P(A∣1)]P(A|B) = [P(A|0), P(A|1)]P(A∣B)=[P(A∣0),P(A∣1)].

Output:

Readout errors may also be combined usingcompose,tensorandexpand, like with quantum errors.

When adding a quantum error to a noise model, we must specify the type ofinstructionthat it acts on and what qubits to apply it to. There are two cases of quantum errors:

This applies the same error to any occurrence of an instruction, regardless of which qubits it acts on.

It is added asnoise_model.add_all_qubit_quantum_error(error, instructions):

Output:

This applies the error to any occurrence of an instruction acting on a specified list of qubits. Note that the order of the qubit matters: for example, an error applied to qubits [0, 1] for a two-qubit gate is different to one applied to qubits [1, 0].

It is added asnoise_model.add_quantum_error(error, instructions, qubits):

Output:

NoiseModeldoes not support addition of non-local qubit quantum errors. They should be handled outside ofNoiseModel. That suggests you shouldwrite your own transpiler pass(TransformationPass) and run the pass just before running the simulator if you need to insert your quantum errors into your circuit under your own conditions.

The commandAerSimulator(noise_model=noise_model)returns a simulator configured to the given noise model. In addition to setting the simulator's noise model, it also overrides the simulator's basis gates, according to the gates of the noise model.

We will now give some examples of noise models. For our demonstrations we use a simple test circuit generating a n-qubit GHZ state:

Output:

Output:

Let's consider a simple toy noise model example common in quantum information theory research:

Output:

Output:

Now consider a more realistic error model based on thermal relaxation with the qubit environment:

Output:

Output:

On this page

© IBM Corp., 2017-2025


---

# Efficient simulation of stabilizer circuits with Qiskit Aer primitives







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page shows how to use Qiskit Aer primitives to efficiently simulate stabilizer circuits, including those subject to Pauli noise.

Stabilizer circuits, also known as Clifford circuits, are an important restricted class of quantum circuits that can be efficiently simulated classically. There are several equivalent ways to define stabilizer circuits. One definition is that a stabilizer circuit is a quantum circuit that consists solely of the following gates:

Note that using Hadamard and S, we can construct any Pauli rotation gate (RxR_xRx​,RyR_yRy​, andRzR_zRz​) that has an angle contained in the set{0,π2,π,3π2}\{0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}\}{0,2π​,π,23π​}(up to global phase), so we can include these gates in the definition as well.

Stabilizer circuits are important to the study of quantum error correction. Their classical simulability also makes them useful for verifying the output of quantum computers. For example, suppose you want to execute a quantum circuit that uses 100 qubits on a quantum computer. How do you know that the quantum computer is behaving correctly? A quantum circuit on 100 qubits is beyond the reach of brute-force classical simulation. By modifying your circuit so that it becomes a stabilizer circuit, you can run circuits on the quantum computer that have a similar structure to your desired circuit, but which you can simulate on a classical computer. By checking the output of the quantum computer on the stabilizer circuits, you can gain confidence that it is behaving correctly on the non-stabilizer circuits as well. SeeEvidence for the utility of quantum computing before fault tolerancefor an example of this idea in practice.

Exact and noisy simulation with Qiskit Aer primitivesshows how to useQiskit Aerto perform exact and noisy simulations of generic quantum circuits. Consider the example circuit used in that article, an 8-qubit circuit built usingefficient_su2:

Output:

Using Qiskit Aer, we were able to simulate this circuit easily. However, suppose we set the number of qubits to 500:

Because the cost of simulating quantum circuits scales exponentially with the number of qubits, such a large circuit would generally exceed the capabilities of even a high-performance simulator like Qiskit Aer. Classical simulation of generic quantum circuits becomes infeasible when the number of qubits exceeds roughly 50 to 100 qubits. However, note that the efficient_su2 circuit is parameterized by angles onRyR_yRy​andRzR_zRz​gates. If all of these angles are contained in the set{0,π2,π,3π2}\{0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}\}{0,2π​,π,23π​}, then the circuit is a stabilizer circuit, and it can be efficiently simulated!

In the following cell, we run the circuit with the Sampler primitive backed by the stabilizer circuit simulator, using parameters chosen randomly such that the circuit is guaranteed to be a stabilizer circuit.

The stabilizer circuit simulator also supports noisy simulation, but only for a restricted class of noise models. Specifically, any quantum noise must be characterized by aPauli errorchannel.Depolarizing errorfalls into this category, so it can be simulated too. Classical noise channels likereadout errorcan also be simulated.

The following code cell runs the same simulation as before, but this time specifying a noise model that adds depolarizing error of 2% to each CX gate, as well as readout error that flips each measured bit with 5% probability.

Now, let's use the Estimator primitive backed by the stabilizer simulator to compute the expectation value of the observableZZ⋯ZZZ \cdots ZZZ⋯Z. Due to the special structure of stabilizer circuits, the result is very likely to be 0.

Output:

On this page

© IBM Corp., 2017-2025


---

# Introduction to primitives







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Similar to the early days of classical computers, when developers had to manipulate CPU registers directly, the early interface to QPUs simply returned the raw data from the control electronics.
This was not a big issue when QPUs lived in labs and only allowed direct access by researchers.
Acknowledging that most developers would not and should not be familiar with distilling such raw data into 0s and 1s, Qiskit introducedbackend.run, a first abstraction for accessing QPUs in the cloud. This allowed developers
to operate on a familiar data format and focus on the bigger picture.

As access to QPUs became more widespread, and with more quantum algorithms being developed,
again the need for a higher-level abstraction emerged. In response, Qiskit introduced
the primitives interface, which is optimized for two core tasks in quantum algorithm development:
expectation value estimation (Estimator) and circuit sampling (Sampler). The goal is once
again to help developers to focus more on innovation and less on data conversion. The primitives interface supersedes thebackend.runinterface, sinceSamplerprovides the same direct hardware access that was offered bybackend.run.

Computing systems are built on multiple layers of abstraction. Abstractions allow you to focus on a
particular level of detail relevant to the task at hand. The closer you get to the hardware,
the lower the level of abstraction you need (for example, you might
want to manipulate electrical signals), and vice versa. The more complex the task you want to perform,
the higher-level the abstractions will be (for example, you could be using a programming library to perform
algebraic calculations).

In this context, aprimitiveis the smallest processing instruction, the simplest building block from which
one can create something useful for a given abstraction level.

The recent progress in quantum computing has increased the need to work at higher levels of abstraction.
As the field moves toward larger quantum processing units (QPUs) and more complex workflows, the focus shifts from interacting with individual
qubit signals to viewing quantum devices as systems that perform necessary tasks.

The two most common tasks for quantum computers are sampling quantum states and calculating expectation values.
These tasks motivated the design of the Qiskit primitives:EstimatorandSampler.

In short, the computational model introduced by the Qiskit primitives moves quantum programming one step closer
to where classical programming is today, where the focus is less on the hardware details and more on the results
you are trying to achieve.

There are two types of Qiskit primitives: the base classes, and their implementations. The Qiskit primitives are defined by open-source primitive base classes that live in the Qiskit SDK (in theqiskit.primitivesmodule). Providers (such as Qiskit Runtime) can use these base classes to derive their own Sampler and Estimator implementations.  Most users will interact with provider implementations, not the base primitives.

BaseEstimatorV2andBaseSamplerV2- Abstract base classes that define a common interface for implementing primitives. All other classes in theqiskit.primitivesmodule inherit from these base classes.  Developers should use these if they are interested in creating their own primitives-based execution model for a specific provider. These classes might also be useful for those who want to do highly customized processing and find that the existing primitives implementations are too simple for their needs. General users will not directly use the base classes.

These are implementations of the primitives base classes:

The Qiskit Runtime primitives (EstimatorV2andSamplerV2) provide a more sophisticated implementation (for example, by including error mitigation) as a cloud-based service. This implementation of the base primitives is used to access IBM Quantum® hardware.  They are accessed through IBM Qiskit Runtime.

StatevectorEstimatorandStatevectorSampler- Reference implementations of the primitives that use the simulator built into Qiskit. They are built with the Qiskitquantum_infomodule, producing results based on ideal statevector simulations.  They are accessed through Qiskit.

BackendEstimatorV2andBackendSamplerV2- You can use these classes to “wrap” any quantum computing resource into a primitive. This lets you write primitive-style code for providers that don’t yet have a primitives-based interface. These classes can be used just like the regular Sampler and Estimator, except they should be initialized with an additionalbackendargument for selecting which quantum computer to run on. They are accessed by using Qiskit.

With primitives, Qiskit users can write quantum code for a specific QPU without having to explicitly
manage every detail. Also, because of the additional layer of abstraction, you might be able to more easily
access advanced hardware capabilities of a given provider. For example, with Qiskit Runtime primitives,
you can take advantage of the latest advancements in error mitigation and suppression by toggling options such as the primitive'sresilience_level,rather than building your own implementation of these techniques.

For hardware providers, implementing primitives natively means you can provide your users with a more “out-of-the-box”
way to access your hardware features such as advanced post-processing techniques. It is therefore easier for your users to benefit from your hardware's best capabilities.

As described previously, all primitives are created from the base classes; therefore, they have the same general structure and usage.  For example, the format of the input for all Estimator primitives is the same.  However, there are differences in implementations that make them unique.

Because most users access the Qiskit Runtime primitives, the examples in the rest of this section are based on Qiskit Runtime primitives.

The Estimator primitive computes the expectation values for one or more observables with respect to states prepared by quantum circuits. The circuits can be parametrized, as long as the parameter values are also provided as input to the primitive.

The input is an array ofPUBs.Each PUB is in the format:

(<single circuit>,<one or more observables>,<optional one or more parameter values>,<optional precision>),

where the optionalparameter valuescan be a list or a single parameter.  Different Estimator implementations support various configuration options. If the input contains measurements, they are ignored.

The output is aPubResultthat contains the computed expectation values per pair, and their standard errors, inPubResultform. EachPubResultcontains both data and metadata.

The Estimator combines elements from observables and parameter values by following NumPy broadcasting rules as described in thePrimitive inputs and outputstopic.

Example:

The Sampler's core task is sampling the output register from the execution of one or more quantum circuits. The input circuits can be parametrized, as long as the parameter values are also provided as input to the primitive.

The input is one or morePUBs,in the format:

(<single circuit>,<one or more optional parameter value>,<optional shots>),

where there can be multipleparameter valuesitems, and each item can be either an array or a single parameter, depending on the chosen circuit. Additionally, the input must contain measurements.

The output is counts or per-shot measurements, asPubResultobjects, without weights. The result class, however, has methods to return weighted samples, such as counts. SeePrimitive inputs and outputsfor full details.

Example:

On this page

© IBM Corp., 2017-2025


---

# Get started with primitives







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The steps in this topic describe how to set up primitives, explore the options you can use to configure them, and invoke them in a program.

To use the newly supportedfractional gates, setuse_fractional_gates=Truewhen requesting a backend from aQiskitRuntimeServiceinstance. For example:

Note that this is an experimental feature and might change in the future.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

Because Qiskit Runtime Estimator is a managed service, you first need to initialize your account. You can then select the QPU you want to use to calculate the expectation value.

Follow the steps in theInstall and set up topicif you don't already have an account.

Output:

You need at least one circuit and one observable as inputs to the Estimator primitive.

Output:

The circuit and observable need to be transformed to only use instructions supported by the QPU (referred to asinstruction set architecture (ISA)circuits). We'll use the transpiler to do this.

Output:

When you initialize the Estimator, use themodeparameter to specify the mode you want it to run in.  Possible values arebatch,session, orbackendobjects for batch, session, and job execution mode, respectively. For more information, seeIntroduction to Qiskit Runtime execution modes.

Next, invoke therun()method to calculate expectation values for the input circuits and observables. The circuit, observable, and optional parameter value sets are input asprimitive unified bloc(PUB) tuples.

Output:

Output:

Because Qiskit Runtime Sampler is a managed service, you first need to initialize your account. You can then select the QPU you want to use to calculate the expectation value.

Follow the steps in theInstall and set up topicif you don't already have an account set up.

You need at least one circuit as the input to the Sampler primitive.

Use the transpiler to get an ISA circuit.

Output:

When you initialize the Sampler, use themodeparameter to specify the mode you want it to run in.  Possible values arebatch,session, orbackendobjects for batch, session, and job execution mode, respectively. For more information, seeIntroduction to Qiskit Runtime execution modes.

Next, invoke therun()method to generate the output. The circuit and optional parameter value sets are input asprimitive unified bloc(PUB) tuples.

Output:

Output:

Unlike provider-specific primitives, backend primitives are generic implementations that can be used with an arbitrarybackendobject, as long as it implements theBackendinterface.

Some providers implement primitives natively.  See theQiskit Ecosystem pagefor details.

The inputs to and outputs fromqiskit.primitives.BackendSamplerV2andqiskit.primitives.BackendEstimatorV2follow the same PUB format as the primitives in Qiskit Runtime. SeePrimitive inputs and outputsfor details.
However, there can be differences in the fields of the returned metadata.

Theqiskit.primitives.BackendEstimatorV2class offers no measurement or gate error mitigation implementations out-of-the-box, as
backend primitives are designed to run locally in the user's machine.

Theqiskit.primitives.BackendSamplerV2class requires a backend that supports thememoryoption.

The backend primitive interfaces expose customSamplerV2andEstimatorV2Optionsthat are different from the Runtime implementations.

On this page

© IBM Corp., 2017-2025


---

# Primitive inputs and outputs







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page gives an overview of the inputs and outputs of the Qiskit Runtime primitives that execute workloads on IBM Quantum® compute resources. These primitives provide you with the ability to efficiently define vectorized workloads by using a data structure known as aPrimitive Unified Bloc (PUB). These PUBs are the fundamental unit of work a QPU needs to execute these workloads. They are used as inputs to therun()method for the Sampler and Estimator primitives, which execute the defined workload as a job. Then, after the job has completed, the results are returned in a format that is dependent on both the PUBs used as well as the runtime options specified from the Sampler or Estimator primitives.

When invoking a primitive'srun()method, the main argument that is required is alistof one or more tuples -- one for each circuit being executed by the primitive. Each of these tuples is considered a PUB, and the required elements of each tuple in the list depends on the primitive used. The data provided to these tuples can also be arranged in a variety of shapes to provide flexibility in a workload through broadcasting -- the rules of which are described in afollowing section.

For the Estimator primitive, the format of the PUB should contain at most four values:

For the Sampler primitive, the format of the PUB tuple contains at most three values:

The following code demonstrates an example set of vectorized inputs to theEstimatorprimitive and executes them on an IBM® backend as a singleRuntimeJobV2object.

The PUBs aggregate elements from multiple arrays (observables and parameter values) by following the same broadcasting rules as NumPy. This section briefly summarizes those rules.  For a detailed explanation, see theNumPy broadcasting rules documentation.

Rules:

Examples of array pairs that broadcast:

Examples of array pairs that do not broadcast:

EstimatorV2returns one expectation value estimate for each element of the broadcasted shape.

Here are some examples of common patterns expressed in terms of array broadcasting.  Their accompanying visual representation is shown in the figure that follows:

Parameter value sets are represented by n x m arrays, and observable arrays are represented by one or more single-column arrays. For each example in the previous code, the parameter value sets are combined with their observable array to create the resulting expectation value estimates.

Example 1: (broadcast single observable) has a parameter value set that is a 5x1 array and a 1x1 observables array.  The one item in the observables array is combined with each item in the parameter value set to create a single 5x1 array where each item is a combination of the original item in the parameter value set with the item in the observables array.

Example 2: (zip) has a 5x1 parameter value set and a 5x1 observables array.  The output is a 5x1 array where each item is a combination of the nth item in the parameter value set with the nth item in the observables array.

Example 3: (outer/product) has a 1x6 parameter value set and a 4x1 observables array.  Their combination results in a 4x6 array that is created by combining each item in the parameter value set witheveryitem in the observables array, and thus each parameter value becomes an entire column in the output.

Example 4: (Standard nd generalization) has a 3x6 parameter value set array and two 3x1 observables array.  These combine to create two 3x6 output arrays in a similar manner to the previous example.

EachSparsePauliOpcounts as a single element in this context, regardless of the number of Paulis contained in theSparsePauliOp. Thus, for the purpose of these broadcasting rules, all of the following elements have the same shape:

The following lists of operators, while equivalent in terms of information contained, have different shapes:

Once one or more PUBs are sent to a QPU for execution and a job successfully completes, the data is returned as aPrimitiveResultcontainer object accessed by calling theRuntimeJobV2.result()method. ThePrimitiveResultcontains an iterable list ofPubResultobjects that contain the execution results for each PUB. Depending on the primitive used, these data will be either expectation values and their error bars in the case of the Estimator, or samples of the circuit output in the case of the Sampler.

Each element of this list corresponds to each PUB submitted to the primitive'srun()method (for example, a job submitted with 20 PUBs will return aPrimitiveResultobject that contains a list of 20PubResults, one corresponding to each PUB).

Each of thesePubResultobjects possess both adataand ametadataattribute. Thedataattribute is a customizedDataBinthat contains the actual measurement values, standard deviations, and so forth. ThisDataBinhas various attributes depending on the shape or structure of the associated PUB as well as the error mitigation options specified by the primitive used to submit the job (for example,ZNEorPEC). Meanwhile, themetadataattribute contains information about the runtime and error mitigation options used (explained later in theResult metadatasection of this page).

The following is a visual outline of thePrimitiveResultdata structure:

Put simply, a single job returns aPrimitiveResultobject and contains a list of one or morePubResults. ThesePubResultobjects then store the measurement data for each PUB that was submitted to the job.

EachPubResultpossesses different formats and attributes based on the type of primitive that was used for the job. The specifics are explained below.

EachPubResultfor the Estimator primitive contains at least an array of expectation values (PubResult.data.evs) and associated standard deviations (eitherPubResult.data.stdsorPubResult.data.ensemble_standard_errordepending on theresilience_levelused), but can contain more data depending on the error mitigation options that were specified.

The below code snippet describes thePrimitiveResult(and associatedPubResult) format for the job created above.

Output:

In addition to the estimate of the mean of the observables passed in the input PUBs (theevsfield of theDataBin), the Estimator also attempts to deliver an estimate of the error associated with those expectation values. All estimator queries will populate thestdsfield with a quantity like the standard error of the mean for each expectation value, but some error mitigation options produce additional information, such asensemble_standard_error.

Consider a single observableO\mathcal{O}O. In the absence ofZNE, you can think of each shot of the Estimator execution as providing a point estimate of the expectation value⟨O⟩\langle \mathcal{O} \rangle⟨O⟩. If the pointwise estimates are in a vectorOs, then the value returned inensemble_standard_erroris equivalent to the following (in whichσO\sigma_{\mathcal{O}}σO​is the standard deviation of the expectation value estimate andNshotsN_{shots}Nshots​is the number of shots):

σONshots,\frac{ \sigma_{\mathcal{O}} }{ \sqrt{N_{shots}} },Nshots​​σO​​,

which treats all shots as part of a single ensemble. If you requested gatetwirling(twirling.enable_gates = True), you can sort the pointwise estimates of⟨O⟩\langle \mathcal{O} \rangle⟨O⟩into sets that share a common twirl. Call these sets of estimatesO_twirls, and there arenum_randomizations(number of twirls) of them. Thenstdsis the standard error of the mean ofO_twirls, as in

σONtwirls,\frac{ \sigma_{\mathcal{O}} }{ \sqrt{N_{twirls}} },Ntwirls​​σO​​,

whereσO\sigma_{\mathcal{O}}σO​is the standard deviation ofO_twirlsandNtwirlsN_{twirls}Ntwirls​is the number of twirls. When you do not enable twirling,stdsandensemble_standard_errorare equal.

If you enable ZNE, then thestdsdescribed above become weights in a non-linear regression to an extrapolator model. What finally gets returned in thestdsin this case is the uncertainty of the fit model evaluated at a noise factor of zero. When there is a poor fit, or large uncertainty in the fit, the reportedstdscan become very large. When ZNE is enabled,pub_result.data.evs_noise_factorsandpub_result.data.stds_noise_factorsare also populated, so that you can do your own extrapolation.

When a Sampler job is completed successfully, the returnedPrimitiveResultobject contains a list ofSamplerPubResults, one per PUB. The data bins of theseSamplerPubResults are dict-like objects that contain oneBitArrayperClassicalRegisterin the circuit.

TheBitArrayclass is a container for ordered shot data. In more detail, it stores the sampled bitstrings as bytes inside a two-dimensional array. The left-most axis of this array runs over ordered shots, while the right-most axis runs over bytes.

As a first example, let us look at the following ten-qubit circuit:

Output:

It can sometimes be convenient to convert away from the bytes format in theBitArrayto bitstrings. Theget_countmethod returns a dictionary mapping bitstrings to the number of times that they occurred.

When a circuit contains more than one classical register, the results are stored in differentBitArrays. The following example modifies the previous snippet by splitting the classical register into two distinct registers:

Since arrays generally offer better performance compared to dictionaries, it is advisable to perform any post-processing directly on theBitArrays rather than on dictionaries of counts. TheBitArrayclass offers a range of methods to perform some common post-processing operations:

In addition to the execution results, both thePrimitiveResultandPubResultobjects contain a metadata attribute about the job that was submitted. The metadata containing information for all submitted PUBs (such as the variousruntime optionsavailable) can be found in thePrimitiveResult.metatada, while the metadata specific to each PUB is found inPubResult.metadata.

Output:

For Sampler jobs, you can also review the result metadata to understand when certain data was run; this is called theexecution span.

On this page

© IBM Corp., 2017-2025


---

# Primitives examples







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The examples in this section illustrate some common ways to use primitives. Before running these examples, follow the instructions inInstall and set up.

These examples all use the primitives from Qiskit Runtime, but you could use the base primitives instead.

Efficiently calculate and interpret expectation values of the quantum operators required for many algorithms with Estimator. Explore uses in molecular modeling, machine learning, and complex optimization problems.

Use Estimator to determine the expectation value of a single circuit-observable pair.

Output:

Use Estimator to determine the expectation values of multiple circuit-observable pairs.

Output:

Use Estimator to run three experiments in a single job, leveraging parameter values to increase circuit reusability.

Output:

Explore sessions and advanced options to optimize circuit performance on QPUs.

Output:

Generate entire error-mitigated quasi-probability distributions sampled from quantum circuit outputs. Leverage Sampler’s capabilities for search and classification algorithms like Grover’s and QVSM.

Use Sampler to return the measurement outcome as bitstrings or counts of a single circuit.

Output:

Use Sampler to return the measurement outcome as bitstrings or counts of multiple circuits in one job.

Output:

Run several experiments in a single job, leveraging parameter values to increase circuit reusability.

Output:

Explore sessions and advanced options to optimize circuit performance on QPUs.

Output:

Output:

On this page

© IBM Corp., 2017-2025


---

# Primitives with REST API







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

The steps in this topic describe how to run and configure primitive workloads with REST API, and demonstrate how to invoke them in any program of your choice.

This documentation utilizes the Pythonrequestsmodule to demonstrate the Qiskit Runtime REST API. However, this workflow can be executed using any language or framework that supports working with REST APIs. Refer to theAPI reference documentationfor details.

Because Qiskit Runtime Estimator is a managed service, you first need to initialize your account. You can then select the device you want to use to calculate the expectation value.

Find details on how to initialize your account, view available backends, and invalidate tokens in thistopic.

You need at least one circuit as the input to the Estimator primitive.

Define a QASM quantum circuit. For example:

The following code snippets assume that theqasm_stringhas been transpiled to a new stringresulting_qasm. Find detailed instructions on how to use the Qiskit Transpiler Service API in thistopic.

The following jobs useQiskit Runtime V2 primitives. BothSamplerV2andEstimatorV2take one or more primitive unified blocs (PUBs) as the input. Each PUB is a tuple that contains one circuit and the data broadcasted to that circuit, which can be multiple observables and parameters. Each PUB returns a result.

Next, pass thejob_idto the API:

Output

Get job results:

Output

Error mitigation techniques allow users to mitigate circuit errors by modeling the device noise at the time of execution. This typically results in quantum pre-processing overhead related to model training, and classical post-processing overhead to mitigate errors in the raw results by using the generated model.

The error mitigation techniques built in to primitives are advanced resilience options. To specify these options, use theresilience_leveloption when submitting your job.

The following examples demonstrate the default options for dynamical decoupling, twirling, and TREX + ZNE. Find more options and further details in theError mitigation and suppression techniquestopic.

Because Qiskit Runtime Sampler is a managed service, you first need to initialize your account. You can then select the device you want to use to run your calculations on.

Find details on how to initialize your account, view available backends, and invalidate tokens in thistopic.

You need at least one circuit as the input to the Sampler primitive.

Define a QASM quantum circuit:

The code snippets given below assume that theqasm_stringhas been transpiled to a new stringresulting_qasm. Find detailed instructions on how to use the Qiskit Transpiler Service API in thistopic.

The jobs below useQiskit Runtime V2 primitives. BothSamplerV2andEstimatorV2take one or more primitive unified blocs (PUBs) as the input. Each PUB is a tuple that contains one circuit and the data broadcasted to that circuit, which can be multiple observables and parameters. Each PUB returns a result.

Next, pass thejob_idto the API:

Output

Get job results:

Output

Error mitigation techniques allow users to mitigate circuit errors by modeling the device noise at the time of execution. This typically results in quantum pre-processing overhead related to model training, and classical post-processing overhead to mitigate errors in the raw results by using the generated model.

The error mitigation techniques built in to primitives are advanced resilience options. To specify these options, use theresilience_leveloption when submitting your job.
Sampler V2 does not support specifying resilience levels. However, you can turn on or off individual error mitigation / suppression methods.

The following examples demonstrate the default options for dynamical decoupling and twirling. Find more options and further details in theError mitigation and suppression techniquestopic.

Because Qiskit Runtime is a managed service, you first need to initialize your account. You can then select the device you want to use to run your calculations on.

Find details on how to initialize your account, view available backends, and invalidate tokens in thistopic.

The following jobs use Qiskit Runtime V2primitives. BothSamplerV2andEstimatorV2take one or moreprimitive unified blocs (PUBs)as the input. Each PUB is a tuple that contains one circuit and the data broadcasted to that circuit, which can be multiple observables and parameters. Each PUB returns a result.

Next, pass thejob_idto the API:

Output

Get job results:

Output

On this page

© IBM Corp., 2017-2025


---

# Noise learning helper







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

The error mitigation techniquesPEAandPECboth utilize a noise learning component based on aPauli-Lindblad noise model, which is typically managed during execution after submitting one or more jobs throughqiskit-ibm-runtimewithout any local access to the fitted noise model. However, as ofqiskit-ibm-runtime0.27.1, aNoiseLearnerand associatedNoiseLearnerOptionsclass have been created to obtain the results of these noise learning experiments. These results can then be stored locally as aNoiseLearnerResultand used as input in later experiments. This page provides an overview of its usage and the associated options available.

TheNoiseLearnerclass performs experiments that characterize noise processes based on a Pauli-Lindblad noise model for one (or more) circuits. It possesses arun()method that executes the learning experiments and takes as input either a list of circuits or aPUB, and returns aNoiseLearnerResultcontaining the learned noise channels and metadata about the job(s) submitted. Below is a code snippet demonstrating the usage of the helper program.

The resultingNoiseLearnerResult.datais a list ofLayerErrorobjects containing thenoise modelfor each individual entangling layer that belongs to the target circuit(s). EachLayerErrorstores the layer information, in the form of a circuit and a set of qubit labels, alongside thePauliLindbladErrorfor the noise model that was learned for the given layer.

Output:

TheLayerError.errorattribute of the noise learning result contains the generators and error rates of the fitted Pauli Lindblad model, which has the form

Λ(ρ)=exp⁡∑jrj(PjρPj†−ρ),\Lambda(\rho) = \exp{\sum_j r_j \left(P_j \rho P_j^\dagger - \rho\right)},Λ(ρ)=exp∑j​rj​(Pj​ρPj†​−ρ),

where therjr_jrj​are theLayerError.ratesandPjP_jPj​are the Pauli operators specified inLayerError.generators.

You can choose among several options to input when you instantiate aNoiseLearnerobject. These options are encapsulated by theqiskit_ibm_runtime.options.NoiseLearnerOptionsclass and include the ability to specify the maximum layers to learn, number of randomizations, and the twirling strategy, among others. Refer to the API documentation aboutNoiseLearnerOptionsfor more detailed information.

Below is a simple example showing how to use theNoiseLearnerOptionsin aNoiseLeanerexperiment:

The noise model learned on the circuit can also be used as an input to theEstimatorV2primitive implemented in Qiskit IBM Runtime. This can be passed into the primitive a few different ways. The next three examples show how you can pass the noise model to theestimator.optionsattribute directly, via aResilienceOptionsV2object before instantiating an Estimator primitive, and by passing in an appropriately formatted dictionary.

Once the noise model is passed into theEstimatorV2object, it can be used to run workloads and perform error mitigation as normal.

On this page

© IBM Corp., 2017-2025


---

# Introduction to options







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

You can pass options to primitives to customize them to meet your needs. This section focuses on Qiskit Runtime primitive options. While the interface of the primitives'run()method is common across all implementations, their options are not. Consult the corresponding API references for information about theqiskit.primitivesandqiskit_aer.primitivesoptions.

When calling the primitives, you can pass in options by using an options class or a dictionary. Commonly-used options, such asresilience_level, are at the first level. Other options are grouped into different categories, such asexecution. See theSet primitive optionssection for full details.

If you do not specify a value for an option, it is given a special value ofUnsetand the server default value is used. Thus, the default value will be the same regardless of your code version.

The tables in theOptions classes summarysection lists the default values.

Options can be defined before a primitive is constructed and passed to the primitive, which makes a copy of them. This can be done either as a nested dictionary, or by using the options classes. Additionally, after the primitive is constructed, its options can be changed. Use the workflow that works best for your application.  SeeSpecify optionsfor full details.

The following table documents options from the latest version ofqiskit-ibm-runtime. To see older option versions, visit theqiskit-ibm-runtimeAPI referenceand select a previous version.

Scroll to see the full table.

Settinggen3-turboenables the next-generation execution path, which provides a great improvement in performance. This option is experimental (subject to change without notice, and stability is not guaranteed).

Due to differences in the device compilation process, certain runtime features cannot be used together in a single job. Click the appropriate tab for a list of features that are incompatible with the selected feature:

Incompatible with:

Other notes:

Incompatible with dynamic circuits.

Incompatible with:

Incompatible with:

Might not work when using custom gates.

Incompatible with fractional gates.

Other notes:

Incompatible with:

Incompatible with:

Incompatible with:

On this page

© IBM Corp., 2017-2025


---

# Specify options







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

You can use options to customize the Estimator and Sampler primitives. This section focuses on how to specify Qiskit Runtime primitive options. While the interface of the primitives'run()method is common across all implementations, their options are not. Consult the corresponding API references for information about theqiskit.primitivesandqiskit_aer.primitivesoptions.

Notes about specifying options in the primitives:

You can set options when initializing the primitive, after initializing the primitive, or in therun()method. See theprecedence rulessection to understand what happens when the same option is specified in multiple places.

You can pass in an instance of the options class or a dictionary when initializing a primitive, which then makes a copy of those options. Thus, changing the original dictionary or options instance doesn't affect the options owned by the primitives.

When creating an instance of theEstimatorV2orSamplerV2class, you can pass in an instance of the options class. Those options will then be applied when you userun()to perform the calculation.  Specify the options in this format:options.option.sub-option.sub-sub-option = choice.  For example:options.dynamical_decoupling.enable = True

Example:

SamplerV2andEstimatorV2have separate options classes (EstimatorOptionsandSamplerOptions).

You can specify options as a dictionary when initializing the primitive.

You can specify the options in this format:primitive.options.option.sub-option.sub-sub-option = choiceto take advantage of auto-complete, or use theupdate()method to make bulk updates.

TheSamplerV2andEstimatorV2options classes (EstimatorOptionsandSamplerOptions) do not need to be instantiated if you are setting options after initializing the primitive.

The only values you can pass torun()are those defined in the interface.  That is,shotsfor Sampler andprecisionfor Estimator. This overwrites any value set fordefault_shotsordefault_precisionfor the current run.

Output:

The resilience level is not actually an option that directly impacts the primitive query, but specifies a base set of curated options to build off of. In general, level 0 turns off all error mitigation, level 1 turns on options for measurement error mitigation, and level 2 turns on options for gate and measurement error mitigation.

Any options you manually specify in addition to the resilience level are applied on top of the base set of options defined by the resilience level. Therefore, in principle, you could set the resilience level to 1, but then turn off measurement mitigation, although this is not advised.

In the following example, setting the resilience level to 0 initially turns offzne_mitigation, butestimator.options.resilience.zne_mitigation = Trueoverrides the relevant setup fromestimator.options.resilience_level = 0.

TheSamplerV2.runmethod accepts two arguments: a list of PUBs, each of which can specify a PUB-specific value for shots, and a shots keyword argument. These shot values are a part of the Sampler execution interface, and are independent of the Runtime Sampler's options.  They take precedence over any values specified as options in order to comply with the Sampler abstraction.

However, ifshotsis not specified by any PUB or in the run keyword argument (or if they are allNone), then the shots value from the options is used, most notablydefault_shots.

Finally, because thetwirlingoptionsnum_randomizationsandshots_per_randomizationare enabled by default, the number of shots will actually be the product ofnum_randomizationsandshots_per_randomizationif thedefault_shotsvalue is the only way shots are specified.

To summarize, this is the order of precedence for specifying shots in the Sampler, for any particular PUB:

Thus, if shots are specified in all possible places, the one with highest precedence (shots specified in the PUB) is used.

Precision is analogous to shots, described in the previous section, except that the Estimator options contain bothdefault_shotsanddefault_precision.

Specifically, for any particular Estimator PUB:

For example, if precision is specified in all four places, the one with highest precedence (precision specified in the PUB) is used.

Precision scales inversely with usage.  That is, the lower the precision, the more QPU time it takes to run.

There are many available options, but the following are the most commonly used:

For some algorithms, setting a specific number of shots is a core part of their routines.  Shots (or precision) can be specified in multiple places.  They are prioritized as follows:

For any Sampler PUB:

For any Estimator PUB:

Example:

Output:

The maximum execution time (max_execution_time) limits how long a job can run.  If a job exceeds this time limit, it is forcibly canceled.  This value applies to single jobs, whether they are run in job, session, or batch mode.

The value is set in seconds, based on quantum time (not wall clock time), which is the amount of time that the QPU is dedicated to processing your job.  It is ignored when using local testing mode because that mode does not use quantum time.

You can turn off all error mitigation and suppression if you are, for example, doing research on your own mitigation techniques. To accomplish this, for EstimatorV2, setresilience_level = 0. For SamplerV2, no changes are necessary because no error mitigation or suppression options are enabled by default.

Example:

Turn off all error mitigation and suppression in Estimator.

On this page

© IBM Corp., 2017-2025


---

# Error mitigation and suppression techniques







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

The code on this page was developed using the following requirements.
We recommend using these versions or newer.

This page provides high-level explanations of the error suppression and error mitigation techniques available through Qiskit Runtime.

The following cell imports the Estimator primitive and creates a backend that will be used for initializing the Estimator in later code cells.

Quantum circuits are executed on IBM® hardware as sequences of microwave pulses that need to be scheduled and run at precise time intervals.
Unfortunately, unwanted interactions between qubits can lead to coherent errors on idling qubits. Dynamical decoupling works by inserting pulse sequences on idling qubits to approximately cancel out the effect of these errors. Each inserted pulse sequence amounts to an identity operation, but the physical presence of the pulses has the effect of suppressing errors.
There are many possible choices of pulse sequences, and which sequence is better for each particular case remains anactive area of research.

Note that dynamical decoupling is mainly useful for circuits containing gaps in which some qubits sit idle without any operations acting on them. If the operations in the circuit are packed very densely, such that all of the qubits are busy most of the time, then the addition of dynamical decoupling pulses might not improve performance. In fact, it could even worsen performance due to imperfections in the pulses themselves.

The diagram below depicts dynamical decoupling with an XX pulse sequence. The abstract circuit on the left is mapped onto a microwave pulse schedule on the top right. The bottom right depicts the same schedule, but with a sequence of two X pulses inserted during an idle period of the first qubit.

Dynamical decoupling can be enabled by settingenabletoTruein thedynamical decoupling options. Thesequence_typeoption can be used to pick from several different pulse sequences. The default sequence type is"XX".

The following code cell shows how to enable dynamical decoupling for the Estimator and choose a dynamical decoupling sequence.

Twirling, also known asrandomized compiling, is a widely used technique for converting arbitrary noise channels into noise channels with more specific structure.

Pauli twirling is a special kind of twirling that uses Pauli operations. It has the effect of transforming any quantum channel into a Pauli channel. Performed alone, it can mitigate coherent noise because coherent noise tends to accumulate quadratically with the number of operations, whereas Pauli noise accumulates linearly. Pauli twirling is often combined with other error mitigation techniques that work better with Pauli noise than with arbitrary noise.

Pauli twirling is implemented by sandwiching a chosen set of gates with randomly chosen single-qubit Pauli gates in such a way that the ideal effect of the gate remains the same. The result is that a single circuit is replaced with a random ensemble of circuits, all with the same ideal effect. When sampling the circuit, samples are drawn from multiple random instances, rather than just a single one.

Since most of the errors in current quantum hardware come from two-qubit gates, this technique is often applied exclusively to (native) two-qubit gates. The following diagram depicts some Pauli twirls for the CNOT and ECR gates. Every circuit within a row has the same ideal effect.

Pauli twirling can be enabled by settingenable_gatestoTruein thetwirling options. Other notable options include:

The following code cell shows how to enable Pauli twirling and set these options for the estimator. None of these options are required to be set explicitly.

Twirled readout error extinction (TREX)mitigates the effect of measurement errors for the estimation of Pauli observable expectation values.
It is based on the notion of twirled measurements, which are accomplished by randomly substituting measurement gates by a sequence of (1) a Pauli X gate, (2) a measurement, and (3) classical bit flip. Just like in standard gate twirling, this sequence is equivalent to a plain measurement in the absence of noise, as depicted in the following diagram:

In the presence of readout error, measurement twirling has the effect of diagonalizing the readout-error transfer matrix, making it easy to invert. Estimating the readout-error transfer matrix requires executing additional calibration circuits, which introduces a small overhead.

TREX can be enabled by settingmeasure_mitigationtoTruein theQiskit Runtime resilience optionsfor Estimator. Options for measurement noise learning are describedhere. As with gate twirling, you can set the number of circuit randomizations and the number of shots per randomization.

The following code cell shows how to enable TREX and set these options for the estimator. None of these options are required to be set explicitly.

Zero-noise extrapolation (ZNE) is a technique for mitigating errors in estimating expectation values of observables. While it often improves results, it is not guaranteed to produce an unbiased result.

ZNE consists of two stages:

Both the noise amplification and extrapolation stages can be implemented in many different ways. Qiskit Runtime implements noise amplification by "digital gate folding," which means that two-qubit gates are replaced with equivalent sequences of the gate and its inverse. For example, replacing a unitaryUUUwithUU†UU U^\dagger UUU†Uwould yield a noise amplification factor of 3. For the extrapolation, you can choose from one of several functional forms, including a linear fit or an exponential fit.
The image below depicts digital gate folding on the left, and the extrapolation procedure on the right.

ZNE can be enabled by settingzne_mitigationtoTruein theQiskit Runtime resilience optionsfor Estimator.
The Qiskit Runtime options for ZNE are describedhere. The following options are notable:

The following code cell shows how to enable ZNE and set these options for the estimator. None of these options are required to be set explicitly.

One of the main challenges in ZNE is to accurately amplify the noise affecting the target circuit. Gate folding provides an easy way to perform this amplification, but is potentially inaccurate and might lead to incorrect results.  See the article"Scalable error mitigation for noisy quantum circuits produces competitive expectation values", and specifically page 4 of the supplementary information for details. Probabilistic error amplification provides a more accurate approach to error amplification through noise learning.

PEA is a more sophisticated technique that performs preliminary experiments to reconstruct the noise and then uses this information to perform an accurate amplification. It starts by learning the twirled noise model of each layer of entangling gates in the circuit before they are run (seeLayerNoiseLearningOptionsfor relevant learning options). After the learning phase, the circuits are executed at each noise factor, where every entangling layer of the circuits is amplified by probabilistically injecting single-qubit noise proportional to the corresponding learned noise model. See the article"Evidence for the utility of quantum computing before fault tolerance"for more details.

PEA consists of three stages:

For utility-scale experiments, PEA is often the best choice.

Because PEA is a ZNE noise amplification technique, you also need to enable ZNE by settingresilience.zne_mitigation = True. Otherresilience.zneoptions can additionally be used to set extrapolators, amplification levels, and so on. PEA requires a noise model, which is automatically generated when using primitives.

The following snippet provides an example where PEA is used to mitigate the result of an Estimator job:

Probabilistic error cancellation (PEC) is a technique for mitigating errors in estimating expectation values of observables. Unlike ZNE, it returns an unbiased estimate of the expectation value. However, it generally incurs a greater overhead.

In PEC, the effect of an ideal target circuit is expressed as a linear combination of noisy circuits that are actually implementable in practice:

The output of the ideal circuit can then be reproduced by executing different noisy circuit instances drawn from a random ensemble defined by the linear combination. If the coefficientsηi\eta_iηi​form a probability distribution, they can be used directly as the probabilities of the ensemble. In practice, some of the coefficients are negative, so they form a quasi-probability distribution instead. They can still be used to define a random ensemble, but there is a sampling overhead related to the negativity of the quasi-probability distribution, which is characterized by the quantity

The sampling overhead is a multiplicative factor on the number of shots required to estimate an expectation value to a given precision, compared to the number of shots that would be needed from the ideal circuit. It scales quadratically withγ\gammaγ, which in turn scales exponentially with the depth of the circuit.

PEC can be enabled by settingpec_mitigationtoTruein theQiskit Runtime resilience optionsfor Estimator.
The Qiskit Runtime options for PEC are describedhere. A limit on the sampling overhead can be set using themax_overheadoption. Note that limiting the sampling overhead can cause the precision of the result to exceed the requested precision. The default value ofmax_overheadis 100.

The following code cell shows how to enable PEC and set themax_overheadoption for the estimator.

On this page

© IBM Corp., 2017-2025


---

# Configure error mitigation







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Error mitigation techniques allow users to mitigate circuit errors by
modeling the device noise at the time of execution. This typically
results in quantum pre-processing overhead related to model training and
classical post-processing overhead to mitigate errors in the raw results
by using the generated model.

The Estimator primitive supports several error mitigation techniques, includingTREX,ZNE,PEC, andPEA. SeeError mitigation and suppression techniquesfor an explanation of each. When using primitives, you can turn on or off individual methods. See theCustom error settingssection for details.

Sampler does not support error mitigation, but you can use themthree(matrix-free measurement mitigation) package to perform error mitigation locally.

Estimator also supportsresilience_level. The resilience level specifies how much resilience to build against
errors. Higher levels generate more accurate results, at the expense of
longer processing times. Resilience levels can be used to configure the
cost/accuracy trade-off when applying error mitigation to your primitive
query. Error mitigation reduces errors (bias) in results by processing
the outputs from a collection, or ensemble, of related circuits. The
degree of error reduction depends on the method applied. The resilience
level abstracts the detailed choice of error mitigation method to allow
users to reason about the cost/accuracy trade that is appropriate to
their application.

Given this, each level corresponds to a method or methods with
increasing level of quantum sampling overhead to enable you experiment
with different time-accuracy tradeoffs. The following table shows you
which levels and corresponding methods are available for each of the
primitives.

Error mitigation is task-specific, so the techniques you can
apply vary based whether you are sampling a distribution or generating
expectation values.

Estimator supports the following resilience levels.  Sampler does not support resilience levels.

Resilience levels are currently in beta so sampling overhead and
solution quality will vary from circuit to circuit. New features,
advanced options, and management tools will be released on a rolling
basis. Specific error mitigation methods are not guaranteed to be
applied at each resilience level.

You can use resilience levels to specify error mitigation techniques, or you can set custom techniques individually as described inCustom error settings.

No error mitigation is applied to the user program.

Level 1 appliesreadout error mitigationandmeasurement twirlingby applying a model-free technique known
as Twirled Readout Error eXtinction (TREX). It reduces measurement error
by diagonalizing the noise channel associated with measurement by
randomly flipping qubits through X gates immediately before measurement. A
rescaling term from the diagonal noise channel is learned by
benchmarking random circuits initialized in the zero state. This allows
the service to remove bias from expectation values that result from
readout noise. This approach is described further inModel-free
readout-error mitigation for quantum expectation
values.

Level 2 applies theerror mitigation techniques included in level 1and also appliesgate twirlingand uses theZero Noise Extrapolation method (ZNE).  ZNE computes an
expectation value of the observable for different noise factors
(amplification stage) and then uses the measured expectation values to
infer the ideal expectation value at the zero-noise limit (extrapolation
stage). This approach tends to reduce errors in expectation values, but
is not guaranteed to produce an unbiased result.

The overhead of this method scales with the number of noise factors. The
default settings sample the expectation value at three noise factors,
leading to a roughly 3x overhead when employing this resilience level.

In Level 2, the TREX method randomly flips qubits through X gates immediately before measurement,
and flips the corresponding measured bit if an X gate was applied. This approach is described further inModel-free
readout-error mitigation for quantum expectation
values.

TheEstimatorV2interface lets users seamlessly work with the variety of
error mitigation methods to reduce error in expectation values of
observables. The following code uses Zero Noise Extrapolation and readout error mitigation by simply
settingresilience_level 2.

You can turn on and off individual error mitigation and suppression methods, including dynamical decoupling, gate and measurement twirling, measurement error mitigation, PEC, and ZNE. SeeError mitigation and suppression techniquesfor an explanation of each.

For instructions to turn off all error mitigation, see theTurn off all error suppression and mitigationsection.

On this page

© IBM Corp., 2017-2025


---

# Configure error suppression







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Error suppression refers to techniques where you use knowledge about the undesirable effects to introduce customization that can anticipate and avoid the potential impacts of those effects. These techniques often consist of altering or adding control signals to ensure that the quantum processor returns the desired results.  This typically results in quantum pre-processing overhead; therefore, it is important to achieve a balance between perfecting your results and ensuring that your job completes in a reasonable amount of time.

Primitives support a number of error suppression techniques, includingdynamical decouplingandPauli twirling. SeeError mitigation and suppression techniquesfor an explanation of each. When using primitives, you can turn on or off individual methods. See theAdvanced error suppression optionssection for details.

Estimator employs error suppression and mitigation by default. If you don't want any processing done to your input circuits, follow the instructions in theTurn off all error mitigation and error suppressionsection.

In the primitives, you can explicitly enable and disable individual error mitigation and suppression methods, such as dynamical decoupling.

Output:

Can't remember the right attributes? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

For instructions to turn off all error suppression, see theTurn off all error suppression and mitigationsection.

On this page

© IBM Corp., 2017-2025


---

# Configure error suppression







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Error suppression refers to techniques where you use knowledge about the undesirable effects to introduce customization that can anticipate and avoid the potential impacts of those effects. These techniques often consist of altering or adding control signals to ensure that the quantum processor returns the desired results.  This typically results in quantum pre-processing overhead; therefore, it is important to achieve a balance between perfecting your results and ensuring that your job completes in a reasonable amount of time.

Primitives support a number of error suppression techniques, includingdynamical decouplingandPauli twirling. SeeError mitigation and suppression techniquesfor an explanation of each. When using primitives, you can turn on or off individual methods. See theAdvanced error suppression optionssection for details.

Estimator employs error suppression and mitigation by default. If you don't want any processing done to your input circuits, follow the instructions in theTurn off all error mitigation and error suppressionsection.

In the primitives, you can explicitly enable and disable individual error mitigation and suppression methods, such as dynamical decoupling.

Output:

Can't remember the right attributes? Try asking Qiskit Code Assistant.

New to the code assistant? SeeQiskit Code Assistantfor installation and usage. Note this is an experimental feature and only available to IBM Quantum™ Premium Plan users.

For instructions to turn off all error suppression, see theTurn off all error suppression and mitigationsection.

On this page

© IBM Corp., 2017-2025


---

# Choose the right execution mode







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

Utility-scale workloads can take many hours to complete, so it is important that both the classical and quantum resources are scheduled efficiently to streamline the execution. Execution modes provide flexibility in balancing the cost and time tradeoff to use resources optimally for your workloads. There are several aspects to consider when choosing which execution mode to use, such as overall execution time (maximum time to live, or TTL) and time between jobs (interactive TTL).

The benefits of each are summarized below:

Generally, use batch mode unless you have workloads that don’t have all inputs ready at the outset.

To ensure the most efficient use of the execution modes, the following practices are recommended:

There is a fixed overhead associated with running a job. In general, if each of your jobs uses less than one minute ofQPU time, consider combining several into one larger job (this applies to all execution modes). "QPU time" refers to time spent by the QPU complex to process your job.

If each of your jobs consumes more than one minute of QPU time, or if combining jobs is not practical, you can still run multiple jobs in parallel. Every job goes through both classical and quantum processing. While a QPU can process only one job at a time, up to five classical jobs can be processed in parallel. You can take advantage of this by submitting multiple jobs inbatchorsessionexecution mode.

The above are general guidelines, and you should tune your workload to find the optimal ratio, especially when using sessions. For example, if you are using a session to get exclusive access to a backend, consider breaking up large jobs into smaller ones and running them in parallel. This might be more cost-effective because it can reduce wall-clock time.

Running a quantum variational algorithm typically follows this flow:

In this case, if you were using job or batch mode, each job generated by step (2) needs to go back through the queue. This drastically increases the experiment length (wall-clock time) due to the queuing time. It could also take longer to converge due to device drift.  That is, every iteration is supposed give you a better result, but device drift could make subsequent results worse.

In addition, if you usePEAorPEC, you canlearn the noise modelonce and apply it to subsequent jobs when running in dedicated session. This usually doesn't work with batch or job mode because the noise model could become stale by the time the next job is out of the queue.

To compare the effects of the available error mitigation methods, you might follow this flow:

In this case, all jobs (which are related but independent) are available at the outset. If you use batch mode, they are scheduled collectively so you only have to wait for them to go through the queue once.  Additionally, because the goal is to compare the effects of various error mitigation methods, it's beneficial that they run as closely together as possible. Thus, batch would be a good choice.  Youcouldrun these jobs in a session, but because sessions are generally more expensive, it is recommended that you use batch whenever you don't need the additional functionality sessions provides.

On this page

© IBM Corp., 2017-2025


---

# Run jobs in a batch







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Use batch mode to submit multiple primitive jobs simultaneously. Following are examples of working with batches.

Before starting a batch, you mustset up Qiskit Runtimeand initialize it as a service:

You can open a runtime batch by using the context managerwith Batch(...)or by initializing theBatchclass. When you start a batch,  you must specify a QPU by passing abackendobject.  The batch starts when its first job begins execution.

Batch class

Context manager

The context manager automatically opens and closes the batch.

You can define the batch's maximum time to live (TTL) with themax_timeparameter. This should exceed the longest job's execution time. This timer starts when the batch starts.  When the value is reached, the batch is closed.  Any jobs that are running will finish, but jobs still queued are failed.

There is also an interactive time to live (interactive TTL) value that cannot be configured (1 minute for all plans).  If no batch jobs are queued within that window, the batch is temporarily deactivated.

Default maximum TTL values:

To determine a batch's maximum TTL or interactive TTL, follow the instructions inDetermine batch detailsand look for themax_timeorinteractive_timeoutvalue, respectively.

A batch automatically closes when it exits the context manager. When the batch context manager is exited, the batch is put into "In progress, not accepting new jobs" status. This means that the batch finishes processing all running or queued jobs until the maximum TTL value is reached. After all jobs are completed, the batch is immediately closed. You cannot submit jobs to a closed batch.

If you are not using a context manager, manually close the batch.  If you leave the batch open and submit more jobs to it later, it is possible that the maximum TTL will be reached before the subsequent jobs start running; causing them to be canceled. You can close a batch as soon as you are done submitting jobs to it. When a batch is closed withbatch.close(), it no longer accepts new jobs, but the already submitted jobs will still run until completion and their results can be retrieved.

For a comprehensive overview of a batch's configuration and status, including its interactive and max TTL, use thebatch.details() method.

There are multiple ways you can reconfigure your jobs to take advantage of the parallel processing provided by batching. The following example shows how you can partition a long list of circuits into multiple jobs and run them as a batch to take advantage of the parallel processing.

If you setbackend=backendin a primitive, the program is run in job mode, even if it's inside a batch or session context. Settingbackend=backendis deprecated as of Qiskit Runtime 0.24.0.  Instead, use themodeparameter.

On this page

© IBM Corp., 2017-2025


---

# Run jobs in a session







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Use sessions when you need dedicated and exclusive access to the QPU.

Before starting a session, you mustset up Qiskit Runtimeand initialize it as a service:

You can open a runtime session by using the context managerwith Session(...)or by initializing theSessionclass. When you start a session,  you must specify a QPU by passing abackendobject. The session starts when its first job begins execution.

If you open a session but do not submit any jobs to it for 30 minutes, the session automatically closes.

Session class

Context manager

The context manager automatically opens and closes the session.

The maximum session time to live (TTL) determines how long a session can run.  You can set this value with themax_timeparameter. This should exceed the longest job's execution time.

This timer starts when the session starts.  When the value is reached, the session is closed.  Any jobs that are running will finish, but jobs still queued are failed.

There is also an interactive time to live (interactive TTL) value that cannot be configured.  If no session jobs are queued within that window, the session is temporarily deactivated.

Default values:

* Certain Premium Plan instances might be configured to have a different value.

To determine a session's max TTL or  interactive TTL, follow the instructions inDetermine session detailsand look for themax_timeorinteractive_timeoutvalue, respectively.

A session ends in the following circumstances:

A session automatically closes when it exits the context manager. When the session context manager is exited, the session is put into "In progress, not accepting new jobs" status. This means that the session finishes processing all running or queued jobs until the maximum timeout value is reached. After all jobs are completed, the session is immediately closed. This allows the scheduler to run the next job without waiting for the session interactive timeout, thereby reducing the average job queuing time. You cannot submit jobs to a closed session.

If you are not using a context manager, manually close the session to avoid unwanted cost. You can close a session as soon as you are done submitting jobs to it. When a session is closed withsession.close(), it no longer accepts new jobs, but the already submitted jobs will still run until completion and their results can be retrieved.

You can query a session's status to understand its current state by usingsession.status()or by viewing the Workloads page for your channel.

Session status can be one of the following:

For a comprehensive overview of a session's configuration and status, use thesession.details() method.

Sessions are especially useful for algorithms that require frequent communication between classical and quantum resources.

Example: Run an iterative workload that uses the classical SciPy optimizer to minimize a cost function. In this model, SciPy uses the output of the cost function to calculate its next input.

You can get more out of a session by running multiple workloads simultaneously. The following example shows how you can run two VQE algorithms, each using a different classical optimizer, simultaneously inside a single session. Job tags are also used to differentiate jobs from each workload.

On this page

© IBM Corp., 2017-2025


---

# Execution modes using REST API







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

This documentation is relevant to IBM Quantum® Platform Classic. If you need the newer version, go to the newIBM Quantum Platform documentation.

You can run your Qiskit primitive workloads using REST APIs in one of three execution modes, depending on your needs: job, session, and batch. This topic explains these modes.

This documentation utilizes the Pythonrequestsmodule to demonstrate the Qiskit Runtime REST API. However, this workflow can be executed using any language or framework that supports working with REST APIs. Refer to theAPI reference documentationfor details.

In job mode, a single primitive request of the Estimator or the Sampler is made without a context manager. See how to run a quantum circuit usingEstimatorandSamplerfor some examples.

A session is a Qiskit Runtime feature that lets you efficiently run multi-job iterative workloads on quantum computers. Using sessions helps avoid delays caused by queuing each job separately, which can be particularly useful for iterative tasks that require frequent communication between classical and quantum resources. More details about Sessions can be found in thedocumentation.

Begin by creating a session and obtaining a session ID.

Output

It is good practice to close aSessionwhen all jobs are done. This will reduce wait time for subsequent users.

Output

Alternatively, you can submit a batch job by specifying themodein the request payload. Batch mode can help shorten processing time if all jobs can be provided at the outset. Learn about batch mode in theintroduction to execution modesguide.

Once a session is set up, one or more Sampler or Estimator jobs can be submitted to the same session by specifying the session ID.

The<parameter values>in aPUBcan either be a single parameter or a list of parameters. It also supportsnumpybroadcasting.

On this page

© IBM Corp., 2017-2025


---

# Qiskit Runtime execution modes FAQs







IBM Quantum Platform is moving and this version will be sunset on July 1. To get started on the new platform,read the migration guide.

Does Qiskit Runtime local testing mode support different execution modes?

Local testing mode supports the syntax for the different execution modes, but because there is no scheduling involved when testing locally, the modes are ignored.

How many jobs can run in parallel for a specific backend?

The number of jobs running in parallel is based on the degree of parallelism configured for the backend, which is five for most backends today.

How is usage reported for failed or canceled jobs?

See theFailed and canceled jobssection on the Execution modes page.

What happens to my jobs if a session is closed?

If you are using theSessionclass inqiskit-ibm-runtime:

If you are using the REST API directly:

If I am using session mode and expect my experiment to take many hours, is there a way to ask for calibrations to happen?

No. On-demand calibration is not available.

Is there an interactive timeout (interactive TTL) with session mode?

Yes. This reduces unwanted cost if a user forgets to close their session.

Can I change the interactive TTL or the maximum TTL of a session?

You cannot change the interactive TTL value. You can change the maximum TTL value of a session (seeSpecify the session length), but it must be less than the system-defined maximum. Ask your administrator to contact IBM support if you need a different interactive TTL or system maximum TTL.

How does session usage impact IBM Quantum Network members who are not billed by usage?

IBM Quantum Network members gain reserved capacity on IBM Quantum® QPUs. Usage is deducted from this capacity and instances with lower capacity have longer queueing time.

Do I get the same parallelism in session mode that I get with batch mode?

Yes. If you submit multiple jobs simultaneously in a session, these jobs will run in parallel.

Can sessions be interrupted by QPU upgrades or calibrations?

No.  Sessions run in dedicated mode, which means that the user has total access to the backend.  Sessions are never interrupted by calibrations or software upgrades.

Is compilation time counted as usage in session mode?

Yes.  In session mode, usage is the wall clock time the QPU iscommitted to the session. It starts when the first session job starts and ends when the session goes inactive, is closed, or when the last job completes, whichever happenslast. Thus, usage continues to accumulate after a session ends if the QPU is still running a job. Additionally, time after a job completes while the QPU waits for another session job (the interactive TTL) counts as usage. This is why you should ensure the session is closed as soon as you are done submitting jobs to it.

How many jobs run in parallel in batch mode?

The number of jobs running in parallel is based on the degree of parallelism configured for the backend, which is five for most backends. However, the number of concurrent jobs in an active batch could be lower because there could be other jobs already running when the batch becomes active.

How is runningNPUBs in job mode different from runningNsingle-PUB jobs in batch mode?

The main difference is the time and cost tradeoff:

Batch mode:

Job mode:

In general, if your each of your jobs consumes less than a minute of QPU time, consider combining them into a larger job (this applies to all execution modes).

How many jobs I can submit in a batch?

While there are no limits to the number of jobs you can submit in a batch, there is a maximum time associated with a batch. That is, when a batch's wall clock time (which starts when the first batch job starts running) exceeds the system-defined maximum time, the batch will not accept any new jobs, and any jobs queued but not running are canceled. Additionally, there are limits on how much usage your jobs can consume based on your plan. To determine the maximum time associated with a batch, use thebatch.details()methodand look for themax_timevalue.

When would my batch mode jobs run in parallel with other users' jobs?

The degree of parallelism configured for a backend is also called "execution lanes". If there are one or more execution lanes available, and your batch jobs are next in line to be run, the scheduler starts enough jobs to fill the lanes. Similarly, if your batch doesn't have enough jobs to fill the lanes, the scheduler starts other users' jobs.

Example: The backend you choose has five execution lanes, and two of them are currently occupied by other users' jobs. Your batch of six jobs is next in line to be run.

Because there are three available lanes, the scheduler starts three of your six batch jobs. It continues to start jobs in your batch as jobs finish and execution lanes become available. If a lane becomes available and there are no more jobs in your batch, the scheduler starts the next job in line.

Do all of my batch jobs need to wait in the queue?

Because QPUs are limited and shared resources, all jobs need to wait in the queue. However, when the first job in your batch starts running, all the other jobs in that batch essentially jump to the front of the queue and are prioritized by the scheduler.

Does a batch end automatically when the last associated job ends?

Yes. However, there is a slight overhead associated with this auto-detection, so you should always close your batch and session.

Can batches be interrupted by calibrations or software upgrades

Yes.  Batch workloads might be interrupted by calibrations or software upgrades.

Is compilation time counted as usage in batch mode?

No.  In batch mode, only time spent on the quantum hardware counts as usage.

On this page

© IBM Corp., 2017-2025


---

