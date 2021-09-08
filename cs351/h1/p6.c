\
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

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

  uint32_t a = atoi(argv[1]);
  uint32_t b = atoi(argv[2]);

  uint32_t mask = 1;
  uint32_t result = 0;
  uint32_t carry = 0;

  while(mask < 1<<31){
    uint32_t abit = mask&a;
    uint32_t bbit = mask&b;
    result = result|(abit^bbit^carry);
    carry = (abit&bbit)|(abit&carry)|(bbit&carry);
    carry = carry<<1;

    mask = mask<<1;
  }
  if(carry>0) carry=1;
  printf("%d + %d = %d (carry out = %d)\n", a, b, result, carry);

  return 0;
}
