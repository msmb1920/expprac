import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="mysql", db="employee")
cur = con.cursor()

print("Displaying the records before updating...")
cur.execute("select * from empl")
data = cur.fetchall()
for i in data:
    print(i)

cur.execute("update emp set Ename='sumita' where Eno=2")
con.commit()

print("displaying the records after updating...")
cur.execute("select * from empl")
data=cut.fetchall()
for i in data:
    print(i)

