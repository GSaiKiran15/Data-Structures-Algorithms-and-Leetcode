gas = [2,3,4]
cost = [3,4,3]

if sum(gas) < sum(cost):
    print(False, -1)

res = 0
total = 0

for i in range(len(gas)):
    total += gas[i] - cost[i]
    if total < 0:
        total = 0
        res = i + 1
print(res)