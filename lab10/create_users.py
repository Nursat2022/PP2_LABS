import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

sql = '''
create table users (
    user_name varchar(255) primary key,
    level int,
    score int,
    highscore int
);
'''    

cursor = conn.cursor()

cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()