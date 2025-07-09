gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
total = 0
res = 0

if sum(gas) < sum(cost):
    print(-1)
else:    
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            res = i + 1
print(res)