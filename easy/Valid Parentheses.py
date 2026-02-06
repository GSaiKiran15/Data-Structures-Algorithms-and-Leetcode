parantheses = {
    "}" : "{",
    ")" : "(",
    "]" : "["
}

s = "()"
stack = []
for i in s:
    if i in parantheses:
        if not stack:
            print(False)
        if stack[-1] != parantheses[i]:
            print(False)
        else:
            stack.pop(-1)
    else:
        stack.append(i)
print(True if not stack else False)