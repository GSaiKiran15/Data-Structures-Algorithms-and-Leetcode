def isPalindrome(self, s: str) -> bool:
    output = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i].isalnum():
            output += s[i]
    return output == output[::-1]