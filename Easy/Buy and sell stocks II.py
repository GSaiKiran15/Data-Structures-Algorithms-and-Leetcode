def maxProfit(self, prices: List[int]) -> int:
    output = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            output += prices[i] - prices[i-1]
    return output
