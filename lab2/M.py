a = list(map(int, input().split()))
arr = [a[::-1]]
while True:
    a = list(map(int, input().split()))
    if len(a) == 1: break 
    a = a[::-1]
    arr.append(a)

arr = sorted(arr)

for ll in arr:
    y = str(ll[0])
    m = str(ll[1])
    d = str(ll[2])
    while len(y) != 4:
        y = '0' + y
    while len(m) != 2:
        m = '0' + m
    while len(d) != 2:
        d = '0' + d
    print(d, m, y)    
                    
