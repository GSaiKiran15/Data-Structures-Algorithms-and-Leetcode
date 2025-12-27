nums = [2,2,1,1,1,2,2]
candidate = None
count = 0

for i in nums:
    if count == 0:
        candidate = i
    count += 1 if i == candidate else -1

print(candidate)