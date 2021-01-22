#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program that takes two integers from the command line and adds them
 * together using a binary ripple carry addition circuit.  You are not allowed to
 * use any addition or subtraction operations (you can use a loop with an
 * increment to iterate over the bits.)  Display the inputs and the resulting
 * output and if there is a carry out from the last bit.
 * Example input/output:
 * ./p6 42 723
 * 42 + 723 = 765 (carry out = 0)
 */

int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Usage: p6 <a> <b>\n");
    exit(1);
  }


  return 0;
}
