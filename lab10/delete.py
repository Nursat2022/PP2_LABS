import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cursor = conn.cursor()

b = input('by:\n')

if b == 'number':
    d = input()
    print(type(d))

    sql = '''
    delete from phonebook where number = %s;  
    '''
    cursor.execute(sql, d)

elif b == 'name':
    d = input()
    sql = '''
    delete from phonebook where name = %s;
    '''
    cursor.execute(sql, d)


cursor.close()
conn.commit()
conn.close()


