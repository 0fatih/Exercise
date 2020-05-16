"""
Oznitelik, bir fonksiyonu kullanirken '.' ile onun elemanlarini cagirmaktir. Nokta ile cagirilan her eleman
daha fazla islem yuku yaptiracaktir. O yuzden yapilmamasi gereken bazi islemler var:

import X --> Bir kutuphaneyi boyle cagirirsak, kullanacagimiz elemenlarini '.' ile cagirmak zorunda kaliriz.

Bu istemedigimiz bir sey oldugu icin:

from X import Somehing

Seklinde cagirma islemi yapmamiz bizi daha avantajli bir konuma getirir.
"""

# Yavas
import re
def slow_func():
    for i in range(10000):
        re.findall(regex, line) # Yavas!

# Hizli
from re import findall
def fast_func():
    for i in range(10000):
        findall(regex, line) # Daha hizli!
