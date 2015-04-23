import client
import random
import rho
from fractions import gcd
import time
import sys


# autre info
# https://github.com/ralphleon/Python-Algorithms/blob/master/Cryptology/pollard.py

forbidenNumber = []
forbidenNumber.append(21)

level = "3"

if(len(sys.argv) == 2):
    classGet = sys.argv[1]
else:
    classGet = "C"

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
            tmp = rho.pollardrho1(n, oldepoch)
            n = n // tmp
            print("factor = " + str(tmp))
            # I have tried to make it go a bit faster... I noticed that number 21 (not a prime number) came very often... there is no point trying an answer with this number
            if tmp in forbidenNumber:
                print("forbidden number % i" % tmp)
                break
            result.append(int(tmp))
    except:
        print("fin")

    return result


result = []
while True:
    print("================ NEW ================")
    getParam(link_param)
    # utilisé pour arreter la fonction au bout de x minutes
    print(n)
    oldepoch = time.time()
    result =  factorisationPollard(n, oldepoch)
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


