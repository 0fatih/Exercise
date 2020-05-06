section .tex:
	global _start						; Linker(ld) icin kullanmamiz gerekiyor

	_start:								; Linkerin baslangic adresi
		mov edx, len					; edx'e, .data bolumunde tanimladigimiz len degiskenini at
		mov ecx, msg					; yazilacak mesaj, .data'da belirlenir
		mov ebx, 1						; dosya aciklayicisi(stdout) ; ne oldugu hakkinda bir fikrim yok
		mov eax, 4						; sistem cagri numarasi(sys_write)
		int 0x80						; kernel'i cagir

		mov eax, 1						; sistem cagri numarasi (sys_exit)
		int 0x80						; kernel'i cagir

section .data
	msg db 'Hello, world!', 0xa			; yazilacak string
	len equ $ - msg 					; stringin uzunlugu