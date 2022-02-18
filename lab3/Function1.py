# 1)
def conv(g):
    return 28.3495231*g
# 2)
def toFar(F):
    return 5/9 * (F-32)
# 3)
def solve(numheads, numlegs):
    for i in range(numheads):
        for j in range(numheads):
            if i + j == numheads and 2*i + 4*j == numlegs:
                print(f'number of chickens - {i}')
                print(f'number of rabbits - {j}')
                return

# 4)
def filter_prime(arr):
    import math
    l = []
    for i in arr: #arr = [3, 5 ,6]
        ok = True
        num = int(math.sqrt(i))
        for j in range(2, num+1):
            if i % j == 0:
                ok = False
                break
        if ok == True:
            l.append(i)    
    return l

# 5)
from itertools import permutations
def permut(s):
    permuts = [''.join(i) for i in permutations(s)]
    return permuts
# 6)
def rev(s): 
    s = s.split()
    l = ""
    for i in range(len(s)-1, -1, -1):
        l += s[i] + " "
    return l

# 7)
def has_33(arr):
    for i in range(len(arr)-1):
        if arr[i] == 3 and arr[i+1] == 3:
            return True
    return False  

# 8)
def con_007(arr):
    l = []
    for i in arr:
        if i == 0 or i == 7:
            l.append(i)

    for i in range(len(l)-2):
        if l[i] == 0 and l[i+1] == 0 and l[i+2] == 7:
            return True  

    return False

# 9)
def volume(r):
    from math import pi
    return 4/3 * pi * r**3

# 10)
def uniq(arr):
    dict = {}
    l = []
    for i in arr:
        if i not in dict:
            dict[i] = 1
            l.append(i)

    return l

# 11)
def ispol(s):
    if s == s[::-1]:
        return True
    return False

# 12)
def func(arr):
    for i in arr:
        print('*' * i)

# 13)
import random
rnum = random.randint(1,20)
cnt = 1
t = 'Take a guess.'

print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print(t)
num = int(input())
print()
ok = True
while ok == True: 
    if(num > rnum):
        print("Your guess is too high.")
        print(t)
        cnt += 1
        num = int(input())
        print()
    if(num < rnum):
        print("Your guess is too low.")
        print(t)
        cnt +=1
        num = int(input())
        print()
    if(num == rnum):
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        ok = False