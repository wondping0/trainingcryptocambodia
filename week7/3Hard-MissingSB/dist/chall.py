from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import *

flag = b'CNCC{REDACTED}'
flag_padded = pad(pad(flag, 16),16)
assert len(flag_padded) % 16 == 0
temp = [flag_padded[i:i+16] for i in range(0, len(flag_padded), 16)]
# print(temp)
from aes import AES
master_key = 0x1f7e151617cbd2a6abf7657109cdeab1
cipher = AES(master_key)
cip = [long_to_bytes(cipher.encrypt(bytes_to_long(i))) for i in temp]
for i in cip:
    print(i.hex())
# af1cb4005097df9cc73478c09c4ac093
# 95fbfe56a5e4ebf5c62937dccd6e8695
# c283067f3d790052e13879c43fe46a96
# f58d9d44dea3a780b91151a8a818fcce