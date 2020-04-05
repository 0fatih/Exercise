section .data

bNum1   db  42
bNum2   db  82
wAns    db  0
wAns1   db  0

wNum1   dw  4200
wNum2   dw  8200
dAns    dw  0

dNum1   dd  42000
dNum2   dd  82000
qAns    dd  0

section .text
    global _start
        _start:
        ; wAns = bNum1^2 veya bNum'in karesi
        mov al, byte[bNum1]
        mul al                          ; Sonuc ax'in icerisine gidiyor
        mov word[wAns], ax

        ; wAns1 = bNum1 * bNum2
        mov al, byte[bNum1]
        mul byte[bNum2]                 ; Sonuc ax'in icerisine gidiyor
        mov word[wAns1], ax

        ; dAns = wNum1 * wNum2
        mov ax, word[wNum1]
        mul word[dNum2]                 ; Sonuc dx:ax'in icerisine gidiyor
        mov word[dAns], ax
        mov word[dAns+2], dx
        
        ; qAns = dNum1 * dNum2
        mov eax, dword[dNum1]
        mul dword[dNum2]                ; Sonuc eax:edx'in icerisine gidiyor
        mov dword[qAns], eax
        mov dword[qAns+4], edx

    last:
        mov rax, 60
        mov rdi, 0
        syscall
