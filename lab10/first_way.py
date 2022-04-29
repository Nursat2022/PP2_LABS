import psycopg2, csv

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

arr = []

with open('a.csv', 'r') as f:
    x = csv.reader(f, delimiter=',')

    for row in x:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
insert into phonebook values (%s, %s, %s, %s);
'''
cursor = conn.cursor()

for row in arr:
    cursor.execute(sql, (row))

cursor.close()
conn.commit()
conn.close()


