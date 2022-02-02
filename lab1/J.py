s = list(map(str, input().split()))

def func():
    a = ""
    for i in s:
        if(len(i) >= 3):
            a += i + " "
    return a        

print(func())        


