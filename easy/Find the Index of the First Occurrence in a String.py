haystack = "abc"
needle = "c"
if len(needle) > len(haystack):
    print(-1)
if needle == haystack:
    print(0)
for i in range(len(haystack) - len(needle)+1):
    if haystack[i:i + len(needle)+1] == needle:
        print(i)
print(-1)