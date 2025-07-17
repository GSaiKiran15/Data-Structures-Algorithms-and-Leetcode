s = "PAYPALISHIRING"
numRows = 4
val = (numRows - 1) + (numRows - 2) + 1
adder = val - 1
output = ""
for i in range(numRows):
    if i == 0 or i == (numRows-1):
        j = i
        while j in range(len(s)):
            output += s[j]
            j += val
    else:
        j = i
        while j in range(len(s)):
            output += s[j]
            if adder < len(s):
                output += s[adder]
            j += val
            adder += val
        adder = val - i - 1
print(output)
        