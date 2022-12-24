from math import pi
from random import randint

def sintaylor():
    n=int(input("enter the value of n in degrees:"))
    x=(pi/180)*n
    summ=0
    sign=1
    for i in range(1,n+1,2):
        f=1
        for j in range(1):
            f*=j+1
        summ+=((x**i)/f)*sign
        sign*=-1
    print("the result of the series is".summ)

def dice():
    ch=int(input("enter 0 to main menu of 1 to roll the dice:"))
    while ch==1:
        print("the number for u is...")
        print(randint(1,6))
        ch=int(input("enter 0 to main menu or 1 to roll the dice:"))

while true:
    print("main menu")
    print("1. sin series - Taylor series")
    print("2.simulate a dice")
    print("3.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        sintaylor()
    if choice==2:
        dice()
    if choice==3:
        break
