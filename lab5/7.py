import re
s = input()
pattern = r'[a-z][^_]*'

arr = re.findall(pattern, s)

t = ""

for i in arr:
    t += i.capitalize()

print(t)
