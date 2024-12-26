'''9.	Create a function that finds the mode (most frequent element) in a list.'''

def find_mode(lst):
    if not lst:
        return None
    # dictionary to count occurrences of each element
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    # Find the maximum frequency
    max_freq = max(frequency.values())
    # if more than 1 string with maximum frequency
    mode = [key for key, value in frequency.items() if value == max_freq]
    return mode

if __name__=="__main__":
    numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]
    print(f"Mode: {find_mode(numbers)}")