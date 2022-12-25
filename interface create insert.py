import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="bvm", db="employee")
cur = con.cursor()
cur.execute("create table empl(Eno int, Ename varchar(10), Esal float)")
print("Table created successfully")


while True:
    eno = int(input("Enter employee number: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    query = "insert into empl values({},'{}',{})".format(eno, name, salary)
    cur.execute(query)
    con.commit()
    print("Row inserted successfully...")
    ch = input("Do you want to enter more records (y/n): ")
    if ch == "n":
        break

cur.execute("select * from empl")
data = cur.fetchall()
for i in data:
    print(i)
print("Total number of rows retrieved =", cur.rowcount)
