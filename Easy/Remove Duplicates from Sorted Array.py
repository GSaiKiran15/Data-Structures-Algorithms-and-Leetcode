nums = [1,2]
l = 1
for r in range(1, len(nums)):
    if nums[r-1] != nums[r]:
        nums[l] = nums[r]
        l += 1
print(l, nums)
    