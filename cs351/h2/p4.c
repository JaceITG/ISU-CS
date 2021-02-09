#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (3pts)
 * Make a program to divide two integers a by b in binary.  You may only use
 * the bitwise operations &, |, ^, <<, >> and addition and subtraction. The
 * program should print the result as well as the amount remaining after
 * division.
 * Hint: Don't try to divide negative numbers, convert them to positives and
 * keep track of how many were negative and if only one was, convert the result
 * to negative.
 * 
 * Example input/output:
 * ./p4 42 5
 * 8 R 2
 */

int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Usage: p4 <a> <b>\n");
    exit(1);
  }
  int negatives = 0;

  int dividend = atoi(argv[1]);
  if(dividend<0){
    dividend *= -1;
    negatives++;
  }

  int divisor = atoi(argv[2]);
  if(divisor<0){
    divisor *= -1;
    negatives++;
  }

  int quotient = 0;
  int remainder = dividend;

  while(remainder>=divisor){
    quotient++;
    remainder -= divisor;
  }
  if(negatives==1) {quotient*=-1;}
  printf("%d R %d\n", quotient, remainder);

  return 0;
}
