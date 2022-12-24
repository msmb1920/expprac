def palind(s):
    if s==s[::-1]:
        return 1
    else:
        return 0

def check(s):
    if s.isalpha:
        if s in "aeiouAEIOU":
            return 'v'
        else:
            return 'c'
n=int(input("enter number of strings:"))
p=v=c=0
print("enter",n,"strings:")

for i in range(n):
    a=input()
    if palind(a)==1:
        p+=1
    res=check(a)
    if res=='v':
        v+=1
    elif res=='c':
        c+=1

print("palindrome:",p)
print("consoonant:",c)
print("vowel:",v)
