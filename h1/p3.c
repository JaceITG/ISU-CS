#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program to get a integer from the command line and negate it
 * using only binary operations and increments (you can also use the addition
 * of +1).  Display both the original number and the negated number in binary
 * followed by the decimal value.
 * Example input/output:
 * ./p3 345
 * 00000000000000000000000101011001 345
 * 11111111111111111111111010100111 -345
 */

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: p3 <integer>\n");
    exit(1);
  }
  

  return 0;
}
