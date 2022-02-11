n = int(input())

pw = []

def isupp(s):
    for i in range(len(s)):
        if s[i].isupper(): 
            return True
    return False        

def islow(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
    return False

def isdig(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True            
    return False

for i in range(n):
    s = input()
    if isupp(s) and islow(s) and isdig(s):
        pw.append(s)

pw = set(pw)


print(len(pw))

for i in sorted(pw):
    print(i)

