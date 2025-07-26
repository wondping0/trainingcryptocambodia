import os

def pkcs7_padding(data, block_size=8):
    """
    PKCS#7 Padding - Most common in cryptography (used in AES/CBC)
    Pads with bytes, each of which is the value of the number of padding bytes added
    """
    padding_length = block_size - (len(data) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    padding = bytes([padding_length] * padding_length)
    return data + padding

def pkcs7_unpadding(padded_data):
    """
    Remove PKCS#7 padding
    """
    padding_length = padded_data[-1]
    return padded_data[:-padding_length]

def ansi_x923_padding(data, block_size=8):
    """
    ANSI X.923 - Pads with zeroes, except for the last byte, 
    which stores the number of padding bytes
    """
    padding_length = block_size - (len(data) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    padding = b'\x00' * (padding_length - 1) + bytes([padding_length])
    return data + padding

def ansi_x923_unpadding(padded_data):
    """
    Remove ANSI X.923 padding
    """
    padding_length = padded_data[-1]
    return padded_data[:-padding_length]

def iso_iec_7816_4_padding(data, block_size=8):
    """
    ISO/IEC 7816-4 - Pads with 0x80 followed by zeroes
    """
    padding_length = block_size - (len(data) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    padding = b'\x80' + b'\x00' * (padding_length - 1)
    return data + padding

def iso_iec_7816_4_unpadding(padded_data):
    """
    Remove ISO/IEC 7816-4 padding
    """
    # Find the last 0x80 byte
    for i in range(len(padded_data) - 1, -1, -1):
        if padded_data[i] == 0x80:
            return padded_data[:i]
    return padded_data

def zero_padding(data, block_size=8):
    """
    Zero Padding (null padding) - Adds 0x00 bytes
    Only safe when the message never ends with 0x00
    """
    padding_length = block_size - (len(data) % block_size)
    if padding_length == 0:
        return data
    
    padding = b'\x00' * padding_length
    return data + padding

def zero_unpadding(padded_data):
    """
    Remove zero padding (remove trailing zeros)
    """
    return padded_data.rstrip(b'\x00')

def bit_padding(data, block_size=8):
    """
    Bit Padding (ISO/IEC 9797-1 Method 2) - Similar to ISO/IEC 7816-4
    Add a single 1 bit (0x80), then 0 bits (0x00) as needed
    """
    return iso_iec_7816_4_padding(data, block_size)

def iso_10126_padding(data, block_size=8):
    """
    ISO 10126 (deprecated) - Add random bytes for padding, 
    except the last byte indicating the padding length
    """
    padding_length = block_size - (len(data) % block_size)
    if padding_length == 0:
        padding_length = block_size
    
    # Generate random bytes for padding (except last byte)
    random_bytes = os.urandom(padding_length - 1)
    padding = random_bytes + bytes([padding_length])
    return data + padding

def iso_10126_unpadding(padded_data):
    """
    Remove ISO 10126 padding
    """
    padding_length = padded_data[-1]
    return padded_data[:-padding_length]

def demonstrate_padding_algorithm(name, padding_func, unpadding_func, data, block_size=8):
    """
    Demonstrate a specific padding algorithm
    """
    print(f"\n🔐 {name}")
    print("-" * 50)
    print(f"Original data: {data}")
    print(f"Original length: {len(data)} bytes")
    print(f"Block size: {block_size} bytes")
    
    # Apply padding
    padded = padding_func(data, block_size)
    print(f"Padded data: {padded}")
    print(f"Padded length: {len(padded)} bytes")
    print(f"Padding bytes: {padded[len(data):]}")
    print(f"Padding as hex: {padded[len(data):].hex()}")
    print(f"Padding as list: {list(padded[len(data):])}")
    
    # Remove padding if unpadding function is provided
    if unpadding_func:
        try:
            unpadded = unpadding_func(padded)
            print(f"Unpadded data: {unpadded}")
            print(f"Unpadding successful: {unpadded == data}")
        except Exception as e:
            print(f"Unpadding error: {e}")

def demonstrate_all_padding_algorithms():
    """
    Demonstrate all padding algorithms with different examples
    """
    print("=" * 60)
    print("PADDING ALGORITHMS DEMONSTRATION")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        (b"YELLOW", 8),      # 6 bytes to 8 (example from description)
        (b"DATA", 8),        # 4 bytes to 8 (example from description)
        (b"HELLO", 8),       # 5 bytes to 8 (example from description)
        (b"TEXT", 8),        # 4 bytes to 8 (example from description)
        (b"ABCDEFGH", 8),    # 8 bytes (full block)
        (b"ABC", 16),        # 3 bytes to 16 (AES block size)
    ]
    
    for i, (data, block_size) in enumerate(test_cases):
        print(f"\n{'='*20} TEST CASE {i+1} {'='*20}")
        print(f"Input: {data} ({len(data)} bytes) -> {block_size} bytes block")
        
        # 1. PKCS#7 Padding
        demonstrate_padding_algorithm(
            "1. PKCS#7 Padding", 
            pkcs7_padding, 
            pkcs7_unpadding, 
            data, 
            block_size
        )
        
        # 2. ANSI X.923
        demonstrate_padding_algorithm(
            "2. ANSI X.923", 
            ansi_x923_padding, 
            ansi_x923_unpadding, 
            data, 
            block_size
        )
        
        # 3. ISO/IEC 7816-4
        demonstrate_padding_algorithm(
            "3. ISO/IEC 7816-4", 
            iso_iec_7816_4_padding, 
            iso_iec_7816_4_unpadding, 
            data, 
            block_size
        )
        
        # 4. Zero Padding
        demonstrate_padding_algorithm(
            "4. Zero Padding", 
            zero_padding, 
            zero_unpadding, 
            data, 
            block_size
        )
        
        # 5. Bit Padding (ISO/IEC 9797-1 Method 2)
        demonstrate_padding_algorithm(
            "5. Bit Padding (ISO/IEC 9797-1 Method 2)", 
            bit_padding, 
            iso_iec_7816_4_unpadding, 
            data, 
            block_size
        )
        
        # 6. ISO 10126 (deprecated)
        demonstrate_padding_algorithm(
            "6. ISO 10126 (deprecated)", 
            iso_10126_padding, 
            iso_10126_unpadding, 
            data, 
            block_size
        )
        
        print("\n" + "="*60)

def specific_examples():
    """
    Show the specific examples mentioned in the requirements
    """
    print("\n" + "="*60)
    print("SPECIFIC EXAMPLES FROM REQUIREMENTS")
    print("="*60)
    
    # PKCS#7 Example: YELLOW (6 bytes) to 8 bytes
    print("\n🔐 PKCS#7 Example:")
    data = b"YELLOW"
    padded = pkcs7_padding(data, 8)
    print(f"YELLOW (6 bytes) -> {padded}")
    print(f"Padding: {padded[6:]} (each byte = 0x02)")
    
    # ANSI X.923 Example: YELLOW (6 bytes) to 8 bytes
    print("\n🔐 ANSI X.923 Example:")
    padded = ansi_x923_padding(data, 8)
    print(f"YELLOW (6 bytes) -> {padded}")
    print(f"Padding: {padded[6:]} (zeros + length)")
    
    # ISO/IEC 7816-4 Example: DATA (4 bytes) to 8 bytes
    print("\n🔐 ISO/IEC 7816-4 Example:")
    data = b"DATA"
    padded = iso_iec_7816_4_padding(data, 8)
    print(f"DATA (4 bytes) -> {padded}")
    print(f"Padding: {padded[4:]} (0x80 + zeros)")
    
    # Zero Padding Example: HELLO (5 bytes) to 8 bytes
    print("\n🔐 Zero Padding Example:")
    data = b"HELLO"
    padded = zero_padding(data, 8)
    print(f"HELLO (5 bytes) -> {padded}")
    print(f"Padding: {padded[5:]} (all zeros)")

# Main execution
if __name__ == "__main__":
    # Show specific examples first
    specific_examples()
    
    # Show comprehensive demonstration
    demonstrate_all_padding_algorithms()
    
    print("\n" + "="*60)
    print("NOTES:")
    print("- PKCS#7 is most commonly used in AES/CBC")
    print("- Zero padding is ambiguous if data ends with 0x00")
    print("- ISO 10126 is deprecated due to unpredictability")
    print("- No padding is used with stream ciphers or AEAD modes")
    print("="*60)
