def longestConsecutive(self, nums: List[int]) -> int:
    nums = set(nums)
    res = 0
    for i in nums:
        if i - 1 not in nums:
            length = 1
            while i + length in nums:
                length += 1
            res = max(res, length)
    return res

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))