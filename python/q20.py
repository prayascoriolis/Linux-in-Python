'''20. Write a program to encrypt and decrypt text using the RSA algorithm.'''

import random
from math import gcd

def generate_keys():
    # two distinct large prime numbers
    p = 61
    q = 53
    
    n = p * q
    # Euler's totient function: it tells us how many no.s are smaller than n and co prime to n
    # every no. below a prime no. is co prime to the prime no.
    phi_n = (p - 1) * (q - 1)
    
    # Choose an integer e (public component) such that  1 < 𝑒 < phi_n, 
    # and e is coprime with phi_n (i.e., gcd (e, phi_n) = 1)
    e = 17

    # Calculate d (private exponent), 𝑑 × 𝑒 ≡ 1.(mod(phi_n))
    # The modular inverse of e w.r.t phi_n:
    # This means that when you multiply d by e and divide the result by phi_n, the remainder (or modulus) will be 1.
    d = mod_inverse(e, phi_n)

    # Public key (e, n), Private key (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def mod_inverse(e, phi_n):
    # find the modular inverse
    for d in range(3, phi_n):
        if (d*e) % phi_n==1:
            return d
    raise ValueError ("mod inverse does not exsist")

def encrypt(public_key, message):
    e, n = public_key
    # Convert each character to its ASCII value, encrypt and return the result
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(private_key, encrypted_msg):
    d, n = private_key
    # Decrypt each number and convert back to character
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

if __name__ == "__main__":
    # Generate public and private keys
    public_key, private_key = generate_keys()
    message = "HELLO123"
    print(f"Original message: {message}")
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")
