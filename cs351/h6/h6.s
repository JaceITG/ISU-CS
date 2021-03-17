%include "lib/lib.h"

extern printnum, putchar, exit

SECTION .text


; This function should print (rdx-1) * 4 number of spaces and return
indent:





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
