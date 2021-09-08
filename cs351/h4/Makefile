AS=nasm -felf64
LD=ld
CC=gcc

all: h4

h4: h4.o lib.o
	$(LD) -o h4 h4.o lib.o

h4.o: h4.s
	$(AS) h4.s

lib.o:	lib.s lib.h
	$(AS) lib.s

p:
	$(CC) -o p p.c

clean:
	rm -f *.o h4 p
