'''16. Develop a script to generate all permutations of a list.'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def permuteRec(arr, idx):

    if idx == len(arr) - 1:
        print(arr)
        return

    for i in range(idx, len(arr)):
        # Swapping
        arr = swap(arr, idx, i)
        # First idx+1 characters fixed
        permuteRec(arr, idx + 1)
        # Backtrack
        arr = swap(arr, idx, i)

if __name__ == "__main__":
    arr = [1,2,3]
    permuteRec(arr, 0)