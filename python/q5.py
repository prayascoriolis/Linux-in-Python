'''5.	Write a program to check if two strings are anagrams of each other.'''

def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    str1="listen"
    str2="silent"
    print('YES') if check_anagrams(str1, str2) is True else print('NO')