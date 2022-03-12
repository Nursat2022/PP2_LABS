import re
s = input()
pattern = r'a.+b$'
print(re.search(pattern, s))