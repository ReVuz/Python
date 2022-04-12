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
  for i in data_dict:					  #'i' is the dictionary element in the list
    if (i['species']=='setosa'):
        print('Sepel length : %f '%(i['sepalLength']))

def get_areas(data_dict):
  petal_areas=[i['petalLength']*i['petalWidth']  for i in data_dict]
  sepal_areas=[i['sepalLength']*i['sepalWidth'] for i in data_dict]
  return petal_areas,sepal_areas

def get_min_petal_area(petal_areas):
  m1 = min([area for area,species in petal_areas if species=='setosa'])
  m2 = min([area for area,species in petal_areas if species=='virginica'])
  m3 = min([area for area,species in petal_areas if species=='versicolor'])
  return (m1,m2,m3)
def get_max_sepal_area(sepal_areas):
  m4 = max([area for area,species in petal_areas if species=='setosa'])
  m5 = max([area for area,species in petal_areas if species=='virginica'])
  m6 = max([area for area,species in petal_areas if species=='versicolor'])
  return(m4,m5,m6)

data = read_as_list('iris.json')
for line in data:
  print(line)

data_dict = read_as_dict('iris.json')
for row in data_dict:
  print(row)

print_details_setosa(data_dict)
abc,pqr=get_areas(data_dict)
get_min_petal_area(abc)
