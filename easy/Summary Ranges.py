nums = [0,2,3,4,6,8,9]
i = 0
ans = []
while i < len(nums):
    start = nums[i]
    while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]:
        i += 1
    if start != nums[i]:
        ans.append(str(start) + '->' + str(nums[i]))
    else:
        ans.append(str(nums[i]))
    i += 1
print(ans)