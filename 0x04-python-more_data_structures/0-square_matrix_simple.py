#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Check if the input matrix is empty
    if not matrix:
        return []

    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with the same dimensions as the input matrix
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Loop through each element in the input matrix and square it
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

