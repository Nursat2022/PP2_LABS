import json

print("Interface Status")
print("=" * 80)
print("DN" + " "*50 + "Description" + " "*10 + "Speed" + " " *5 + "MTU")
print("-"*51 + " " + "-"*19 + " "*2 + "-"*6 + " "*3 + "-"*6)


with open('sample-data.json', 'r') as f:
    x = f.read()

d = json.loads(x)

def gen():
    for i in d['imdata']:
        yield len(i["l1PhysIf"]["attributes"]["dn"])

mx = max(*gen())

for i in d['imdata']:
    siz_of_dn = len(i["l1PhysIf"]["attributes"]["dn"])

    while siz_of_dn != mx:
        i["l1PhysIf"]["attributes"]["dn"] += ' '
        siz_of_dn = len(i["l1PhysIf"]["attributes"]["dn"])

    print( i["l1PhysIf"]["attributes"]["dn"] +' '*30 + i["l1PhysIf"]["attributes"]["speed"] + ' '*4 + i['l1PhysIf']["attributes"]['mtu'])



