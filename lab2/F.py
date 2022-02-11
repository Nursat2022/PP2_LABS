n = int(input())

students = dict()

for i in range(n):
    s = input().split()
    name = s[0]
    num = int(s[1])
    if name not in students:
        students[name] = num
    else:
        students[name] += num    

mx = 0
for i in students.values():
    if mx < i:
        mx = i
for k, v in sorted(students.items()):
    if v == mx:
        print("{} is lucky!".format(k))
    else:
        print("{} has to receive {} tenge".format(k, mx - v))     