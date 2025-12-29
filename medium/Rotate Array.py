nums = [1,2,3,4,5,6,7]
k = 3
k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]
print(nums)