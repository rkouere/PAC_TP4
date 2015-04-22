# merci a http://python.jpvweb.com/mesrecettespython/doku.php?id=liste_des_nombres_premiers

# utilisation 
# premiers = [p for p in eratosthene_ba_iter(1000)]


from bitarray import bitarray
def eratosthene_ba_iter(n):
    """Itérateur retourne tous les nb premiers <= n (crible d'Eratosthene)
    on utilise ici le module 'bitarray' pour stocker les booléens
    """
    if n<2:
        pass # il n'y a aucun nb 1er en dessous de 2!
    else:
        n += 1 # pour avoir les nb 1ers <=n et pas seulement <n
        tableau = bitarray(n)
        tableau.setall(True)
        tableau[0], tableau[1] = False, False # 1 n'est pas un nb 1er
        yield 2  # 2 est un nombre premier
        tableau[2::2] = False # on élimine tous les nombres pairs
        racine = int(n**0.5)
        racine = racine + [1,0][racine%2] # pour que racine de n soit impair
        i, fin, pas = 3, racine+1, 2
        while i<fin: # on ne traite que les nb impairs
            if tableau[i]:
                yield i # on a trouvé un nouveau nb 1er: on le renvoie
                tableau[i::i] = False # on élimine i et ses multiples
            i += pas
        i, fin, pas = racine, n, 2
        while i<fin:  # on ne traite que les nb impairs
            if tableau[i]:
                yield i # on a trouvé un nouveau nb 1er: on le renvoie
            i += pas
