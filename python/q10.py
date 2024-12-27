'''10. Write a script to find the longest common prefix of a list of strings.'''

def longest_common_prefix(strings):
    try:
        # first string as the potential prefix
        prefix = strings[0]
        for string in strings[1:]:
            # Compare the prefix with each string and shorten it if necessary
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1] # up to but not including the last character.
                if len(prefix) == 0:
                    return "Doesn't exsist"
        return prefix
    except Exception as e:
        print('Error: ', e)

if __name__ == "__main__":
    string_lists = [
        ["prayas", "prajinay", "pratap"],
        ["ndjscn", "qjdod", "jsj"]
    ]
    
    for strings in string_lists:
        print(f"Strings: {strings}")
        print(f"Longest Common Prefix: {longest_common_prefix(strings)}\n")
