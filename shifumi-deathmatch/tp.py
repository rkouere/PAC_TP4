import client
import elgamal
import base64




# valeur = hexa
# fini par bit à 1
pierre  = "PIERRE"
feuille = "FEUILLE"
# fini par bit à 0
ciseau  = "CISEAU"


URL="http://pac.bouillaguet.info/TP4"
start_game = "/shifumi-deathmatch/insert-coin/echallier"
serverObj = client.Server(URL)

gage = "/shifumi-deathmatch/move"

play_round = "/shifumi-deathmatch/start/echallier"



# we start the round
serverObj.query(start_game)

play = serverObj.query(play_round)

# checks wether we have a commitment or a waiting status
try:
    if(play['commitment']):
        ciphertext = play['ciphertext']
        PK = play['PK']
        print("com")
except:
    print("status")

foobar = play['foobar']
print(play)

myElGamal = elgamal.generate_keys()
print(myElGamal)
myCryptedMsg = elgamal.encrypt(myElGamal['publicKey'], feuille)
print(myCryptedMsg)



# elGamal.ElGamal.generate(1024, Random.new().read)
