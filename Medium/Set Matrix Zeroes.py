from collections import defaultdict

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

rows = defaultdict(set)
cols = defaultdict(set)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
            rows[r].add(r)
            cols[c].add(c)

for r in rows:
    for i in range(len(matrix[0])):
        matrix[r][i] = 0
for c in cols:
    for i in range(len(matrix)):
        matrix[i][c] = 0
print(matrix)
    