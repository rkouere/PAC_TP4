import client
import elgamal




URL="http://pac.bouillaguet.info/TP4"
link_param = "/shifumi-deathmatch/insert-coin/echallier"
serverObj = client.Server(URL)

gage = "/shifumi-deathmatch/move"

roundStarter = "/shifumi-deathmatch/start/echallier"


# we start the round
#serverObj.query(link_param)

#play = serverObj.query(roundStarter)

print(elgamal.generate_keys())

# elGamal.ElGamal.generate(1024, Random.new().read)
