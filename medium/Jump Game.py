nums = [3,2,1,0,4]
index = len(nums) - 1
for i in range(len(nums)-2, -1, -1):
    if nums[i] + i >= index:
        index = i
print(True) if index == 0 else print(False)