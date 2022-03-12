import re
s = input()
x = re.split(r'[A-Z]+', s)
print(*x)