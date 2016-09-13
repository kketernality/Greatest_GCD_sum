'''
This file demonstrates the potential for this algorithm to be implemented in hardware.
'''

import numpy as np

# This function will be implemented as ROM to speed up the system
# input: num, output: 64 bits row to represent its divisors
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

# Helper function, identical to priority encoder
def get_leftmost(entry):
    for i in xrange(64):
        if entry[i] == 1:
            return i

input_data = [21, 8, 5, 21, 11, 12]

# Table is a bitmap to record all divisors of the input numbers
# row => divisor, col => index of number
# e.g. Table[i] records the numbers which have divisor i
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
for gcd in xrange(63, 0, -1):
    while cnts[gcd] >= 2:
        # remove A from table
        A = get_leftmost(table[gcd])
        rowA = get_divisors(input_data[A])
        for i in xrange(64):
            if rowA[i] == 1:
                table[i, A] = 0
                cnts[i] -= 1
        # remove B from table
        B = get_leftmost(table[gcd])
        rowB = get_divisors(input_data[B])
        for i in xrange(64):
            if rowB[i] == 1:
                table[i, B] = 0
                cnts[i] -= 1
        # Output A, B, G.C.D
        print A, B, gcd
