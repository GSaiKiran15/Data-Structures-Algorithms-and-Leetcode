from collections import deque
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

rows = len(grid)
cols = len(grid[0])
visited = set()
islands = 0

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited.add((r,c))
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            r, c = dr + row, dc + col
            if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == "1"):
                q.append((r,c))
                visited.add((r,c))
        

for r in range(rows):
    for c in range(cols):
        if (grid[r][c] == "1" and (r,c) not in visited):
            bfs(r,c)
            islands += 1
print(islands)
            