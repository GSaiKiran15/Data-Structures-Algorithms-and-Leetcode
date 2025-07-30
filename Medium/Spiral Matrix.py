matrix = [[1,2,3],[4,5,6],[7,8,9]]

left = 0
right = len(matrix[0])-1
top = 0
bottom = len(matrix)-1
output = []

def move_right(matrix, left, right, top, bottom, output):
    if len(output) == len(matrix) * len(matrix[0]):
        return output
    for i in range(left, right+1):
        output.append(matrix[left][i])
    top += 1
    return move_down(matrix, left, right, top, bottom, output)

def move_down(matrix, left, right, top, bottom, output):
    if len(output) == len(matrix) * len(matrix[0]):
        return output
    for i in range(top, bottom+1):
        output.append(matrix[i][right])
    right -= 1
    return move_left(matrix, left, right, top, bottom, output)

def move_left(matrix, left, right, top, bottom, output):
    if len(output) == len(matrix) * len(matrix[0]):
        return output
    for i in range(right, left-1, -1):
        output.append(matrix[bottom][i])
    bottom -= 1
    return move_up(matrix, left, right, top, bottom, output)

def move_up(matrix, left, right, top, bottom, output):
    if len(output) == len(matrix) * len(matrix[0]):
        return output
    for i in range(bottom, top-1, -1):
        output.append(matrix[i][left])
    left += 1
    return move_right(matrix, left, right, top, bottom, output)

print(move_right(matrix, left, right, top, bottom, output))