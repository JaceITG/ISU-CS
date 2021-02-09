#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (3pts)
 * Create a program that takes two integers (a and b) from the command line
 * and multiplies them in binary, printing the result.  You may only use
 * binary operators &, |, ^, <<, >> and addition.
 * 
 * Example input/output:
 * ./p3 54 3
 * 162
 */

int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Usage: p3 <a> <b>\n");
    exit(1);
  }

  int n1 = atoi(argv[1]);
  int n2 = atoi(argv[2]);

  int neg = 0;
  if(n1<0){
    neg++;
    n1*=-1;
  }

  if(n2<0){
    neg++;
    n2*=-1;
  }

  int res = 0;
  int i = 0;

  while(n2>0){
    //if there is a 1 at this point in n2
    //add n1<<i to result
    if(n2&1) res += (n1<<i);

    //shift n2 over and increment counter
    n2 = n2>>1;
    i++;
  }
  if(neg==1){res*=-1;}
  printf("%d\n",res);

  return 0;
}
