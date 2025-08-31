import secrets

import ed25519


sk = secrets.token_bytes(16)
sk1 = secrets.token_bytes(16)
pk = ed25519.publickey_unsafe(sk)
pk1 = ed25519.publickey_unsafe(sk1)

for i in range(100):
    try:
        MESSAGE = secrets.token_bytes(16)
        sig = ed25519.signature_unsafe(MESSAGE, sk, pk)
        ed25519.checkvalid(sig, MESSAGE, pk)
        print("Validd")
    except:
        pass
    exit(1)
    
    # if(hasil): print("Found!!")
    # else: 
    #     print("bisa bang")

# sig2 = ed25519.signature_unsafe(b"2016 Q1", sk, pk)
# ed25519.checkvalid(sig, MESSAGE, pk)
# print(sig)
# print(sig2)