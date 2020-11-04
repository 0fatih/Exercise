import matplotlib.pyplot as plt

plt.axis([2009,2015,30,80])
plt.title("Turkiye'nin Tasima Sektorune Ait Sera Gazi Emisyon Degerleri")
plt.xlabel("Yillar")
plt.ylabel("Emisyon Degeri(bin Gg)")
plt.text(2009.7,47, "En Dusuk", color="Green", style="italic", weight="bold", size="7")
plt.text(2013.7,75, "En Dusuk", color="Green", style="italic", weight="bold", size="7")
plt.plot([2010,2011,2012,2013,2014],[45,47,62,68,73], 'r--')
"""

### Burada "r" red, "-" ise cubuk grafik olacagini belirtiyor. "

r = red
b = blue
g = green
...

. = nokta
o = yuvarlak
s = kare
^ = ^
- = cubuk grafik
-- = cizgili cubuk grafik
D = elmas
* = yildiz
p = besgen
"""
