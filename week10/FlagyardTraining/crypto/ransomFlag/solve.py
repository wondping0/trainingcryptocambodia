import base64
from Crypto.Cipher import ChaCha20

enc = '4HGJ/3Y6iekXR+FXdpdpa+ww4601QUtLGAzHO/8='
nonce = 'nFE+9jfXTKM='
ecnm = [41179, 49562, 30232, 7343, 51179, 49562, 24766, 36190, 30119, 33040, 22179, 44468, 15095, 22179, 3838, 28703, 32061, 17380, 34902, 51373, 41673, 6824, 41673, 26412, 27116, 51179, 34646, 15095, 10590, 11075, 1613, 20320, 31597, 51373, 20320, 44468, 23130, 47991, 11075, 15095, 34928, 20768, 15095, 8054]
n = 57833
d = 56771


p1 = "".join([chr(pow(i,d,n)) for i in ecnm])
obskey = base64.b64decode(p1)
xor_key = "0x1337" 
chacha_key = bytearray(obskey[i] ^ ord(xor_key[i % len(xor_key)]) for i in range(len(obskey)))

nonce = base64.b64decode(nonce)
cipher = ChaCha20.new(key=chacha_key, nonce=nonce)
ciphertext = base64.b64decode(enc)
flag = cipher.decrypt(ciphertext)
print(flag)