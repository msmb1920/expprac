import csv

def create():
    heading=["name","age","sex"]
    rows=[["rat",43,"m"],["anu",45,"f"],["raja",50,"m"],["rani",53,"f"]]
    with open("data.csv","w",newline="") as f:
        obj=csv.writer(f)
        obj.writerow(heading)
        obj.wrterows(rows)
        print("records are wrttien in date,csv file")

def display():
    with open("date.csv","r",newline="") as f:
        obj=csv.reader(f)
        for x in obj:
            print(x)

def search():
    found=0
    with open("data.csv","r",newline="") as f:
        obj=csv.reader(f)
        n-input("enter name to search:")
        for row in obj:
            if row[0]==n:
                print("name=",row[0])
                print("age=",row[1])
                print("sex=",row[2])
                found=1
            if dound==0:
                print("sorry, record not found")


create()
display()
search()
