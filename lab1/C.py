s = input()
def tolowercase():
    t = ""
    for i in s:
        if (i >= 'A' and i <= 'Z'):
            i = chr(ord(i) + 32)
        t += i
    return t

print(tolowercase())
