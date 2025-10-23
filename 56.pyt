class Rectangle:
  def __init__(self,width,height):
    self._width = width
    self._height = height
  @property
  def width(self):
    return f"{self._width:.1f}cm"
  @property
  def height(self):
    return f"{self._height:.1f}cm"
  @width.setter
  def width(self,new_width):
    if new_width > 0:
      self._width = new_width
    else:
      print("Width must be greater than 0")
  @height.setter
  def height(self,new_height):
    if new_height > 0:
      self._width = new_height
    else:
      print("Width must be greater than 0")
  @width.deleter
  def width(self):
    del self._width
    print("Width has been deleted")
  @height.deleter
  def height(self):
    del self._height
    print("height has been deleted")  
rectangle = Rectangle(3,4)
rectangle.width = 5
del rectangle.width
del rectangle.height
print(rectangle.width)
print(rectangle.height)