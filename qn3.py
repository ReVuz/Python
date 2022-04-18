'''Read the file 'iris.json' as a text file :
1. Create a list having each line of the file as an element
2. Convert it into a list of dictionary objects.
3. Show the details of all flowers whose species is "setosa".
4. Print the minimum petal area and max sepal area in each species
5. Sort the list of dictionaries according to the total area are sepal and petal.'''

import json


def read_as_list(filename):
  fp=open(filename,"r")                             
  data=fp.readlines() 	
  print("List : ")		          #The file elements as list elements
  fp.close()
  return data
   
def read_as_dict(filename):
  fp=open(filename,'r')                            
  dictionary=json.load(fp)
  print("List of dictionary : ") 	
  return dictionary			 #list of dictionary

def print_details_setosa(data_dict):
  print("\nAll flowers whose species is setosa\n")
  for i in data_dict:			      
    if (i['species']=='setosa'):
        print('Sepel length : %f '%(i['sepalLength']))

def min_and_max_area(data):
  species_list = list()             # species names
  for i in data:
    species_list.append(i['species'])
  #removing duplicates
  species_list = list(set(species_list))
  sepal_area = []                #list to store sepal and petal area
  petal_area = []
  for i in species_list:
    for j in data:
      if(j['species']==i):
        sepal_area.append(j['sepalLength']*j['sepalWidth'])
        petal_area.append(j['petalLength']*j['petalWidth'])
    print()
    print(i.capitalize())
    #print minimum and maximum areas
    print("Minimum Petal Area : ",round(min(petal_area),2))
    print("Maximum Sepal Area : ",round(max(sepal_area),2))
    sepal_area.clear()
    petal_area.clear()
    
def total_sort(data):
  for i in data:
    #add total area to dictionary
    total_area = (i['petalLength']*i['petalWidth'])+(i['sepalLength']*i['sepalWidth'])
    i.update({'total_area':round(total_area,2)})
  sortedList = sorted(data,key=lambda i:i['total_area'])
  print("\nSorted List : ")
  for i in sortedList:
    print(i)

data = read_as_list('iris.json')
for line in data:
  print(line)

data_dict = read_as_dict('iris.json')
for row in data_dict:
  print(row)

print_details_setosa(data_dict)
min_and_max_area(data_dict)
total_sort(data_dict)
