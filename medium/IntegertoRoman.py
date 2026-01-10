roman = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["DM", 900], ["M", 1000]]
num = 3749
res = ""
for sym, val in reversed(roman):
    if num // val:
        count = num // val
        res += (sym * count)
        num = num % val
print(res)