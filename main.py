from qiskit import IBMQ, QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import random
import numpy as np
import matplotlib
from math import pi

n = 100

np.random.seed(seed=13)
alice_bases = randint(3, size=n)
print(alice_bases)

np.random.seed(seed=15)
bob_bases = randint(3, size=n)
print(bob_bases)

def create_eprPairs():
    pairs = []
    for i in range(n):
        qc = QuantumCircuit(2,3)
        qc.x(0)
        qc.x(1)
        qc.h(0)
        qc.cx(0,1)
        qc.barrier()
        pairs.append(qc)
    return(pairs)

def measure_pairs(pairs, alice, bob):
    backend = Aer.get_backend('qasm_simulator')
    measurements = []
    for q in range(n):
        if alice[q] == 0:
            pass
        if alice[q] == 1:
            pairs[q].rz(pi/2, 0)
        if alice[q] == 2:
            pairs[q].rz(pi/4, 0)
        pairs[q].h(0)
        pairs[q].measure(0,0)
        pairs[q].barrier()
        if bob[q] == 0:
            pass
        if bob[q] == 1:
            message[q].rz(-pi/4,1)
        if bob[q] == 2:
            message[q].rz(pi/4, 1)        
        pairs[q].h(1)
        pairs[q].measure(1,1)
        result = execute(pairs[q], backend, shots=1, memory=True).result()
        one_bit_measurement = []
        alice_measured_bit = (int(result.get_memory()[0][1]))
        bob_measured_bit = (int(result.get_memory()[0][2]))
        one_bit_measurement.append(alice_measured_bit)
        one_bit_measurement.append(bob_measured_bit)
        measurements.append(one_bit_measurement)
    return(measurements)

def create_sifted_key(measurement, alice, bob):
    sifted_key = []
    notEntangledBits = 0
    for i in range(n):
        if (alice[i] == bob[i] == 0) or (alice[i] == bob[i] == 2):
            sifted_bit = []
            sifted_bit.append(measurement[i][0])
            sifted_bit.append(measurement[i][1])
            sifted_key.append(sifted_bit)
            if measurement[i][0] == measurement[i][1]:
                notEntangledBits += 1
    return(sifted_key, "length of sifted key is " + str(len(sifted_key)) + ". " + "number of bits not perfectly entangled: "+ str(notEntangledBits))

def expected_value(measurement, alice, bob, alice_setting, bob_setting):
    pp = 0
    mm = 0
    pm = 0
    mp = 0
    for i in range(n):
        if alice[i] == alice_setting and bob[i] == bob_setting:
            if measurement[i][0] == measurement[i][1] == 1:
                pp+=1
            if measurement[i][0] == measurement[i][1] == 0:
                mm+=1
            if measurement[i][0] == 1 and measurement[i][1] == 0:
                pm+=1
            if measurement[i][0] == 0 and measurement[i][1] == 1:
                mp+=1
    return((pp - mp - pm + mm)/(pp + mp + pm + mm))

def CHSH_calc(measurements, alice, bob):
    S = 0
    S += expected_value(measurements,alice,bob,0,2)
    S += expected_value(measurements,alice,bob,0,1)
    S += expected_value(measurements,alice,bob,1,2)
    S -= expected_value(measurements,alice,bob,1,1)
    return(abs(S))

eve_bits = random.sample(range(n),n//4)
eve_bits.sort()
print(eve_bits)

def eve_drop(pairs, eve):
    for i in eve:
        pairs[i].measure(1,2)
        pairs[i].barrier()
        
def eve_detected(s_value):
    if s_value > 2.8:
        print("Eve went undetected")
    elif 2.5 < s_value <= 2.8:
        print("it is possible that Eve is evesdropping but could be just be noise")
    elif 2 < s_value <= 2.5:
        print("it is likely that Eve is evesdropping")
    else:
        print("Eve is almost certanily evedropping")
        
def encode_message(bits, bases):
    message = []
    for i in range(n):
        qc = QuantumCircuit(1,1)
        if bases[i]== 0:
            if bits[i] == 0:
                pass 
            else:
                qc.x(0)
        else:
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    return message
                
 def measure_message(message, bases):
    IBMQ.load_account()
    from qiskit.providers.ibmq import least_busy
    from qiskit.tools.monitor import job_monitor
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = provider.get_backend('ibmq_vigo')
    measurements = []
    for q in range(n):
        if bases[q] == 0:
            message[q].measure(0,0)
        if bases[q] == 1:
            message[q].h(0)
            message[q].measure(0,0)
        result = execute(message[q], backend, shots=1, memory=True).result()
        result_monitor(result)
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit
    return measurements
                            
def createBB84SiftedKey(a_bases, b_bases, bits):
    good_bits = []
    for q in range(n):
        if a_bases[q] == b_bases[q]:
            good_bits.append(bits[q])
    return good_bits 
                            
def sample_bits(bits, selection):
    sample = []
    for i in selection:
        i = np.mod(i, len(bits))
        sample.append(bits.pop(i))
    return sample
                            
def passErrorThreshold(alice_bits, bob_bits, t):
    counter = 0
    for i in range(alice_bits):
        if alice_bits[i] != bob_bits[i]:
            counter+=1
    if (counter > t):
        return(True)
    else:
        return(False)
                                   
def BB84Detection(alice_bits, bob_bits, t)
    if passErrorThreshold(alice_bits, bob_bits, t):
        print("Eve's interference was detected.")
    else:
        print("Eve went undetected!")
                            
message = create_eprPairs()
#eve_drop(message, eve_bits) 
output = measure_pairs(message, alice_bases, bob_bases)
key = create_sifted_key(output, alice_bases, bob_bases)
s = CHSH_calc(output, alice_bases, bob_bases)
print(key)
print(s)
eve_detected(s)
