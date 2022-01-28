import cx_Oracle

conn = cx_Oracle.connect("ansible/ansible@192.168.1.232:1521/ORCLPDB1")

c = conn.cursor()

# checking if table ANSIBLE_TEST exists

c.execute("select table_name from user_tables where table_name='ANSIBLE_TEST'")  
rows = c.fetchall()

#  if query retuns 1 row - table already exists, and needs to be dropped 

if len(rows) == 1: 
    c.execute("drop table ansible_test purge")

#  creating table

c.execute("create table ansible_test(id number, adate date, achar varchar2(100 byte)) tablespace users")

conn.close()
