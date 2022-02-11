s = input().split('+')
m = dict()

m["ONE"] = 1
m["TWO"] = 2
m["THR"] = 3
m["FOU"] = 4
m["FIV"] = 5
m["SIX"] = 6
m["SEV"] = 7
m["EIG"] = 8
m["NIN"] = 9
m["ZER"] = 0

arr = []
def func():
    for word in s:
        string = ""
        for i in range(0, len(word)-2, 3):
            t = ""
            t += word[i] + word[i+1] + word[i+2]
            k = m[t]
            string += str(k)
        arr.append(string)

    cnt = 0
    for i in arr:
        cnt += int(i)

    st = str(cnt)
    t = ""
    for i in st:
        for k, v in m.items():
            if i == str(v):
                t += k
    return t

print(func())


            