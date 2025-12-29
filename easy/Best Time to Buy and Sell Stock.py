prices = [7,6,4,3,1]
max_profit = 0
min_number = prices[0]
for i in range(1, len(prices)):
    if min_number > prices[i]:
        min_number = prices[i]
    max_profit = max(max_profit, prices[i] - min_number)
print(max_profit)
    