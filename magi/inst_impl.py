# coding: utf-8

'''
    magi.inst_impl
    ~~~~~~~~~~~~~~

    Instructions implements.
'''

from magi import const


def inst_halt(src, dest, machine):
    machine.halt()


def inst_jmp(src, dest, machine):
    machine.update_register(const.SPRegisters.PC)


def inst_movir(src, dest, machine):
    machine.update_register(dest)


def inst_movrr(src, dest, machine):
    machine.update_register(dest, machine.get_register(src))


def inst_movrm(src, dest, machine):
    machine.mem[machine.get_register(dest)] = machine.get_register(src)


def inst_movmr(src, dest, machine):
    machine.update_register(machine.mem[machine.get_register(dest)])


def inst_movim(src, dest, machine):
    machine.mem[machine.get_immediate()] = machine.get_register(src)


def inst_movmi(src, dest, machine):
    machine.update_register(machine.mem[machine.get_immediate()])


def inst_add(src, dest, machine):
    nv = machine.get_register(dest) + machine.get_register(src)
    machine.update_register(dest, nv)


def inst_sub(src, dest, machine):
    nv = machine.get_register(dest) - machine.get_register(src)
    machine.update_register(dest, nv)


def inst_and(src, dest, machine):
    nv = machine.get_register(dest) & machine.get_register(src)
    machine.update_register(dest, nv)


def inst_xor(src, dest, machine):
    nv = machine.get_register(dest) ^ machine.get_register(src)
    machine.update_register(dest, nv)


def inst_je(src, dest, machine):
    target = machine.get_immediate()
    if machine.get_register(src) == 0:
        machine.update_register(const.SPRegisters.PC, target)


def inst_jne(src, dest, machine):
    target = machine.get_immediate()
    if machine.get_register(src) != 0:
        machine.update_register(const.SPRegisters.PC, target)


def inst_jg(src, dest, machine):
    target = machine.get_immediate()
    if machine.get_register(src) > 0:
        machine.update_register(const.SPRegisters.PC, target)


def inst_jl(src, dest, machine):
    target = machine.get_immediate()
    if machine.get_register(src) < 0:
        machine.update_register(const.SPRegisters.PC, target)
