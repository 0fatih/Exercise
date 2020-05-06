"""
 Soru 1:

    p = Ogrenci, vizeden 60 ve ustu puan alir.
    q = Ogrenci finalden 60'in altinda puan alir.
    r = Ogrenci finalden 100 almaz.

    Ogrenci, vizeden 60 ve ustu puan alir ve finalden 60 ve ustu bir puan alir veya 
    finalden 100 alir ise dersi gecer.
"""

class performans:


    # Soru 2: Kume sorusu
    def kume(self, isim, soyisim):
        kesisim = []
        birlesim = []
        fark = []
        for i in isim:
            for j in soyisim:
                if(i == j and i not in kesisim): # bir harfi iki defa eklememesi icin not in kullandim
                    kesisim.append(i)

        for i in isim:
            birlesim.append(i)
            if(i not in kesisim):
                fark.append(i)

        for j in soyisim:
            birlesim.append(j)
        print(f"{isim} ∩ {soyisim} = {kesisim}\n{isim} ∪ {soyisim} = {birlesim}\n{isim} - {soyisim} = {fark}")


    # Soru 3: Seminer sorusu icin yazilan metot
    def seminer(self):
        # Buradan anladigim kadariyla belirtilen her sure icin yapilabilecek max seminer sayisi isteniyor.
        # O halde 8 saati, yani 480 dakikayi bu surelere bolmeliyiz.
        print(f"Bu salon icin; 5 dakikalik {int(480/5)}, 10 dakikalik {int(480/10)}, 30 dakikalik {int(480/30)}, 60 dakikalik {int(480/60)}, 120 dakikalik {int(480/120)} seminer duzenlenebilir.")


    # Soru 4: Taban Donusturme metodu
    def tabanDonustur(self, no, dogum_yili):
        birler_basamagi = int(str(no)[-1]) # Sayinin birler basamagi sayi % 10 sonucunu verecegi icin boyle yaptim
    
        def donustur( dogum_yili, taban):
            sonuc = "" # bolumden kalanlari ekle
            while(dogum_yili > 0):
                sonuc += str(int(dogum_yili % taban))
                dogum_yili = int(dogum_yili / taban)
            return sonuc[::-1] # Sayimiz sondan basa dogru okunmali. O yuzden ters ceviriyoruz
            

        if(birler_basamagi == 0 or birler_basamagi == 1 or birler_basamagi == 2):
            return bin(dogum_yili).replace("0b", "") # Ciktinin basindaki 0b'yi kaldiralim
        elif(birler_basamagi == 3):
            donustur(dogum_yili, 3)
        elif(birler_basamagi == 4):
            donustur(dogum_yili, 4)
        elif(birler_basamagi == 5):
            donustur(dogum_yili, 5)           
        elif(birler_basamagi == 6):
            donustur(dogum_yili, 6)
        elif(birler_basamagi == 7):
            donustur(dogum_yili, 7)
        elif(birler_basamagi == 8):
            donustur(dogum_yili, 8)
        else:
            donustur(dogum_yili, 9)
   
    
    # Soru 5: Affine sifreleme icin yazilan metot
    def affine(self, metin, dogum_ayi, dogum_gunu): # Aslinda dogum_ayi ve dogum_gunu parametreleri sabit olarak alinabilir
        sayisal_liste = [] # Donusum sonucu olusacak sayilari buraya ekleyecegim
        metin = metin.lower() # Buyuk kucuk harflerde sikinti olmasin diye her harfi kucultuyorum
        harfler = "abcdefghijklmnopqrstuvwxyz " # bosluk icin son indisi kullaniyorum
        donecek_metin = ""
        for i in metin:
            for j in range(0, len(harfler)): # burada uzunluk almamin sebebi: j'yi direkt olarak listeye ekleyecek olmam.
                if(i == harfler[j]):
                    sayisal_liste.append(j)
        for k in range(0, len(sayisal_liste)):
            sayisal_liste[k] = ((dogum_ayi * sayisal_liste[k]) + dogum_gunu) % 27
        
        for a in sayisal_liste:
            donecek_metin += harfler[a]

        return donecek_metin 
       

odev = performans()
print("\"furkan\" metninin affine sifrelenmis hali:",odev.affine("furkan", 5, 15)) # 5. sorunun cevabi
odev.seminer() # 3. sorunun cevabi
odev.kume("fatih", "hatipoglu")
print("Dogum yilim olan 1999'nin, numaramin son rakami olan 1 tabanindaki hali: ",odev.tabanDonustur(101101101, 1999))
# Kodu Github'da yayinlayacagim icin dogum gunum ve numarami dogru girmedim). 