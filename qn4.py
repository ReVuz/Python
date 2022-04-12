'''Write a program to create a class Box with data members length, breadth, height, area, and volume.
Provider constructor that enables initialization with one parameter (for cube), two parameters (for square prism)
three parameters (rectangular prism). Also, provide functions to calculate area and volume.
Create a list of N boxes with random measurements and print the details of the box with maximum volume: area ratio.'''
import random

class Box:
  def __init__(self,l,b,h):
    if (b==None and h==None):
      self.length=self.breadth=self.height=l
      print("\nCube")
    elif (h==None):
      self.length=self.breadth=l
      self.height=b
      print("\nSquare Prism")
    else:
      self.length=l
      self.breadth=b
      self.height=h
      print("\nRectangle Prism")

  def area(self):
    self.ar=self.length*self.breadth

  def vol(self):
    self.volume=self.length*self.breadth*self.breadth*self.height

  def details(self):
    self.area()
    self.vol()
    if self.length==self.breadth==self.height:
      print("\nlength ",self.length)
    elif self.length==self.breadth:
      print("\nlength",self.length,
      "\nbreadth",self.breadth)
    else:
      print("\nlength",self.length,
        "\nbreadth",self.breadth,
        "\nheight",self.height)
    
    print("\nArea: ",self.ar)
    print("\nVolume: ",self.volume)

  def ratio(self):
    ratio=self.volume/self.ar
    return ratio

c=[]
r=[]
s=[]
cube_ratio=[]
sqr_ratio=[]
rect_ratio=[]
n= int(input("enter range : "))
for i in range(n):
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
  print("\nMost area to volume ratio is for Cube ")
  c[pos].details()
  print(" The ratio is: ",c[pos].ratio())
elif ind==1:
  pos=sqr_ratio.index(max(sqr_ratio))
  print("\nMost area to volume ratio is for Square Prism")
  s[pos].details()
  print("The ratio is: ",s[pos].ratio())
  
elif ind==2:
  pos=rect_ratio.index(max(rect_ratio))
  print("\nMost area to volume ratio is for Rectangle Prism")
  r[pos].details()
  print("The ratio is: ",r[pos].ratio())
        
