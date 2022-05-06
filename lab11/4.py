import psycopg2

limit = int(input('limit:\n'))
offset = int(input('offset:\n'))

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cur = conn.cursor()

sql = '''
    select * from phonebook limit %s offset %s;
'''

cur.execute(sql, (limit, offset))
res = cur.fetchall()
for i in res:
    print(i)

cur.close()
conn.commit()
conn.close()