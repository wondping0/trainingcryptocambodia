from pwn import *
from binascii import hexlify
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

# io = process("./server.py")
io = remote("54.78.163.105","31935")

def inp(x):
    io.recvuntil(b'ciphertext (hex): ')
    io.sendline(hexlify(x))
    ret = io.recvline().decode().strip()
    return ret

def recoveryPlain(base3):
    knownKey = b''
    for k in range(16):
        bfk = chr(k+1).encode() * (k)
        for i in range(256):
            bfi = i.to_bytes(1,"big")
            added = bfi + strxor(knownKey, bfk)
            base2 = b'\x00'*(15-k) + added
            base = base2 + base3
            res = inp(base)
            if(res != "failed to decrypt"):
                knownKey = strxor(added, chr(k+1).encode() * (k+1))
                break
            print("kecepatan",i)
    return knownKey

if __name__ == "__main__":
    target = pad(b'propagating cipher block chaining',16)
    target = [target[i:i+16] for i in range(0, len(target), 16)]
    base3 = b'\x48'*16
    knownKey = recoveryPlain(base3)
    iv3 = strxor(knownKey, target[2])
    print("getting iv3")
    base2 = strxor(iv3, target[1])
    knownKey2 = recoveryPlain(base2)
    iv2 = strxor(knownKey2, target[1])
    
    base1 = strxor(iv2, target[0])
    knownKey3 = recoveryPlain(base1)
    iv1 = strxor(knownKey3, target[0])

    flag = inp(iv1 + base1 + base2 + base3)
    print(flag)
