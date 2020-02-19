#!/usr/bin/env python3
import pyautogui
import random
import keyboard
import time

def WP_spammer(mesaj_sayisi):
    ekran = pyautogui.size()
    text_x = ekran[0]*(41/100)
    text_y = ekran[1]*(95/100)
    submit_x = ekran[0]*(85/100)
    submit_y = ekran[1]*(95/100)
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

        pyautogui.click(x=text_x,y=text_y,clicks=1,button='left')
        pyautogui.typewrite(randomstring)
        pyautogui.click(x=submit_x,y=submit_y,clicks=1,button='left')

def menu():
    print(" WhatsApp Spam Bot'a Hosgeldiniz! ", " Programin Calisma Bicimi: ", "   1-WhatsApp Web'e girin","   2-Mesaj atacaginiz kisi ile konusma paneline girin",
    "   3-Programi calistirin",sep="\n")
    giris = input("\nProgrami baslatayim mi?(e/h): ")
    if(giris=='e'):
        ms=int(input("Kac tane mesaj atmak istersiniz?:"))
        if(type(ms)!=int):
            raise ValueError("Hatali deger girdiniz!")
        else:
            print("Program basliyor... Cikmak icin 'q' ya basiniz.")
            time.sleep(2)
            WP_spammer(ms)
    
    elif(giris=='h'):
        print("Gorusuruz...")
    
    else:
        print("Gecersiz bir deger girdiniz! Lutfen tekrar deneyin!\n")
        menu()

menu()