prices = [7,1,5,3,6,4]
res = 0
for i in range(1, len(prices)):
    if prices[i-1] < prices[i]:
        res += prices[i] - prices[i-1]
print(res)