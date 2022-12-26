import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", passwd="mysql", db="employee")
cur = con.cursor()
print("Displaying the records before delete..")
cur.execute("select * from emp1")
for i in cur:
    print(i)

temp=int(input("enter roll number to delete:"))
query="delete from emp1 where eno={}".format(temp)
cur.execute(query)
con.commit()
print("row deleted successfully")

print("displaying the records after deletion")
cur.execute("select * from emp1")
for i in cur:
    print(i)

    
