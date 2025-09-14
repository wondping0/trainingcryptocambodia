SECRET = b'CTF{Data)dumm+2ronoirnaoiwnfoianwnriubwgiure_flag}'

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pwn import xor

# key = os.urandom(16)
key = b'A'*16

def enc(message, key):
    cipher = AES.new(key, AES.MODE_CTR)
    cip = cipher.encrypt(message)
    print(len(cip), key)
    print(xor(cip, message))
    return cip.hex()

message = SECRET + b'\x00'*(16-(len(SECRET)%16))
message = pad(message, 16)
print(message)

split_message = [message[i:i+16] for i in range(0, len(message), 16)]
cips = [enc(i, key) for i in split_message]
c = "".join(cips)
print(c)
# 2f9f1edfdacc8060867a9712082b213cddec81f811e67ed01c76be818b749b53da7053bea1679fdd4b4aec677ba7c6b4d9891cb1d29e0cb40062156c35130f46c0ea5e5ac7893909305f99cc3ab76e345f6374798370dff10f975485b51d9c00