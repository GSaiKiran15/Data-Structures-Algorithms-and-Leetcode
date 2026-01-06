numbers = [2,7,11,15]
target = 9
l, r = 0, len(numbers) - 1
while l < len(numbers) and r > 0:
    if numbers[l] + numbers[r] > target:
        r -= 1
    elif numbers[l] + numbers[r] < target:
        l += 1
    else:
        print(numbers[l], numbers[r])
        break
