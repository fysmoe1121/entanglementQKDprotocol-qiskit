from qiskit import IBMQ, QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np
import matplotlib
%matplotlib inline
from math import pi

def create_message():
    message = []
    for i in range(0,n):
        qc = QuantumCircuit(2,2)
        qc.x(0)
        qc.x(1)
        qc.h(0)
        qc.cx(0,1)
        qc.barrier()
        message.append(qc)
    return(message)
    
np.random.seed(seed=0)
n = 20
alice_bases = randint(3, size=n)
print(alice_bases)

np.random.seed(seed=1)
n = 20
bob_bases = randint(3, size=n)
print(bob_bases)

def measure_message(message, alice, bob):
    backend = Aer.get_backend('qasm_simulator')
    alice_measurements = []
    bob_measurements = []
    for q in range(n):
        if alice[q] == 0:
            pass
        if alice[q] == 1:
            message[q].rz(pi/2, 0)
        if alice[q] == 2:
            message[q].rz(pi/4, 0)
        message[q].h(0)
        message[q].measure(0,0)
        message[q].barrier()
        if bob[q] == 0:
            pass
        if bob[q] == 1:
            message[q].rz(-pi/4,1)
        if bob[q] == 2:
            message[q].rz(pi/4, 1)
        message[q].h(1)
        message[q].measure(1,1)
        result = execute(message[q], backend, shots=1, memory=True).result()
        alice_measured_bit = (int(result.get_memory()[0]))//10
        bob_measured_bit = (int(result.get_memory()[0]))%10
        alice_measurements.append(alice_measured_bit)
        bob_measurements.append(bob_measured_bit)
    return(alice_measurements, bob_measurements)
    

  
