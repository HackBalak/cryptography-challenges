import pyqrcode
import random
import base64
import json
from typing import Callable
from hashlib import sha1

def from_qrcode(filepath: str) -> str:
    qr = qrtools.QR()
    qr.decode(filepath)


def crypt(data: str, key: bytes) -> str:
    """RC4 algorithm"""
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + int(box[i]) + int(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)


def encrypt(data: str, key: str, encode: Callable = base64.b64encode, salt_length: int = 16) -> str:
    """RC4 encryption """
    salt = ''
    for n in range(salt_length):
        salt += chr(random.randrange(256))
    data = salt + crypt(data, sha1((key + salt).encode()).digest())
    if encode:
        data = encode(data.encode())
    return data


def decrypt(data: str, key: str, decode: Callable = base64.b64decode, salt_length: int = 16) -> str:
    """RC4 decryption of encoded data"""
    if decode:
        data = decode(data).decode()
    salt = data[:salt_length]
    return crypt(data[salt_length:], sha1((key + salt).encode()).digest())

if __name__ == '__main__':
    print('TESTING ENCRYPTION')
    msg = input('Message...: ')
    key_enc = input('Key...: ')
    print('Ciphertext:', encrypt(msg, key_enc).decode('utf-8'))

    print('\nTESTING DECRYPTION')
    cte = input('Ciphertext: ')
    key_dec = input('Password..: ')
    print('Message...:', decrypt(cte, key_dec))
