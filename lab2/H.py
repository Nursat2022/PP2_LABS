main_x, main_y = map(int ,input().split())
n = int(input())

result = dict()

for i in range(n):
    x, y = map(int, input().split())
    dis = pow(pow((x - main_x), 2) + pow((y - main_y), 2), 1/2)
    if dis not in result:
        result[dis] = [x, y]
    else:
        result[dis].append(x)
        result[dis].append(y)

for k in sorted(result.keys()):
    v = result[k]
    if len(v) > 2:
        for i in range(0, len(v), 2):
            print(v[i], v[i+1])

    else:        
        print(*result[k])


