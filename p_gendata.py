import random
import string
import datetime
import cx_Oracle

conn = cx_Oracle.connect("ansible/ansible@192.168.1.232:1521/ORCLPDB1")

c = conn.cursor()
dcn = 10000     # First commit at that number of rows

for a in range(0, 1000000):
    a_num1 =  ''.join(random.choice(string.digits) for i in range(15))
    a_date1 = datetime.date(1920, 1, 1) + datetime.timedelta(days=random.randrange(365*150))
    a_str1 = ''.join(random.choice(string.ascii_letters) for i in range(100))
    c.execute("insert into ansible_test values(:N, :D, :S)" , [a_num1, a_date1, a_str1])
    
    if a >= dcn : # check if there is time to commit
        conn.commit()
        dcn +=10000   # next commit increament

conn.commit()
conn.close()
