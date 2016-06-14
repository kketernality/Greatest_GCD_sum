# Greatest G.C.D sum
Final project for IC lab course of NCTU

### Spec and Requirements

64 numbers ranging from 0 to 63 are given as input. We need to pair these numbers into groups of two and calculate corresponding G.C.D(Greatest common divisor) for these groups. 32 G.C.Ds will be obtained after the calculation. At this project, we are asked to pair these numbers carefully so that the sum of these 32 G.C.Ds is maximized.

### Algorithm

In file 'greatest_gcd_sum.py', I have implemented and tested the algorithm for this project. 

This algorithm makes use of a central **table** to record all divisor given by the input numbers. This table contains 64 entries which stand for number 0~63(due to one of the constraints of this project, can be extended if needed), and each entry keeps a list of number which has it as its divisor. At the first step of this algorithm, we calculate the divisors for each input number and link them to corresponding entries in the table according to their divisors. After gathering the information from every input number and linking everything up, this table now can serve as a scoreboard and give us all the possible common divisor by seeking entries with 2 or more numbers linking to. 

For the next step, here I adopted the greedy strategy, that is, to find the largest entry with 2 or more numbers linking to and then casually choose two numbers linked by the divisor, then remove them and update the table accordingly. We will repeat the above step iteratively until every number has been removed from the table. Once this process has been done, we can get 32 pairs of numbers and their G.C.Ds. The final result can nicely approximate the real greatest sum of the G.C.Ds of these numbers and achieve linear time complexity in the same time. 

### Bitmap implementation

In file 'greatest_gcd_sum_bitmap.py', I adopted a hardware-friendly way to implement the algorithm for this project. This is bitmap-based implementation.
