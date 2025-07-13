def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    from collections import Counter

    c=Counter(ransomNote)
    d=Counter(magazine)

    for i in c:
        if c[i] > d[i]:
            return False
    return True