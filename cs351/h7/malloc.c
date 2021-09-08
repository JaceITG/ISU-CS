#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
  char *buf = malloc(1000);
  int max = 10;
  char **ptrs = calloc(max, sizeof(char *));
  
  int n = 0;

  while (fgets(buf, 1000, stdin) != NULL) {
    long len = strlen(buf);
    char *s = malloc(len + 1);
    strcpy(s, buf);

    if (n >= max) {
      max += 10;
      ptrs = reallocarray(ptrs, max, sizeof(char *));
    }

    ptrs[n] = s;
    n++;
  }

  for(int i=n-1; i >= 0; i--) {
    printf("%3d: %s", i, ptrs[i]);
  }
  return 0;
}
