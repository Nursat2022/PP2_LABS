arr = list(map(str, input().split()))
with open('input5.txt', 'w') as f:
    for i in arr:
        f.write(i)
        f.write('\n')

with open('input5.txt', 'r') as r:
    x = r.read()
print(x)    
