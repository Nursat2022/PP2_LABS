s = input()

st = []

for i in range(len(s)):
    if s[i] == '[' or s[i] == '(' or s[i] == '{':
        st.append(s[i])
    else:
        if len(st) == 0:
            print("No")
            exit()
        st_top = st[len(st)-1]
        if s[i] == ')' and st_top != '(' or s[i] == ']' and st_top != '[' or s[i] == '}' and st_top != '{':
            print("No")
            exit()
        st.pop()

if len(st) != 0:
    print("No")
else:
    print("Yes")    