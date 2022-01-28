import cx_Oracle
import csv  

conn = cx_Oracle.connect("ansible/ansible@192.168.1.232:1521/ORCLPDB1")


with open('p_ansible.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    c = conn.cursor()
    c.execute('select id,adate,achar from ansible_test where rownum <101') # use triple quotes if you want to spread your query across multiple lines
    for row in c:
        writer.writerow(row)
#    print (row[0], ',', row[1], ',' ,row[2]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    conn.close()
