import numpy as np

def get_divisors(num):
    # the divisors of the num
    divisors = []
    for n in xrange(1, num+1, 1):
        if num % n == 0:
            divisors.append(n)
    # bitrow to record the divisors
    bitrow = np.zeros(64)
    for i in xrange(64):
        if i in divisors:
            bitrow[i] = 1
        else:
            bitrow[i] = 0
    return bitrow

input_data = [21, 8, 5, 21, 11, 12]

# one bitmap to record the divisors of numbers
# row => divisor, col => index of number 
# Table[i] records number which has divisor i
table = np.zeros((64, 64))
cnts = np.zeros(64)

# Phase1: build table
for index, num in enumerate(input_data):
    row = get_divisors(num)
    for i in xrange(64):
        if row[i] == 1:
            table[i, index] = 1
            cnts[i] += 1

# Phase2: remove pairs
