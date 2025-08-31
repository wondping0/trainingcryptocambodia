from Crypto.Util.number import *
from math import gcd
from random import randrange
from pwn import *

io = remote("54.78.163.105","30471")

def factorize_multi_prime(N, phi):
    """
    Recovers the prime factors from a modulus if Euler's totient is known.
    This method works for a modulus consisting of any number of primes, but is considerably be slower than factorize.
    More information: Hinek M. J., Low M. K., Teske E., "On Some Attacks on Multi-prime RSA" (Section 3)
    :param N: the modulus
    :param phi: Euler's totient, the order of the multiplicative group modulo N
    :return: a tuple containing the prime factors
    """
    prime_factors = set()
    factors = [N]
    while len(factors) > 0:
        N = factors[0]
        w = randrange(2, N - 1)
        i = 1
        while phi % (2 ** i) == 0:
            sqrt_1 = pow(w, phi // (2 ** i), N)
            if sqrt_1 > 1 and sqrt_1 != N - 1:
                factors = factors[1:]
                p = gcd(N, sqrt_1 + 1)
                q = N // p
                if isPrime(p):
                    prime_factors.add(p)
                elif p > 1:
                    factors.append(p)
                if isPrime(q):
                    prime_factors.add(q)
                elif q > 1:
                    factors.append(q)
                break
            i += 1
    return tuple(prime_factors)

if __name__ == '__main__':
    for _ in range(2):
        io.recvuntil(b'n = ')
        n = int(io.recvline().decode().strip())
        io.recvuntil(b'phi = ')
        phi = int(io.recvline().decode().strip())
        p,q = factorize_multi_prime(n,phi)
        io.recvuntil(b'input factors\n')
        io.sendline(str(p).encode())
        io.sendline(str(q).encode())
    
    print(io.recvline())
    e = (1 << 16) + 1
    io.recvuntil(b'n = ')
    n = int(io.recvline().decode().strip())
    hom = pow(2, e, n)
    io.recvuntil(b'encryption result = ')
    enc = int(io.recvline().decode().strip())
    io.sendline(str((hom*enc)%n).encode())
    io.recvuntil(b'decryption result = ')
    dec = int(io.recvline().decode().strip())
    io.sendline(str((dec*pow(2,-1,n))%n).encode())
    flag = io.recvline()
    print(flag)