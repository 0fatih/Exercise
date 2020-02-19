import pyautogui
import time
import random

def instagram_giris():
    username="5539074614"
    password="KontraktilKofUl51"
    pyautogui.click(x=350,y=113,button='left',clicks=2)
    pyautogui.press('backspace')
    pyautogui.typewrite('https://www.instagram.com/accounts/login/?source=auth_switcher')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=845,y=404,button='left')
    pyautogui.typewrite(username)
    pyautogui.click(x=840,y=448,button='left')
    pyautogui.typewrite(password)
    pyautogui.click(x=942,y=497,button='left')
    time.sleep(3)
    

def sikayet_et():
    username="arifalkan_"
    url = "https://www.instagram.com/"+username
    pyautogui.click(x=350,y=113,button='left',clicks=2)
    pyautogui.press('backspace')
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('tab',presses=5,interval=0.1)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.click(x=962,y=566,button='left')
    time.sleep(0.2)
    pyautogui.click(x=869,y=638,button='left')
    time.sleep(0.7)
    pyautogui.click(x=1216,y=529,button='left')
    time.sleep(0.2)
    pyautogui.click(x=1421,y=202,button='left')
    time.sleep(0.2)
    pyautogui.click(x=1104,y=314,button='left')
    time.sleep(0.2)
    pyautogui.click(x=961,y=762,button='left')
    time.sleep(1)
    
def instagram_kayit():
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
    username = ""
    email = ""
    name = ""
    password =""
    for i in range(0,17):
        username += random.choice(chars)
        email += random.choice(chars)
        name += random.choice(chars)
        password += random.choice(chars)
    
    email+="@hotmail.com"
    pyautogui.click(x=350,y=113,button='left',clicks=2)
    pyautogui.press('backspace')
    pyautogui.typewrite('https://www.instagram.com')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=1072,y=455,button='left')
    pyautogui.typewrite(email)
    pyautogui.click(x=1051,y=502,button='left')
    fullname = name[:7]+" "+name[7:]
    pyautogui.typewrite(fullname)
    pyautogui.click(x=1056,y=546,button='left')
    pyautogui.typewrite(username)
    pyautogui.click(x=1068,y=589,button='left')
    pyautogui.typewrite(password)
    pyautogui.click(x=1135,y=639,button='left')
    time.sleep(2)
    pyautogui.click(x=787,y=656,button='left')
    pyautogui.click(x=959,y=720,button='left')
    time.sleep(2)
    pyautogui.click(x=959,y=720,button='left')

    
def menu():
    print("*"*30)
    print("     Instagram Banner'a Hosgeldiniz      ")
    print("\n\ncoded by Fatih Furkan")
    print("\n","*"*30)
    username=input("Kullanici adini giriniz:")
    password=input("Sifrenizi giriniz:")
    sikayet=input("Sikayet edeceginiz kullanici adi:")
    instagram_giris(username,password)
    
    
instagram_kayit()