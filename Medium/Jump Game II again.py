nums = [2,3,1,1,4]

near = far = jumps = 0

while far < len(nums) - 1:
    farthest = 0
    for i in range(near, far + 1):
        farthest = max(farthest, i + nums[i])
    
    near = far + 1
    far = farthest
    jumps += 1

print(jumps)

# My solution
# right = len(nums) - 1
# res = 0
# left = 0
# while right > 0:
#     while left < 0:
#         left += 1
#     if left + nums[left] >= right:
#         res += 1
#         right = left
#         left = 0
#     else:
#         left += 1
#         if left >= right:
#             print(False)
#             break
        
# print(res)