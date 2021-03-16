%include "lib/lib.h"

extern puts, putchar, exit, printnum

SECTION .bss
    statbuf: resb 144

SECTION .data
    usage: db`Usage: h5 <file>\n`,0
    unable: db`Unable to stat file.\n`,0
    newl: db`\n`,0

SECTION .text

global _start
_start:
    mov r15, [rsp]
    cmp r15, 2
    jge .hasargs
    mov rsi, usage
    call puts
    mov rdi, 1
    call exit
    .hasargs:
    mov rax, 4
    mov rdi, [rsp+16]
    mov rsi, statbuf
    syscall
    cmp rax, 0
    jge .printfields
    mov rsi, unable
    call puts
    mov rdi, 1
    call exit

    .printfields:
    mov al, byte[statbuf+8]
    call printnum
    mov rsi, newl
    call puts
    .exit:
        mov rdi,0
        call exit
