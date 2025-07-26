text = b'ThisKindOfanther'

def text_to_aes_blocks(data, block_size=16):
    """
    Convert text to AES blocks (16 bytes each) without padding
    """
    blocks = []
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        blocks.append(block)
    
    return blocks

def display_blocks_as_lists(blocks):
    """
    Display blocks as Python lists
    """
    print("Text as AES Blocks (Lists):")
    print("-" * 40)
    
    for i, block in enumerate(blocks):
        block_list = list(block)
        print(f"Block {i + 1}: {block_list}")
        print(f"Block {i + 1} length: {len(block)} bytes")
        print()

def display_blocks_detailed(blocks):
    """
    Display blocks in multiple formats
    """
    print("Detailed Block Information:")
    print("-" * 40)
    
    for i, block in enumerate(blocks):
        print(f"Block {i + 1}:")
        print(f"  Raw bytes: {block}")
        print(f"  As string: {block.decode('utf-8', errors='ignore')}")
        print(f"  As list:   {list(block)}")
        print(f"  Hex:       {block.hex()}")
        print(f"  Length:    {len(block)} bytes")
        print()

# Main execution
if __name__ == "__main__":
    print(f"Original text: {text}")
    print(f"Text length: {len(text)} bytes")
    print(f"Text as string: '{text.decode()}'")
    print()
    
    # Convert to AES blocks
    aes_blocks = text_to_aes_blocks(text)
    
    print(f"Number of blocks: {len(aes_blocks)}")
    print()
    
    # Display blocks as lists (main request)
    display_blocks_as_lists(aes_blocks)
    
    # Display detailed information
    display_blocks_detailed(aes_blocks)
