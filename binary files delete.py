import pickle,os

def append():
    f=open("std.dat","ab")
    while True:
        rno=int(input("enter roll no:"))
        name=input("enter name:")
        mark=int(input("enter mark:"))
        data={"rollno":rno, "name":name, "mark":mark}
        pickle.dump(data,f)
        ch=input("do you want to continue(y/n):")
        if ch=='n':
            break
    f.close()

def display():
    f=open("std.dat","rb")
    try:
        while True:
            k=pickle.load(f)
            print("rollno:",k["rollno"])
            print("name:",k["name"])
            print("mark",k["mark"])
    except EOFError:
        f.close()

def delete():
    f=open("std.dat","rb")
    t=open("temp.dat","wb")
    rno=int(input("enter roll no to delete:"))
    flag=0
    try:
        while True:
            k=pickle.load(f)
            if k["rollno"]==rno:
                flag=1
            else:
                pickle.dump(k,t)
    except EOFError:
        f.close()
        t.close()
    if flag==0:
        print("sorry record not found")
    os.remove("std,.dat")
    os.remove("temp.dat","std.dat")

while True:
    print("main menu\n1.append\n2.display\n3.delete\n4.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        append()
    elif ch==2:
        display()
    elif ch==3:
        modify()
    elif ch==4:
        break
