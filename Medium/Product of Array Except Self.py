nums = [1,2,3,4]
prefix = 1
res = [1] * len(nums)
for i in range(len(nums)):
    res[i] = prefix 
    prefix *= nums[i] 
postfix = 1
for i in range(len(nums)-1, -1 ,-1):
    res[i] *= postfix
    postfix *= nums[i] 
print(res)