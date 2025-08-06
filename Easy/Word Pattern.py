def wordPattern(pattern: str, s: str) -> bool:
    s= s.split()
    if len(pattern) != len(s):
        return False
    
    map_p_s = {}
    map_s_p = {}

    for pc, sc in zip(pattern, s):
        if pc in map_p_s and map_p_s[pc] != sc:
            return False
        if sc in map_s_p and map_s_p[sc] != pc:
            return False
        map_p_s[pc] = sc
        map_s_p[sc] = pc
    return True
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))