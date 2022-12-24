def print_diagonal(a,n):
    for i in range(n):
        for j in range(n):
            if i==j or i+j==n-1:
                print(a[i][j],end=" ")
            else:
                print(" ",end=" ")
            print()

def swap_diagonal(a,n):
    for i in range(n):
        a[i][i], a[i][n-i-1]=a[n-i-1], a[i][i]

a=[]
n=int(input("enter size of matrix:"))
print("enter values for sqr matrix of",n,"x",n)

for i in range(n):
    t=[]
    for j in range(n):
        t.append(int(input()))
    a.append(t)

print("diagonal before swapping:")
print_diagonal(a,n)
swap_diagonal(a,n)
print("diagonal after swapping:")
print_diagonal(a,n)
