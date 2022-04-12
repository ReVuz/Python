'''Write a program to create a class Box with data members length, breadth, height, area, and volume.
Provider constructor that enables initialization with one parameter (for cube), two parameters (for square prism)
three parameters (rectangular prism). Also, provide functions to calculate area and volume.
Create a list of N boxes with random measurements and print the details of the box with maximum volume: area ratio.'''
from random import *

class Box:
  def __init__(self,l,b,h):
    if (b==None and h==None):
      self.length=self.breadth=self.height=l
      print("\ncube")
    elif (h==None):
      self.length=self.breadth=l
      self.height=b
      print("\nsquare")
    else:
      self.length=l
      self.breadth=b
      self.height=h
      print("\nrectangle")

  def area(self):
    self.area=self.length*self.breadth

  def vol(self):
    self.vol=self.length*self.breadth*self.breadth*self.height

  def details(self):
    self.area()
    self.vol()
    if self.length==self.breadth==self.height:
      print("length ",self.length)
    elif self.length==self.breadth:
      print("length",self.length,
      "breadth",self.breadth)
    else:
      print("length",self.length,
        "breadth",self.breadth,
        "hieght",self.height)
    
    print("Area: ",self.area)
    print("Volume: ",self.vol)

  def ratio(self):
    ratio=self.vol/self.area
    return ratio

c=[]
r=[]
s=[]
cube_ratio=[]
sqr_ratio=[]
rect_ratio=[]

for i in range(2):
  #cube
  c.append("")
  c[i]=(Box(random.randint(1,100),None,None))
  c[i].details()
  cube_ratio.append(c[i].ratio())

  #sqr
  s.append("")
  s[i]=Box(random.randrange(1,100),random.randint(1,100),None)
  s[i].details()
  sqr_ratio.append(s[i].ratio())

  #rect
  r.append("")
  r[i]=Box(random.randint(1,100),random.randint(1,100),random.randint(1,100))
  r[i].details()
  rect_ratio.append(r[i].ratio()) 
  rect_ratio.append(r[i].ratio()) 

full_ratio=[max(cube_ratio),max(sqr_ratio),max(rect_ratio)] #getting the highest ratio from each shape
ind=full_ratio.index(max(full_ratio))
print()
if ind==0:                                                  #printing the shape details ofthe highest ratio shape
  pos=int(cube_ratio.index(max(cube_ratio)))
  print("max cube",max(cube_ratio))
  print("\nCube with Most area to volume ratio: ")
  c[pos].details()
  print(" THE ratio is: ",c[pos].ratio())
elif ind==1:
  pos=sqr_ratio.index(max(sqr_ratio))
  print("\nSquare with Most area to volume ratio: ")
  s[pos].details()
  print("THE ratio is: ",s[pos].ratio())
  
elif ind==2:
  pos=rect_ratio.index(max(rect_ratio))
  print("\nRectangle with Most area to volume ratio: ")
  r[pos].details()
  print("THE ratio is: ",r[pos].ratio())
        
