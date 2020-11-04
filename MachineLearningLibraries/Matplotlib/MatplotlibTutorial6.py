import matplotlib.pyplot as plt
import numpy as np

# Histogram Grafigi
x = np.random.randint(40,100,80) # Rastgele puanlar icin bir liste
print(x)
plt.title("Puanlar")
plt.xlabel("Notlar")
plt.ylabel("Ogrenci Sayisi")
plt.axis([0,100, 0,15])
plt.grid(True)
n, bins, patches = plt.hist(x, bins=15, facecolor='blue', alpha=0.75)
