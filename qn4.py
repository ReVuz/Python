'''Write a program to create a class Box with data members length, breadth, height, area, and volume.
Provider constructor that enables initialization with one parameter (for cube), two parameters (for square prism)
three parameters (rectangular prism). Also, provide functions to calculate area and volume.
Create a list of N boxes with random measurements and print the details of the box with maximum volume: area ratio.'''
import random

class Box:
  def __init__(self,l,b,h):
    if (b==None and h==None):
      self.__length=self.__breadth=self.__height=l
      print("\ncube")
    elif (h==None):
      self.__length=self.__breadth=l
      self.__height=b
      print("\nsquare")
    else:
      self.__length=l
      self.__breadth=b
      self.__height=h
      print("\nrectangle")

  def area(self):
    self.__area=self.__length*self.__breadth

  def vol(self):
    self.__vol=self.__length*self.__breadth*self.__breadth*self.__height

  def details(self):
    self.area()
    self.vol()
    if self.__length==self.__breadth==self.__height:
      print("length ",self.__length)
    elif self.__length==self.__breadth:
      print("length",self.__length,
      "breadth",self.__breadth)
    else:
      print("length",self.__length,
        "breadth",self.__breadth,
        "hieght",self.__height)
    
    print("area is: ",self.__area)
    print("volume is: ",self.__vol)

  def ratio(self):
    ratio=self.__vol/self.__area
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
print("\nThe ratios of cube square and rectangle")
print(cube_ratio)#just to nkow whats going on
print(sqr_ratio)
print(rect_ratio)

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
        
