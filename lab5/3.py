import re
s = input()
pattern = r'([a-z]+_[a-z]+(_[a-z]+)*)'
print(re.search(pattern, s))