#Program to find distance between two points on a number line
x1=int(input("Enter the value for x1 "))
x2=int(input("Enter the value for x2 "))
y1=int(input("Enter the value for y1 "))
y2=int(input("Enter the value for y2 "))
if(x1>x2 or y1>y2):
    d=((x1**2-x2**2)+(y1**2-y2**2))**0.5
else:
    d=((x2**2-x1**2)+(y2**2-y1**2))**0.5
    
print("Distance between ",x1,",",y1," and ",x2,",", y2," is ",d)
