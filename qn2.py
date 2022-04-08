'''Write a program to read a string containing numbers separated by a space and convert it as a list of integers. Perform the following operations on it.
1. Rotate elements in a list by 'k' position to the right
2. Convert the list into a tuple using list comprehension
3. Remove all duplicates from the tuple and convert them into a list again.
4. Create another list by putting the results of the evaluation of the function 𝑓(𝑥) = 𝑥2 – 𝑥 with each element in the final list
5. After sorting them individually, merge the two lists to create a single sorted list.'''

string=str(input("Enter some numbers : "))
print("String : ",string)
l=string.split()
print("String converted to list : ",l)
tup=tuple([int(i) for i in l])
print("List to tuple : ",tup)
s=set(tup)
print("After removing the duplicates : ",s)
l2=list(s)
print("After converting to list again : ",l2)
l3=list()
for i in l2:
    x=(i*i)-i
    l3.append(x)
print("List after evaluation : ",l3)
l4=[]
l4=l2+l3
print("Final sorted list : ",sorted(l4))
