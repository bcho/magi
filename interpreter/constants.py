# coding: utf-8

from enum import Enum


class OP(Enum):
    '''OP code'''

    halt = 0x0000
    jmp = 0x0001
    movir = 0x0010
    movrr = 0x0011

    movrm = 0x0100
    movmr = 0x0101
    movim = 0x0110
    movmi = 0x0111

    add = 0x1000
    sub = 0x1001
    and_ = 0x1010
    xor = 0x1011

    je = 0x1100
    jne = 0x1101
    jg = 0x1110
    jl = 0x1111


class Registers(Enum):
    '''Programmer viable registers.'''

    ax = 0x00
    cx = 0x01
    dx = 0x10
    bx = 0x11


class SPRegisters(Enum):
    '''Special purpose registers.'''

    PC = 0x00
    ACC = 0x01
    IR = 0x10
