a = int(input())
arr = [a]
while a != 0:
    a = int(input())
    if a == 0: break
    arr.append(a)

n = int(len(arr)/2)
l = []

for i in range(n):
    res = arr[i] + arr[len(arr)-1-i]
    l.append(res)

if len(arr) % 2 == 0:
    print(*l)
else:
    num = arr[n]
    print(*l, num)    

    

