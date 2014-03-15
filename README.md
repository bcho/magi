magi
====

An 8 bits CPU implementation for my 计算机组成 course.


## Fetch Mode

Instruction:

```
Base Instruction:

 0                    7
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+

  op1   op2   Rsrc  Rdest

Immediate Instruction (optional):

8                    15
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+
```

1. A full instruction should be ready up to 2 cycles.
2. The maximum address is 2^8 - 1, so we can have 2^8 bytes.


## Instruction Structure

```
 0           4        7
+--+--+--+--+--+--+--+--+
|  |  |  |  |  |  |  |  |
+--+--+--+--+--+--+--+--+
 
 op1   op2  |  Rsrc  Rdest    $Immediate

opcode (4 bits)        address (4 bits)
```

### Instructions List

| name | sequence | example | explanation |
|:----:|:--------:|:-------:|:------------|
| halt | 0000 | halt; | Stop execution. |
| jmp | 0001 | jmp $imm; | PC <- $imm |
| movir | 0010 | movir %ax, $imm; | %ax <- $imm |
| movrr | 0011 | movrr %ax, %bx; | %ax <- %bx |
| movrm | 0100 | movrm %ax, (%bx); | mem[%bx] <- %ax |
| movmr | 0101 | movmr %ax, (%bx); | %ax <- mem[%bx] |
| movim | 0110 | movim %ax, $imm; | mem[$imm] <- %ax |
| movmi | 0111 | movmi %ax, $imm; | %ax <- mem[$imm] |
| add | 1000 | add %ax, %bx; | %ax <- %ax + %bx |
| sub | 1001 | sub %ax, %bx; | %ax <- %ax - %bx |
| and | 1010 | and %ax, %bx; | %ax <- %ax & %bx (bitwise) |
| or | 1011 | or %ax, %bx; | %ax <- %ax | %bx (bitwise) |
| je | 1100 | je %ax, $imm; | PC <- $imm if %ax == 0 |
| jne | 1100 | jne %ax, $imm; | PC <- $imm if %ax != 0 |
| jg | 1100 | jg %ax, $imm; | PC <- $imm if %ax > 0 |
| jl | 1100 | jl %ax, $imm; | PC <- $imm if %ax < 0 |


## Registers

### Programmer Viable:

| name | sequence |
|:----:|:--------:|
| %ax |  00      |
| %cx |  01      |
| %dx |  10      |
| %bx |  11      |


### Execute Status:

| name | explanation |
|:----:|:------------|
| PC   | Program Counter|
| ACC  | Accumulator |
| IR   | [Instruction Register][0] |


[ [0] Since the instruction may be 2 words size wide, so may be it's necessary to extend the IR. ]


## Data Path

(TODO)



## Notes

Instructions design was inspired by [Mannie's tutorial](http://minnie.tuhs.org/CompArch/Tutes/).
