def isPrime(n): 
    sayac = 0
    for i in range(2,n):
        if(n%i==0):
            sayac+=1
        else:
            pass
    if(sayac==0):
        return True
    else:
        return False

def isPandigital(t):
    res = list(map(int, str(t)))
    a = res[0]
    b = res[1]
    c = res[2]
    d = res[3]
    e = res[4]        
    if(a!=b and a!=c and a!=d and a!=e and b!=c and a!=d and a!=e and c!=d and c!=e and d!=e):
        return True
    else:
        return False

t = 98765

while True:    
    if(isPandigital(t)==True and isPrime(t)==True):
        print("Sayimiz pan ve prime {}".format(t))
        break
    else:
        t-=2
        pass