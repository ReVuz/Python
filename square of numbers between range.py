#Square of natural number between two given numbers
a=int(input("Enter starting range "))
b=int(input("Enter ending range "))
print("Square of numbers between ",a," and ",b," are: ")
for i in range(a+1,b):
    i=i**2
    print(i,end=',')
