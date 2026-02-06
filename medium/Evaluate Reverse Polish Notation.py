tokens = ["4","13","5","/","+"]
stack = []
for i in tokens:
    if i in ["+", "-", "*", "/"]:
        if i == "+":
            stack[-2] = stack[-1] + stack[-2]
        elif i == "-":
            stack[-2] = stack[-2] - stack[1]
        elif i == "*":
            stack[-2] = stack[-1] * stack[-2]
        elif i == "/":
            stack[-2] = int(stack[-2] / stack[-1])
        stack.pop(-1)
    else:
        stack.append(int(i))
print(stack[0])