
import random
import time
from fractions import gcd

prime = []


# commencer pour A avec 500.000
# generation premier (7.5 millions) : crible eratostene

# info : les nombres a factoriser ont un nom !

# pollard p-1
def level3_1(n):
    u = []
    u.append(5000000)
    for i in range(len(prime)):
        u.append(pow(u[i], findHighestEntier(n, i), n))
    return u[i+1]


# 


def findHighestEntier(n, index):
#def findHighestEntier(B, p):
    cpt = 1;
    powAr = pow(prime[index], cpt)
    cpt+=1
    # si le resultat de la puissance est superieur ca ne marche pas
    if powAr > n:
        return -1
    # sinon on peut commencer a boucler
    while True:
        # on stoque l'ancienne version de powAr, au cas ou
        tmp = powAr
        powAr = pow(prime[index], cpt)
        cpt+=1
        if powAr <= n:
            continue
        else:
            return tmp
        

# def pollardMinus1(n,b):
#     """ Factor using Pollard's p-1 method """
#     a = 2
#     for j in range(2,b):
#         a = pow(a, j, n)
#     d = gcd(a-1,n)
#     if 1 < d < n: 
#         return d
#     else: 
#         return -1
 


def minute_passed(oldepoch):
    return time.time() - oldepoch >= 60*10


def pollardrho1(n, oldepoch):
    
    if (n % 2) == 0:
        return 2
    c = 1
    x = 2
    y = 5
    p = lambda z: ((pow(z, 2, n))%n+c)%n
    g = 1
    while g==1:
        if minute_passed(oldepoch):
            print("TROP LONNNNNNNNNNNNNNNNNNNG")
            raise Exception("We didn't find a factor")        
            
        x = p(x)
        y = p(p(y))
        tmp = abs(x - y)

        g = gcd(tmp, n)
        if(c > n or abs(g) > n):
            raise Exception("We didn't find a factor")        
        if(abs(g) == n):
            c = c + 1
    return g


# 1000 iterations pour racourcir le calcul du pgcd
# ne marche pas
def pollardrho2(n):
    if (n % 2) == 0:
        return 2
    c = 1
    x = 2
    y = 5
    tmp = 1

    p = lambda z: ((pow(z, 2, n))%n+c)%n
    g = 1
    while g==1:
        for i in range(10):
            x = p(x)
            y = p(p(y))
            tmp = abs(x - y) * tmp
        g = gcd(tmp, n)
        if(c > n):
            raise Exception("We didn't find a factor")        
        if(abs(g) == n):
            c = c + 1
    return g



def testFactor():
    print ("Pollard's p-1 factoring")
    n = 13493
    s = 2
    d = -1
    print ("n=%i, initial bound=%i" % (n,s))
    while s < n and d == -1:
        s +=1
        d = factor(n,s)
        print ("Round %i = %i" % (s,d))
    if d == -1: 
        print("No Factor could be found ...")
    else:
        print("%i has a factor of %i, with b=%i" % (n,d,s))



# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollardrho3(n, oldepoch):
    if n%2==0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    g = 1
    while g==1:
        if minute_passed(oldepoch):
            print("----- C'est beaucoup trop long tout ça !")
            raise Exception("We didn't find a factor")        
            
        x = ((x*x)%n+c)%n
        for i in range(100):
            y = ((y*y)%n+c)%n
        
        g = gcd(abs(x-y),n)
    return g





def lrac(x):
    """Racine carrée entière d'un nb entier x (méth. de Héron d'Alexandrie)"""
    r1 = 1
    while True:
        r2 = (r1+x//r1)//2 
        if abs(r1-r2) < 2:
            if r1*r1 <= x and (r1+1)*(r1+1) > x:
                return r1
        r1 = r2



def facteurs(n):
    """facteurs(n): décomposition d'un nombre entier n en facteurs premiers"""
    F = []
    if n==1:
        return F
    # recherche de tous les facteurs 2 s'il y en a
    while n>=2:
        x,r = divmod(n,2)
        if r!=0:
            break
        F.append(2)
        n = x
    # recherche des facteurs 1er >2
    i=3
    rn = lrac(n)+1
    while i<=n:
        if i>rn:
            F.append(n)
            break
        x,r = divmod(n,i)
        if r==0:
            F.append(i)
            n=x
            rn = lrac(n)+1
        else:
            i += 2
    return F
