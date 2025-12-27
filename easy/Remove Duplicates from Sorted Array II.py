nums = [-5, -5, -5, -3, -3, -1, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3]
k = 2
for i in range(2, len(nums)):
    if nums[k-2] != nums[i]:
        nums[k] = nums[i]
        k += 1
print(k, nums)        