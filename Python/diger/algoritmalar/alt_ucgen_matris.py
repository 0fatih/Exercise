import numpy
'''
giris = int(input("Satir sayisini girin:"))
giris = int((giris*(giris+1))/2)
print("Verdiginiz satira kadar bulunan eleman sayisi {}'dir.".format(giris))

koseler = int(input("Kare matrisiniz bir kosesi ne kadar uzunlukta olsun?>>"))
matris = numpy.random.randint(20,size=(koseler,koseler)) # 5x5 lik, sayilari max 20 olan bir matris olustur

k = koseler-1
i=0

print("Matrisin ilk hali:\n",matris)
print("\n\n")


while (i<k):
    for i in range(koseler):
        for j in range(koseler):
            if(i>=j):
                print(matris[i,j],end=' ')
            else:break
        print("\n")
    i = i + 1
    '''

def matrisi_simetrik_yap(matris):
    for i in range(matris):
        for j in range(matris):
            matris[i,j]=matris[j,i]
    

giris = int(input("Satir sayisini girin:"))
giris = int((giris*(giris+1))/2)
print("Verdiginiz satira kadar bulunan eleman sayisi {}'dir.".format(giris))

koseler = int(input("Kare matrisiniz bir kosesi ne kadar uzunlukta olsun?>>"))
matris = numpy.random.randint(20,size=(koseler,koseler)) # 5x5 lik, sayilari max 20 olan bir matris olustur

k = koseler-1
i=0

print("Matrisin ilk hali:\n",matris)
print("\n\n")


while (i<k):
    for i in range(koseler):
        for j in range(koseler):
            if(i>=j):
                print(matris[i,j],end=' ')
            else:break
        print("\n")
    i = i + 1

print("Simetrik matris:\n")
print(matrisi_simetrik_yap(matris))
