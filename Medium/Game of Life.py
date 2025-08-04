board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
orig = [rows[:] for rows in board]
order = [[-1,-1], [-1,0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
max_row = len(board)
max_col = len(board[0])
for r in range(max_row):
    for c in range(max_col):
        one_count = 0
        for i, j in order:
            if 0 <= r + i < max_row and 0 <= c + j < max_col:
                if board[r + i][c + j] == 1:
                    one_count += 1
        if orig[r][c] == 1:
            board[r][c] = 1 if one_count in (2,3) else 0
        else:
            board[r][c] = 1 if one_count == 3 else 0
print(board)