import re
s = input()
pattern = r'ab*'
print(re.search(pattern, s))
