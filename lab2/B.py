n = int(input())

arr = list(map(int, input().split()))
arr.sort()
print(arr[n-1] * arr[n-2])