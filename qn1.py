'''Suppose a newly born pair of rabbits, one male and one female, are put in a field. Rabbits can mate at the age of one month so that at the end of its second month,
a female has produced another pair of rabbits. Suppose that our rabbits never die and that the female always produces one new pair every month from the second month.
Develop a program to show a table containing the number of pairs of rabbits in the first N months.'''

month = int(input("Enter the number of months : "))
a,pair=0,0
b=1
print("Month \tPairs")
for i in range(1,month+1):
    if(i==1):
        print(i,"\t",b)
    else:
        pair=a+b
        a=b
        b=pair
        print(i,"\t",pair)


