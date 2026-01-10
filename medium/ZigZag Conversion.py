s = "PAYPALISHIRING"
numRows = 4
res = ""
for i in range(numRows):
    res += s[i]
    val = i
    for j in range(i, len(s)):
        if j == val + ((2 * numRows) - 2):
            print(i, s[i], j, s[j], ((2 * numRows) - 2))
            res += s[j]
            val = j
        elif j == ((2 * numRows) - (3 * val)):
            print(j, s[j], ((2 * numRows) - (3 * val)))
print(res)