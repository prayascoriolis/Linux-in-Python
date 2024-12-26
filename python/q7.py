'''7.	Implement a function to generate Pascal's triangle up to n rows.'''

def generate_pascals_triangle(n):
    if n<=0:
        print('enter no. greater than 0')
        return []
    triangle = []
    for row_num in range(n):
        print(row_num)
        row = [1] * (row_num + 1)
        # Each element (except the first and last) is the sum of the two numbers above it
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    n = 5
    triangle = generate_pascals_triangle(n)
    for row in triangle:
        print(row)
