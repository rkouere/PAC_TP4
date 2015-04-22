import client
import random
import rho
import lenstra
from fractions import gcd
from miller import *


##############################################################################
def lrac(x):
    """Racine carrée entière d'un nb entier x (méth. de Héron d'Alexandrie)"""
    r1 = 1
    while True:
        r2 = (r1+x//r1)//2 
        if abs(r1-r2) < 2:
            if r1*r1 <= x and (r1+1)*(r1+1) > x:
                return r1
        r1 = r2
 
 
##############################################################################
def facteursdiv2(n):
    """Décomposition par division de n (entier) en 2 facteurs quelconques"""
    pp = [2, 3, 5, 7, 11]
    racn = lrac(n)+1  # lrac(n) = racine carrée entière de n
    for p in pp:
        if p>racn:
            return [n, 1]  # n est premier
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
    p = pp[-1] + 2
    while p <= racn:
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
        p += 2
    # si on arrive ici, n est premier
    return [n, 1]
 
#############################################################################
def pollardrho(n):
    """Factorisation d'un nombre entier décomposable (méth. rho de pollard)"""   
    f = lambda z: z*z+1
    x, y, d = 2, 2, 1
    while d==1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(x-y, n)
    return [d, n//d]
 
##############################################################################
def factpremiers(n):
    """liste des facteurs premiers de n, avec la fonction 'a, b = decomp(n)' """
    R = []  # liste des facteurs premiers trouvés
    P = [n]  # pile de calcul
    while P!=[]:
        x = P.pop(-1)  # lecture et dépilage de la dernière valeur empilée
        # if estpremier(x):
        #     R.append(x)  # on a trouvé un facteur 1er => on ajoute à la liste
        # else:
        #     a, b = pollardrho(x)  # on calcule une nouvelle décomposition
        #     if a==1 or b==1:
        #         # echec: x n'est pas 1er mais sa decomposition ne se fait pas
        #         # on essaie une décomposition par division
        #         a, b = facteursdiv2(x)
        #     P.append(a)  # on empile a
        #     P.append(b)  # on empile b


        a, b = pollardrho(x)  # pollardrho(x)on calcule une nouvelle décomposition

        
        if a==1 or b==1:            
            print("echec: x n'est pas 1er mais sa decomposition ne se fait pas")
            # on essaie une décomposition par division
            a, b = facteursdiv2(x)
        P.append(a)  # on empile a
        P.append(b)  # on empile b
        print("P = " + str(P))
    R.sort()
    return R

def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g    


# autre info
# https://github.com/ralphleon/Python-Algorithms/blob/master/Cryptology/pollard.py

forbidenNumber = []
forbidenNumber.append(21)

level = "3"
classGet = "C"
URL="http://pac.bouillaguet.info/TP4"
link_param = "/factoring/get/" + level + "/" + classGet
answer = "/factoring/submit/echallier"
serverObj = client.Server(URL)

param = ""
idChallenge = ""
n = ""

def getParam(link_param):
    global param
    global idChallenge
    global n
    param = serverObj.query(link_param)
    idChallenge = param["id"]
    n = param["n"]


def factorisationPollard(n):
    result = []
    try:
        while True:
            tmp = rho.pollardrho1(n)
            n = n // tmp
            print("factor = " + str(tmp))
            # I have tried to make it go a bit faster... I noticed that number 21 (not a prime number) came very often... there is no point trying an answer with this number
            if tmp in forbidenNumber:
                break
            result.append(int(tmp))
    except:
        print("fin")

    return result

result = []
while True:
    getParam(link_param)
    print(n)
    result =  factorisationPollard(n)
    try:
        print("sending the reply")
        print(result)
        reply = serverObj.query(answer, {'id': idChallenge, 'factors': result})
        break
    except client.ServerError as e:
        print(result)
        print(e)
print("===============OK================")
print(result)
print(reply)

# while True:
#     tmp = rho.pollardrho3(n)
#     P.append(tmp)
#     print("rest = " + str(n))
#     print(P)
#     n = n//tmp


