target = 11
nums = [1,1,1,1,1,1,1,1]

l = 0
r = 0
output = float('inf')
sum = nums[r]
while r < len(nums) or l < len(nums):
    if sum >= target:
        output = min(output, (r-l)+1)
    if sum < target:
        r += 1
        if r == len(nums):
            break
        sum += nums[r]
    else:
        sum -= nums[l]
        l += 1
print(output)

        