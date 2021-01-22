#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program that takes a filename from the command line, opens it and
 * reads a sequence of 8 bit decimal numbers and prints them as "binary",
 * substituting # for 1 and a space for 0 instead.
 * Example input/output
 * ./p5 data/cs351
  ####  
 #    # 
#       
...
   #    
   #    
 #####  

 */

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: p5 <file>\n");
    exit(1);
  }
  

  return 0;
}
