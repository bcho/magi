# coding: utf-8

from magi.machine import Machine
from magi.instruction import Instruction, OperationSet
from magi import const, inst_impl


OperationSet.add(const.OP.halt, inst_impl.inst_halt)
OperationSet.add(const.OP.jmp, inst_impl.inst_jmp)
OperationSet.add(const.OP.movir, inst_impl.inst_movir)
OperationSet.add(const.OP.movrr, inst_impl.inst_movrr)
OperationSet.add(const.OP.movrm, inst_impl.inst_movrm)
OperationSet.add(const.OP.movmr, inst_impl.inst_movrm)
OperationSet.add(const.OP.movim, inst_impl.inst_movim)
OperationSet.add(const.OP.movmi, inst_impl.inst_movmi)
OperationSet.add(const.OP.add, inst_impl.inst_add)
OperationSet.add(const.OP.sub, inst_impl.inst_sub)
OperationSet.add(const.OP.and_, inst_impl.inst_and)
OperationSet.add(const.OP.xor, inst_impl.inst_xor)
OperationSet.add(const.OP.je, inst_impl.inst_je)
OperationSet.add(const.OP.jne, inst_impl.inst_jne)
OperationSet.add(const.OP.jg, inst_impl.inst_jg)
OperationSet.add(const.OP.jl, inst_impl.inst_jl)


r = const.Registers

m = Machine()
# bx should be 45 (0x2d)
m.run([
    # start:
    Instruction(const.OP.movir, r.ax).bytecode,
    0x01,
    Instruction(const.OP.movir, r.cx).bytecode,
    0x0a,
    Instruction(const.OP.xor, r.bx, r.bx).bytecode,

    # loop:
    Instruction(const.OP.movrr, r.dx, r.cx).bytecode,
    Instruction(const.OP.sub, r.dx, r.ax).bytecode,
    Instruction(const.OP.je, src_register=r.dx).bytecode,
    0x0f,  # stop
    Instruction(const.OP.add, r.bx, r.ax).bytecode,
    Instruction(const.OP.movir, r.dx).bytecode,
    0x01,
    Instruction(const.OP.add, r.ax, r.dx).bytecode,
    Instruction(const.OP.jmp).bytecode,
    0x05,  # loop

    # stop:
    Instruction(const.OP.movrm, r.bx).bytecode,
    0x0f,
    Instruction(const.OP.halt).bytecode
])
