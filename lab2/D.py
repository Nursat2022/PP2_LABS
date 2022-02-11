n = int(input())

index = n - 1

if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i == j or i > j:
                print("#", end="")
            else:
                print(".", end="")        
        print()
else:
    for i in range(n):
        for j in range(n):
            if i + j == n-1 or i + j >= n:
                print("#", end="")
            else:
                 print(".", end="") 
        print()         