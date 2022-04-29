import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cursor = conn.cursor()

change = input('what do you want to change:\n')

if change == 'number':
    new = input('new:\n')
    id = int(input('id:\n'))
    sql = '''
    update phonebook set number = %s where id = %s;  
    '''
    cursor.execute(sql, (new, id))

elif change == 'name':
    new = input('new:\n')
    id = int(input('id:\n'))
    sql = '''
    update phonebook set name = %s where id = %s;
    '''
    cursor.execute(sql, (new, id))


cursor.close()
conn.commit()
conn.close()


