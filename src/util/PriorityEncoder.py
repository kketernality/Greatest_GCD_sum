'''
This file makes use of `myhdl` to do RTL-level design.
'''

from myhdl import *

def PriorityEncoder(din, dout):
    @always_comb
    def logic():
        for i in reversed(xrange(len(din))):
            if din[i] == 1:
                dout.next = i
                break
        else:
            dout.next = 0

    return logic

if __name__ == '__main__':
    from random import randrange
    def testbench():
        din  = Signal(intbv(0)[64:])
        dout = Signal(intbv(0)[8:])

        testee = PriorityEncoder(din, dout)

        def get_leftmost(din):
            n = intbv(din)
            for i in reversed(xrange(64)):
                if n[i] == 1:
                    return i
            else:
                return 0

        @instance
        def tester():
            for t in xrange(100):
                num = randrange(2**randrange(64))
                din.next = num
                yield delay(1)
                print str(bin(num)).rjust(64,str(0)), dout
                assert dout == get_leftmost(num)

        return tester, testee

    sim = Simulation(testbench())
    sim.run()
