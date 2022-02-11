n = int(input())
arr = []
t = []
for i in range(n):
    s = input().split()
    if len(s) == 2:
        arr.append(s[1])
    else:
        t.append(arr[0])
        arr.remove(arr[0])

print(*t)

