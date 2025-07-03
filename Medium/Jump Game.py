nums = [2,3,1,1,4]

goal = len(nums)-1

for left in range(len(nums)-2, -1, -1):
    if nums[left] >= goal - left:
        goal = left
print(goal == 0)

    