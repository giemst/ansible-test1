import random
import string
import datetime
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('192.168.1.231', '1521', service_name='ORCLPDB1') 
conn = cx_Oracle.connect(user=r'ansible', password='ansible', dsn=dsn_tns)
#conn = cx_Oracle('ansible/ansible@srvoradb1/ORCLPDB1')

c = conn.cursor()
for a in range(1, 100):
    a_num1 =  ''.join(random.choice(string.digits) for i in range(15))
    a_date1 = datetime.date(1920, 1, 1) + datetime.timedelta(days=random.randrange(365*150))
    a_str1 = ''.join(random.choice(string.ascii_letters) for i in range(100))
    c.execute("insert into ansible_test values(:N, :D, :S)" , [a_num1, a_date1, a_str1])
    conn.commit()
conn.close()
