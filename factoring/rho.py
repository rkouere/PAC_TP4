from fractions import gcd



def pollardrho1(n):
    if (n % 2) == 0:
        return 2
    c = 1
    x = 2
    y = 5
    p = lambda z: ((pow(z, 2, n))%n+c)%n
    g = 1
    while g==1:
        x = p(x)
        y = p(p(y))
        g = gcd(abs(x - y), n)
        if(c > n):
            raise Exception("We didn't find a factor")        
        if(abs(g) == n):
            c = c + 1
    return g


# 1000 iterations pour racourcir le calcul du pgcd
def pollardrho2(n):
    if (n % 2) == 0:
        return 2
    if (n % 3) == 0:
        return 3
    if (n % 5) == 0:
        return 5
    c = 1
    x = 2
    y = 5
    tmp = 1

    p = lambda z: ((pow(z, 2, n))%n+c)%n
    g = 1
    while g==1:
        for i in range(10):
            x = p(x)
            y = p(p(y))
            tmp = abs(x - y) * tmp
        g = gcd(tmp, n)
        if(c > n):
            raise Exception("We didn't find a factor")        
        if(abs(g) == n):
            c = c + 1
    return g




def factor(n,b):
    """ Factor using Pollard's p-1 method """
    a = 2;
    for j in range(2,b):
        a = pow(a, j, n)
    d = gcd(a-1,n);
    print("d:" + str(d) + "a-1:" +str(a-1))
    if 1 < d < n: 
        return d;
    else: 
        return -1;

def testFactor():
    print ("Pollard's p-1 factoring")
    n = 13493
    s = 2
    d = -1
    print ("n=%i, initial bound=%i" % (n,s))
    while s < n and d == -1:
        s +=1
        d = factor(n,s)
        print ("Round %i = %i" % (s,d))
    if d == -1: 
        print("No Factor could be found ...")
    else:
        print("%i has a factor of %i, with b=%i" % (n,d,s))



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
