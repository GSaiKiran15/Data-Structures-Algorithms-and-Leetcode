matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rows = len(matrix)
cols = len(matrix[0])
rowZero = False
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 0:
            matrix[0][c] = 0
            if r > 0:
                matrix[r][0] = 0
            else:
                rowZero = True

for r in range(1, rows):
    for c in range(1, cols):
        if matrix[0][r] == 0 or matrix[r][0] == 0:
            matrix[r][c] = 0

if matrix[0][0] == 0:
    for r in range(rows):
        matrix[r][0] = 0

if rowZero:
    for c in range(cols):
        matrix[0][c] = 0

print(matrix)

zeros = set()

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 0:
            zeros.add((r, c))
# print(zeros)
for row, col in zeros:
    for r in range(0, row):
        for c in range(0, col):
            matrix[row][c] = 0
            matrix[r][col] = 0
# print(matrix)