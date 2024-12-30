'''12. Develop a program that compresses a string using run-length encoding.'''

def run_length_encode(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    # last character and its count
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

if __name__=="__main__":
    input_string = "babababa"
    encoded_string = run_length_encode(input_string)
    print(f"Compressed: {encoded_string}")
