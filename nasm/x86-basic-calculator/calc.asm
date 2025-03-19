section .data
    ; variables

input_func:
    ; take input
    mov eax, 0
    mov ebx, 0
    
    int 0x80

    sub esp, 8

    ; sum
    mov eax, esp
    add eax, esp + 4

    ;return value

section .text
    global _start
    

_start:




    ; Program exit boilerplate
	mov eax, 1 ; syscall num of sys_exit()
	xor ebx, ebx ; Exit code 0 success
	int 0x80 ; interrupt to make syscall bleh 

; take two numbers as input, return sum (for now)