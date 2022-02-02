cnt = 0

s = input()

for i in s:
    cnt += ord(i)

if (cnt > 300):
    print("It is tasty!")
else:
    print("Oh, no!")
