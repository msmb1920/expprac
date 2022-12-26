def create():
    f=open("school.txt","w")
    while True:
        ch=input("enter data to store:")
        f.write(ch+"\n")
        choice=input("do you want to enter more lines(y/n):")
        if choice=="n":
            break
    break

def display(filename):
    f=open(filename,"r")
    data=f.read()
    print(filename,"content:\n"+data)
    f.close()

def transfer():
    x=open("school.txt","r")
    y=open("myschool.txt","w")
    k=x.readlines()
    for i in k:
        if 'z' not in i:
            y.write(i+"\n")
    x.close()
    y.close()

create()
display("school.txt")
transfer()
display("myschool.txt")
