import cx_Oracle

conn = cx_Oracle.connect("ansible/ansible@192.168.1.232:1521/ORCLPDB1")

c = conn.cursor()
try:
    c.execute("drop table ansible_test purge")
except cx_Oracle.IntegrityError:
    print("Table doesn't exits, trying to create...")
else:
    print("Table droppped.")

try:
    c.execute("create table ansible_test(id number, adate date, achar varchar2(100 byte)) tablespace users")
except cx_Oracle.IntegrityEror:
    print("Cannot create table!!")
else:
    print("Table created.")
conn.close()
