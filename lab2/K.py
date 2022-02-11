s = input().split()
arr = []
for i in s:
    if not i.isalpha():
        index = len(i)-1
        i = i[:index]
    arr.append(i)

arr = set(arr)

print(len(arr))

for i in sorted(arr):
    print(i)
