section .data
    bNum    db 42
    wNum    dw 4321
    dNum    dd 42000
    qNum    dq 42000000

section .text
    global _start
    _start:
        inc rax             ; rax registerindaki degeri 1 arttirir
        inc byte[bNum]      ; bNum += 1
        inc word[wNum]      ; wNum += 1
        inc dword[dNum]     ; dNum += 1
        inc qword[qNum]     ; qNum += 1
        
        ; Veri türlerinin ve büyüklüklerinin gerçekleştirilen işlemler için uygun olmasını sağlamak programcının sorumluluğundadır.

    last:
        mov rax, 60
        mov rdi, 0
        syscall
