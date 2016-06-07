# Greatest G.C.D sum
Final project for IC lab course of NCTU

64 numbers ranging from 0 to 63 are given as input. We need to pair these numbers into groups of two and calculate corresponding G.C.D(Greatest common divisor) for these groups. 32 G.C.Ds will be obtained after the calculation. At this project, we are asked to pair these numbers carefully so that the sum of these 32 G.C.Ds is maximized.

At file 'greatest_gcd_sum.py', I implemented the algorithm for this project. This algorithm makes use of a table to record all divisor derived from each number. After gathering the information of all divisor, this table now provide us all the possible common divisor by seeking the divisor with 2 or more numbers linking to. Here I adopt the greedy strategy, that is, finding the largest divisor with 2 or more numbers linking to and then remove two numbers linked by the divisor and update the table accordingly iteratively. Until every number has been removed from the table, we can get 32 pairs of number and its G.C.D. The result can approximite the real greatest sum of the G.C.D of these numbers and achieve linear time complexity in the same time. 
