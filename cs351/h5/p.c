#include <stdio.h>
#include <sys/stat.h>
#include <stdlib.h>

void printperms(int n)
{
  if (n & 4) putchar('r');
  else putchar('-');
  if (n & 2) putchar('w');
  else putchar('-');
  if (n & 1) putchar('x');
  else putchar('-');
}

void file_type(int n)
{
  if (n == 1) printf("fifo\n");
  else if (n == 2) printf("char\n");
  else if (n == 4) printf("directory\n");
  else if (n == 6) printf("block\n");
  else if (n == 8) printf("regular\n");
  else if (n == 10) printf("link\n");
  else if (n == 12) printf("socket\n");
  else printf("unknown\n");
}

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: h5 <file>\n");
    exit(2);
  }

  struct stat st;

  if (stat(argv[1], &st) < 0) {
    printf("Unable to stat file.\n");
    exit(1);
  }

  printf("File: %s\n", argv[1]);
  printf("Type: ");
   file_type((st.st_mode >> 12) & 0xF);
  printf("Size: %d\n", st.st_size);
  printf("Owner: %d, Group: %d\n", st.st_uid, st.st_gid);
  printf("Perms: ");
   printperms((st.st_mode>>6) & 7);
   printperms((st.st_mode>>3) & 7);
   printperms(     st.st_mode & 7);
  putchar('\n');

  exit(0);
}
