'''16. Develop a script to generate all permutations of a list.'''

def generate_permutations(arr):
    def permutation_process(current, remaining):
        if len(remaining) == 0:
            permutations.append(current)
        for i in range(len(remaining)):
            permutation_process(current + [remaining[i]], remaining[:i] + remaining[i+1:])

    permutations = []
    permutation_process([], arr)
    return permutations

if __name__ == "__main__":
    data = [1, 2, 3]
    result = generate_permutations(data)
    print("All permutations:")
    for perm in result:
        print(perm)
