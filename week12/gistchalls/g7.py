SECRET = 'REDACTED'

# CLUE:
# FOLLOW my github may get new information/hint

import os
import random
import hashlib
from pwn import xor

code = list(os.urandom(16))
for _ in range(random.getrandbits(10)):
    random.shuffle(code)

for _ in range(random.getrandbits(10)):
    code = code[:2]+code[:2]

keys = hashlib.sha256(str(code).encode()).digest()
for _ in range(random.getrandbits(10)):
    keys = hashlib.sha256(keys).digest()

print(len(keys))

c = xor(keys, SECRET)
print(c)
# b'N\xcdV\x03d\x8f\x96x\xc8 6\xb8I\xe2\x9b\x94\xea\xef<\xd1\xdfx9\x13SC#\x15c\xd5\xb5\xf9\x16\x96D\x12"\x80\xdcd\x9cz!\xfdP\xe1\x97\xd4\xe4\xfc=\xc9\xdas6\x04\x11J.@w\x8a\xe2\xaeC\x80'