#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define K	1024

/** (3pts)
 * Make a program that accepts two numbers from the command line, an integer
 * and a base.  Convert the first number to a string in the given base, then
 * output the string.  Base may range from 2 to 16.  You may use atoi(), but
 * you may not use %d,%x or %o in printf or sprintf to directly print any
 * numbers.
 * 
 * Example input/output:
 * ./p2 101 2
 * 1100101
 * ./p2 65535 16
 * FFFF
 */

int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Usage: p2 <integer> <base>\n");
    exit(1);
  }
  
  int num = atoi(argv[1]);
  int base = atoi(argv[2]);


  return 0;
}
