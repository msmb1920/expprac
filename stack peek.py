def Push(stk,item,top):
    stk.append(item)
    top+=1
    return top

def Pop(stk,top):
    if stk==[]:
        return "underflow",top
    item=stk.pop()
    top-=1
    return item,top

def Peek(stk,top):
    if stk==[]:
        return"underflow"
    return stk[top]

def Display(stk,top):
    if stk==[]:
        print("stack is empty")
    else:
        print("stack values are:")
        for i in range(top,-1,-1):
            print(stk[i])

stack=[]
top=-1
while True:
    print("\nStack Menu\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    ch = int(input("Enter your choice(1-5): "))
    if ch == 1:
        item = int(input("Enter any value: "))
        top = Push(stack, item, top)
        print(item, "is inserted")
    elif ch==2:
        item,top = Pop(stack,top)
        if item == "underflow":
            print("Stack is empty, Underflow")
        else:
            print("poped item is", item)
    elif ch==3:
        item=Peek(stack,top)
        if item=="underflow":
            print("Stack is empty")
        else:
            print("topmost item is",item)
    elif ch==4:
        Display(stack,top)
    elif ch==5:
        break
    else:
        print("invalid choice")
            
