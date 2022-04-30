import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cursor = conn.cursor()

b = input('by:\n')
d = input()

if b == 'name':
    sql = '''
    delete from phonebook where name = %s;
    '''
elif b == 'number':
    sql = '''
    delete from phonebook where number = %s;
    '''

cursor.execute(sql, [d])

cursor.close()
conn.commit()
conn.close()


