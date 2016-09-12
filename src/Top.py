'''
This file makes use of `myhdl` to do RTL-level design.
'''

from myhdl import *
from ROM import *
from RAM import *

state_t = enum('Complete','Phase1','Phase2')

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

    inst_0 = Clkgen(clk)
    inst_1 = Divisors_ROM(rom_addr, rom_dout)
    inst_3 = RAM(clk, ram_addr, ram_din, ram_we, ram_dout)
