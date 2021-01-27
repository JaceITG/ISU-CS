#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program that takes one or more integers from the command line,
 * each representing a bit position to set in an integer that is initially
 * zeroed.  Print the resulting integer as binary, hex (0 padded to 8 digits)
 * and decimal after all the bits have been set.
 * Example input/output:
 * ./p4 1 2 4 5 7 20
 * 00000000000100000000000010110110 001000B6 1048758
 */

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: p4 <integers>\n");
    exit(1);
  }

    uint32_t n = 0;
    for(int i=1; i<argc; i++){
        
    }


  return 0;
}
