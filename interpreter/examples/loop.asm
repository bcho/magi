start:
  movir   %ax, $0x1    # counter
  movir   %cx, $0xa    # upper bound
  xor     %bx, %bx     # make 0
loop:
  movrr   %dx, %cx
  sub     %dx, %ax
  je      %dx, stop    # test against upper bound
  movir   %dx, $0x1    # increase counter
  add     %bx, %ax
  jmp     loop
stop:
  halt
