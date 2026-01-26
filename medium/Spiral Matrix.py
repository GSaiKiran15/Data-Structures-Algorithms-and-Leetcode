matrix = [[1,2,3],[4,5,6],[7,8,9]]
res_len = len(matrix) * len(matrix[0])
res = []
top = 0
right = len(matrix)
bottom = len(matrix[0])
left = 0

while top < bottom and left < right:

    for i in range(left, right):
        res.append(matrix[top][i])
    top += 1

    for i in range(top, bottom):
        res.append(matrix[i][right-1])
    right -= 1

    if not (top < bottom and left < right):
        break
    
    for i in range(right-1, left-1, -1):
        res.append(matrix[bottom - 1][i])
    bottom -= 1
    
    for i in range(bottom - 1, top - 1, -1):
        res.append(matrix[i][left])
    left += 1

print(res)