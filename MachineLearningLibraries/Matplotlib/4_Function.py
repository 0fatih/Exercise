import matplotlib.pyplot as plt
import numpy as np

# Fonksiyonlarin grafige dokumu
x = np.linspace(-5, 5, 1000) # x, -5 ile 5 arasindaki sayilardan olusan 1000 elemanli bir liste
y = (x**3) +4*x + 6 # Herhangi bir fonksiyon
plt.text(-2, 100, '$y=x^3+4*x+6$', fontsize=12, bbox={'facecolor':'blue','alpha':0.2})
plt.grid()
plt.plot(x, y)
