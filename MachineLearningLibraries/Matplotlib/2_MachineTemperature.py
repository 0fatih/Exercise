import matplotlib.pyplot as plt
import datetime

plt.axis('auto')
plt.title("Makine Sicaklik Takip Grafigi ",fontsize=14)
plt.xlabel("Saat", fontsize=12)
plt.ylabel("Sicaklik (C)", fontsize=12)
y1 = [120,122,124.5,126,126.4]
y2 = [100,102,103.5,104,105]
x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(len(y1))] 
plt.grid()
plt.plot(x, y1, 'sr')
plt.plot(x, y2, 'm*')
plt.legend(["Makine 1", "Makine 2"], loc=2)
plt.gcf().autofmt_xdate()
plt.show()
