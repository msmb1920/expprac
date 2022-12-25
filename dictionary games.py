def Input(d,n):
    for i in range(n):
        game=input("enter the game:")
        p=[]
        p.append(input("enter playr name:"))
        p.append(input("enter country name:"))
        p.append(input("enter the points:"))
        d[game]=p
    print("-"*70)

def show(d):
    print("\nrecords in ascending order of game:")
    for k in sorted(d):
        print(k,d[k])
    print("-"*70)

def search(d,coun):
    flag=0
    for key in d:
         d[key][2]+=d[key][2]*1.5
         flag+=1
    if flag==0:
        print("country not found")
    else:
        print(flag,"records updated")
    print("-"*70)

def modify(d,game):
    flag=0
    for key in d:
        if key==game:
            d[key][2]+=d[key][2]*1.5
            flag+=1
    if flag==0:
        print("country not found")
    else:
        print(flag,"records updated")
    print("-"*70)

d={}
n=int(input("how many games:"))
Input(d,n)
coun=input("enter country name to be searched:")
show(d)
search(d,coun)
game=input("enter game name to increase points:")
modify(d,game)
print("records after updation")
show(d)
