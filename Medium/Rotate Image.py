matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    top = 0
    bottom = len(matrix) - 1
    while bottom > top:
        matrix[bottom][i], matrix[top][i] = matrix[top][i], matrix[bottom][i]
        top += 1
        bottom -= 1
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
print(matrix)