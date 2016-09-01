'''
This file provides a proof of concept for the algorithm described in README.
'''

def get_divisors(num):
    # Implemented as ROM
    divisors = []
    for n in xrange(1, num+1, 1):
        if num % n == 0:
            divisors.append(n)
    return divisors

def build_table(input_data, table):
    # Execution Routine 1
    for index, num in enumerate(input_data):
        divisors = get_divisors(num)
        for divisor in divisors:
            table[divisor].append(index)

def remove_from_table(input_data, table, index):
    # Execution Routine 2
    divisors = get_divisors(input_data[index])
    for divisor in divisors:
        table[divisor].remove(index)

# Input data
input_data = [21, 8, 5, 21, 11, 12]
# Declaration
table = [[] for i in xrange(0, 64, 1)]
# Execution
build_table(input_data, table)
i = 63
while i > 0:
    if len(table[i]) >= 2:
        a = table[i][0]
        b = table[i][1]
        remove_from_table(input_data, table, a)
        remove_from_table(input_data, table, b)
        # Output data
        print a, b, i
    else:
        i -= 1
