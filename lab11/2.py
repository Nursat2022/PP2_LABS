from locale import currency
import psycopg2

name = input('Enter name:\n')
number = input('Enter phone\n')
id = input('Enter id:\n')

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cur = conn.cursor()

sql = '''
create or replace procedure ins(id integer, name varchar, number varchar)
as 
$$
begin   
    insert into phonebook values ($1, $2, $3, 'None');
end;
$$ language plpgsql;
'''

cur.execute(sql)
cur.execute('call ins(%s, %s, %s);', (id, name, number))

cur.close()
conn.commit()
conn.close()