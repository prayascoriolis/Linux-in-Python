'''26. Implement a script to simulate a file compression algorithm (e.g., Huffman coding).'''

import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Whenever the HuffmanNode objects are inserted into a heap (heapq.heappush() or heapq.heapify()),
    # Python will use the __lt__ method to compare nodes and organize them in the heap.
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # count character frequency
    freq = Counter(text)
    # single-node priority queue
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    # A min-heap (node with the smallest frequency is at the root (index 0) of the heap)
    heapq.heapify(heap)
    # Build the Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged) # appended back at end of priority queue
    return heap[0]  # root of the tree

def build_huffman_codes(root, code="", codes={}):
    # assigning code to Leaf node
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = code
    # Traverse
    build_huffman_codes(root.left, code + "0", codes) # left subtree
    build_huffman_codes(root.right, code + "1", codes) # right subtree
    return codes

def encode(text, codes):
    # returns a binary string
    return ''.join(codes[char] for char in text)

def decode_text(encoded_text, codes):
    # Reverse the codes dictionary to map encoded sequences to characters
    reverse_codes = {value: key for key, value in codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:  # found a matching code
            decoded_text += reverse_codes[current_code]
            current_code = ""  # reset for the next iteration
    return decoded_text

def get_byte_array(encoded_text):
    # Byte arrays are compact, storing 8 bits per byte, 
    # while binary strings use a character ('0' or '1') 
    # i.e, 1 byte for each char, consuming more memory.
    b_arr = bytearray()
    # iterating binary string with 8 char at a time
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        b_arr.append(int(byte, 2)) # convert binary to decimal
    return b_arr

def compress(encoded_text, file_path):
    # making & saving compressed file
    output_path = file_path.replace(".txt", "_compressed.bin")
    with open(output_path, 'wb') as output:
        output.write(get_byte_array(encoded_text))
    print(f"Compressed file saved at: {output_path}")
    return output_path

def decompress(input_path, codes):
    with open(input_path, 'rb') as file:
        bit_string = ""
        byte = file.read(1) # reads a single byte from the file
        while byte:
            byte = ord(byte) # converts a single-byte binary data to corresponding decimal int.
            bits = bin(byte)[2:].rjust(8, '0') # convert decimal to binary
            bit_string += bits
            byte = file.read(1)
    # convert text from binary to raw text
    decompressed_text = decode_text(bit_string, codes)
    # making & saving decompressed file
    output_path = input_path.replace("_compressed.bin", "_decompressed.txt")
    with open(output_path, 'w') as output:
        output.write(decompressed_text)
    print(f"Decompressed file saved at: {output_path}")

if __name__ == "__main__":

    # reading .txt file
    file_path = "dir/huffman.txt"
    with open(file_path, 'r') as file:
        text = file.read()

    # Build Huffman Tree and Codes
    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)

    # Encode the text
    encoded_text = encode(text, codes)

    # compress
    output_path = compress(encoded_text, file_path)

    # decompressing
    decompress(output_path, codes)
