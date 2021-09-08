%include "lib.h"

; To compile: nasm -felf64 lib.s

; Exports the following "symbols" (an address for something) so that our program
; in a different file can access them:
GLOBAL strlen, puts, putchar, getchar, exit, getrandom

SEGMENT .bss
      _ch: resb 1
  _rndbuf: resb 8


SEGMENT .text

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
getchar:
	mov	rax, SYS_read
	mov	rdi, STDIN_FILENO
	mov	rsi, _ch
	mov	rdx, 1
	syscall
	mov	al, BYTE [_ch]
	ret

; character to print is in al
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
