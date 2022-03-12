import re
s = input()

pattern = r'([a-z])([A-Z])'

x = re.sub(pattern, r'\1_\2', s).lower()
print(x)