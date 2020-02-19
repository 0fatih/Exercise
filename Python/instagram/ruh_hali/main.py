# Kullanacağımız kütüphaneleri tanıtarak başlıyoruz.

# Bot için kullandığım kütüphaneler
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# Çıktı alma işlemi için kullandığım kütüphaneler
import matplotlib.pyplot as plt # Görselleştirme 
import time
# Emojileri barındıran kütüphanemiz
import emoji

def getComments(username,which_post):
    
    # Botun gideceği adresi tanıtıyoruz.
    url = "https://www.instagram.com/"+username
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

    links = []
    # Gidilen adresteki başlıkların genel olarak içinde bulunduğu adresi xpath olarak veriyoruz.
    for i in range(1,8):
        for s in range(1,4):
            obje = driver.find_element_by_xpath('//article[@class="FyNDV"]/div[1]/div/div['+str(i)+']/div['+str(s)+']/a')
            links.append(obje.get_attribute("href"))
    driver.get(links[which_post])
    does_it_continue=True
    while does_it_continue:
        try:            
            if driver.current_url != links[which_post]:
                driver.back()
            else:
                loadMoreButton = driver.find_element_by_xpath('//ul[@class ="k59kT"]/li[2]/button[@type="button"][.="Daha fazla yorum yükle"]')
                if loadMoreButton.is_enabled():
                    ActionChains(driver).move_to_element(loadMoreButton).click(loadMoreButton).perform()
                    time.sleep(3)
                else:
                    continue
        except:
            get_comments = driver.find_elements_by_xpath('//ul[@class ="k59kT"]/li/div/div/div')
            does_it_continue = False
    # Ardından bu adreste bulunan her bir başlığı bir stringe alıyoruz.
    for option in get_comments:
        print(option.find_element_by_xpath('span').text)
        headers.append(option.find_element_by_xpath('span').text)
    return headers

comments = []
comments = getComments("ahmtkural",0) # 10 yıl önceki başlıkları çekiyoruz.

len(comments)

def extract_emojis(str):
    return(''.join(c for c in str if c in emoji.UNICODE_EMOJI))

posEmoji = "😀😃😄😁😆😅😂🤣☺😊😇🙂🙃😉😌😍😘😗😙😚😋😛😝😜🤪💞🤩😏😭🤗💕❤️💙🧡💚💯👑❣️💖💫⭐🌟✨⚡🔥"
negEmoji = "😞😔😟😕🙁☹😣😖😫😩😢😓😪😭😤😠😡🤬🤯🤢🤮😷❌❗🤒🤕👹👺👻💀👽😾🖕🏿👎🏻👎🧟‍♂🧟‍♀"

posEmojiCount = 0
negEmojiCount = 0
notrCount = 0
for seciliEmoji in emojiler:
    if seciliEmoji in posEmoji:        
        posEmojiCount += 1
    elif seciliEmoji in negEmoji:
        negEmojiCount += 1
    else:
        notrCount += 1

labels = 'Pozitif Emojiler', 'Negatif Emojiler', 'Notr Emojiler' #pastadaki başlıkları tanımlıyoruz.
sizes = [posEmojiCount,negEmojiCount, notrCount ] #pastada gözükecek verileri tanımlıyoruz.
 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Instagram Sosyal Analizi") 
plt.savefig("analizCikti.png")
plt.show() #oluşturduğumuz pastayı çıktı alıyoruz.
