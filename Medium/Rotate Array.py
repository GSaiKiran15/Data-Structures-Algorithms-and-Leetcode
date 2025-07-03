nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
k = k % n
nums[:] = nums[-k:] + nums[:-k]
print(nums)
# for i in range(k):
#     val = nums.pop(-1)
#     nums.insert(0, val)
# print(nums)