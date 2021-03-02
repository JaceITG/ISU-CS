CS351 HW#5	10 Points

Create an X86_64 assembly program (h5.s) using the "p.c" C program as the basis
for your assembly code.  Consider converting the program line by line to
assembly.  Considering doing so in these steps:

1) Replace variable names with register names where applicable, not every
   variable can be a register

2) Define the string constants in the data section.

3) Convert each statement using the templates found in the asm.pdf

The lib.s and lib.h files are provided for you to use for the library
functions puts, putchar, and exit.  Use the make command to build your program.

Hints:
- The stat system call number is documented in /usr/include/asm/unistd_64.h

- A stat.c is provided to display the offsets for each parameter in the
  stat structure.

- The value of argc is at [rsp] (i.e. the first 64 bit value on the stack)

- The value of argv[1] is at [rsp+16]

