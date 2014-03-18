# Interpreter


## Example:

```asm
start:
  movir   %ax, $0x1    # counter
  movir   %cx, $0xa    # upper bound
  xor     %bx, %bx     # make 0
loop:
  movrr   %dx, %cx
  sub     %dx, %ax
  je      %dx, stop    # test against upper bound
  add     %bx, %ax
  add     %ax, $0x1    # increase counter
  jmp     loop
stop:
  movrm   %bx, $0xf    # store at mem[0xf]
  halt
```

Run it:

```bash

$ interpreter loop.asm

Register Stats:

  PC: 0xdeadbeef    ACC: 0xdeadbeef   IR: 0x0

  %ax: 0xa  %bx: 0x37 %cx: 0x10 %dx: 0x1
```
