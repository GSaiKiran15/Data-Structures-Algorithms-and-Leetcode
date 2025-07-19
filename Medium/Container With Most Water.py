height = [8,7,2,1]
l = 0
r = len(height) - 1
output = (r-l) * min(height[l], height[r])
while r > l:
    output = max(output, (r-l) * min(height[l], height[r]))
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(output)