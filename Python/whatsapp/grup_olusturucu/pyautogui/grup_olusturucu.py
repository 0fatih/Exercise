import pyautogui
import time
import keyboard

def grup_olustur(hedef,mesaj):
    
    pyautogui.click(x=643,y=206,clicks=1,button="left") #Uc nokta
    time.sleep(0.3)
    pyautogui.click(x=583,y=254,clicks=1,button="left") #New group
    time.sleep(1)
    pyautogui.click(x=406,y=326,clicks=1,button="left") #Kisi arama
    pyautogui.typewrite(hedef)
    time.sleep(0.6)
    pyautogui.click(x=387,y=396,clicks=1,button="left") #Kisiye tikla
    
    pyautogui.click(x=466,y=1004,clicks=1,button="left") #Ileri butonu
    time.sleep(0.1)
    pyautogui.click(x=349,y=583,clicks=1,button="left") #Grup ismi
    pyautogui.typewrite(".")
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(x=377,y=406,clicks=1,button="left") #Chat menuden grup

    pyautogui.click(x=774,y=1030,clicks=1,button="left") #Yazi yazma yeri

    pyautogui.typewrite(mesaj)
    pyautogui.press('enter')
    pyautogui.click(x=774,y=189,clicks=1,button="left") #Grup isminin yeri
    time.sleep(1)
    pyautogui.click(x=1652,y=1031,clicks=1,button="left") #Cubugu asagi cek
    time.sleep(1)
    pyautogui.click(x=1379,y=912,clicks=1,button="left") #Exit group
    time.sleep(1)
    pyautogui.click(x=1092,y=648,clicks=1,button="left") #Exit onayla
    time.sleep(1)
    pyautogui.click(x=1389,y=987,clicks=1,button="left") #Delete group
    time.sleep(1)
    pyautogui.click(x=1075,y=647,clicks=1,button="left") #Delete group onayla
    time.sleep(1)
  
    

def menu():
    hedef = input("Saldiracaginiz kisinin ismini tamamen dogru sekilde girin:")
    grup_sayisi = int(input("Kac grup olusturmak istiyorsunuz?:"))
    mesaj = input("Mesajinizi girin:")
    for i in range(0,grup_sayisi):
        try:
            if(keyboard.is_pressed('q')):
                break
            else:
                pass
        finally:
            pass
        grup_olustur(hedef,mesaj)
    
    
menu()