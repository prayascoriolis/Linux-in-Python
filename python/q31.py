'''31. Create a function to solve the Subset Sum problem using recursion and dynamic programming.'''

def permuteRec(arr, idx, sum1, sum_arr):
    if idx == len(arr):
        sum_arr.append(sum1)
        return
    permuteRec(arr, idx+1, sum1+arr[idx], sum_arr)
    permuteRec(arr, idx+1, sum1, sum_arr)

if __name__ == "__main__":
    arr = [1,2,3]
    sum_arr=[]
    permuteRec(arr, 0, 0, sum_arr)
    print(sorted(sum_arr))