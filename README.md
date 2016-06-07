# Greatest G.C.D sum
Final project for IC lab course of NCTU

64 numbers ranging from 0 to 63 are given as input. We need to pair these numbers into groups of two and calculate corresponding G.C.D(Greatest common divisor) for these groups. 32 G.C.Ds will be obtained after the calculation. At this project, we are asked to pair these numbers carefully so that the sum of these 32 G.C.Ds is maximized.

At file 'greatest_gcd_sum.py', I implemented the algorithm for this project. This algorithm makes use of a table to record all divisor from each number. Then at each step, we scan through the table and find the largest entry.    
