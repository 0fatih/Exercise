from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

#input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')

#msg_box = driver.find_element_by_class_name('_3FeAD _1PRhq')


for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('hnQHL')
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    button.click()
