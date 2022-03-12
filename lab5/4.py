import re
s = input()
pattern = r'[A-Z][a-z]{2,}'
print(re.search(pattern, s))