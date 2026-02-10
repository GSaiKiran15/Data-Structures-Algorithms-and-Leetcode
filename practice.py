nums = [321,5,684,651,35,84,98,98,654,321,86,498,7,4,651,321,354,987,98,75647954,68,3,6,9]
top_3 = []
first = second = third = float('-inf')

for num in nums:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num

top_3 = [first, second, third]