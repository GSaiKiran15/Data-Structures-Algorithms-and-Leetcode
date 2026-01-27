matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(matrix)
cols = len(matrix[0])
n = len(matrix)-1
for r in range(rows):
    for c in range(cols):
        if type(matrix[c][n]) != list:
            print(type(matrix[r][c]), matrix[r][c], matrix[c][n])
            if type(matrix[r][c]) != list:
                matrix[c][n] = [matrix[c][n], matrix[r][c]]
            else:
                matrix[c][n] = [matrix[c][n], matrix[r][c][0]]
    n -= 1
for r in range(rows):
    for c in range(cols):
        matrix[r][c] = matrix[r][c][1]
print(matrix)
print(type([1,2,3]) == list)
