def create():
    f = open("India.txt", "w")
    while True:
        data = input("Enter data to be stored: ")
        f.write(data + "\n")
        ch = input("Do you want to continue(y/n): ")
        if ch == "n":
            break
    f.close()

def counti():
    f = open("India.txt", "r")
    lines = f.readlines()
    c = 0
    for line in lines:
        c += line.count("india") + line.count("India")
    print("Number of lines =", len(lines))
    print("Number of times 'india' appears =", c)
    f.close()

def display():
    f = open("India.txt", "r")
    data = f.readlines()
    for k in data:
        print(k.replace(" ", "#"))
    f.close()

while True:
    print("Main menu")
    print("1. Create\n2. No. of line and india count\n3. Display with #\n4. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        create()
    elif ch == 2:
        counti()
    elif ch == 3:
        display()
    elif ch == 4:
        break
