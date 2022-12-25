import csv

def create():
    with open("myfile.csv","w",newline="") as csvfile:
              mywriter=csv.writer(csvfile,delimiter=",")
              ch='y'
              while ch.lower()=='y':
                  eno = int(input("Enter the employee number: "))
                  name = input("Enter Name : ")
                  salary = int(input("Enter salary : "))
                  mywriter.writerow([eno, name, salary])
                  print("Data saved...")
                  ch = input("Add more(y/n): ")

def totalsalary():    
    with open("myfile.csv","r",newline="") as csvfile:
        myreader = csv.reader(csvfile, delimiter=",")
        totalsal=0
        print("***********Salary Slip***********")
        print("-"*33)
        print("EMPNO", "%15s" % "NAME", "%10s" % "SALARY")
        print("-"*33)
        for row in myreader:
            totalsal +=int(row[2])
            print("%5s" % row[0], "%15s" % row[1], "%10s" % row[2])
        print("-"*33)
        print("%21s" % "TOTAL SALARY:", "%10s" % totalsal)
        print("-"*33)

def salarysearch():
    with open("myfile.csv","r",newline="") as csvfile:
        myreader=csv.reader(csvfile,delimiter=",")
        totalsal=0
        count=0
        print("\n\n\n******Salary less than 40000******")
        print("-"*34)
        print(" EMPNO", "%15s" % "NAME", "%10s" % "SALARY")
        print("-"*34)
        for row in myreader:
            if int(row[2])<40000:
                totalsal+=int(row[2])
                count+=1
                print("%6s" % row[0], "%15s" % row[1], "%10s" % row[2])
        print("-"*34)
        print("%22s" % "TOTAL sal < 40000:", "%10s" % totalsal)
        print("-"*34)
        print("No of employees sal < 40000:", count)
        print("-"*34)

create()
totalsalary()
salarysearch()
