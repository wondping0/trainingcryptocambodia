import random
import os
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = bytes.fromhex('82bb20b1ab38fd19f96c25220a865f1a')
plain = b'CTF{AESr_data_1}'
ciphertext = bytes.fromhex('39ca1426866b50c57fc9f4f6aeb3da51')

cipher = AES.new(key, AES.MODE_ECB)
# ciphertext = cipher.encrypt(plain)
plaintext = cipher.decrypt(ciphertext)

# print(ciphertext.hex())
print(key.hex())
print(plaintext)