def majorityElement(self, nums: List[int]) -> int:
    return sorted(nums)[len(nums)//2]