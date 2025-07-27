intervals = [[1,4],[0,2],[3,5]]
intervals.sort()
print(intervals)
output = []
temp = intervals[0]
for i in range(len(intervals)-1):
    if (intervals[i+1][0] <= temp[1] and intervals[i+1][1] >= temp[0]):
        temp = [min(temp[0], intervals[i+1][0]), max(temp[1], intervals[i+1][1])]
    else:
        output.append(temp)
        if i < len(intervals):
            temp = intervals[i+1]
output.append(temp)

print(output)