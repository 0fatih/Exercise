word_to_number={
    "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,
    "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}
giris=input("Bana bir kelime gonder:")
ayir=list(giris.upper())
sonuc=0
for i in ayir:
    sayi=word_to_number[i]
    sonuc+=sayi
cevap=0
j=0
for i in range(sonuc):
    j+=i
    if(j==sonuc):
        cevap=1
    else:
        pass

if(cevap==1):
    print("Kelimesinin sayisi {} oldugu icin ucgensel".format(sonuc))
else:
    print("Kelimesinin sayisi {} oldugu icin ucgensel degil".format(sonuc))