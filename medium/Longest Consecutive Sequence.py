nums = [1,2,6,7,8]

# my solution both works but neetcode is better 

nums = sorted(list(set(nums)))
print(nums)
res = 0
l = 0
for i in range(1, len(nums)):
    if nums[i - 1] == nums[i] - 1:
        l += 1
    else:
        res = max(l, res)
        l = 0
if l:
    res = l
print(res+1)

#neetcode solution

nums = set(nums)
res = 0
for n in nums:
    if (n-1) not in nums:
        length = 0
        while (n+length) in nums:
            length += 1
        res = max(res, length)
print(res) 