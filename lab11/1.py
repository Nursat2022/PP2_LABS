import psycopg2
 
name = input('name:\n')

conn = psycopg2.connect(
    host='localhost', 
    database='pp2demo',
    user='pp2demo_user',
    password='123'
)

cur = conn.cursor()

sql = '''
create or replace function get_info(name varchar)
    returns record 
as
$$
declare
    student record;
begin
    select * into student from phonebook where phonebook.name = $1;
    return student;
end;
$$
language plpgsql;
'''

cur.execute(sql)
cur.execute("select get_info(%s);", [name])

info = cur.fetchone()
print(info)
cur.close()
conn.commit()
conn.close()