def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0: return False 
    if len(s) == 0: return True
    parantheses = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) == 0 or s[i] not in parantheses:
            stack.append(s[i])
        elif stack[-1] == parantheses[s[i]]:
            stack.pop(-1)
        else:
            stack.append(s[i])
    if stack:
        return False
    return True

s = "([])"
print(isValid(s))