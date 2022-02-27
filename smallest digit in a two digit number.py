#Smallest digit of a two digit number
a= int(input("Enter a two digit number "))
ones=a%10
tens=a//10
if ones>tens :
    print(tens," is the smallest number in ",a)
else :
    print(ones," is the smallest number in ",a)
