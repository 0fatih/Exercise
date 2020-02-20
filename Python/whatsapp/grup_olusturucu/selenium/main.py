from selenium import webdriver
import time


def menu():
    print("""

            Whatsapp Grup Olusturucuya Hosgeldiniz!



    -Coded by FFH
    """)
    
    hedef = input("Saldiracaganiz kisiyi girin :")
    grup_ismi = input("Gruplarin ismi :")
    grup_mesaj = input("Gruplara yazilacak mesaj :")
    grup_sayisi = int(input("Kac grup kurulsun :"))
    
    grup_olustur(hedef,grup_ismi,grup_mesaj,grup_sayisi)
    

def grup_olustur(hedef,grup_ismi,grup_mesaj,grup_sayisi):
    
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    input("QR Kodu okuttuktan sonra bir tusa basin!")
    
    for i in range(grup_sayisi):
        uc_nokta = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/div/span")
        uc_nokta.click()
        time.sleep(0.3)

        yeni_grup = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div")
        yeni_grup.click()
        time.sleep(1.2)
        
        isim_yeri = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
        isim_yeri.click()
        isim_yeri.send_keys(hedef)
        time.sleep(1.2)
        
        kisi = driver.find_element_by_class_name("_2WP9Q")
        kisi.click()
        time.sleep(1.2)
        
        ileri_butonu = driver.find_element_by_class_name("_1g8sv")
        ileri_butonu.click()
        time.sleep(1.2)
        
        grup_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')
        grup_name.click()                         
        grup_name.send_keys(grup_ismi)
        time.sleep(0.3)
        
        ok_butonu = driver.find_element_by_class_name("_1g8sv")
        ok_butonu.click()
        time.sleep(2)
        
        msg_box = driver.find_element_by_css_selector('._3u328')
        msg_box.send_keys(grup_mesaj)

        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        button.click()                          

        uc_nokta2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span")
        uc_nokta2.click()
        time.sleep(1.2)
        
        gruptan_cik = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div')
        gruptan_cik.click()
        time.sleep(1.2)
        
        cik_butonu = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
        cik_butonu.click()
        
        grup = driver.find_element_by_xpath('//*[@id="main"]/header')
        grup.click()
        time.sleep(1)
        
        grubu_sil = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[6]/div/div[2]/div/span')
        grubu_sil.click()
        time.sleep(1)
        
        sil_butonu = driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
        sil_butonu.click()
        
    driver.quit()

    
menu()
