def createListNumber(n):
    L = []
    for i in range(2, n + 1):
        L.append(i)
    return L


def eratosthene(n):
    L = createListNumber(n)
    res = []
    for i in range(len(L)):
        if(L[i] != False):
            print("currently dealing with")
            print(L[i])
            for y in range(i + 1, len(L)):
                if((L[y] % L[i]) == 0):
                    L[y] = False
            print("================")

    for i in range(0, len(L)):
        if(L[i] != False):
            res.append(L[i])
    return res
