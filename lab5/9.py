import re
s = input()
pattern = r'([a-z])([A-Z])'

print(re.sub(pattern, r'\1 \2', s))