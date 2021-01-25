#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program that accepts an integer on the command line and prints the
 * number in hexadecimal followed by a count of the number of set (1) bits in
 * that integer.
 * Example input/output:
 * ./p1 1111
 * 00000457: 6
 */

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: p1 <integer>\n");
    exit(1);
  }

  //Find set bits
  int input = atoi(argv[1]);
  int n = input;
  int num_bits = 0;
  //while n has bits
  while(n!=0){
    num_bits += n&1;
    n = n>>1;
  }
  printf("%08x: %i\n",input, num_bits);

  return 0;
}
