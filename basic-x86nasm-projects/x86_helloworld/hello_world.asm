section .data
	hello db "Hello World!", 0 ; db = define byte, var name = hello

section .text
	global _start


_start:
	mov eax, 4 ; syscall for sys_write = 4
	mov ebx, 1 ; stdout is 1
	mov ecx, hello ; our variable address
	mov edx, 12 ; length of the string = 12
	int 0x80 ; call interrupt to make the syscall

	; Program exit boilerplate
	mov eax, 1 ; syscall num of sys_exit()
	xor ebx, ebx ; Exit code 0 success
	int 0x80 ; interrupt to make syscall bleh 