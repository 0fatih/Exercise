import requests as r
import subprocess as sp
import time 

def sendClap():
    url = "https://alkislarlayasiyorum.com/actions/alkis"
    x = r.post(url)
    mp3text = '|<object height="0" widt="0" data="https://static.alkislarlayasiyorum/images/v3/sounds/alkis.mp3"></object>'
    resp = x.content.decode('utf-8').replace(mp3text,'')
    sp.call('clear',shell=True)
    print('Toplam',resp)
    
while 5:
    