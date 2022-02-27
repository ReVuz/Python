#Print first n odd number
n=int(input("Enter range "))
s=1
for i in range(0,n):
    print(s,end=',')
    s=s+2
