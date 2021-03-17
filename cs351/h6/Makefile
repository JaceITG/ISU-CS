AS=nasm -g -F dwarf -felf64
LD=ld
CC=gcc

all: h6

h6: h6.o lib/lib.o
	$(LD) -o h6 h6.o lib/lib.o

h6.o: h6.s
	$(AS) h6.s

lib/lib.o: lib/lib.s
	make -C lib

clean:
	rm -f *.o h5 p
