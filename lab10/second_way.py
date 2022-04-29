import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

id = 1
name = 'student 1'
number = '87053453445'
email = 'asdf@gmail.com'


sql = '''
insert into phonebook values (%s, %s, %s, %s);
'''

cursor = conn.cursor()
cursor.execute(sql, (id, name, number, email))

cursor.close()
conn.commit()
conn.close()


