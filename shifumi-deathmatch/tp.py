import client
from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
import random

import random


def chiffrementElgamal(m,g,h,p,k):
    return pow(g,k,p),(m*pow(h,k,p)%p)


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




# valeur = hexa
# fini par bit à 1
coup_nom = ["PIERRE", "FEUILLE","CISEAUX"]
coup_nombre = [88275625857605, 19779480974019653, 18939445432636760]



URL="http://pac.bouillaguet.info/TP4"
start_game = "/shifumi-deathmatch/insert-coin/echallier"
serverObj = client.Server(URL)

play_round = "/shifumi-deathmatch/start/echallier"
gage = "/shifumi-deathmatch/move"
result = "/shifumi-deathmatch/result"


# we start the round
serverObj.query(start_game)


# checks wether we have a commitment or a waiting status


p = 126798359029914725446765887403169477519710893205663996572711475980038063553457495178744862292562847742465894626874889751934758582848940157444562550949063732757958459459886990743094452792556886304484392991418833890084084001940300195029472204862655426238937132561895294468214558595080776128725724878240040526139
g = 85543749741524579357020566756475220154243204610146158865620251114256401177989994298955973667374521136040174355612744483492390583396536047339715697885972609970040568912561730110082790588474162380415743122166513653134275896588019590398774709214269308209421581422223786905620010591421914900974543040356711909881
# clef public
h =  50130097922389799180391308817701723888508855550182258404510513769784536981678223174962029030424075090218485420477812113902469984150055563709013560780033802910322023571589119927361158692777116556687256466766016605087414948182340063433888751144836263099269532974132746747052818230701297645947945549448181494231 
x = 40896478988371711300850196248951225606042524670499321080240771871648153366451566792530868339996969388325342613201901949828791809476505411558944575353003174095498648803931101811437139835186068132494742577345636728037660903092441734051991461531959935545720116564357048979591502994473690252115292755373963094449

myElGamal = ElGamal.ElGamalobj()
myElGamal.p = p
myElGamal.g = g
myElGamal.y = h
myElGamal.x = x

# # # on cree le chiffre du message avec ma clef public 
# print("===== kripting message ========")
#r = chiffrementElgamal(coup_nombre[1], g, h, p, p-3)

index_coup = 0

for i in range(100):
    print("===============")
    print("new round")
    play = serverObj.query(play_round)
    
    
    try:
        enemy_public_key = play['commitment']['PK']
        print("TRYIN MY LUCK 1")
        g_pow_x = enemy_public_key['h']
        g_pow_y = enemy_public_key['p']
        #g_pow_y = 20
        # si c'est un residu quadratique il a joue pierre
        if(((g_pow_x%2)== 1) and ((g_pow_y%2) == 1) and ((play['commitment']['ciphertext'][0]%2) == 1)):
            index_coup = 1
        else:
            index_coup = 0
        print("TRYIN MY LUCK 2")

    except:
        print("EXCEPT")
        index_coup = 2

    foobar = play['foobar']

    # myCryptedMsg = myElGamal.encrypt(coup_nombre[index_coup], (p-3))
    myCryptedMsg = chiffrementElgamal(coup_nombre[index_coup], g, h, p, (p-3))
    print("!!!!!!!!!!sending coup " +  coup_nom[index_coup])

    print("sending commitment")

    commit = serverObj.query(gage, 
                             {
                                 'commitment': {
                                     'ciphertext': myCryptedMsg, 
                                     'PK': {
                                         'h': myElGamal.y, 
                                         'p': myElGamal.p, 
                                         'g': myElGamal.g
                                     }
                                 },
                                 'foobar': foobar
                             })
    print("commitment sent")
    
    verification = serverObj.query(result, 
    {
        'move': coup_nom[index_coup], 
        'k': myElGamal.p-3, 
        'barfoo': commit['barfoo']
    })
    print(verification)
    print(serverObj.query("/shifumi-deathmatch/status/echallier"))
