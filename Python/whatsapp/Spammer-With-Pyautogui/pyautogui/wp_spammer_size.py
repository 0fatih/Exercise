import pyautogui
import random
import keyboard
import time

def WP_spammer(mesaj_sayisi,mesaj):
    for i in range(mesaj_sayisi):
        characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        randomstring=""
    
        for j in range(0,24):
            randomstring+=random.choice(characters)
    
        try:
            if(keyboard.is_pressed('q')):
                break
            else:
                pass
        finally:
            pass

        pyautogui.click(x=790,y=1028,clicks=1,button='left')
        pyautogui.typewrite(mesaj)
        pyautogui.click(x=1629,y=1027,clicks=1,button='left')

def menu():
    print(" WhatsApp Spam Bot'a Hosgeldiniz! ", " Programin Calisma Bicimi: ", "   1-WhatsApp Web'e girin","   2-Mesaj atacaginiz kisi ile konusma paneline girin",
    "   3-Programi calistirin",sep="\n")
    giris = input("\nProgrami baslatayim mi?(e/h): ")
    if(giris=='e'):
        ms=int(input("Kac tane mesaj atmak istersiniz?:"))
        if(type(ms)!=int):
            raise ValueError("Hatali deger girdiniz!")
        else:
            mesaj = input("Ne yazmak istersiniz?")
            print("Program basliyor... Cikmak icin 'q' ya basiniz.")
            time.sleep(2)
            WP_spammer(ms,mesaj)
    
    elif(giris=='h'):
        print("Gorusuruz...")
    
    else:
        print("Gecersiz bir deger girdiniz! Lutfen tekrar deneyin!\n")
        menu()

menu()
