from Crypto.Util.number import *
import random

flag = b'CSDD{REDACTED}'

def genrsa():
  while True:
    try:
      p = getPrime(512)
      q = getPrime(512)
      n = p*q
      phi = (p-1)*(q-1)
      e = 3
      d = pow(e, -1, phi)
      return e, d, n
    except:
      continue
  return None

e, d, n = genrsa()
c1 = pow(bytes_to_long(flag+b'\x44444444444444444'), e, n)
# print(pow((pow(256, 16)*bytes_to_long(flag) + 90658561971338262202129460362336285748),3,n))
c2 = pow(bytes_to_long(flag)+random.getrandbits(10), e, n)

print(c1)
# exit(1)
print(c2)
print(n)
print(e)
print("GENERATED")

R.<X> = Zmod(n)[]

for r in range(1024):
  f1 = (pow(256, 16)*X + 90658561971338262202129460362336285748)^3 - c1
  f2 = (X + r)^3 - c2

  # GCD is not implemented for rings over composite modulus in Sage
  # so we'll do it ourselves. Might fail in rare cases, but we
  # don't care.
  def my_gcd(a, b): 
    return a.monic() if b == 0 else my_gcd(b, a % b)

  m = bytes_to_long(flag)
  m2 = -my_gcd(f1, f2).coefficients()[0] # coefficient 0 = -m
  print(m, m2)
  if(m==m2):
    print('real m:', m)
    print('recover m:', m2)
    break



