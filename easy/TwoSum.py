nums = [2, 7, 11, 15]
target = 9
h = {}
for i in range(len(nums)):
    if target - nums[i] in h:
        print([i, h[target - nums[i]]])
    else:
        h[nums[i]] = i