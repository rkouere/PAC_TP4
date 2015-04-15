import client

import rho
from fractions import gcd


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


getParam(link_param)
result = []
# on va incrementer le a pour essayer de trouver un nombre qui a un gdc != n ou de 1 pour la puissance de tous ses chiffres.
# si c'est le cas, on a un diviseur !
print(n) 
MB = rho.level3_1(n)
print("MB = %i" % (MB)) 
tmp = gcd(MB, n)
print("TMP = %i" % tmp)
n = n//tmp


print(n) 
MB = rho.level3_1(n)
print("MB = %i" % (MB)) 
tmp = gcd(MB, n)
print("TMP = %i" % tmp)
n = n//tmp


print(n) 
MB = rho.level3_1(n)
print("MB = %i" % (MB)) 
tmp = gcd(MB, n)
print("TMP = %i" % tmp)
n = n//tmp
