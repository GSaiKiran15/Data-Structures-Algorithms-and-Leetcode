nums = [3,2,2,3]
val = 3
for i in range(len(nums[:])-1):
    if nums[i] == val:
        nums.pop(i)
print(len(nums))