strs = ["eat","tea","tan","ate","nat","bat"]
sorted_strings = {}
for i in strs:
    sorted_string = "".join(sorted(i))
    if sorted_string in sorted_strings:
        sorted_strings[sorted_string].append(i)
    else:
        sorted_strings[sorted_string] = [i]
print(list(sorted_strings.values()))
