# entanglement-qkd
Ekert Protocol aka EPR Protocol implementation in Qiskit.
1. generates Alice and Bob choice of basis vectors to perform their measurement
2. creates n=100 entangled qubits in the |psi-> Bell state
3. measures the state of the qubits using Alice and Bob choice of basis measurements 
4. creates sifted key when Alice and Bob measure along compatible basis vectors
5. uses rest of the bits to perform CHSH test and calculates S.
6. if S is approx 2rt2, no evedropping as occured by the CHSH inequality
7. we can add in an evedropper Eve who will be able to measure n/4 of Alice's qubits 
8. we calculate the S value from CHSH and Alice and Bob use it to determine if there is an evedropper present

BB84 entangled
1. Alice creates 2n EPR pairs in state |psi> = |belta_00>^tensor2n
2. she randomly selectes n epr pairs and saves them for testing.
3. she creates a random 2n bitstring
4. for n qubits if bitstring[i] equals 1, she performs Hadamard transform of the second qubit of psi[i]
5. she sends the second qubits of psi to Bob
6. Alice announces her bitstring
7. Bob performs H when bitstring[i] = 1
8. Alice and Bob measure their qubits in |0> and |1> bases
9. If there are more than n discrepinces, Alice and Bob comclude Eve is eveasdropping and abort the protocl 
10. If they conclude no eveasdropper, they measure the rest of their n qubits to optain a key.

In E91, Alice creates n entangled qubit pairs in the  $|\Psi^+> $ Bell state. Alice and Bob then generate random strings of integers in {0,1,2} corresponding to three angles to set their detector to when measuring their qubits. The different angles are implemented in Qiskit with $HR_z(\theta)$H gates. Eve then intercepts $x$ of Bob’s qubits, measures them, and sends them to Bob. Alice and Bob then measure their qubits, compare, and create a sifted key with the qubits they measured incompatible settings. They then use the rest of their measurements to run a CHSH test. This is implemented by using a counting function to calculate the expected value. The expected value is then used to calculate the CHSH value, $S$. The value of $S$ is then used to determine if Eve was present. For the e-BB84 protocol, Alice creates  |\Phi^+>^{\otimesn} state. She then applies Hadamard transform the second qubit in n/4 pairs randomly and sends n/2 of the second qubit to Bob. Like before, Eve intercepts x of Bob’s qubits from Alice, measures them, and sends them to Bob. Bob then apply Hadamard transform to all the qubits that Alice sent him that Alice applied Hadamard to. Alice and Bob both measure their qubits and compare n/4 of them. If the quantum bit error rate (QBRT) exceeds some value $t$, they assume that their conenction has been comprised by Eve.
