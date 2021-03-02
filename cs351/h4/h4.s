%include "lib.h"
extern putchar, puts, exit


SECTION .data
    usage: db `Usage: h4 <file>\n`,0
    ferror: db `Unable to open file for reading.\n`,0

SECTION .bss
    _num: resb 1
    fd: resd 1
    r: resd 1
    i: resd 1
    mask: resd 1

SECTION .text

; print binary number stored in num as a string of spaces and #
printbinary:
    mov i, 7
    .loop:
        mov mask, 1
        shl mask, i
        test _num, mask
        jne .else
        mov al, '#'
        call putchar
        jmp .after

        .else:
        mov al, ' '
        call putchar

        .after:
        dec i
        cmp i, 0
        jge .loop



global _start
_start:

mov eax, [rsp]
cmp eax, 2
jge .cont
mov rsi, usage ; no args passed
call puts
call exit

.cont:
mov rax, SYS_open
mov rdi, [rsp+16]
mov rsi, O_RDONLY
syscall
mov fd, ah

cmp fd, 0
jge .loop
mov rsi, ferror ; unable to open file
call puts
call exit

.loop:
mov rax, SYS_read
mov rdi, fd
mov rsi, _num
mov rdx, 1
syscall ; read(fd, num, 1)

mov r, rax

cmp r, 1
jne .end ; exit loop
call printbinary
mov al, `\n`
call putchar
jmp .loop

.end:
mov rax, SYS_close
mov rdi, fd
syscall ; close(fd)
call exit
