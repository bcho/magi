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
