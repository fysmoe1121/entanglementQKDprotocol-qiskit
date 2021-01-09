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
