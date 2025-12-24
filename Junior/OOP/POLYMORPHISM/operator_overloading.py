# class Vector2D:
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#   def __add__(self,other):
#     return Vector2D(self.a + other.a, self.b+other.b)
#   def __sub__(self,other):
#     return Vector2D(self.a - other.a, self.b-other.b)
#   def __repr__(self):
#     return f"Vector2D({self.a} ,{self.b})"
# v1=Vector2D(3,4)
# v2=Vector2D(1,2)
# print(v1+v2)
# print(v1-v2)

# from fractions import Fraction
# class Fractions:
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#   def __add__(self,other):
#     return self.a/other.a + self.b/other.b
#   def __sub__(self,other):
#     return self.a/other.a - self.b/other.b
#   def __mul__(self,other):
#     return self.a/other.a * self.b/other.b

# f1 = Fractions(1, 2)
# f2 = Fractions(1, 3)
# print(f1 + f2)  
# print(f1 - f2) 
# print(f1 * f2) 
# print(Fraction(0.333333))
