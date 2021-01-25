#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/** (2pts)
 * Create a program to print for i ranging from 0 to 31 the binary value for a
 * 1 shifted to position i, to be displayed in both binary and then decimal.
 * Prefix the values with the bit position.
 * Example output:
 *  0: 00000000000000000000000000000001 1
 *  1: 00000000000000000000000000000010 2
 *  2: 00000000000000000000000000000100 4
 * ...
 * 30: 01000000000000000000000000000000 1073741824
 * 31: 10000000000000000000000000000000 -2147483648
 */

int main(void)
{
    for(int i=0; i<32; i++){
        uint32_t n = 1;
        n = n<<i;
        printf("%2d: ",i);
        //print binary representation
        uint32_t mask = 1<<31;  //mask starting at 32nd bit to fill leading zeros
        while(mask){
            printf("%d",(mask & n) != 0);
            mask = mask>>1;
        }
        printf(" %d\n", n);
    }

  return 0;
}
