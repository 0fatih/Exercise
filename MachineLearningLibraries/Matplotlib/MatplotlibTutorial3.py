import matplotlib.pyplot as plt
import numpy as np

plt.axis("auto")
plt.title("Esik Deger Asimi", fontsize=14)
y = np.array([2,3,4,5,7,9,12,13,14,7,10,11,14,15,17])
x = np.arange(len(y))
plt.plot(x,y,color='black')
esik = 9
altEsik = y<esik
plt.scatter(x[altEsik], y[altEsik], color='black')
ustEsik = np.logical_not(altEsik)
plt.scatter(x[ustEsik], y[ustEsik], color='red')
plt.axhline(esik, color="red", linestyle="--")