from itertools import zip_longest

s = "egg"
t = "add"

print(len(set(s)) == len(set(t)) == len(set(zip_longest(s, t))))