
#### Transposition or Permutation ::::

def split_text(liname, key): # i use that to count the length of the string, i then use the
                              # length to determine how many columns to create within the program
     length=len(key)
     return [liname[i:i + length] for i in range(0, len(liname), length)]






def encrypt(texte, key):
       res=""  #  result
       len(key) # len of key
       list_texte=split_text(texte, key) #

       lenght_key_uplit=len(list_texte) #len of listname

       listkey=list(key) # convertion oon list

       listkey.sort() #sort of the key

       for car in listkey: # pour chaque element in listkey ,en prend son index and  we take  all indice  correspondantes
                           #dans chaque element in  list_text
         indice=key.index(car) # index of car in th firt key before  has sorted
         for i in range(lenght_key_uplit):
            char=str(list_texte[i])
            res+=char[indice]


       return res



text="BONJOUR TOUT LE MONDE CHEZ ICCN2   "
texte=text.replace(" ","#")
key="HAAID"
if len(texte) % len(key) ==0:

      cipher_text = encrypt(texte, key)
      cipher_text=cipher_text.replace("#"," ")
      print(cipher_text)

else:
 print("length of key must multiple of the  length texte in this case {} is not multiple to {} , so you could add spaces to completed".format(len(texte),len(key)))







