from Crypto.Util.number import *
from sage.all import matrix, Zmod

# p = getPrime(256)
# q = getPrime(256)
p = 75071689350809092788066946686375498542328749222644075665496079869562681154857
q = 108218392356542584084431007423698942182652670113587932818197594419456406241169
n = p*q

p_inv = pow(p,-1,q)
q_inv = pow(q,-1,p)

k1 = (p*p_inv-1)//q
k2 = (p*p_inv-1)//p
print(k1, k1.bit_length())
print(k2, k2.bit_length())
# p*p_inv = 1+k1q
# q*q_inv = 1+k2p
# p*p_inv-k1q = k2p-q*q_inv 
# (p_inv+k2)p = q(q_inv+k1)
# p = (q_inv+k1)
# q = (p_inv+k2)
# n = pq
# n = (q_inv+k1)(p_inv+k2)
# 0 = p_inv*q_inv+p_inv*k1+q_inv*k2+k1*k2-n

B = 1
M = 2**256
mt = [
    [B,0,0,0,p_inv*M],
    [0,B,0,0,q_inv*M],
    [0,0,B,0,1*M],
    [0,0,0,B*M**3-1,-(n-p_inv*q_inv)*M],
]

Mat = matrix(mt)
for i in Mat.LLL():
    print(i)