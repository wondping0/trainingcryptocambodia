import random
flag = b'REDACTED'
xor_bytes = lambda a, b: bytes(x ^ y for x, y in zip(a, b))

f = open('data','w')

for i in range(640):
  f.write(str(random.getrandbits(32))+'\n')
key = b''
for i in range(8):
  tr = random.getrandbits(32)
  key += tr.to_bytes(4, "big")
f.write(str(len(key) > len(flag))+'\n')
f.write(xor_bytes(flag, key).hex()+'\n')