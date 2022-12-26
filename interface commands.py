import mysql.connector

def fetchdata():
    mycursor.execute("select * from student")
    result = mycursor.fetchall()
    for x in result:
        print(x)

def adddata():
    mycursor.execute("insert into student values('Ritu', 4000, 'Science', 345, 'B', 11)")
    mycursor.execute("insert into student values('Ankush', 6000, 'Commce', 445, 'A', 12)")
    mycursor.execute("insert into student values('Pihu', 3566, 'Humanis', 446, 'A', 11)")
    mycursor.execute("insert into student values('Tinku', 8900, 'Science', 545, 'A+', 12)")
    mydb.commit()
    print("Records added")

def updatedata():
    mycursor.execute("update student set stipend=5000 where name='Ritu'")
    mydb.commit()
    print("Record updated")


def deletedata():
    mycursor.execute("delete from student where name='ritu'")
    mydb.commit()
    print("record deleted")

mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql", db="s1")
mycursor = mydb.cursor()

while True:
    print("1. Add record\n2. Update record\n3. Delete record\n4. Display record\n5. Exit")
    c = int(input("Enter choice: "))
    if c == 1:
        adddata()
    elif c == 2:
        updatedata()
    elif c == 3:
        deldata()
    elif c == 4:
        fetchdata()
    elif c == 5:
        print('Exiting')
        break
    else:
        print('Wrong input')
