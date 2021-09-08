%include "lib/lib.h"

extern printnum, putchar, exit, puts

SECTION .bss
    num: equ 8

SECTION .data
    newl: db`\n`,0

SECTION .text


; This function should print (rdx-1) * 4 number of spaces and return
indent:
    mov r15, rdx
    imul r15, 4
    .loop:
        cmp r15, 0
        jle .done
        mov al, ' '
        call putchar
        dec r15
        jmp .loop
    .done:
    ret



; C "Pseudo-code" for this function:
; Takes its parameter in rdx, i.e.:
; stacklevel(rdx) {
;    num = rdx;
;    if (num >= 5) return;
;    rsp = rsp - (rdx*8);
;    indent(num);
;    printnum(rbp);
;    putchar('-');
;    printnum(rsp);
;    putchar('\n');
;    stacklevel(num+1);
;    return;
; }

stacklevel:
    enter 8, 0
    mov QWORD[rbp-num], rdx
    cmp QWORD[rbp-num], 5
    jl .prints
    mov rax, 1
    jmp .done

.prints:
    mov r14, QWORD[rbp-num]
    imul r14, 8
    sub rsp, r14
    call indent
    mov rax, rbp
    call printnum
    mov al, '-'
    call putchar
    mov rax, rsp
    call printnum
    mov al, `\n`
    call putchar
    inc QWORD[rbp-num]
    mov rdx, QWORD[rbp-num]
    call stacklevel

.done:
    leave
    ret


; Do not modify this function
; Example output:
;140720308464848-140720308464832
;    140720308464816-140720308464792
;        140720308464776-140720308464744
;            140720308464728-140720308464688

global _start
_start:
	mov	rdx, 1
	call	stacklevel

	mov	rdi, 0
	call	exit
