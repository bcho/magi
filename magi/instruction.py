# coding: utf-8

'''
    magi.instruction
    ~~~~~~~~~~~~~~~~

    CPU instructions.
'''

from magi import const


class MalformatInstruction(ValueError):
    '''Unable to decode your instruction.'''


class OperationSet(object):

    # Operations.
    ops = {}

    @classmethod
    def add(cls, opcode, func):
        '''Add an operation implement.'''
        cls.ops[opcode] = func
        return cls

    @classmethod
    def has(cls, opcode):
        '''Do we have this operation?'''
        return opcode in cls.ops

    @classmethod
    def get(cls, opcode):
        '''Get an operation.'''
        return cls.ops[opcode]


class Instruction(object):

    def __init__(self, opcode, dest_register=None, src_register=None):
        if opcode not in const.OP or not OperationSet.has(opcode):
            raise MalformatInstruction('Unknown opcode: {0}'.format(opcode))
        if src_register and src_register not in const.Registers:
            raise MalformatInstruction(
                'Unknown register: {0}'.format(src_register)
            )
        if dest_register and dest_register not in const.Registers:
            raise MalformatInstruction(
                'Unknown register: {0}'.format(dest_register)
            )

        self.opcode = opcode
        self.src = src_register
        self.dest = dest_register

    def execute(self, machine):
        '''Execute instruction.

        :param machine: machine state.
        '''
        OperationSet.get(self.opcode)(self.src, self.dest, machine)

    @property
    def bytecode(self):
        return (const.FROM_OP(self.opcode)
                + const.FROM_SRC(self.src)
                + const.FROM_DEST(self.dest))

    def __str__(self):
        return '<Inst: {r.opcode}: {r.dest}, {r.src}>'.format(r=self)

    def __repr__(self):
        return self.__str__()

    @classmethod
    def from_bytecode(cls, bytecode):
        '''Decode an instruction from bytecode.

        :param bytecode: input bytecode.
        '''
        if not isinstance(bytecode, int):
            raise MalformatInstruction

        return Instruction(
            const.GET_OP(bytecode),
            const.GET_DEST(bytecode),
            const.GET_SRC(bytecode)
        )
