# # transpositition

# FLAG = 'THISWASFLAG'

# # enc = FLAG[3:] + FLAG[:3] 
# # enc = FLAG[::-1]

# FLAG1 = 'THISWA' #-> 6 letter
# FLAG2 = 'SFLAG ' #-> 5 letter

# key = [1,4,3,2,5,0]

# ENC1 = [0]*6
# ENC2 = [0]*6
# for i in range(len(key)):
#     ENC1[key[i]] = FLAG1[i]
#     ENC2[key[i]] = FLAG2[i]

# enc = ''.join(ENC1) + ''.join(ENC2)
# print(enc)

# subtitution


FLAG = 'CAESARCIPHERKNOWLEDGE'

key = 13
# key = 3-13-11
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# DEFGHIJKLMNOPQRSTUVWXYZABC

# ENC = 'FDHV ...'

def caesar(x, key):
    ret = ""
    for i in x:
        ret += chr((((ord(i) - ord('A')) + key) % 26) + ord('A'))
    return ret

enc = caesar(FLAG, key)
print("encryption text:", enc)