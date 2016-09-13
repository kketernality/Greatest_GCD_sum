'''
This file makes use of `myhdl` to do RTL-level design.
'''

from myhdl import *
from ROM import *
from RAM import *
from PriorityEncoder import *

state_t = enum('IDLE','INPUT','BUILD','TAKE','COMP')

def Clkgen(clk):
    @always(delay(1))
    def gener():
        clk.next = not clk

def Top():
    clk = Signal(bool(0))

    rom_addr = Signal(intbv(0)[8:])
    rom_dout = Signal(intbv(0)[64:])

    ram_we   = Signal(bool(0))
    ram_addr = Signal(intbv(0)[8:])
    ram_din  = Signal(intbv(0)[64:])
    ram_dout = Signal(intbv(0)[64:])

    pe_din  = Signal(intbv(0)[64:])
    pe_dout = Signal(intbv(0)[8:])

    cnts = [Signal(intbv(0)[8:]) for i in xrange(64)]

    inst_0 = Clkgen(clk)
    inst_1 = DivisorsROM(rom_addr, rom_dout)
    inst_2 = RAM(clk, ram_addr, ram_din, ram_we, ram_dout)
    inst_3 = PriorityEncoder(pe_din, pe_dout)

    state = Signal(state_t.IDLE)
    lp_cnt = Signal(intbv(0)[8:])

    @always(clk.posedge)
    def main():
        ''' Classical FSM '''
        if state == state_t.IDLE:
            pass
        elif state == state_t.INPUT:
            pass
        elif state == state_t.BUILD:
            pass
        elif state == state_t.TAKE:
            pass
        elif state == state_t.COMP:
            pass
        else:
            raise ValueError('Unknown state')

    return inst_0, inst_1, inst_2, inst_3, main
