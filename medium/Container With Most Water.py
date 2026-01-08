height = [1,8,6,2,5,4,8,3,7]
l = 0
r = len(height)-1
res = 0
while r > l:
    res = max(res, (min(height[l], height[r]) * (r - l)))
    if height[r] >= height[l]:
        l += 1
    else:
        r -= 1
print(res)