def isSubsequence(self, s: str, t: str) -> bool:
    if s == "":
        return True
    s_pointer = 0
    for i in t:
        if i == s[s_pointer]:
            s_pointer += 1
            if s_pointer == len(s):
                return True
    return False    