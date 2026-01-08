pointer = 0
s = "abc"
t = "ahbgdc"
for i in t:
    if i == s[pointer]:
        pointer += 1
        if pointer == len(s):
            print(True)
print(False)