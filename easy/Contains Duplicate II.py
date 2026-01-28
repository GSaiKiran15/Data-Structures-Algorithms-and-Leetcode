nums = [1,2,3,1,2,3]
k = 2
h = {}
for i, j in enumerate(nums):
    if j in h:
        if abs(h[j] - i) <= k:
            print(True)
        h[j] = i
    else:
        h[j] = i
print(False)