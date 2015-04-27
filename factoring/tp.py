import client
import random
import rho
from fractions import gcd
import time
import sys
from miller_rabin import *

# autre info
# https://github.com/ralphleon/Python-Algorithms/blob/master/Cryptology/pollard.py

forbidenNumber = []
forbidenNumber.append(21)

level = sys.argv[1]

classGet = sys.argv[2]

print("Dealing with difficulti " + classGet)

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



def factorisationPollard(n, oldepoch):
    result = []
    try:
        while True:
            tmp = rho.pollardrho2(n, oldepoch)
            n = n // tmp
            print("factor = " + str(tmp))
            # I have tried to make it go a bit faster... I noticed that number 21 (not a prime number) came very often... there is no point trying an answer with this number
            if tmp in forbidenNumber:
                print("forbidden number % i" % tmp)
                break
            if not is_probable_prime(tmp):
                
                result.append(int(tmp))
    except:
        print("fin")

    return result


def factpremiers(n, oldepoch):
    """liste des facteurs premiers de n, avec la fonction 'a, b = decomp(n)' """
    R = []  # liste des facteurs premiers trouvés
    P = [n]  # pile de calcul
    try:
        while P!=[]:
            x = P.pop(-1)  # lecture et dépilage de la dernière valeur empilée
            if is_probable_prime(x):
                print(x)
                R.append(x)  # on a trouvé un facteur 1er => on ajoute à la liste
            else:
                a, b = rho.pollardrho5(x, oldepoch)  # on calcule une nouvelle décomposition
                if a==1 or b==1:
                    # echec: x n'est pas 1er mais sa decomposition ne se fait pas
                    # on essaie une décomposition par division
                    a, b = rho.facteursdiv2(x)
                print(a)
                P.append(a)  # on empile a
                P.append(b)  # on empile b
        R.sort()
        return R
    except:
        print("fin")



result = []
while True:
    print("================ NEW ================")
    getParam(link_param)
    # utilisé pour arreter la fonction au bout de x minutes
    print(n)
    oldepoch = time.time()
    result =  factpremiers(n, oldepoch)
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


