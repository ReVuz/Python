#Sum of first n natural numbers
n=int(input("Enter range "))
sum=0
for i in range(1,n+1):
    sum+=i

print("Sum of ",n," natural numbers are : ",sum)
