import client

import rho


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
