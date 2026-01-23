from collections import defaultdict

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

rows = defaultdict(set)
cols = defaultdict(set)
squares = defaultdict(set)

for r in range(9):
    for c in range(9):
        if board[r][c] == ".":
            continue
        if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
            print(False)
            break
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        squares[(r // 3, c // 3)].add(board[r][c])
print(True)