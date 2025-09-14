from pwn import xor

enc = "3128ed89d5df5adf8028438e105ba9b905bbc43ade47a0814baa4261d1689947a3aa175acca6046e7165a311d4304a1b1a753f3d9f292d3b0ebee416db0ce545561e6956082ab3c9401ccef0542c0178"
split_enc = [bytes.fromhex(enc[i:i+32]) for i in range(0, len(enc), 32)]

print(len(split_enc[-1]))

enccounter = xor(split_enc[-1], b'\x10'*16)
flag = b''

for i in range(len(split_enc)):
    flag += xor(split_enc[i], enccounter)

print(flag)