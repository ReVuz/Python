#Number multiple of another or not
a=int(input("Enter a number "))
b=int(input("Enter another number "))
if a%b==0 :
    print(a," is a multiple of ",b)
else:
    print(a," is not a multiple of ",b)

if b%a==0 :
    print(b," is a multiple of ",a)
else:
    print(b," is not a multiple of ",a)
