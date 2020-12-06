import pyaes, pbkdf2, binascii, os, secrets

# Derive a 256-bit AES encryption key from the password
password = input("Password... :")
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key).decode('utf-8'))

# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
iv = secrets.randbits(256)
plaintext = input("PlainText... : ")
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted Text:', binascii.hexlify(ciphertext).decode('utf-8'))

# Decrypt the ciphertext with the given key:
#   plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext).decode('utf-8')
print('Decrypted CipherText:', decrypted)



