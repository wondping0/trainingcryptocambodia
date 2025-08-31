import secrets, math, struct, hashlib
from decimal import getcontext, Decimal as D
getcontext().prec = 28
# getcontext().prec = 50
xor = lambda A, B: bytes([a ^ b for a, b in zip(A, B)])


class RealNumberGenerator():
    def __init__(self, seed):
        self.state = seed
        # print("seed:",D(self.state))

    def random(self):
        # self.state = D(math.e) * D(self.state) % D(math.pi)
        # print(D(self.state)%D(math.pi))
        print(D(math.e)*D(self.state)%D(math.e))
        print(int(D(math.e)*10**28)*int(D(self.state)*10**28)%int(D(math.e)*10**28))
        print(D(math.e))
        self.state = (D(math.e) * D(self.state)) % D(math.pi)
        # print(D(2*D(self.state))%D(math.pi))
        # print(D(self.state), D(math.e) * D(self.state) % D(math.pi))
        # print(D(str(self.state)))
        # temp = D(str(self.state)+'0'*50)
        # st = 0.4892516661687690683985973010
        # print(D(st))
        # print(D(math.asin(D(math.sin(self.state)))))
        # print(D(math.asin(D(math.sin(0.23232323243423422)))))
        # print(D(math.asin(D(math.sin(1.329923913689877315098295339)))))
        # print(D(math.asin(D(math.sin(1.329923913689875915274736449)))))
        # print(D(math.asin(D(math.sin(0.4892516661687690683985973010)))))
        # # print(D(self.state))
        print("manaj")
        # # print(math.sin(2*D(self.state)))
        # print(math.pi-math.asin(math.sin(self.state)))
        # print(D(math.asin(D(math.sin(D(1*D(self.state)))))))
        # # print(D(math.asin(D(math.sin(D(1*D(self.state)))))/2))
        # print(-math.asin(math.sin(1*D(self.state))))
        # print(math.pi+math.asin(math.sin(1*D(self.state))))
        # print("Lines")
        # print(math.cos(D(self.state)))
        # print(math.fabs(math.sin(D(self.state)) + math.cos(D(self.state))))
        # print(math.sin(D(self.state)) + math.cos(D(self.state)))
        return math.sqrt(math.fabs(math.sin(D(self.state)) + math.cos(D(self.state))))

    def next_bytes(self):
        while True:
            r = self.random()
            B = struct.pack('d', r)
            print(B)
            for b in B:
                yield b


def main():
    # seed = secrets.randbits(48)
    # print(seed)
    seed = 191574590091770
    rng1 = RealNumberGenerator(seed)
    rng2 = RealNumberGenerator(seed)
    mess = b'\x01'*8
    hasil = xor(mess, rng1.next_bytes())
    
    r = struct.unpack('d',xor(mess[:8], hasil[:8]))[0]
    # print(r)
    # getcontext().prec = 50
    sc2 = D(D(D(r**2)**2)-D(1))
    # print(sc2)
    pr_a2 = [
        (math.asin(sc2)),
        -D(math.asin(sc2)),
        (D(math.pi)-D(math.asin(sc2))),
        D(D(math.pi)+D(math.asin(sc2)))
    ]
    print("port")
    for a2 in pr_a2:
        state = D(a2/2)
        print(state)
        tk = (D(state)/D(math.e))
        print(tk)
        # print(state, D(state), (D(math.e) * D(state) % D(math.pi)),end=" ")
        temp = math.sqrt(math.fabs(math.sin(D(state)) + math.cos(D(state))))
        B = struct.pack('d', temp)
        # print(B)
    # print(r)
    print("trying")
    # self.state = (D(math.e) * D(self.state)) % D(math.pi)
    w = D(10)/D(math.pi)
    print(w*D(math.pi))


    # print(xor(b'\x00'*8, rng2.next_bytes()))
    # print(xor(b'\x00'*100, rng2.next_bytes()))
    # flag = open('flag.txt', 'rb').read().strip()

    # msg = b'The flag is: ' + xor(flag, hashlib.shake_256(str(seed).encode()).digest(len(flag)))
    # enc = xor(msg, rng.next_bytes())
    # print(enc.hex())

if __name__ == '__main__':
    main()
