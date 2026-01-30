from collections import defaultdict 
strs = ["eat","tea","tan","ate","nat","bat"]
result = defaultdict(list)
for i in strs:
    letters = [0] * 26
    for j in i:
        letters[ord(j) - ord("a")] += 1
    result[tuple(letters)].append(i)
print(list(result.values()))