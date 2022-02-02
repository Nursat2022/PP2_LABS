n = int(input())
st = []
for i in range(n):
    s = input()
    if("@gmail.com" in s):
        index = s.find("@gmail.com")
        s = s[:index]
        st.append(s)

for i in st:
    print(i)