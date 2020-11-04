import pandas as pd

# En basit haliyle bir seri olusturma
seri1 = pd.Series([2020, 'Fatih', -5.25])
print(f"Basit bir seri ornegi:\n{seri1}\n")

# Serileri spesifik index ile olusturma
seri2 = pd.Series([2020, 'Furkan', 23.21], index=['A', 'B', 'C'])
print(f"Spesifik indexli seri ornegi:\n{seri2}\n")

# Serilere erisim
print(f"2. serinin 2. indexindeki eleman:{seri2[2]}\n")

# Serilerin dilimlenmesi
seri3 = pd.Series([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print(f"Seri dilimleme:\n{seri3[2:4]}\n")

# Python'daki 'sozlukler' seriye donusturulebilir
sozluk = {"Matematik":80, "Turkce":85, "Felsefe":82}
seri4 = pd.Series(sozluk)
print(f"Sozlukten donusturulen seri ornegi:\n{seri4}\n")

# Seri icerisinde bir deger arama islemi !! Buyuk kucuk harf onemli
print(f"Ustteki seride Fizik var mi?: {'Fizik' in seri4}\n")

# Seriler uzerinde matematiksel islemler
print(f"Seriler uzerinde matematiksel islemler yapabiliriz:\n{seri4*1.05}\n")

# Seri icerisinden belli bir sayidan buyuk elemanlari alma islemi
print(f"Seri3 icerisinde 30'den buyuk sayilari:\n{seri3[seri3>30]}\n")

# Seri icerisindeki elemanlardan o seride kac tane oldugunu bulma
seri5 = pd.Series([10,10,23,34,234,435,654,23,45,56,34,34])
print(f"Elemanlarin seride bulunus sayisi:\n{seri5.value_counts()}\n")

# Serideki elemanlarin her birinin bir kere gosterilmesi
print(f"Serideki elemanlarin birer kere gosterilmesi:\n{seri5.unique()}\n")

# !!DATA FRAME!!
ogrenciler_dict = {
        "okulNo": pd.Series([100, 101, 102], index=["Merve", "Betul", "Can"]),
        "ortalama": pd.Series([90, 95, 100], index=["Merve", "Betul", "Can"]),
        "bolum": pd.Series(['Bil. muh', 'Bil muh', 'Makine Muh'], index=["Merve", "Betul", "Can"]),
        "dTarihi": pd.Series([2000,2000,2001], index=["Merve", "Betul", "Can"])
        }
tablo = pd.DataFrame(ogrenciler_dict)
print(f"Basit bir DataFrame ornegi:|n{tablo}\n")

# DataFrame'den spesifik eleman yazdirma
print(f"Ortalamasi 93'den kucuk olan elemanlar:\n{tablo[tablo['ortalama']< 93]}\n")

# .csv dosya turu ile islemler yapma
veriseti = pd.read_csv('data.csv', sep=",", engine='python', )
print(f"Ornek bir csv dosyasi:\n{veriseti}\n")

# Veriler arasindaki korelasyon
print(f"Veriler arasindaki korelasyon:\n{veriseti.corr()}\n")

# Korelasyonu sekillendirmek
import seaborn as sb
sb.heatmap(veriseti.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.01)



