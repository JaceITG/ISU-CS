#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int offset(void *start, void *pos)
{
  return (int)(pos-start);
}

int main(void)
{
  struct stat st;

  printf("st           = %lX\n", &st);
  printf("sizeof(stat) = %d\n", sizeof(st));
  printf("st_dev       = %d / %d\n", offset(&st, &(st.st_dev    )), sizeof(st.st_dev    ));
  printf("st_ino       = %d / %d\n", offset(&st, &(st.st_ino    )), sizeof(st.st_ino    ));
  printf("st_mode      = %d / %d\n", offset(&st, &(st.st_mode   )), sizeof(st.st_mode   ));
  printf("st_nlink     = %d / %d\n", offset(&st, &(st.st_nlink  )), sizeof(st.st_nlink  ));
  printf("st_uid       = %d / %d\n", offset(&st, &(st.st_uid    )), sizeof(st.st_uid    ));
  printf("st_gid       = %d / %d\n", offset(&st, &(st.st_gid    )), sizeof(st.st_gid    ));
  printf("st_rdev      = %d / %d\n", offset(&st, &(st.st_rdev   )), sizeof(st.st_rdev   ));
  printf("st_size      = %d / %d\n", offset(&st, &(st.st_size   )), sizeof(st.st_size   ));
  printf("st_blksize   = %d / %d\n", offset(&st, &(st.st_blksize)), sizeof(st.st_blksize));
  printf("st_blocks    = %d / %d\n", offset(&st, &(st.st_blocks )), sizeof(st.st_blocks ));

  printf("File types:\n");
  printf("socket    = %d\n", S_IFSOCK >> 12);
  printf("sym link  = %d\n", S_IFLNK >> 12);
  printf("regular   = %d\n", S_IFREG >> 12);
  printf("block     = %d\n", S_IFBLK >> 12);
  printf("directory = %d\n", S_IFDIR >> 12);
  printf("char      = %d\n", S_IFCHR >> 12);
  printf("fifo      = %d\n", S_IFIFO >> 12);
  
  return 0;
}
