#Binary to decimal

b=int(input("Enter a binary number "))
num=b
i=0
dec=0
while num!=0 :
    r=num%10
    r=(r*2)**i
    i=i+1
    dec=dec+r
    num=num//10
print(b," to decimal value wil be ",dec)
