import math
a, b = map(int, input().split())
ok = True

num = int(math.sqrt(a))
for i in range(2, num+1):
    if(a%i == 0):
        ok = False
        break

if (a <= 500 and ok == True and b%2 == 0):
    print("Good job!")
else:
    print("Try next time!")