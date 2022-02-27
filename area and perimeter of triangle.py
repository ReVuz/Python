#Area and perimeter of a triangle
a=int(input("Enter side a "))
b=int(input("Enter side b "))
c=int(input("Enter side c "))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))*0.5
print("Perimeter of triangle : ",p)
print("Area of triangle : ",area)
