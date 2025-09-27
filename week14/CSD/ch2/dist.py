from Crypto.Util.number import *
import random

flag = b'CSDD{REDACTED}'

def genrsa():
  p = getPrime(512)
  q = getPrime(512)
  n = p*q
  phi = (p-1)*(q-1)
  e = 3
  d = pow(e, -1, phi)
  return e, d, n

e, d, n = genrsa()
c1 = pow(bytes_to_long(flag+b'\x44444444444444444'), e, n)
c2 = pow(bytes_to_long(flag)+random.getrandbits(10), e, n)

# c1 = flag ^ e mod n
# c2 = flag+x2 ^ e mod n


print(c1)
print(c2)
print(n)
print(e)