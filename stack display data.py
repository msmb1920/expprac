def PUSH(student,top):
    ch='y'
    while ch=='y':
        rollno=int(input("enter roll number:"))
        name=int(input("enter name:"))
        student.append((rollno,name))
        top+=1
        ch=input("do you want to add more(?y/n):")
    return top

def POP(student,top):
    if len(student)<=0:
        print("stack is empty,underflow")
    else:
        rollno,name=student.pop()
        top-=1
        print("value deleted from stack is:",rollno,name)
    return top
        
def SHOW(student,top):
    if len(student)<=0:
        print("stack is empty")
    else:
        print("the stack elements are:")
        for i in range(top,-1,-1):
            rollno,name=student[i]
            print(rollno,name)

student=[]
top=-1

while True:
    print()
    print("S T A C K   O P E R A T I O N")
    print("-"*15)
    print("1.add student data")
    print("2.remove student data")
    print("3.display student data")
    print("4.stop operation")
    cho=int(input("enter option:"))
    if cho==1:
        top=PUSH(student,top)
    elif cho==2:
        top=POP(student,top)
    elif cho==3:
        top=SHOW(student,top)
    elif cho==4:
        break
