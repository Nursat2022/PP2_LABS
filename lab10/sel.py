import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cursor = conn.cursor()

id = input('id:\n')

sql = '''
select name, number from phonebook where id = %s;
'''

cursor.execute(sql, id)

text = cursor.fetchone()
print(text)

cursor.close()
conn.commit()
conn.close()


