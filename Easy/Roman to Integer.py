def romanToInt(self, s: str) -> int:
    h = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    output = 0
    i = 0
    while i < len(s):
        if i == len(s)-1:
            output += h[s[i]]
            i += 1
        elif h[s[i]] < h[s[i+1]]:
            output += h[s[i+1]] - h[s[i]]
            i += 2
        else:
            output += h[s[i]]
            i += 1

    return output