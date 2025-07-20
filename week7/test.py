from aes import AES

if __name__=="__main__":
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    plaintext = 0x3243f6a8885a308d313198a2e0370734

    aes = AES(key)
    ciphertext = aes.encrypt(plaintext)

    print("Ciphertext:", hex(ciphertext))