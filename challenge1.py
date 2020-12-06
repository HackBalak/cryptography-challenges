


def trouve(mots, lettre): # Fonction qui correspond à lambda (permet de retourne de tout position  d'une  lettre  dans un mots
    indextrouves = [] # indextrouves correspond à i dans le code de tyrtamos. Ici une liste.
    for index, caractere in enumerate(mots): # enumerate retourne le tuple index/caractere. Attention, l'index commence à zero.
        if caractere == lettre:
            indextrouves.append(index) # Si le caractere correspond à la lettre on mets sons index d'en 'i'.
    return indextrouves # Retourne les index.


def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.

    Note: borne_inf doit être inférieure à borne_sup"""

    while borne_inf < borne_sup:
        yield borne_inf
        borne_inf += 1


def homocrypto(origine,lk={}):#cette fonction  permet de crypter  un mot  par la  méthode de Homophonic Substitution Code
     liorigi=list(origine.strip())#convertion chaine en list
     for car in liorigi:  #
         position=trouve(origine,car)#la liste position contient tous les position de car dans la chaine origine
         for cle, valeur in lk.items():#  parcour du dictionnaire
             if car == cle :
                codecar = valeur
                bo=0
                for i in intervalle(0,len(position)):
                   # if  i> =len(codecar):
                    if (len(position) > len(codecar)  ):
                        j=0
                        K=0

                        while j<len(position) :

                             liorigi[position[j]]= codecar[K]

                             j=j+1
                             K=K+1
                             if(K>=len(codecar)):
                                K=0


                    else:
                     liorigi[position[i]]=codecar[i]



     return liorigi

dicr={"a": [ "07", "31", "50", "63", "66", "77", "84" ],"b": [ "11", "64" ],"c" :[ "17", "33", "49" ],"d" :[ "10", "27", "51", "76" ],
      "e":[ "25", "26", "28", "32", "48", "67", "69", "72", "75", "79", "82", "85" ],"f": [ "08", "09" ], "g": [ "44", "83" ], "h":[ "19", "20", "21", "54", "70", "87" ],
"i":[ "02", "03", "29", "53", "68", "73" ],"j": [ "18" ] , "k": [ "41" ] ,
 "l":[ "42", "81", "86", "95" ], "m":[ "40", "52" ],"n":[ "00", "43", "80", "88", "89" ],
 "o":[ "16", "30", "61", "65", "91", "94", "96" ],"p":[ "01", "62" ],  "q" :[ "15" ],
 "r":[ "04", "24", "39", "58", "71", "99" ],"s":[ "06", "34", "56", "57", "59", "90" ],
"t":[ "05", "23", "35", "37", "38", "60", "74", "78", "92" ],"u":[ "13", "14", "36" ],
"v":[ "22" ]   , "w":[ "45", "46" ],  "x":[ "12" ],  "y":[ "55", "93" ],  "z":[ "47" ]}

msg = input("Entrer votre msg svp : ")
cipherText=homocrypto(msg,dicr)
print(*cipherText)