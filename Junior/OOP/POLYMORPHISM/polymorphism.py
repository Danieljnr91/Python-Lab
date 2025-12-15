# class Person:
#   def walk(self):
#     print("I can walk")
#   def eat(self):
#     print("I eat cooked food")
# class Animal:
#   def eat(self):
#     print("I can eat uncooked food")
#   def walk(self):
#     print("I have multiple legs")
# def display(d_typing):
#   d_typing.walk()
#   d_typing.eat()

# p=Person()
# a=Animal()
# display(p)
# display(a)
  
  
class Circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*self.radius**2
class Triangle:
  def __init__(self,base,height):
    self.base=base
    self.height=height
  def area(self):
    return 0.5*self.base*self.height
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
def shape_area(output):
  print(output.area())

cirlce=Circle(3)
triangle=Triangle(3,4)
rectangle=Rectangle(3,4)

shape_area(cirlce)
shape_area(triangle)
shape_area(rectangle)


