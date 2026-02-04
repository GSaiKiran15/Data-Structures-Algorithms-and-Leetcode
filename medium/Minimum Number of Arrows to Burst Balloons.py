points = [[1,2],[2,3],[3,4],[4,5]]
res = len(points)
points.sort()
cur = points[0]
for i in range(1, len(points)):
    if points[i][0] < cur[1]:
        res -= 1
        cur = [cur[0], min(cur[1], points[i][1])]
    else:
        cur = points[i]
print(res)