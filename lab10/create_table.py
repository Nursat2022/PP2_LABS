import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

sql = '''
create table phonebook (
    id  int primary key,
    name  varchar(255),
    number  varchar(255),
    email  varchar(255)
);
'''

cursor = conn.cursor()
cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()


