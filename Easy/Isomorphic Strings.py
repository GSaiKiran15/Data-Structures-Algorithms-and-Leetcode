s = "badc"
t = "baba"
if len(s) != len(t):
    print(False)

map_s_t = {}
map_t_s = {}

for sc, tc in zip(s, t):
    if sc in map_s_t and map_s_t[sc] != tc:
        print(False)
    if tc in map_t_s and map_t_s[tc] != sc:
        print(False)
    map_t_s[tc] = sc
    map_s_t[sc] = tc
print(True)