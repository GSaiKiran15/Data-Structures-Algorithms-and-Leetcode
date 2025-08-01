matrix = [[1,2,3],[4,5,6],[7,8,9]]
h = 0
while h < len(matrix):
    for i in range(len(matrix[:])):
        for j in range(len(matrix[:])):
            matrix[h][j] = matrix[j][i]
        h += 1  

print(matrix)