AS=nasm -g -F dwarf -felf64
LD=ld
CC=gcc

h7: h7.o
	$(CC) -o h7 h7.o

h7.o: h7.s
	$(AS) h7.s

malloc: malloc.c
	$(CC) -o malloc malloc.c

clean:
	rm -f *.o h7 malloc

