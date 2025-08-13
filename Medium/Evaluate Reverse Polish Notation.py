operators = ('+', '-', '*', '/')
tokens = ["4","3","-"]
stack = []
for i in range(len(tokens)):
    element = tokens[i]
    if element not in operators:
        stack.append(int(element))
    else:
        sol = 0
        if element == '*':
            sol = stack[-1] * stack[-2]
        elif element == '+':
            sol = stack[-1] + stack[-2]
        elif element == '-':
            sol = stack[-1] - stack[-2]
        else:
            sol = int(stack[-2] / stack[-1])
            print(sol, stack[-2], stack[-1])
        stack.pop()
        stack[-1] = sol       
print(int(stack[0]))