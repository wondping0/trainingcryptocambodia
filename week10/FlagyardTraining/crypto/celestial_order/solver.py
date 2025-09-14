from pwn import *
from ed25519 import *
import random

io = process(["python","server.py"])
# io = remote("54.78.163.105","30099")

io.recvuntil(b'pk (hex): ')
pk = bytes.fromhex(io.recvline().decode().strip())
l = 2**252 + 27742317777372353535851937790883648493

def sign(message):
    io.sendlineafter(b"command: ",b"sign")
    io.sendlineafter(b"(hex): ",message.hex().encode())
    # temp = ((io.recvline().decode().strip()))
    # print('h1:', temp)
    return io.recvline().decode().strip()

def getflag(message):
    io.sendlineafter(b"command: ",b"verify")
    io.sendlineafter(b"(hex): ",message.hex().encode())
    # temp = (int(io.recvline().decode().strip()))
    return io.recvline().decode().strip()

dat = []
mes1 = b'TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x02\x00\x00\x00\x00\x00\x00'
mes2 = b'TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x02\x00\x00\x00\x00\x00\x00'

print(mes1==mes2)

s1 = bytes.fromhex(sign(mes1))
s2 = bytes.fromhex(sign(mes2))

def retval(s, pk, m):
    R = decodepoint(s[: b // 8])
    A = decodepoint(pk)
    S = decodeint(s[b // 8 : b // 4])
    h = Hint(encodepoint(R) + pk + m)
    # print("S", S)
    # print("h", h)
    # print("R", R)
    return [S, h]

S1, h1 = retval(s1, pk, mes1)
S2, h2 = retval(s2, pk, mes2)

a = (pow(h2-h1, -1, l)*(S2-S1))%l

m = b'gimme the flag'
r = (S1 - a * h1) % l
R = scalarmult_B(r)
S = (r + Hint(encodepoint(R) + pk + m) * a) % l
newsign = encodepoint(R) + encodeint(S)

print(checkvalid(s1, mes1, pk))

flag = getflag(newsign)
print(flag)