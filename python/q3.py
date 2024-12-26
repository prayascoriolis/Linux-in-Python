'''3.	Write a program to find the transpose of a matrix.'''

def two_d_matrix(matrix):
    for x in matrix:
        for y in x:
            print(y, end=" ")
        print('\n')

def get_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transpose_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3], [11, 21, 31], [12, 22, 32]]
    print('Before transpose:\n')
    two_d_matrix(matrix)
    matrix = get_transpose(matrix)
    print('After transpose:\n')
    two_d_matrix(matrix)
