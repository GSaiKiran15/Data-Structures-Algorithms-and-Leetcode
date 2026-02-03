intervals = [[1,5]]
newInterval = [0,0]
res = []
for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
        res.append(newInterval)
        print(res + intervals[i:])
        break
    elif newInterval[0] > intervals[i][1]:
        res.append(intervals[i])
    else:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
res.append(newInterval)
print(res)