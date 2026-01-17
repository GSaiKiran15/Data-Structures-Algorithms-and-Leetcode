s = "dvdf"
res = 0
h = {}
l = 0
for i, j in enumerate(s):
    if j not in h:
        h[j] = 1
    else:
        res = max(res, len(h))
        h[j] += 1
        while h[j] > 1 and l < i:
            if h[s[l]] > 1:
                h[s[l]] -= 1
            else:
                h.pop(s[l])
            l += 1
if h:
    res = max(res, len(h))
print(res, h)        