class Shapes:
  _volume = None
  _area   = None

  def printVolume(self):
    print("Volume = ",self._volume)
  def printArea(self):
    print("Area = ",self._area)


class Cylinder(Shapes):
  __height = None
  __radius = None

  def __init__(self,r,h):
    self.__height=h
    self.__radius=r

  def calcArea(self):
    self._area= 6.28*self.__radius*(self.__height + self.__radius)

  def calcVolume(self):
    self._volume=3.14*self.__radius*self.__radius*self.__height


class Sphere(Shapes):
  __radius = None

  def __init__(self,r):
    self.__radius = r

  def calcVolume(self):
    self._volume = 4.19*self.__radius*self.__radius*self.__radius

  def calcArea(self):
    self._area = 12.56*self.__radius*self.__radius

r1=float(input("Enter the radius of Sphere : "))
print("---Sphere---")
s = Sphere(r1)
s.calcVolume()
s.calcArea()
s.printVolume()
s.printArea()
print(" ")

r2=float(input("Enter the radius of Cylinder : "))
h=float(input("Enter the height of cylinder : "))
print("Cylinder---")
c= Cylinder(r2,h)
c.calcArea()
c.calcVolume()
c.printArea()
c.printVolume()
