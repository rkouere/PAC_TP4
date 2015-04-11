import client
import eratosthene
import random
import cheat

# merci http://python.jpvweb.com/mesrecettespython/doku.php?id=pgcd_ppcm
def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        r=a%b
        a,b=b,r
    return a

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)



def pollardrho(n):
    """Factorisation d'un nombre entier décomposable (méth. de rho pollard)"""
    c = 0
    f = lambda z: pow(z, z)+c
    x, y, d = 2, 5, 1
    while True:
        x = f(x) % n
        y = f(f(y)) % n
        d = pgcd(x-y, n)
        if((d == 1) or (d == -1)):
           continue
        elif((d == n) or (d == -n)):
           c = c + 1
        else:
             return d

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
                        g = pgcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g    

level = "1"
classGet = "D"
URL="http://pac.bouillaguet.info/TP4"
link_param = "/factoring/get/" + level + "/" + classGet
answer = "/factoring/submit/echallier"
serverObj = client.Server(URL)

param = serverObj.query(link_param)
idChallenge = param["id"]
n = param["n"]
print(n)
L = cheat.fac(n)
print(L)

# print(serverObj.query(answer, {'id': idChallenge, 'factors': L}))
