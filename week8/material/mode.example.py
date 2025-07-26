from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def demonstrate_ecb_mode():
    """
    Electronic Codebook (ECB) Mode
    Formula: Yi = F(PlainTexti, Key)
    Ciphertext: Yi
    """
    print("\n🔐 ELECTRONIC CODEBOOK (ECB) MODE")
    print("=" * 50)
    print("Formula: Yi = F(PlainTexti, Key)")
    print("Each block is encrypted independently")
    print("⚠️  WARNING: Not secure for real use - identical blocks produce identical ciphertext")
    
    # Setup
    key = get_random_bytes(16)  # 128-bit key
    plaintext = b"Hello World! This is a test message for ECB mode demonstration."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext length: {len(plaintext)} bytes")
    
    # Padding
    padded_plaintext = pad(plaintext, AES.block_size)
    print(f"Padded plaintext: {padded_plaintext}")
    print(f"Padded length: {len(padded_plaintext)} bytes")
    
    # Encryption
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_plaintext)
    
    print(f"\nCiphertext: {binascii.hexlify(ciphertext).decode()}")
    print(f"Ciphertext length: {len(ciphertext)} bytes")
    
    # Show blocks
    print("\nBlock-by-block encryption:")
    for i in range(0, len(padded_plaintext), AES.block_size):
        block = padded_plaintext[i:i+AES.block_size]
        cipher_block = ciphertext[i:i+AES.block_size]
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Plaintext:  {block}")
        print(f"  Ciphertext: {binascii.hexlify(cipher_block).decode()}")
    
    # Decryption
    cipher_decrypt = AES.new(key, AES.MODE_ECB)
    decrypted_padded = cipher_decrypt.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, AES.block_size)
    
    print(f"\nDecrypted: {decrypted}")
    print(f"Decryption successful: {decrypted == plaintext}")
    
    return key, plaintext, ciphertext

def demonstrate_cbc_mode():
    """
    Cipher Block Chaining (CBC) Mode
    Formula: Yi = PlainTexti XOR Ciphertexti-1
    Ciphertext: F(Yi, Key); Ciphertext0 = IV
    """
    print("\n🔐 CIPHER BLOCK CHAINING (CBC) MODE")
    print("=" * 50)
    print("Formula: Yi = PlainTexti XOR Ciphertexti-1")
    print("Each block depends on all previous blocks")
    print("Uses Initialization Vector (IV)")
    
    # Setup
    key = get_random_bytes(16)  # 128-bit key
    iv = get_random_bytes(16)   # 128-bit IV
    plaintext = b"CBC mode chains blocks together using XOR operations."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"IV:  {binascii.hexlify(iv).decode()}")
    print(f"Plaintext: {plaintext}")
    
    # Padding
    padded_plaintext = pad(plaintext, AES.block_size)
    print(f"Padded plaintext: {padded_plaintext}")
    
    # Encryption
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)
    
    print(f"\nCiphertext: {binascii.hexlify(ciphertext).decode()}")
    
    # Manual demonstration of CBC chaining
    print("\nCBC Chaining demonstration:")
    previous_block = iv
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    
    for i in range(0, len(padded_plaintext), AES.block_size):
        plaintext_block = padded_plaintext[i:i+AES.block_size]
        
        # XOR with previous ciphertext block (or IV for first block)
        xor_input = bytes(a ^ b for a, b in zip(plaintext_block, previous_block))
        
        # Encrypt the XOR result
        cipher_block = cipher_ecb.encrypt(xor_input)
        previous_block = cipher_block
        
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Plaintext:     {plaintext_block}")
        print(f"  Previous/IV:   {previous_block if i == 0 else ciphertext[i-AES.block_size:i]}")
        print(f"  XOR input:     {xor_input}")
        print(f"  Ciphertext:    {binascii.hexlify(cipher_block).decode()}")
    
    # Decryption
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher_decrypt.decrypt(ciphertext)
    decrypted = unpad(decrypted_padded, AES.block_size)
    
    print(f"\nDecrypted: {decrypted}")
    print(f"Decryption successful: {decrypted == plaintext}")
    
    return key, iv, plaintext, ciphertext

def demonstrate_pcbc_mode():
    """
    Propagating Cipher Block Chaining (PCBC) Mode
    Formula: Yi = PlainTexti XOR (Ciphertexti-1 XOR PlainTexti-1)
    Ciphertext: F(Yi, Key); Ciphertext0 = IV
    """
    print("\n🔐 PROPAGATING CIPHER BLOCK CHAINING (PCBC) MODE")
    print("=" * 50)
    print("Formula: Yi = PlainTexti XOR (Ciphertexti-1 XOR PlainTexti-1)")
    print("⚠️  Note: PCBC is not directly supported in PyCryptodome")
    print("This is a manual implementation for demonstration")
    
    # Setup
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    plaintext = b"PCBC propagates both plaintext and ciphertext."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"IV:  {binascii.hexlify(iv).decode()}")
    print(f"Plaintext: {plaintext}")
    
    # Padding
    padded_plaintext = pad(plaintext, AES.block_size)
    print(f"Padded plaintext: {padded_plaintext}")
    
    # Manual PCBC encryption
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext_blocks = []
    previous_cipher = iv
    previous_plain = b'\x00' * AES.block_size  # Initial value
    
    print("\nPCBC Encryption process:")
    for i in range(0, len(padded_plaintext), AES.block_size):
        plaintext_block = padded_plaintext[i:i+AES.block_size]
        
        # PCBC XOR: current_plain XOR (previous_cipher XOR previous_plain)
        if i == 0:
            xor_input = bytes(a ^ b for a, b in zip(plaintext_block, previous_cipher))
        else:
            feedback = bytes(a ^ b for a, b in zip(previous_cipher, previous_plain))
            xor_input = bytes(a ^ b for a, b in zip(plaintext_block, feedback))
        
        # Encrypt
        cipher_block = cipher_ecb.encrypt(xor_input)
        ciphertext_blocks.append(cipher_block)
        
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Plaintext:       {plaintext_block}")
        print(f"  Previous cipher: {binascii.hexlify(previous_cipher).decode()}")
        print(f"  Previous plain:  {binascii.hexlify(previous_plain).decode()}")
        print(f"  XOR input:       {binascii.hexlify(xor_input).decode()}")
        print(f"  Ciphertext:      {binascii.hexlify(cipher_block).decode()}")
        
        # Update for next iteration
        previous_cipher = cipher_block
        previous_plain = plaintext_block
    
    ciphertext = b''.join(ciphertext_blocks)
    print(f"\nFinal ciphertext: {binascii.hexlify(ciphertext).decode()}")
    
    return key, iv, plaintext, ciphertext

def demonstrate_cfb_mode():
    """
    Cipher Feedback (CFB) Mode
    Formula: Yi = Ciphertexti-1
    Ciphertext: Plaintext XOR F(Yi, Key); Ciphertext0 = IV
    """
    print("\n🔐 CIPHER FEEDBACK (CFB) MODE")
    print("=" * 50)
    print("Formula: Yi = Ciphertexti-1")
    print("Ciphertext: Plaintext XOR F(Yi, Key)")
    print("Converts block cipher into stream cipher")
    
    # Setup
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    plaintext = b"CFB mode creates a stream cipher from block cipher."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"IV:  {binascii.hexlify(iv).decode()}")
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext length: {len(plaintext)} bytes (no padding needed)")
    
    # Encryption
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    
    print(f"\nCiphertext: {binascii.hexlify(ciphertext).decode()}")
    
    # Manual demonstration of CFB
    print("\nCFB process demonstration:")
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    previous_cipher = iv
    manual_ciphertext = b''
    
    for i in range(0, len(plaintext), AES.block_size):
        plaintext_block = plaintext[i:i+AES.block_size]
        
        # Encrypt the previous ciphertext block (or IV)
        keystream = cipher_ecb.encrypt(previous_cipher)
        
        # XOR with plaintext
        cipher_block = bytes(a ^ b for a, b in zip(plaintext_block, keystream[:len(plaintext_block)]))
        manual_ciphertext += cipher_block
        
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Previous cipher: {binascii.hexlify(previous_cipher).decode()}")
        print(f"  Keystream:       {binascii.hexlify(keystream[:len(plaintext_block)]).decode()}")
        print(f"  Plaintext:       {plaintext_block}")
        print(f"  Ciphertext:      {binascii.hexlify(cipher_block).decode()}")
        
        # Update for next iteration (pad cipher block to full block size)
        if len(cipher_block) < AES.block_size:
            previous_cipher = cipher_block + previous_cipher[len(cipher_block):]
        else:
            previous_cipher = cipher_block
    
    # Decryption
    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv)
    decrypted = cipher_decrypt.decrypt(ciphertext)
    
    print(f"\nDecrypted: {decrypted}")
    print(f"Decryption successful: {decrypted == plaintext}")
    
    return key, iv, plaintext, ciphertext

def demonstrate_ofb_mode():
    """
    Output Feedback (OFB) Mode
    Formula: Yi = F(Yi-1, Key); Y0 = F(IV, Key)
    Ciphertext: Plaintext XOR Yi
    """
    print("\n🔐 OUTPUT FEEDBACK (OFB) MODE")
    print("=" * 50)
    print("Formula: Yi = F(Yi-1, Key); Y0 = F(IV, Key)")
    print("Ciphertext: Plaintext XOR Yi")
    print("Creates a keystream independent of plaintext")
    
    # Setup
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    plaintext = b"OFB mode generates keystream independently."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"IV:  {binascii.hexlify(iv).decode()}")
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext length: {len(plaintext)} bytes (no padding needed)")
    
    # Encryption
    cipher = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    
    print(f"\nCiphertext: {binascii.hexlify(ciphertext).decode()}")
    
    # Manual demonstration of OFB
    print("\nOFB process demonstration:")
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    keystream_input = iv
    manual_ciphertext = b''
    
    for i in range(0, len(plaintext), AES.block_size):
        plaintext_block = plaintext[i:i+AES.block_size]
        
        # Generate keystream by encrypting the keystream input
        keystream_block = cipher_ecb.encrypt(keystream_input)
        
        # XOR with plaintext
        cipher_block = bytes(a ^ b for a, b in zip(plaintext_block, keystream_block[:len(plaintext_block)]))
        manual_ciphertext += cipher_block
        
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Keystream input: {binascii.hexlify(keystream_input).decode()}")
        print(f"  Keystream:       {binascii.hexlify(keystream_block[:len(plaintext_block)]).decode()}")
        print(f"  Plaintext:       {plaintext_block}")
        print(f"  Ciphertext:      {binascii.hexlify(cipher_block).decode()}")
        
        # Next keystream input is the current keystream output
        keystream_input = keystream_block
    
    # Decryption
    cipher_decrypt = AES.new(key, AES.MODE_OFB, iv)
    decrypted = cipher_decrypt.decrypt(ciphertext)
    
    print(f"\nDecrypted: {decrypted}")
    print(f"Decryption successful: {decrypted == plaintext}")
    
    return key, iv, plaintext, ciphertext

def demonstrate_ctr_mode():
    """
    Counter (CTR) Mode
    Formula: Yi = F(IV + g(i), Key); IV = token()
    Ciphertext: Plaintext XOR Yi
    """
    print("\n🔐 COUNTER (CTR) MODE")
    print("=" * 50)
    print("Formula: Yi = F(IV + g(i), Key); IV = token()")
    print("Ciphertext: Plaintext XOR Yi")
    print("Uses counter that increments for each block")
    
    # Setup
    key = get_random_bytes(16)
    nonce = get_random_bytes(8)  # CTR uses nonce, not full IV
    plaintext = b"CTR mode uses counter for keystream generation."
    
    print(f"\nKey: {binascii.hexlify(key).decode()}")
    print(f"Nonce: {binascii.hexlify(nonce).decode()}")
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext length: {len(plaintext)} bytes (no padding needed)")
    
    # Encryption
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext)
    
    print(f"\nCiphertext: {binascii.hexlify(ciphertext).decode()}")
    
    # Manual demonstration of CTR
    print("\nCTR process demonstration:")
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    manual_ciphertext = b''
    
    for i in range(0, len(plaintext), AES.block_size):
        plaintext_block = plaintext[i:i+AES.block_size]
        
        # Create counter block (nonce + counter)
        counter = (i // AES.block_size).to_bytes(8, byteorder='big')
        counter_block = nonce + counter
        
        # Generate keystream by encrypting counter
        keystream_block = cipher_ecb.encrypt(counter_block)
        
        # XOR with plaintext
        cipher_block = bytes(a ^ b for a, b in zip(plaintext_block, keystream_block[:len(plaintext_block)]))
        manual_ciphertext += cipher_block
        
        print(f"Block {i//AES.block_size + 1}:")
        print(f"  Counter:         {counter.hex()}")
        print(f"  Counter block:   {binascii.hexlify(counter_block).decode()}")
        print(f"  Keystream:       {binascii.hexlify(keystream_block[:len(plaintext_block)]).decode()}")
        print(f"  Plaintext:       {plaintext_block}")
        print(f"  Ciphertext:      {binascii.hexlify(cipher_block).decode()}")
    
    # Decryption
    cipher_decrypt = AES.new(key, AES.MODE_CTR, nonce=nonce)
    decrypted = cipher_decrypt.decrypt(ciphertext)
    
    print(f"\nDecrypted: {decrypted}")
    print(f"Decryption successful: {decrypted == plaintext}")
    
    return key, nonce, plaintext, ciphertext

def compare_modes():
    """
    Compare different AES modes
    """
    print("\n" + "="*60)
    print("AES MODES COMPARISON")
    print("="*60)
    
    print("\n📊 Mode Characteristics:")
    print("-" * 40)
    print("ECB: Simple, parallel, NOT secure (identical blocks)")
    print("CBC: Sequential, secure, requires padding")
    print("PCBC: Propagates errors, rarely used")
    print("CFB: Stream cipher, no padding, sequential")
    print("OFB: Stream cipher, no padding, keystream independent")
    print("CTR: Stream cipher, no padding, parallel, most flexible")
    
    print("\n🔒 Security Recommendations:")
    print("-" * 40)
    print("✅ RECOMMENDED: CBC, CFB, OFB, CTR")
    print("❌ NOT RECOMMENDED: ECB (except for single blocks)")
    print("⚠️  RARELY USED: PCBC")
    
    print("\n⚡ Performance Characteristics:")
    print("-" * 40)
    print("Parallel encryption: ECB, CTR")
    print("Sequential only: CBC, PCBC, CFB, OFB")
    print("No padding needed: CFB, OFB, CTR")
    print("Requires padding: ECB, CBC, PCBC")

def main():
    """
    Main demonstration function
    """
    print("AES ENCRYPTION MODES DEMONSTRATION")
    print("Using PyCryptodome library")
    print("="*60)
    
    # Demonstrate each mode
    demonstrate_ecb_mode()
    demonstrate_cbc_mode()
    demonstrate_pcbc_mode()
    demonstrate_cfb_mode()
    demonstrate_ofb_mode()
    demonstrate_ctr_mode()
    
    # Compare modes
    compare_modes()
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETE")
    print("All modes have been demonstrated with AES encryption")
    print("="*60)

if __name__ == "__main__":
    main()
