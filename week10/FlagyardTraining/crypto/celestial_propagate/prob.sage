import random
coefs = [random.randrange(2**512) for _ in range(5)]
Sums = []
public = []

for i in range(2):
    public_values = [random.randrange(2**1024) for _ in range(5)]
    S = 0
    for l,r in zip(coefs, public_values):
        S += l*r
    Sums.append(S)
    public.append(public_values)

P = Primes()
scale_inf = P.next(2^1024)
mat = [
    [1, 0, 0, 0, 0, 0,        scale_inf * public[0][0], scale_inf * public[1][0]],
    [0, 1, 0, 0, 0, 0,        scale_inf * public[0][1], scale_inf * public[1][1]],
    [0, 0, 1, 0, 0, 0,        scale_inf * public[0][2], scale_inf * public[1][2]],
    [0, 0, 0, 1, 0, 0,        scale_inf * public[0][3], scale_inf * public[1][3]],
    [0, 0, 0, 0, 1, 0,        scale_inf * public[0][4], scale_inf * public[1][4]],
    [0, 0, 0, 0, 0, 1 * 2^512, scale_inf * -Sums[0],     scale_inf * -Sums[1]   ],
]

mat = Matrix(ZZ, mat).LLL()
print(mat[0])
print(coefs)