import numpy as np

# Tek boyutlu dizi olusturma
tekBoyutluDizi = np.array([2,3,4])
print(f"Tek boyutlu dizi:\n{tekBoyutluDizi}\n")

# Iki boyutlu dizi olusturma
ikiBoyutluDizi = np.array([[2,3,4],
                           [5,6,7]])
print(f"Iki boyutlu dizi:\n{ikiBoyutluDizi}\n")

# Uc boyutlu dizi olusturma
ucBoyutluDizi = np.array([[[1,2,3]],
                          [[4,5,6]],
                          [[7,8,9]]])
print(f"Uc boyutlu dizi:\n{ucBoyutluDizi}\n")

# Sadece birlerden olusan bir boyutlu dizi olusturma
sadeceBirler = np.ones(5)
print(f"Sadece birlerden olusan 1D 4'luk dizi:\n{sadeceBirler}\n")

# Sadece birlerden olusan iki boyutlu 3x4'luk dizi olusturma
sadeceBirler2 = np.ones((3,4))
print(f"Sadece birlerden olusan 2D 3x4'luk dizi:\n{sadeceBirler2}\n")

# Sadece birlerden olusan uc boyutlu 3x4'luk dizi olusturma
sadeceBirler3 = np.ones((3,3,4))
print(f"Sadece birlerden olusan 3D 3x4'luk dizi:\n{sadeceBirler3}\n")

# Sadece sifirlardan olusan bir boyutlu dizi olusturma
sadeceSifirlar = np.ones(5)
print(f"Sadece sifirlardan olusan 1D 4'luk dizi:\n{sadeceSifirlar}\n")

# Sadece sifirlardan olusan iki boyutlu 3x4'luk dizi olusturma
sadeceSifirlar2 = np.ones((3,4))
print(f"Sadece sifirlardan olusan 2D 3x4'luk dizi:\n{sadeceSifirlar2}\n")

# Sadece sifirlardan olusan uc boyutlu 3x4'luk dizi olusturma
sadeceSifirlar3 = np.ones((3,3,4))
print(f"Sadece sifirlardan olusan 3D 3x4'luk dizi:\n{sadeceSifirlar3}\n")

# Full fonksiyonu kullanarak dizi olusturma
fullDizi = np.full((3,3), "Fatih")
print(f"Full fonksiyonu kullanarak dizi olusturma:\n{fullDizi}\n")

# Arange fonksiyonu ile dizi olusturma
arangeDizi = np.arange(0,1,0.2) # arange(start, stop, steps)
print(f"Arange fonksiyonu ile dizi olusturma:\n{arangeDizi}\n")

# Linspace fonksiyonu ile dizi olusturma
linspaceDizi = np.linspace(0.0,1.0,num=5)
print(f"Linspace fonksiyonu ile dizi olusturma:\n{linspaceDizi}\n")

# Linspace fonksiyonu ile dizi olustururken stop degerini de dahil etmeme
linspaceDizi2 = np.linspace(0.0,1.0,num=5,endpoint=False)
print(f"Linspace fonksiyonu ile dizi olustururken stop degerini de dahil etmeme:\n{linspaceDizi2}\n")

# Rastgele float degerlerden dizi olusturma
randomDizi = np.random.rand(3,3)
print(f"Rastgele float degerlerden olusan dizi:\n{randomDizi}\n")

# Rastgele integer degerlerden dizi olusturma
randomDizi2 = np.random.randint(0,10, size=(3,3))
print(f"Rastgele integer degerlerden (0-10 arasi) olusan dizi:\n{randomDizi2}\n")

# Numpy dizilerinde aritmetik islemler
dizi1 = np.array([1,2,3,4])
dizi2 = np.array([5,6,7,8])
print(f"Dizi1 = {dizi1} ve Dizi2 = {dizi2} 'nin toplami:\n{dizi1+dizi2}\n")
print(f"Dizi1 = {dizi1} ve Dizi2 = {dizi2} 'nin farki:\n{dizi1-dizi2}\n")
print(f"Dizi1 = {dizi1} ve Dizi2 = {dizi2} 'nin bolumu:\n{dizi1/dizi2}\n")
print(f"Dizi1 = {dizi1} ve Dizi2 = {dizi2} 'nin ussu:\n{dizi1**dizi2}\n")

# Numpy temel matematik ve istatistik fonksiyonlari
dizi = np.random.randint(0,25, size=(3,2))
for i in (dizi.min, dizi.max, dizi.sum, dizi.prod, dizi.std, dizi.var):
    print(i.__name__, "=", i())

# !ONEMLI: Numpy'da bir diziyi kopyaladigimizda ya da esitledigimizde o diziler birbirine baglanir
diziKopyala1 = np.array([2,3,4,5,6])
diziKopyala2 = diziKopyala1[0:3]
print(f"\nDizilerin ilk hali, 1. dizi: {diziKopyala1} , 2. dizi: {diziKopyala2}")
diziKopyala2[0] = 100
print(f"Degisim sonrasi,    1. dizi: {diziKopyala1} , 2. dizi: {diziKopyala2}")
diziKopyala2 = diziKopyala1.copy()
diziKopyala2[1] = 200
print(f"Dizilerin son hali, 1. dizi: {diziKopyala1} , 2. dizi: {diziKopyala2}\n")

# Cok boyutlu dizileri dilimleme
diziDilimle = np.arange(12)
diziDilimle.shape = (3,4)
print(f"Dilimlenmis dizi:\n{diziDilimle}\n")

# Dizilerin birlestirilmesi ve ayrilmasi
diziBirlestirme1 = np.full((2,4), 0.0)
diziBirlestirme2 = np.full((3,4), 1.0)
diziBirlestirme3 = np.full((4,4), 2.0)
diziBirlestirme4 = np.concatenate((diziBirlestirme1, diziBirlestirme2, diziBirlestirme3), axis = 0)
print(f"Dizi birlestirme (axis=0):\n{diziBirlestirme4}\n")
diziBirlestirme5 = np.full((3,2), 0.0)
diziBirlestirme6 = np.full((3,3), 1.0)
diziBirlestirme7 = np.concatenate((diziBirlestirme5, diziBirlestirme6), axis = 1)
print(f"Dizi birlestirme (axis=1):\n{diziBirlestirme7}\n")

























