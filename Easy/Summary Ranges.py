nums = [0,2,3,4,6,8,9]

i = 0
output = []

while i < len(nums):
    
    start = nums[i]
    while i < len(nums)-1 and nums[i+1] == nums[i]+1:
        i += 1
    
    if start == nums[i]:
        output.append(f'{start}')
    else:
        output.append(f'{start}->{nums[i]}')    
    i += 1

print(output)