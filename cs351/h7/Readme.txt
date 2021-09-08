CS351 Assignment #7 (10 points)

Convert the malloc.c C file into the assembly file h7.s.  This program should
use the C standard library, thus it will need to be linked with gcc to make,
however consider using 'make' to build your program.

Requirements:
- You may not use any global state, except for string constants.  You should
  use local variables/storage defined in the functions stack frame for long
  term storage.


Hints:
- You will need to make a 'main' function, do not make a '_start' function.

- To access a C function, it should be declared as extern in your assembly
  file.  Read the man page on the function (found in section 3 of the man
  pages,) for more information on how the functions work and the parameters
  passed to them.

- "stdin" is an external FILE * pointer, i.e. it is a quad-word value that is
  an address.

- For best results, make sure your main function allocates a stack frame that
  is at least 16 bytes larger than it needs to be to hold the local variables.

- Local variables are defined relative to the base pointer (rbp), subtract
  from rbp

- With: char *buf, buf's value will be the address to an array of characters.

- With: char **ptrs, ptrs's value will be the address to an array of character
  pointers, each of which is the address to an array of characters.  In the
  call to reallocarray, ptrs is this value, not the address of ptrs.

