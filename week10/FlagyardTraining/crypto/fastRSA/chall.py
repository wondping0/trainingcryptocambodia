#!/usr/local/bin/python
import os
import random
import gmpy2
# from inputimeout import inputimeout 

FLAG = "FlagY{dummy_flag!}"

def encrypt(b, m):
    p = gmpy2.next_prime(2 ** b + random.randint(0, 2 ** b))
    q = gmpy2.next_prime(2 ** b + random.randint(0, 2 ** b))
    # b is constant value 30*inc
    # p = 2**31
    # q
    # e = is too small
    # p, q is also too small, this not checking the primality check for the p and q. 
    # So The RSA challenge or factoring the number of N cannot be solved.
    # phi   
    # d 

    n = p * q
    print(n)
    print(m ** 3 % n)
    print((m + 1) ** 3 % n)

for i in range(1, 15):
    b = 30 * i
    m = random.randint(0, 4 ** b)
    print('m:', m)
    encrypt(b, m)
    try:
        x = int(input("Enter Number : "))
        if x == m:
            print("============================\nKeep Going!\n============================")
            continue
        else:
            print("============================\nWrong Answer!\n============================")
            exit()
    except ValueError:
        print("============================\nNot allowed Answer!\n============================")
        exit()
    except Exception:
        exit()

print(FLAG)
