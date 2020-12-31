# ekertProtocol
Ekert Protocol or EPR Protocol implementation in Qiskit.

1. generates Alice and Bob choice of basis vectors to perform their measurement

2. creates n entangled qubits in the |psi-> Bell state

3. measures the state of the qubits using Alice and Bob choice of basis measurements 

4. creates sifted key when Alice and Bob measure along compadiable basis vectors

5. uses rest of the bits to perform CHSH test and calculates S.

6. if S is approx 2rt2, no evedropping as occured by the CHSH inequality

7. we can add in an evedropper Eve who will be able to measure n/4 of Alice's qubits 

8. we calculate the S value from CHSH and Alice and Bob use it to determine if there is an evedropper present
