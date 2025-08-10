points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
points.sort(key=lambda x: x[1])
arrows = 1
end = points[0][1]
for start, finish in points[1:]:
    if start > end:
        arrows += 1
        end = finish
print(arrows)