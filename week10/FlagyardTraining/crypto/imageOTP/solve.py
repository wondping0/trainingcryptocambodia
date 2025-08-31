from Crypto.Util.number import long_to_bytes, bytes_to_long

p1 = open("tux_clear.bmp","rb").read()
c1 = open("tux.bmp.enc","rb").read()
g1 = open("flag.bmp.enc","rb").read()

def xorbytes(a, b):
    return long_to_bytes(bytes_to_long(a)^bytes_to_long(b))

if __name__ == "__main__":
    assert len(p1)==len(c1)
    key = xorbytes(p1, c1)
    flag = xorbytes(g1, key)
    open("flag.bmp","wb").write(flag)
    print("done and got flag")