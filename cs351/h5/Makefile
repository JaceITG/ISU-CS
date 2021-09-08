AS=nasm -felf64
LD=ld
CC=gcc

all: h5

h5: h5.o lib/lib.o
	$(LD) -o h5 h5.o lib/lib.o

h5.o: h5.s
	$(AS) h5.s

lib/lib.o: lib/lib.s
	make -C lib

p: p.c
	$(CC) -o p p.c

stat: stat.c
	$(CC) -o stat stat.c


clean:
	rm -f *.o h5 p
