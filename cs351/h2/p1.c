#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/** (4pts)
 * In this assignment you may not use atoi or strtol() or any other libc
 * function to convert a string to a number.
 * 
 * Make a program that implements an atoi like function, say ascii2int()
 * that takes a string and an integer base to convert the string to a number
 * of the given base, i.e. ascii2int("101",2) would convert 101 as a binary
 * number where ascii2int("101", 10) would convert 101 as a decimal number.
 * 
 * Your function should handle bases from 2 though 16 (it does not need to
 * error check this input.)  It should stop processing the string if the
 * character is not a valid digit in the given base.
 * 
 * The program should accept two strings, one the number to be converted
 * and a second base (always specified in decimal.)  Use the ascii2int()
 * function to covert both numbers and print the first number after
 * conversion.
 * 
 * Example input/output:
 * ./p1 101 2
 * 5
 * ./p1 101 10
 * 101
 * ./p1 101 16
 * 257
 */


int ascii2int(char* str, int base){
    int pow = 1;
    int res = 0;
    int length = strlen(str);

    //for each digit in string
    for(int i=length-1; i>=0; i--){
        //get value of digit
        int value = 0;
        if(str[i]>='0' && str[i]<='9'){value = str[i]-'0';}
        else if(str[i]>='a' && str[i]<='f'){value = str[i] - 'a' + 10;}
        else if(str[i]>='A' && str[i]<='F'){value = str[i] - 'A' + 10;}
        else{continue;}

        //add value to result, correcting for current power
        res += value*pow;
        //adjust power according to base
        pow *= base;
    }
    return res;
}

int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Usage: p1 <integer> <base>\n");
    return 0;
  }
  
  int base = ascii2int(argv[2], 10);

  printf("%d\n", ascii2int(argv[1], base));
  
  return 0;
}
