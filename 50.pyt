class Shape:
  def __init__(self,color,filled):
    self.color = color
    self.filled = filled
  def describe(self):
    print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")
class Circle(Shape):
  def __init__(self,color,filled,radius):
    super().__init__(color,filled)
    self.radius = radius
class Square(Shape):
  def __init__(self,color,filled,width):
    super().__init__(color,filled)
    self.width = width
class Triangle(Shape):
  def __init__(self,color,filled,width,height):
    super().__init__(color,filled)
    self.width = width
    self.height = height
  def describe(self):
    super().describe()
    print(f"It is a triangle with an area of {self.width*self.height/2}cm^2")
circle = Circle("Red",True,5)
triangle = Triangle("Red",True,5,7)
print(circle.color)
print(circle.filled)
triangle.describe()