import psycopg2
from psycopg2 import Error
 
conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

by = input('by:\n')
d = input()

sql1 = '''
create or replace procedure delete_user(user_name varchar)
as $$
begin
    delete from phonebook where name = user_name;
end
$$
language plpgsql
'''

sql3 = '''
call delete_user(%s)
'''

sql4 = '''
call delete_user2(%s)
'''

sql2 = '''
create or replace procedure delete_user2(num varchar)
as $$
begin
    delete from phonebook where number = num;
end
$$
language plpgsql
'''

cursor = conn.cursor()

if by == 'name':
    cursor.execute(sql1)
    cursor.execute(sql3, [d])
elif by == 'number':
    cursor.execute(sql2)
    cursor.execute(sql4, [d])

cursor.close()
conn.commit()
conn.close()

