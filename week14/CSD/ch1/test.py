import random
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()

for i in range(640):
  x = random.getrandbits(32)
  predictor.setrandbits(x, 32)

key = b''
key2 = b''
for i in range(8):
  tr = random.getrandbits(32)
  tr2 = predictor.getrandbits(32)
  key += tr.to_bytes(4, "big")
  key2 += tr2.to_bytes(4, "big")
  
print(key.hex())
print(key2.hex())
# f.write(str(len(key) > len(flag))+'\n')
# f.write(xor_bytes(flag, key).hex()+'\n')