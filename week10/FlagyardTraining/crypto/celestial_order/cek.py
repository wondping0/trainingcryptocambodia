import hashlib

import HashTools
from os import urandom

# setup context

c1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
c2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
secret = c1.encode()
original_data = b""
sig = HashTools.new(algorithm="md5", raw=secret+original_data).hexdigest()

# attack
append_data = b""
magic = HashTools.new("md5")
new_data, new_sig = magic.extension(
    secret_length=len(c1), original_data=original_data,
    append_data=append_data, signature=sig
)

print((c1.encode()+new_data).hex())
print((c2.encode()+new_data).hex())
print(new_sig)
print(hashlib.md5(c2.encode()+new_data).hexdigest())

# c1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
# c2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"

# print(hashlib.md5(c1.encode()).hexdigest())
# print(hashlib.md5(c2.encode()).hexdigest())

# print(len(c1))
# print(len(c2))