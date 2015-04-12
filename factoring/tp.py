import client

import rho


# autre info
# https://github.com/ralphleon/Python-Algorithms/blob/master/Cryptology/pollard.py


level = "2"
classGet = "D"
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
            tmp = rho.pollardrho2(n)
            n = n // tmp
            result.append(int(tmp))
    except:
        print("fin")

    return result


#rho.factor(long(n), 1000)

# POLLARD
while True:
    getParam(link_param)
    print(n)
    result = factorisationPollard(n)
    try:
        reply = serverObj.query(answer, {'id': idChallenge, 'factors': result})
        break
    except client.ServerError as e:
        print(result)
        print(e)
print("===============OK================")
print(result)
print(reply)
