'''Read the file 'iris.json' as a text file :
1. Create a list having each line of the file as an element
2. Convert it into a list of dictionary objects.
3. Show the details of all flowers whose species is "setosa".
4. Print the minimum petal area and max sepal area in each species
5. Sort the list of dictionaries according to the total area are sepal and petal.'''

import json
file=open('iris.json','r')
iris=file.read()
print("List: \n",iris.split("\n"))
d=json.loads(iris)
print("List of Dictionary: \n",d)
print("Details of all flowers whose species is \"setosa\" : ")
petal_area=[]
sepal_area=[]
dup_species=[]
total_area=[]
for i in d:
    if(i['species']=='setosa'):
        print(i)
    dup_species.append(i['species'])
    petal_area.append(i['petalLength']*i['petalWidth'])
    sepal_area.append(i['sepalLength']*i['sepalWidth'])
    total_area.append(sepal_area[i]*petal_area[i])
dup_species=set(dup_species)
species=list(dup_species)
print("Species \tPetal area(min) \tSepal area(max)")
for j in range(len(species)):
    for k in d:
        if(k['species']==species[j]):
            print(species[j],round(min(petal_area)),max(sepal_area))
sortd=(sorted(sort_d,key=lambda i:i[total_area]))
for l in sortd:
    print(l)
