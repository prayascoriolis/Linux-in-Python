'''31. Create a function to solve the Subset Sum problem using recursion and dynamic programming.'''

memo = {}
def permuteRec(arr, index, current_sum, target):

    # if sum is equal to target
    if target == current_sum:
        return True
    # return false index has crossed arr length or cureent sum is > target
    if index >= len(arr) or current_sum > target:
        return False

    # Check if already computed
    if (index, current_sum) in memo:
        return memo[(index, current_sum)]

    # include arr[index] in sum
    include = permuteRec(arr, index+1, current_sum+arr[index], target)
    # exclude arr[index] in sum
    exclude = permuteRec(arr, index+1, current_sum, target)

    # store result in memo
    memo[(index, current_sum)] = include or exclude
    return memo[(index, current_sum)]

if __name__ == "__main__":
    arr = [1,2,3]
    target = 6
    print(permuteRec(arr, 0, 0, target))