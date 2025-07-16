nums = [2,7,11,15]
target = 9
h = {}
for i,j in enumerate(nums):
    if (target - j) in h:
        print([i, h[target - j]])
    else:
        h[j] = i
