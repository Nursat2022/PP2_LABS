import re
s = input()
pattern = r'ab{2,3}'
print(re.search(pattern, s))