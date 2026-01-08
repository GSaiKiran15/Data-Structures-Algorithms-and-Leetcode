s = "A man, a plan, a canal: Panama"
s = ''.join(filter(str.isalnum, s)).lower()
print(s == s[::-1])