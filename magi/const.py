# coding: utf-8

'''
    magi.const
    ~~~~~~~~~~

    Constant values.
'''

from enum import Enum


class OP(Enum):
    '''OP code'''

    halt = 0b0000
    jmp = 0b0001
    movir = 0b0010
    movrr = 0b0011

    movrm = 0b0100
    movmr = 0b0101
    movim = 0b0110
    movmi = 0b0111

    add = 0b1000
    sub = 0b1001
    and_ = 0b1010
    xor = 0b1011

    je = 0b1100
    jne = 0b1101
    jg = 0b1110
    jl = 0b1111


class Registers(Enum):
    '''Programmer viable registers.'''

    ax = 0b00
    cx = 0b01
    dx = 0b10
    bx = 0b11


class SPRegisters(Enum):
    '''Special purpose registers.'''

    PC = 0b00
    ACC = 0b01
    IR = 0b10


OP_MASK = (1 << 4) - 1
SRC_MASK = (1 << 2) - 1
DEST_MASK = (1 << 2) - 1

GET_OP = lambda x: OP((x >> 4) & OP_MASK)
GET_DEST = lambda x: Registers((x >> 2) & SRC_MASK)
GET_SRC = lambda x: Registers(x & DEST_MASK)

FROM_OP = lambda x: x.value << 4
FROM_DEST = lambda x: x.value << 2 if x is not None else 0
FROM_SRC = lambda x: x.value if x is not None else 0
