n = int(input())
                    
st = input()

if st == "k":
    k = str(input())
    num = "{:." + k + "f}"
    print(num.format(n / 1024))
else:
    print(n * 1024)    