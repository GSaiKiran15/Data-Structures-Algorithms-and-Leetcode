nums = [2,8,5,3,9]
for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        while 