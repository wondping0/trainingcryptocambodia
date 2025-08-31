p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
K = GF(p)
a = K(0x0000000000000000000000000000000000000000000000000000000000000000)
b = K(0x0000000000000000000000000000000000000000000000000000000000000007)
E = EllipticCurve(K, (a, b))
G = E(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
E.set_order(0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 * 0x1)

key = 8671863972918644020891893592264002636093783139480427895849310236719348461381201964156671118636441836060545823975787713255918690787156950587491048317621367
publik = G*key

k1 = 7107248759369583645199803455182591408419807886664892570248268912988152997296738707525728292531494273967624165497625607692935228944726023953531942664870243

difft = 262352607692351500239567664846202472581
k2 = k1 + difft

q = E.order()

def recv(sign1, sign2, h1, h2, diff):
    r1, s1 = sign1
    r2, s2 = sign2
    k1 = ((int(r1) * h2 - int(r1) * int(s2) * diff - int(r2) * h1) * pow((int(r1) * int(s2) - int(s1) * r2), -1, q)) %q
    return k1

def sign(m, k, sk, pk):
    r = k*G
    rx = int(r.xy()[0])
    s = (int(pow(k, -1, q)) * (m + (rx * sk) % q ) % q ) % q
    return rx, s

def verify(m, r, s, pk):
    print(GCD(s, q))
    s1 = int(pow(s, -1, q))
    R_ = ((m * s1) * G) + (r * s1) * pk
    print(R_.xy()[0])
    return int(r) == int(R_.xy()[0])

sg1 = sign(123, k1, key, publik)
sg2 = sign(1234, k2, key, publik)
#print(sg1) 
ver1 = verify(123, sg1[0], sg1[1], publik)
ver2 = verify(1234, sg2[0], sg2[1], publik)
#print(ver1)
#print(ver2)
recov = recv(sg1, sg2, 123, 1234, difft)
#print(recov)
#print(k1%q)

m1 = 123
m2 = 1234
r1 = sg1[0]
r2 = sg2[0]
s1 = sg1[1]
s2 = sg2[1]
# dec
df = (m2 * r1 - m1 * r2) % q
koef1 = (s2 * r1) % q
koef2 = (s1 * r2) % q
print("Delegations!!")
print(df)
print(koef1)
print(koef2)
print("\n")
print("Rules")
inv_koef1 = int(pow(koef1, -1, q))
base_1 = (df * inv_koef1) % q
base_2 = (koef2 * inv_koef1) % q
print(base_1)
print(base_2)

print((base_2 * k1 + base_1)%q)
print(k2%q)
print("founded cores!!")
intv = (s1 * r2 - base_2 * s2 * r1)
print(intv)
print(gcd(intv, q))
kk = ((m1 * r2 + s2 * base_1 * r1 - m2 * r1) % q * int(pow(intv, -1, q))) % q
print(kk)
print(k1%q)