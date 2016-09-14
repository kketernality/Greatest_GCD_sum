'''
This file makes use of `myhdl` to do RTL-level design.
'''
from myhdl import *

def RAM(clk, addr, din, we, dout):
    '''
    A 0.5kB SRAM using 64x64 bits array
    '''
    mem = [Signal(intbv(0)[64:]) for i in range(64)]

    @always(clk.posedge)
    def write():
        if we:
            mem[int(addr)].next = din

    @always_comb
    def read():
        dout.next = mem[int(addr)]

    return write, read

if __name__ == '__main__':
    def testbench():
        # state_t = enum('IDLE','READING','WRITING')
        clk = Signal(bool(0))

        addr = Signal(intbv(0)[8:])
        din  = Signal(intbv(0)[64:])
        dout = Signal(intbv(0)[64:])
        we   = Signal(bool())

        testee = RAM(clk, addr, din, we, dout)

        # state = Signal(state.IDLE)

        @always(delay(1))
        def clkgen():
            clk.next = not clk

        @always(clk.posedge)
        def tester():
            pass

        return tester, testee, clkgen

    sim = Simulation(testbench())
    sim.run(1000)
