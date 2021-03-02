#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>

/** (10pts)
 * Create an X86_64 assembly program (h4.s) using this C program as the basis
 * for your assembly code.  Consider converting the program line by line to
 * assembly.  Considering doing so in these steps:
 * 1) Replace variable names with register names where applicable, not every
 *    variable can be a register (i.e. num below should be in memory)
 * 2) Define the string constants in the data section.
 * 3) Convert any for loops to while loops
 * 4) Convert each statement using the templates found in the asm.pdf
 *
 * ./h4 data/cs351
  ####  
 #    # 
#       
...
   #    
   #    
 #####  

 */

int bittest(uint32_t num, int32_t i)
{
  return num & (1<<i);
}

void printbinary(uint32_t num)
{
  for(int i=7; i >= 0; i--) {
    // Hint: bittest can probably mostly be replaced by the 'test' instruction:
    if (bittest(num, i)) putchar('#');
    else putchar(' ');
  }
}

int main(int argc, char *argv[])
{
  int32_t r, fd;
  uint8_t num;

  // Hint: argc is located in memory at rsp, value of argc is [rsp]:
  if (argc < 2) {
    puts("Usage: h4 <file>\n");
    exit(1);
  }

  // Hint: argv[1] is located in memory at [rsp+16]:
  fd = open(argv[1], O_RDONLY);
  if (fd < 0) {
    puts("Unable to open file for reading.\n");
    exit(1);
  }
  
  while(1) {
    r = read(fd, &num, sizeof(num));
    if (r != 1) break;

    printbinary(num);
    putchar('\n');
  }

  close(fd);
  exit(0);
}
