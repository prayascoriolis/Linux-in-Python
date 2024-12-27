'''14. Create a program that checks if a string is a valid palindrome, ignoring spaces and punctuation.'''

import re

def is_palindrome(input_str):
    # Remove spaces and non-alphabetic characters, and convert to lowercase
    normalized_str = re.sub(r'[^a-zA-Z]', '', input_str).lower()
    return normalized_str == normalized_str[::-1]

input_str = "A man, a plan, a canal, Panama"
print(is_palindrome(input_str))