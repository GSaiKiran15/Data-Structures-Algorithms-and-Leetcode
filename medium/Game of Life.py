board = [[1,1],[1,0]]
sides = [[-1,-1], [-1, 0], [0, -1], [-1, 1], [1, -1], [0,1], [1,0], [1, 1]]
rows = len(board)
cols = len(board[0])
changes = []
for r in range(rows):
    for c in range(cols):
        ones = 0
        for row, col in sides:
            x = r + row
            y = c + col
            if rows > x >= 0 and cols > y >= 0:
                if board[x][y] == 1:
                    ones += 1
        if ones < 2 or ones > 3:
            changes.append([r, c, 0])
        elif ones == 3:
            changes.append([r, c, 1])
for r, c, val in changes:
    board[r][c] = val
print(board)