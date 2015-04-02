import client
import random


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
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

# info = congru 
# g^m  = h^r+(g^b+h^c)^s     mod p
#      = g^xr * g^bs * h^cs  mod p
#      = g^(xr+bs++cxs)      mod p
# # D'apres le lemme 1
# m    = xr+bs+cxs           mod p-1
#      = x(r+cs) + bs        mod p-1
# -> il faut trouver un truc qui fait r+cs = 0


URL="http://pac.bouillaguet.info/TP4"
link_param = "/ElGamal-forgery/PK/echallier"
answer = "/ElGamal-forgery/verify/echallier"

serverObj = client.Server(URL)


param = serverObj.query(link_param)
h = param['h'] # g^x mod p
g = param['g'] # base du g^x
p = param['p'] # modulo
y = h

e = random.randint(1, p-1)
v = random.randint(1, p-1)

print("while")
while(pgcd(v, p-1) != 1):
    v = random.randint(1, p-1)

print("r")
r = ((pow(g, e, p)) * (pow(y, v, p))) % p

print("s")
s = ((p-1)-r*modinv(v, p-1)) % (p-1)
print(s)

m = (e*s) % (p-1) 



print(serverObj.query(answer, {'m': m, 'signature': (r, s)}))
