
extern stdin, malloc, calloc, reallocarray, fgets, printf, strlen, strcpy

SECTION .data
    frm: db`%3d: %s`,0
    ns: db`value n: %d\n`,0
SECTION .text
 buf: equ 40
 max: equ 8
 ptrs: equ 32
 n: equ 0
 s: equ 24
 len: equ 16
 i: equ 48
global main
main:
    enter 48, 0
    sub rsp, 1000

    mov rdi, 1000
    call malloc
    mov QWORD[rbp-buf], rax

    mov QWORD[rbp-max], 10
    mov rdi, QWORD[rbp-max]
    mov rsi, 8
    call calloc
    mov QWORD[rbp-ptrs], rax

    mov QWORD[rbp-n], 0
    
    .while:
    mov rax, 0
    mov rdi, QWORD[rbp-buf]
    mov rsi,1000
    mov rdx, QWORD[stdin]
    call fgets

    cmp rax,0
    je .print ; check for null

    mov rdi,QWORD[rbp-buf]
    call strlen
    mov QWORD[rbp-len], rax ; long len = strlen(buf)

    mov rdi, QWORD[rbp-len]
    inc rdi
    call malloc
    mov QWORD[rbp-s], rax ; char *s = malloc(len-1)

    mov rdi, QWORD[rbp-s]
    mov rsi, QWORD[rbp-buf]
    call strcpy ; strcpy(s, buf)

    mov r15, QWORD[rbp-n]
    mov r14, QWORD[rbp-max]
    cmp r15, r14 
    jl .norealloc ; if(n>=max)

    add QWORD[rbp-max], 10

    mov rdi, QWORD[rbp-ptrs]
    mov rsi, QWORD[rbp-max]
    mov rdx, 8
    call reallocarray
    mov QWORD[rbp-ptrs], rax

    .norealloc:
    mov r15, QWORD[rbp-n]
    imul r15, 8
    mov r14, QWORD[rbp-s]
    mov QWORD[rbp-ptrs+r15], r14
    inc QWORD[rbp-n]

    jmp .while

    .print:

    mov r14, QWORD[rbp-n]
    mov QWORD[rbp-i], r14
    dec QWORD[rbp-i]
   .for:
    cmp QWORD[rbp-i], 0
    jl .leave

    mov rax, 0
    mov rdi, frm
    mov rsi, QWORD[rbp-i]
    mov r15, QWORD[rbp-i]
    imul r15, 8
    mov rdx, QWORD[rbp-ptrs+r15]
    call printf
    dec QWORD[rbp-i]
    jmp .for
    .leave:
    leave
    mov rax,0
    ret
