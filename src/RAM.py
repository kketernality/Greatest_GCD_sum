'''
This file makes use of `myhdl` to do RTL-level design.
'''

def RAM(clk, addr, din, we, dout):
    '''
    A 0.5kB SRAM consisted of 64x64 bits array
    '''
    mem = [Signal(intbv(0)[64:]) for i in range(64)]

    @always(clk.posedge)
    def write():
        if we:
            mem[int(addr)].next = din

    @always(clk.posedge)
    def read():
        dout.next = mem[int(addr)]

    return write, read
