nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
pointer = m + n - 1
while m > 0 and n > 0:
    if nums1[m-1] < nums2[n-1]:
        nums1[pointer] = nums2[n-1]
        n -= 1
    else:
        nums1[pointer] = nums1[m-1]
        m -= 1
    pointer -= 1
print(nums1)