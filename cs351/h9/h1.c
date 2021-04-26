#include <stdio.h>
#include <stdlib.h>

/** (4pts)
 * Complete this function. It should return the files data as a single null
 * character terminated array of characters. It should read the file one
 * character at a time while allocating (and re-allocating) space for the the
 * file in 100 byte increments.
 */

char *readfile(FILE *fp)
{
    char *content = malloc(100);
    int max = 100;
    int n = 0;
    char ch;
    while((ch=fgetc(fp)) != EOF){
        if(n>=max){
            max+=100;
            content = realloc(content,max);
        }

        content[n] = ch;
        n++;
    }
    return content;
}


/**
 * Do not modify this part of the program.
 */
int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: h1 <filename>\n");
    return 0;
  }
  
  FILE *fp = fopen(argv[1], "r");
  if (fp == NULL) {
    perror("fopen");
    return 1;
  }
  
  char *data = readfile(fp);
  printf("%s", data);

  return 0;
}
