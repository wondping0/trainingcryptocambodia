import operator
import hashlib


indexbytes = operator.getitem

def bit(h, i):
    return (indexbytes(h, i // 8) >> (i % 8)) & 1

def H(m):
    out = bytes()
    for i in range(4):
        out += hashlib.md5(m + bytes([i])).digest()
    return out

def reverse_a_to_c(a, b=256):
    """
    Recover c value from a value.
    
    Given:
    - a = 2 ** (b - 2) + sum(2**i * bit(h, i) for i in range(3, b - 2))
    - c = [indexbytes(h, j) for j in range(b // 8, b // 4)]
    
    We need to extract the relevant bits from 'a' to reconstruct 'c'.
    
    Args:
        a: The integer value
        b: The bit parameter (default 256)
    
    Returns:
        list: The c values
    """
    # First, subtract the fixed part: 2 ** (b - 2)
    remaining = a - (2 ** (b - 2))
    
    # Create a byte array to store the reconstructed h
    # We need 64 bytes total since c accesses indices 32-63
    h_bytes = bytearray(b // 4)  # 64 bytes for b=256
    
    # Extract bits from the remaining value and set them in h_bytes
    for i in range(3, b - 2):  # range(3, 254)
        if remaining & (2 ** i):
            # Set the bit in the appropriate byte and position
            byte_index = i // 8
            bit_position = i % 8
            if byte_index < len(h_bytes):
                h_bytes[byte_index] |= (1 << bit_position)
    
    # Extract c values: c = [indexbytes(h, j) for j in range(b // 8, b // 4)]
    # For b=256: range(32, 64)
    c = []
    for j in range(b // 8, b // 4):  # range(32, 64)
        c.append(h_bytes[j])
    
    return c

h = H(b'1111')

# Test the reverse function
print("Original h:", h.hex())
print("h length:", len(h), "bytes")
print("Original a:", end=" ")

b = 256
a = 2 ** (b - 2) + sum(2**i * bit(h, i) for i in range(3, b - 2))
c = [indexbytes(h, j) for j in range(b // 8, b // 4)]
print(a)
print("Original c:", c)
print("c comes from bytes", b // 8, "to", b // 4 - 1, "(indices 32-63)")
print("a encodes bits 3 to", b - 3, "(bits 3-253)")
print("Bit range 3-253 covers bytes", 3 // 8, "to", (b - 3) // 8, "(indices 0-31)")

# Since a only encodes bits 3-253 (bytes 0-31) and c needs bytes 32-63,
# we cannot recover c from a alone - they don't overlap!

print("\nProblem: 'a' encodes information from bytes 0-31, but 'c' needs bytes 32-63")
print("These ranges don't overlap, so we cannot recover 'c' from 'a' alone.")

print("h bytes:", h)
print("a value:", a)