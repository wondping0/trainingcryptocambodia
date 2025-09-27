enc = b'N\xcdV\x03d\x8f\x96x\xc8 6\xb8I\xe2\x9b\x94\xea\xef<\xd1\xdfx9\x13SC#\x15c\xd5\xb5\xf9\x16\x96D\x12"\x80\xdcd\x9cz!\xfdP\xe1\x97\xd4\xe4\xfc=\xc9\xdas6\x04\x11J.@w\x8a\xe2\xaeC\x80'

def xor_bytes(a, b):
    if len(a) < len(b):
        a = len(b) // len(a) * a + a[:len(b) % len(a)]
    elif len(b) < len(a):
        b = len(a) // len(b) * b + b[:len(a) % len(b)]
    
    return bytes(x ^ y for x, y in zip(a, b))

suffix = b'https://gist.github.com/wondping0/'
key = xor_bytes(enc[:32], suffix[:32])

flag = xor_bytes(enc, key)
print(flag)