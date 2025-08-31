from pwn import *
import ed25519

b = 256
q = 2**255 - 19
l = 2**252 + 27742317777372353535851937790883648493

io = remote("54.78.163.105","32247")

# function code
# def signature_unsafe(m, sk, pk):
#     """
#     Not safe to use with secret keys or secret data.

#     See module docstring.  This function should be used for testing only.
#     """
#     h = H(sk)
#     a = 2 ** (b - 2) + sum(2**i * bit(h, i) for i in range(3, b - 2))
#     # r = Hint(
#     #     intlist2bytes([indexbytes(h, j) for j in range(b // 8, b // 4)]) + m
#     # )
#     r = Hint(
#         m + intlist2bytes([indexbytes(h, j) for j in range(b // 8, b // 4)])
#     )
#     R = scalarmult_B(r)
#     S = (r + Hint(encodepoint(R) + pk + m) * a) % l
#     return encodepoint(R) + encodeint(S)

def checksign(s, pk, m):
    R = ed25519.decodepoint(s[: b // 8])
    # A = decodepoint(pk)
    S = ed25519.decodeint(s[b // 8 : b // 4])
    h = ed25519.Hint(ed25519.encodepoint(R) + pk + m)
    return h, S

if __name__ == "__main__":
    io.recvuntil(b"pk (hex): ")
    pk = bytes.fromhex(io.recvline().decode().strip())
    mess = [b"satu",b"dua"]
    hasil = []
    for i in range(2):
        io.recvuntil(b'command: ')
        io.sendline(b'sign')
        io.recvuntil(b'message (hex): ')
        io.sendline(mess[i].hex().encode())
        hasil.append(bytes.fromhex(io.recvline().decode().strip()))

    h1, s1 = checksign(hasil[0], pk, mess[0])
    h2, s2 = checksign(hasil[1], pk, mess[1])

    s1_s2 = (s1-s2) % l
    a1_a2 = (h1-h2) % l
    a_inv = pow(a1_a2, -1, l)
    a = (s1_s2 * a_inv) % l
    r = (s1 - (h1 * a) % l) % l 

    # new_sign:
    R_new = ed25519.scalarmult_B(r)
    
    print(hasil)

        