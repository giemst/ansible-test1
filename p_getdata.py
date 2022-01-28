import cx_Oracle
import csv  

conn = cx_Oracle.connect("ansible/ansible@192.168.1.232:1521/ORCLPDB1")


with open('/tmp/gathered_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    c = conn.cursor()
    c.execute("select id,to_char(adate,'yyyy-mm-dd'),achar from ansible_test where rownum <101")
    for row in c:
        writer.writerow(row)
    conn.close()
