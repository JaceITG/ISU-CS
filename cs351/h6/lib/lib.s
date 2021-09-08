%include "lib.h"

; To compile: nasm -felf64 lib.s

; Exports the following "symbols" (an address for something) so that our program
; in a different file can access them:
GLOBAL printnum, strlen, puts, putchar, getchar, exit, getrandom, memcpy, strchr
GLOBAL flush

SEGMENT .bss
      _ch: resb 1
  _rndbuf: resb 8

SEGMENT .text

; Print number in rax
printnum:
	enter	32, 0
	lea	rsi, [rbp-1]
	mov	BYTE [rsi], 0		; (*rsi) = '\0';

	mov	r8, 10			; r8 = 10;    // The base for our numbers
	mov	r9, 0			; r9 = false; // negative flag
	cmp	rax, 0			; if (rax < 0) {
	jge	.loop
	neg	rax			;   rax = -rax;
	mov	r9, 1			;   neg = true;
					; }

.loop:					; do {
	cqo
	div	r8			;   rax = rax / 10;  rdx = rax % 10
	add	dl, '0'			;   rdx += '0';
	dec	rsi			;   --rsi;
	mov	BYTE [rsi], dl		;   *rsi = dl;
	
	cmp	rax, 0
	jne	.loop			; } while (rax > 0);

	cmp	r9, 1			; if (r9 == true) {
	jne	.skipneg
	dec	rsi			;    --rsi;
	mov	BYTE [rsi], '-'		;    *rsi = '-';
					; }
.skipneg:
	call	puts			; puts(rsi);
	leave
	ret				; return;

; string in register rsi (haystack), character to search for in al (needle)
; leaves address of character in rsi, or sets rsi to 0 if not found
strchr:
	cmp BYTE [rsi], 0
	je .failed
	
	cmp BYTE [rsi], al
	je .found
	
	inc rsi
	jmp strchr

.failed:
	mov rsi, 0
.found:
	ret


; memcpy(dst = rdi, src = rsi, size = rcx);
memcpy:
	cld			; clear direction -> move data from low to high
.loop:
	movsb
	loop	.loop
	ret


; return in rax 64 bits of randomness
getrandom:
	mov	rax, SYS_getrandom
	mov	rdi, _rndbuf
	mov	rsi, 8
	mov	rdx, GRND_NONBLOCK
	syscall
	mov	rax, [_rndbuf]
	ret


; Take the string address in the register rsi
; Set the length in the register rdx
strlen:
	mov	rdx, 0			;  rdx = 0;
.while:
	cmp	BYTE [rsi+rdx], 0	;  while(rsi[rdx] != 0) {
	je	.done
	inc	rdx			;     rdx++
	jmp	.while			;  }

.done:
	ret				;  return


; Prints the string pointed to by rsi:
puts:
	; write(STDOUT_FILENO, mesg, 14);
	mov	rax, SYS_write
	mov	rdi, STDOUT_FILENO
	call	strlen
	syscall
	ret

; gets a character from stdin and stores in al
; read(STDIN_FILENO, &_ch, 1);
; al = _ch or -1 on EOF:
getchar:
	mov	rax, SYS_read
	mov	rdi, STDIN_FILENO
	mov	rsi, _ch
	mov	rdx, 1
	syscall
	cmp	rax, 0
	jle	.eof
	mov	al, BYTE [_ch]
	ret
.eof:
	mov	rax, -1
	ret

flush:
	call	getchar
	cmp	al, -1
	je	.finish
	cmp	al, `\n`
	je	.finish
	jmp	flush
.finish:
	ret

; character to print is in al
; _ch = al;
; write(STDOUT_FILENO, &_ch, 1);
putchar:
	mov	[_ch], al
	mov	rax, SYS_write
	mov	rdi, STDOUT_FILENO
	mov	rsi, _ch
	mov	rdx, 1
	syscall
	ret

; Exit value in rdi:
exit:
	mov	rax, SYS_exit
	syscall
	ret
