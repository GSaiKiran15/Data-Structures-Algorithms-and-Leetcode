from itertools import zip_longest
pattern = "abba"
s = "dog cat cat dog"
s = s.split()
print(len(set(s)) == len(set(pattern)) == len(set(zip_longest(s))))
