a = input()
z = input()
x = -1
y = -1
for i in range(len(a)):
    if (a[i] == z):
        x = i
        break

        
i = len(a)-1

while i != 0:
    if(a[i] == z and i != x):
        y = i
        break
    i -= 1

if(x != -1 and y != -1):
    print(x, y)
elif(x != -1 and y == -1):
    print(x)
        
