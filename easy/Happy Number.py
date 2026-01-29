n = 123456

def sum_of_squares(num):
    total = 0
    while num:
        total += (num % 10) ** 2
        num = num // 10
    return total

visit = set()

while n not in visit:
    visit.add(n)
    n = sum_of_squares(n)
    if n == 1:
        print(True)
print(False)