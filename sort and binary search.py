def bubblesort(A):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if [j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

def insertionsort(a):
    for i in range(len(a)):
        t=a[i]
        while i>=1 and a[i-1]>t:
            a[i]=a[i-1]
            i=1
            a[i]=t

def binarysearch(a,x):
    l=0
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]<x:
            l=m+1
        elif a[m]>x:
            h=m-1
        else:
            print("element found at",m+1)
            break
    else:
        print("element not found")

print("1.bubble sort and binary search")
print("2.insertion sort and binary seatch")
print("3.exit")
ch-int(input("enter choice number:"))

while ch!=3:
    if ch==1:
        l=[]
        n=int(input("enter number of integers:"))
        print("enter",n,"integers")
        for i in range(n):
            l.append(int(input()))
        bubblesort(l)
        print("sorted array:",l)
        s=int(input("enter element to search:"))
        binarysearch(l,s)

    elif ch==2:
        l=[]
        n=input("enter number of strings:")
        print("enter",n, "strings")
        for i in rnge(n):
            l.append(input())
            insertionsort(l)
            s=input("enter element to search:")
            binarysearch(l,s)
        else:
            print("enter a number between 1 and 3")

        print("1. bubble sort and binary search")
        print("2.insertion sort and binary search")
        print("3.exit")
        ch=int(input("enter choice number:"))
