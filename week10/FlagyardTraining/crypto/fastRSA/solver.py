from pwn import *
from sage.all import Zmod

# io = process(["python3","chall.py"])
io = remote("34.252.33.37","32278")


def my_gcd(a, b): 
    return a.monic() if b == 0 else my_gcd(b, a % b)

def fk(c1,c2,n): 
    X = Zmod(n)['X'].gen()
    f1 = X**3 - c1
    f2 = (X + 1)**3 - c2
    return -my_gcd(f1, f2).coefficients()[0] # coefficient 0 = -m

def gt():
    n = int(io.recvline().decode().strip())
    m3 = int(io.recvline().decode().strip())
    m1 = int(io.recvline().decode().strip())
    m = fk(m3, m1, n)
    io.recvuntil(b'Enter Number : ')
    io.sendline(str(m).encode())
    io.recvline()
    temp = io.recvline()
    io.recvline()
    return temp

for  i in range(14):
    gt()
flag = io.recvline()
print(flag)