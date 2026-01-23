
#     row = set()
#     col = set()
#     for c in range(cols):
#         if board[r][c] in row and board[r][c] != "." or board[c][r] in col and board[c][r] != ".":
#             print(False, row,board[r][c], col, board[c][r])
#             break
#         row.add(board[r][c])
#         col.add(board[c][r])