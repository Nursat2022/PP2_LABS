a = input()
cnt = 0
a = a[::-1]
def recursion(i):
    global cnt 
    if (i == len(a)):
        return
    cnt += int(a[i]) * (2**i)    
    return recursion(i+1)

recursion(0)
print(cnt)
