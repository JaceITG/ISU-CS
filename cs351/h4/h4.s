%include "lib.h"
extern putchar, puts, exit


SECTION .data
    usage: db `Usage: h4 <file>\n`,0
    ferror: db `Unable to open file for reading.\n`,0

SECTION .bss
    _num: resb 1

SECTION .text

twopow:
    mov rax, r13 ; move i into rax
    mov rbx, 1 ; start at one
    cmp rax, 0 ; check i against 0
    jle .end ; exit if i is 0
    .loop:
        imul rbx, 2
        dec rax
        cmp rax,0
        jg .loop
    .end:
    ret

; print binary number stored in num as a string of spaces and #
printbinary:
    mov r13, 7
    .loop:
        call twopow
        test [_num], rbx
        je .else
        mov al, '#'
        call putchar
        jmp .after

        .else:
        mov al, ' '
        call putchar

        .after:
        dec r13
        cmp r13, 0
        jge .loop
    ret


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
mov r15, rax

cmp r15, 0
jge .loop
mov rsi, ferror ; unable to open file
call puts
call exit

.loop:
mov rax, SYS_read
mov rdi, r15
mov rsi, _num
mov rdx, 1
syscall ; read(fd, num, 1)

mov r14, rax

cmp r14, 1
jne .end ; exit loop
call printbinary
mov al, `\n`
call putchar
jmp .loop

.end:
mov rax, SYS_close
mov rdi, r15
syscall ; close(fd)
call exit
