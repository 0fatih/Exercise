def binsearch(dizi, bas, son, aranan):
    orta = int((bas+son)/2)
    if( bas <= son):
        if(aranan == dizi[orta]):
            print("Aranan deger {} dizinin {}. indeksi.".format(aranan,int((bas+son)/2)))
            print("Aranan == dizi[orta] Dizinin bas degeri {} dizinin son degeri {} ".format(bas,son))
        elif(aranan < dizi[orta]):
            binsearch(dizi,bas,son-1,aranan)
            print("Aranan < dizi[orta] Dizinin bas degeri {} dizinin son degeri {} ".format(bas,son))
        else:
            binsearch(dizi,bas,son+1,aranan)
            print("Aranan > dizi[orta] Dizinin bas degeri {} dizinin son degeri {} ".format(bas,son))

    
dizi = [1,3,4,5,7,8,9,12,32,43,54,65,76,78,98]
x = 54
binsearch(dizi,0,len(dizi)-1,x)