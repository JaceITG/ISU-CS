#include <stdio.h>
#include <stdlib.h>

struct point {
  int x, y;
  struct point *next;
};

/** (3pts)
 * Complete this function that reads the same input as h2, but in the form
 * of a linked list.  A struct point structure should be allocated for each
 * pair of integers read.  The next pointer should point to the next (or
 * previous, depending on how you wish to implement it,) point structure.
 * The point structures do not need to be arranged in the same order as they
 * are read in as, which should make implementation easier.  The returned
 * value should be that head of the accumulated linked list of data points.
 */
struct point *get_data(FILE *fp)
{
    struct point* pts = calloc(10,sizeof(struct point));
    int max = 10;

    int x;
    int y;
    struct point *last;
    int n=0;
    while(fscanf(fp,"%d %d\n", &x, &y) != EOF){
        if(n>=max){
            max += 10;
            pts = realloc(pts, max*sizeof(struct point));
        }

        struct point newp;
        newp.x = x;
        newp.y = y;
        newp.next = last;
        pts[n] = newp;
        last = &newp;
        n++;
    }
    return &pts[n-1];
}

/**
 * Do not modify this part of the program.
 */
int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("Usage: h2 <filename>\n");
    return 0;
  }

  FILE *fp = fopen(argv[1], "r");
  if (fp == NULL) {
    perror("fopen");
    return 1;
  }

  int npoints = 0;
  struct point *data = get_data(fp);

  int xsum = 0, ysum = 0;
  while (data != NULL) {
    xsum += data->x;
    ysum += data->y;
    data = data->next;
  }
  printf("xsum = %d, ysum = %d\n", xsum, ysum);

  return 0;
}
