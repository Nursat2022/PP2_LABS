n = int(input())

demons = dict()

for i in range(n):
    s = input().split()
    abil = s[1]
    if s[1] not in demons:
        demons[abil] = 1
    else:
        demons[abil] += 1

m = int(input())
hunters = dict()
for i in range(m):
    t = input().split()
    abil = t[1] 
    if abil not in hunters:
        hunters[abil] = int(t[2])
    else:
        hunters[abil] += int(t[2])

cnt = 0

for i in demons.keys():
    for j in hunters.keys():
        if i == j:
            if demons[i] < hunters[j]:
                cnt += demons[i]
            else:
                cnt += hunters[j]

res = n - cnt
print("Demons left: {}".format(res))





# for i in demons.items():
#     print(i)
# print('-'*20)
# for i in hunters.items():
#     print(i)
# print('-'*20)
# print(cnt)
'''
('water', 3)
('thunder', 1)
('sun', 1)
--------------------
('water', 21)
('thunder', 1)
'''