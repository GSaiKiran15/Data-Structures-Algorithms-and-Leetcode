nums = [7,1,5,3,6,4]

output = 0
l = 0
for r in range(1, len(nums)):
    if nums[l] < nums[r]:
        output = max(output, nums[r] - nums[l])
    else:
        l = r
print(output)