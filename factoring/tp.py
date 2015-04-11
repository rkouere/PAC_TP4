import client
from fractions import gcd

import eratosthene
import random
import cheat



# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
# def pollardrho(n):
#     if n%2==0:
#         return 2
#     x = random.randint(1, n-1)
#     y = x
#     c = random.randint(1, n-1)
#     g = 1
#     while g==1:            
#         x = ((x*x)%n+c)%n
#         y = ((y*y)%n+c)%n
#         y = ((y*y)%n+c)%n
#         g = gcd(abs(x-y),n)
#     return g


def pollardrho(n):
    if((n % 2) == 0):
        return 2
    c = 1
    x = 2
    y = 5
    p = lambda z: ((z*z)%n+c)%n
    while True:
        x = p(x)
        y = p(p(y))
        g = gcd(abs(x - y), n)
        if(c > n):
            return False
        
        if(abs(g) == n):
            c = c + 1
        if(abs(g) != 1):
            return g
        

level = "1"
classGet = "C"
URL="http://pac.bouillaguet.info/TP4"
link_param = "/factoring/get/" + level + "/" + classGet
answer = "/factoring/submit/echallier"
serverObj = client.Server(URL)



while True:
    param = serverObj.query(link_param)
    idChallenge = param["id"]
    n = param["n"]
    print(n)
    result = []
    try:
        while True:
            tmp = pollardrho(n)
            n = int(n / tmp)
            result.append(int(tmp))
    except:
        print("fin")

    try:
        reply = serverObj.query(answer, {'id': idChallenge, 'factors': result})
        break
    except:
        print("trying again")

print(reply)
