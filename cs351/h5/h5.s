%include "lib/lib.h"

extern puts, putchar, exit, printnum

SECTION .bss
    statbuf: resb 144

SECTION .data
    usage: db`Usage: h5 <file>\n`,0
    unable: db`Unable to stat file.\n`,0
    newl: db`\n`,0
    file: db`File: `,0
    type: db`Type: `,0
    size: db`Size: `,0
    fi: db`fifo\n`,0
    cha: db`char\n`,0
    dir: db`directory\n`,0
    block: db`block\n`,0
    reg: db`regular\n`,0
    link: db`link\n`,0
    sock: db`socket\n`,0
    unk: db`unknown\n`,0

    own: db`Owner: `,0
    group: db`, Group: `,0
    perm: db`Perms: `,0

SECTION .text

; print perms for value n stored in r14d
perms:
    mov r13d, r14d
    test r13d, 4
    jz .not4
    mov al, 'r'
    call putchar
    jmp .2
    .not4:
    ;put -
    mov al, '-'
    call putchar

    .2:
    mov r13d, r14d
    test r13d, 2
    jz .not2
    mov al, 'w'
    call putchar
    jmp .1

    .not2:
    ;put -
    mov al, '-'
    call putchar

    .1:
    mov r13d, r14d
    test r13d, 1
    jz .not1
    mov al, 'x'
    call putchar
    jmp .done

    .not1:
    ;put -
    mov al, '-'
    call putchar

    .done:
    ret
; print associated file type for st_mode>>12 & 16 in r15d
file_type:
    .1:
    cmp r15d, 1
    jne .2
    mov rsi, fi
    call puts
    jmp .end_type
    .2:
    cmp r15d, 2
    jne .4
    mov rsi, cha
    call puts
    jmp .end_type
    .4:
    cmp r15d, 4
    jne .6
    mov rsi, dir
    call puts
    jmp .end_type
    .6:
    cmp r15d, 6
    jne .8
    mov rsi, block
    call puts
    jmp .end_type
    .8:
    cmp r15d, 8
    jne .10
    mov rsi, reg
    call puts
    jmp .end_type
    .10:
    cmp r15d, 10
    jne .12
    mov rsi, link
    call puts
    jmp .end_type
    .12:
    cmp r15d, 12
    jne .not
    mov rsi, sock
    call puts
    jmp .end_type
    .not:
    mov rsi, unk
    call puts
    .end_type:
    ret

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
    ;File: %s\n
    mov rsi, file
    call puts
    mov rsi, [rsp+16]
    call puts
    mov rsi, newl
    call puts

    ; Type: 
    mov rsi, type
    call puts
    mov r15d, DWORD[statbuf+24]
    sar r15d, 12
    and r15d, 0xF
    call file_type

    ; Size: %d\n
    mov rsi, size
    call puts
    mov rax, [statbuf+48]
    call printnum
    mov rsi, newl
    call puts

    ; Owner: %d, Group: %d\n
    mov rsi, own
    call puts
    mov eax, DWORD[statbuf+28]
    call printnum
    mov rsi, group
    call puts
    mov eax, DWORD[statbuf+32]
    call printnum
    mov rsi, newl
    call puts

    ; Perms:
    mov rsi, perm
    call puts
    ; first perms
    mov r14d, DWORD[statbuf+24]
    sar r14d, 6
    and r14d, 7
    call perms

    ; second perms
    mov r14d, DWORD[statbuf+24]
    sar r14d, 3
    and r14d, 7
    call perms

    ; third perms
    mov r14d, DWORD[statbuf+24]
    and r14d, 7
    call perms

    mov rsi, newl
    call puts
    .exit:
        mov rdi,0
        call exit
