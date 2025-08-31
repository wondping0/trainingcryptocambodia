# from sage.all import matrix, ZZ, Primes
import random

n = 5

list_pub = [random.getrandbits(1024) for _ in range(n)]
list_pub2 = [random.getrandbits(1024) for _ in range(n)]
list_priv = [random.getrandbits(512) for _ in range(n)]

sumer = sum([i*j for i,j in zip(list_pub,list_priv)])
sumer2 = sum([i*j for i,j in zip(list_pub2,list_priv)])

print(sumer)

for jk in range(20, 5000):
    scale = 2**jk
    # P = Primes()
    # scale = 2**1024
    mat = matrix(n+1, n+1)
    for i in range(n):
        mat[i,i] = 1
        mat[i, -1] = scale*list_pub[i]
    mat[-1, -1] = scale * -sumer
    mat[-1, -2] = 1*2**512
    # mat = [
    #     [1, 0, 0, 0, 0, 0,        scale * list_pub[0], scale * list_pub2[0]],
    #     [0, 1, 0, 0, 0, 0,        scale * list_pub[1], scale * list_pub2[1]],
    #     [0, 0, 1, 0, 0, 0,        scale * list_pub[2], scale * list_pub2[2]],
    #     [0, 0, 0, 1, 0, 0,        scale * list_pub[3], scale * list_pub2[3]],
    #     [0, 0, 0, 0, 1, 0,        scale * list_pub[4], scale * list_pub2[4]],
    #     [0, 0, 0, 0, 0, 1 * 2^512, scale * -sumer,     scale * -sumer2   ],
    # ]
    # mat = matrix(ZZ, mat).LLL()
    # print(mat)

    hasil = mat.LLL()
    # print(hasil)
    # break
    for i in hasil:
        if(i[-1]==0 and i[-2]%2**100==0): 
            print(i)
            print("FOUND")
            print(list_priv)
            # exit(1)
