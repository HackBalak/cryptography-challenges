""" Dans notre code , on va forcer d'abord l'utisateur de ce script a entrer la clé
 pour remplir la matrice de 5x5 , puis on va demander de lui par la suite saisir le
 message qu'il veut chiffrer ou dichiffrer
"""
key = input("Entrer La clé : ===> ex: MAROC \n  > ")
key = key.replace(" ", "") # pour supprimer les espaces
key = key.upper()   # pour les rendre majusqule


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

# ici on va editer la cle entrer , par exemple si vous avez entre 'W' il va la remplcer avec 'V'
result = list()
for c in key:  # storing key
    if c not in result:
        if c == 'W':
            result.append('V')
        else:
            result.append(c)
flag = 0 # le flag va nous servir de tester si le carac "W" est entrer ou pas encore
for i in range(65, 91):  # stockage d'autre caractére
    if chr(i) not in result:
        if i == 87 and chr(86) not in result: # verifier si les deux carac "W" et "V" ne sont pas encore stockée :)
            result.append("V")
            flag = 1
        elif flag == 0 and i == 87 or i == 86:
            pass
        else:
            result.append(chr(i))
k = 0
my_matrix = matrix(5, 5, 0)  # initialiser la matrix
for i in range(0, 5):  # making matrix
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1


def locindex(c):  # get location of each character
    loc = list()
    if c == 'W':
        c = 'V'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc


def encrypt():  # Encryption
    msg = str(input("ENTER  VOTRE MSG: > "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    print("CIPHER TEXT:", end=' ')
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]), end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2


def decrypt():  # decryption
    msg = str(input("ENTRER LE TEXTE CHIFFRE: \n > "))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("PLAIN TEXT:", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]), end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2


while (1):
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n > "))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        print("Vous pouvez toujours relancer ce programme  :)  ")
        exit()
    else:
        print("Choix incorrect !!!")