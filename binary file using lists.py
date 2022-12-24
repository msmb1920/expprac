import pickle

def create():
    f=open("student.dat","w")
    while true:
        rn0=int(input("enter roll no:"))
        name=input("enter nmae:")
        gender=input("enter gender:")
        std=int(input("enter standard:")
        sec=input("enter section:")
        data=[rno,name,gender,std,sec]
        pickle.dump(data,f)
        ch=input("do you want to continue(y/n):")
        if ch=='n':
                break
    f.close()

def append():
    f=open("student.dat","ab")
    while true:
        rn0=int(input("enter roll no:"))
        name=input("enter nmae:")
        gender=input("enter gender:")
        std=int(input("enter standard:")
        sec=input("enter section:")
        data=[rno,name,gender,std,sec]
        pickle.dump(data,f)
        ch=input("do you want to continue(y/n):")
        if ch=='n':
                break

def display():
    f=open("student.dat","rb")
    try:
        while true:
            k=pickle.load(f)
            print(k)
    except EOFError:
        f.close()

def search():
    f=open("studnt.dat","rb")
    rn=int(input("enter roll no to find:"))
    flag=0
    try:
        while true:
            k=pickle.load(f)
            if k[0]==rno:
                print(k)
                flag=1
        except EOFError:
            f.close()
        if flag==0:
            print("sorry, record not found")

def create():
    while true:
        print("maine menu")
        print("1.append")
        print("2.display")
        print("3.search")
        print("4.exit")
        ch=int(input("enter your choice:"))
        if ch==1:
            append()
        if ch==2:
            display()
        if ch==3:
            search()
        if ch==4:
            break
