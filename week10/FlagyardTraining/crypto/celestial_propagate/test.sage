from Crypto.Util.number import getPrime

# S1 = (r1 + 1Hint(encodepoint(R) + pk + m) * a) % l
# S2 = (r2 + 2Hint(encodepoint(R) + pk + m) * a) % l
#S1*2Hint - S2*1Hint = r1-r2 mod l

import random
a = random.getrandbits(255)
l = getPrime(257)
B = int(l^0.8)
print(len(bin(B)))
assert B<l
count = 10
Hi = [random.randrange(0, B) for _ in range(count)]
lr = [random.randrange(0, B) for _ in range(count)]

Si = [(j+i*a)%l for i,j in zip(Hi, lr)]


Zn = Zmod(l)

mat = [[0 for _ in range(count+2)] for __ in range(count+2)]
for i in range(count): 
    mat[i][i] = l
    mat[-2][i] = -Hi[i]
    mat[-1][i] = Si[i]
mat[-2][-2] = B/l
mat[-1][-1] = B

L = matrix(QQ, mat).LLL()
#print(L)
for row in list(L):
    if [abs(x) for x in row[:-2]] == lr:
        print("found")