nums = [-1,0,1,2,-1,-4]
nums.sort()
res = []
for i, j in enumerate(nums):
    if i > 0 and j == nums[i - 1]:
        continue
    l = i + 1
    r = len(nums) - 1
    while l < r:
        total = (j + nums[l] + nums[r] )
        if total < 0:
            l += 1
        elif total > 0:
            r -= 1
        else:
            res.append([j, nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1
print(res)