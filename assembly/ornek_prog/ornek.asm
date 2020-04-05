; Ornek program

; Birkac data belirleyelim
section .data
; Sabitleri belirleyelim

EXIT_DIYELIM equ 0      ; Basarili operasyon
SYS_cik      equ 60     ; Codu durdurmak icin cagir

; 8-bit (1 Byte) degisken tanimlamalari
bVar1   db 17
bVar2   db 9
bResult db 0

; 16-bit (1 Word) degisken tanimlamalari
wVar1   dw 17000
wVar2   dw 9000
wResult dw 0

; 32-bit (1 Double-word) degisken tanimlamalari
dVar1   dd 17000000
dVar2   dd 9000000
dResult dd 0

; 64-bit (Quad-word) degisken tanimlamalari
qVar1   dq 170000000
qVar2   dq 90000000
qResult dq 0

; Kod bolumu
section .text
global _start
_start:
;   Byte ornegi; bResult = bVar1 + bVar2
    mov al, byte[bVar1]
    add al, byte[bVar2]
    mov byte[bResult], al

;   Word ornegi; wResult = wVar1 + wVar2
    mov ax, word[wVar1]
    add ax, word[wVar2]
    mov word[wResult], ax

;   Double-word ornegi; dResult = dVar1 + dVar2
    mov eax, dword[dVar1]
    add eax, dword[dVar2]
    mov dword[dResult], eax

;   Quad-word ornegi; qResult = qVar1 + qVar2
    mov rax, qword[qVar1]
    add rax, qword[qVar2]
    mov qword[qResult], rax

;   Simdi programi durduralim.
last:
    mov rax, SYS_cik
    mov rdi, EXIT_DIYELIM
    syscall

