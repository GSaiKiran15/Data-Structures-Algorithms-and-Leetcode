path = "/a//b////c/d//././/.."
path = path.split("/")
stack = []
for i in path:
    if i == "" or i == ".":
        continue
    if i == "..":
        if stack: stack.pop(-1)
    else:
        stack.append(i)
print('/' + '/'.join(stack))