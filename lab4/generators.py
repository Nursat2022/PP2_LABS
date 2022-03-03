# 1)
def square(n):
    for i in range(1, n+1):
        yield i**2

n = int(input())
for i in square(n):
    print(i, end =' ')

print()
print("-" * 30)

# 2)
# arr = [i for i in range(0, int(input(), 2))]
# print(*arr, sep=', ')

def gen(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())

print(*gen(n), sep=', ')

print('-' * 30)

# 3)
n = int(input())

def gen():
    for i in range(n+1):
        if i%3 == 0 and i%4 == 0:
            yield i

for i in gen():
    print(i, end= ' ')

print()
print('-' * 30)

# 4)
a, b = map(int, input().split())
def squares():
    for i in range(a, b+1):
        yield i**2

for i in squares():
    print(i, end=' ')
    
print()
print('-' * 30)

# 5)
def generator(n):
    while n != -1:
        yield n
        n -= 1  
    
n = int(input())
for i in generator(n):
    print(i, end=" ")
