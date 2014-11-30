# coding: utf-8

'''
    magi.machine
    ~~~~~~~~~~~~

    A simple virtual machine implement.
'''

from magi import const, utils
from magi.instruction import Instruction


class MachineRunError(RuntimeError):
    '''Machine runtime error.'''


class MachineHalt(StopIteration):
    '''Halt machine.'''


machine_state_tmpl = '''Machine State:

PC: 0x{m.pc:02x} ACC: 0x{m.acc:02x} IR: {m.instruction}

AX: 0x{m.ax:02x} BX: 0x{m.bx:02x}
CX: 0x{m.cx:02x} DX: 0x{m.dx:02x}

Memory:

{m.mem}
'''


class Machine(object):

    DS_SIZE = 1 << 8

    def __init__(self):
        # PC: points to current instruction.
        self.pc = None

        # ACC: stores last execution result.
        self.acc = None

        # Common usage registers.
        self.ax = None
        self.bx = None
        self.cx = None
        self.dx = None

        # Data storage.
        self.mem = None

        self.reset()

    def reset(self, bytecodes=None):
        '''Reset machine.

        :param bytecodes: instructions.
        '''

        # Reset registers.
        self.pc = 0
        self.acc = 0
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0

        # Reset data storage.
        self.mem = Mem(self.DS_SIZE)
        self.mem[0] = 0

        # Set instructions stream.
        self.bytecodes = bytecodes

    @property
    def ir(self):
        '''Current instruction.'''
        if not self.bytecodes or self.pc >= len(self.bytecodes):
            return None
        return self.bytecodes[self.pc]

    @property
    def instruction(self):
        '''Decoded instruction.'''
        ir = self.ir
        if ir is None:
            return None
        return Instruction.from_bytecode(ir)

    def get_instruction(self):
        '''Get an instruction and advance pc.'''
        instruction = self.instruction
        if instruction is None:
            raise MachineRunError('cannot get instruction')
        self.pc = self.pc + 1
        return instruction

    def get_immediate(self):
        '''Get bytecode as immediate value and advance pc.'''
        immediate = self.ir
        if immediate is None:
            raise MachineRunError('cannot get immediate')
        self.pc = self.pc + 1
        return immediate

    def get_register(self, register):
        '''Get register value.

        :param register: register to be loaded.
        '''
        if register == const.Registers.ax:
            return self.ax
        elif register == const.Registers.bx:
            return self.bx
        elif register == const.Registers.cx:
            return self.cx
        elif register == const.Registers.dx:
            return self.dx
        elif register == const.SPRegisters.PC:
            return self.pc
        elif register == const.SPRegisters.ACC:
            return self.pc
        elif register == const.SPRegisters.IR:
            return self.ir
        else:
            raise MachineRunError('unsupported register: {0}'.format(register))

    def update_register(self, register, value=None):
        '''Update an regiseter.

        :param register: register to be updated.
        :param value: new value, defaults to immediate value.
        '''
        if value is None:
            value = self.get_immediate()
        if not isinstance(value, int):
            raise MachineRunError('unsupported immediate value type')
        if register == const.Registers.ax:
            self.ax = value
        elif register == const.Registers.bx:
            self.bx = value
        elif register == const.Registers.cx:
            self.cx = value
        elif register == const.Registers.dx:
            self.dx = value
        elif register == const.SPRegisters.PC:
            self.pc = value
        elif register == const.SPRegisters.ACC:
            self.acc = value
        else:
            raise MachineRunError('unsupported register: {0}'.format(register))

    def run(self, bytecodes):
        '''Run list of bytecodes.

        :param bytecodes: Instruction bytecodes.
        '''
        self.reset(bytecodes)

        while True:
            try:
                self._executing_instrution = self.get_instruction()
                self._executing_instrution.execute(self)
            except MachineHalt:
                self.dump()
                return

    def halt(self):
        '''Halt the machine.'''
        raise MachineHalt

    def dump(self):
        '''Dump machine state.'''
        print(machine_state_tmpl.format(m=self))

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)


class Mem(list):
    '''Memory storage.'''

    def __init__(self, capacity):
        self.capacity = capacity
        for _ in range(self.capacity):
            self.append(0)

    def __str__(self):
        hex_format = lambda x: '0x{0:02x}'.format(x)
        return '\n'.join(
            [' '.join(map(hex_format, i)) for i in utils.chunks(self, 16)]
        )

    def __repr__(self):
        return self.__str__()
