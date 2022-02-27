#Enter two unequal number and interchange them without using a third variable

a=int(input("Enter a number "))
b=int(input("Enter another number "))
print("Numbers before swapping : \na = ",a,"\nb = ",b)
a=a+b
b=a-b
a=a-b
print("Numbers after swapping : \na = ",a,"\nb = ",b)
