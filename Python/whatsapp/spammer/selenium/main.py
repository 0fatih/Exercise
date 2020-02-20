from selenium import webdriver

def bot(target,msg,ms):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    input("Enter a button after QR code!")

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')

    for i in range(ms):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('hnQHL')
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        button.click()
def menu():
    print("""

           Welcome to WhatsApp Message Spammer 



    Coded by FFH
    """)
    target = input("Please enter a target: ")
    msg = input('Enter your message :')
    mesaj_sayisi = int(input("Counts of messages: "))
    bot(target,msg,mesaj_sayisi)


menu()
