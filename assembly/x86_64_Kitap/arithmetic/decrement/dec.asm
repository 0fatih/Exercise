section .data

bNum    db  254
wNum    dw  65000
dNum    dd  4200000000
qNum    dq  420000000000

section .text
    global _start
    _start:
        dec rax             ; rax = rax - 1
        dec byte[bNum]      ; bNum = bNum - 1
        dec word[wNum]      ; wNum = wNum - 1
        dec dword[dNum]     ; dNum = dNum - 1
        dec qword[qNum]     ; qNum = qNum - 1

    last:
        mov rax, 60
        mov rdi, 0
        syscall
