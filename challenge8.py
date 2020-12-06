"""
si vous avez ce package pycryptodome installed , ce programme ne va pas marchez
donc essayez de le desinstaller avant le lancez :) ,

    # sudo pip3 uninstall pycryptodome

"""

from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES


BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    """
    Usage:
        c = AESCipher('password').encrypt('message')

    """

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')


##
# MAIN
# Test pour encryption :
print('1> ENCRYPTION : \n')
msg = input('Message...: ')
pwd = input('Password..: ')

print('Ciphertext:', AESCipher(pwd).encrypt(msg))

print('2> DECRYPTION : \n')

msgdec = input('CipherText...: ')
pwddec = input('Password..: ')

print('Plaintext:', AESCipher(pwddec).decrypt(msgdec))