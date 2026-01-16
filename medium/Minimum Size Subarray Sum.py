target = 7
nums = [2,3,1,2,4,3]
l, temp_sum = 0, 0
res = float("inf")
for r in range(len(nums)):
    temp_sum += nums[r]
    while temp_sum >= target:
        res = min(r - l + 1, res)
        temp_sum -= nums[l]
        l += 1
print(0 if res == float("inf") else res)