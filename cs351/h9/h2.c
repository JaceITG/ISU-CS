#include <stdio.h>
#include <stdlib.h>

struct point {
  int x, y;
};

/** (3pts)
 * Complete this function that reads an input file, composed of two integers
 * per line.  Use fscanf() in a loop to read the input, stop when it fails to
 * read 2 integers.  The function should return an array of 'struct point'
 * each array element containing the two values read.  The array of structures
 * should be dynamically allocated in units of 10 elements.  Set the npoints
 * value to the number of read integer pairs.
 */
struct point *get_data(FILE *fp, int *npoints)
{
    struct point* pts = calloc(10,sizeof(struct point));
    int max = 10;

    int x;
    int y;
    while(fscanf(fp,"%d %d\n", &x, &y) != EOF){
        if(*npoints>=max){
            max += 10;
            pts = realloc(pts, max*sizeof(struct point));
        }

        struct point newp;
        newp.x = x;
        newp.y = y;
        pts[*npoints] = newp;
        *npoints += 1;
    }
    return pts;
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
  struct point *data = get_data(fp, &npoints);

  int xsum = 0, ysum = 0;
  for(int i=0; i < npoints; i++) {
    xsum += data[i].x;
    ysum += data[i].y;
  }
  printf("npoints = %d, xsum = %d, ysum = %d\n", npoints, xsum, ysum);

  return 0;
}
