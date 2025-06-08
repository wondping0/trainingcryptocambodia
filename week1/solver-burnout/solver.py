from pwn import xor

enc1 = open("enc.enc", "rb").read()
enc2 = open("teach.txt", "rb").read()
enc3 = open("three.png", "rb").read()
# [1, 1, 0, 0] A
# [0, 1, 0, 1] B
# [1, 0, 0, 1] Result

# A B C D E F
# X W Y Z

# RESULT=
# A B C D E F G H I J K L
# X W Y Z X W Y Z X W Y Z

flag = xor(xor(enc1, enc2), enc3) 
print("final result length:", len(flag))
with open("output", "wb") as f:
    f.write(flag)
