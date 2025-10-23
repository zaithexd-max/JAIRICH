class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def makesound(self):
    print("Some generic animal sound")
  def info(self):
    print("Name,Species:",end= "")
    print(f"{self.name} {self.species}")
class Dog(Animal):
  def makesound(self):
    print("Woof")
  def fetch(self):
    print("Fetching the ball")
class Cat(Animal):
  def makesound(self):
    print("Meow")
  def scratch(self):
    print("Scratching the post")
dog = Dog("Lucky","Shiba")
cat = Cat("Jenny","Sigma")
dog.info()
cat.makesound()



