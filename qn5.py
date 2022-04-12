class Shapes:
  volume = None
  area   = None

  def printVolume(self):
    print("Volume = ",self.volume)
  def printArea(self):
    print("Area = ",self.area)


class Cylinder(Shapes):
  height = None
  radius = None

  def __init__(self,r,h):
    self.height=h
    self.radius=r

  def calcArea(self):
    self.area= 6.28*self.radius*(self.height + self.radius)

  def calcVolume(self):
    self.volume=3.14*self.radius*self.radius*self.height


class Sphere(Shapes):
  radius = None

  def __init__(self,r):
    self.radius = r

  def calcVolume(self):
    self.volume = 4.19*self.radius*self.radius*self.radius

  def calcArea(self):
    self.area = 12.56*self.radius*self.radius

r1=float(input("Enter the radius of Sphere : "))
print("\nArea and Volume Of Sphere\n")
s = Sphere(r1)
s.calcVolume()
s.calcArea()
s.printVolume()
s.printArea()
print(" ")

r2=float(input("Enter the radius of a Cylinder : "))
h=float(input("Enter the height of a Cylinder : "))
print("\nArea and Volume of Cylinder\n")
c= Cylinder(r2,h)
c.calcArea()
c.calcVolume()
c.printArea()
c.printVolume()
