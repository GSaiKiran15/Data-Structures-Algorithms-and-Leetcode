strs = ["flower","flow","flight"]

res = ""

for i in range(len(strs[0])):
    for s in strs:
        if i == len(s) or s[i] != strs[0][i]:
            print(res)
            break
    res += strs[0][i]
