section .data
    wNumA   dw  1200
    wNumB   dw  -2000
    wAns1   dw  0
    wAns2   dw  0

    dNumA   dd  42000
    dNumB   dd  -13000
    dAns1   dd  0
    dAns2   dd  0

    qNumA   dq  120000
    qNumB   dq  -230000
    qAns1   dq  0
    qAns2   dq  0

section .text
global _start
_start:
    ; wAns1 = wNumA * -13
    mov ax, word[wNumA]
    imul ax, -13                    ; Sonuc ax'de
    mov word[wAns1], ax

    ; wAns2 = wNumA * wNumB
    mov ax, word[wNumA]
    imul ax, word[wNumB]            ; Sonuc ax'de
    mov word[wAns2], ax

    ; dAns1 = dNumA * 113
    mov eax, dword[dNumA]
    imul eax, 113                   ; Sonuc eax'de
    mov dword[dAns1], eax

    ; dAns2 = dNumA * dNumB
    mov eax, dword[dNumA]
    imul eax, dword[dNumB]          ; Sonuc eax'de
    mov dword[dAns2], eax

    ; qAns1 = qNumA * 7096
    mov rax, qword[qNumA]
    imul rax, 7096
    mov qword[qAns1], rax

    ; qAns1 = qNumA * 7096'nin bir baska yolu
    mov rcx, qword[qNumA]
    imul rbx, rcx, 7096             ; Sonuc rbx'de
    mov qword[qAns1], rbx

    ; qAns2 = qNumA * qNumB
    mov rax, qword[qNumA]
    imul rax, qword[qNumB]          ; Sonuc rax'in icinde
    mov qword[qAns2], rax

last:
    mov rax, 60
    mov rdi, 0
    syscall
