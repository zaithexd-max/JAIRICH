class Animal:
  def __init__(self,name):
    self.name = name
  def eat(self):
    print(f"{self.name} is eatting")
  def sleeping(self):
    print(f"{self.name} is  sleeping")
class Prey(Animal):
  def flee(self):
    print(f"{self.name} is fleeing")
class Predator(Animal):
  def hunt(self):
    print(f"{self.name} is hunting")
class Rabbit(Prey):
  pass
class Hawk(Predator):
  pass
class Fish(Prey,Predator):
  pass
rabbit = Rabbit("Bugs")
hawl = Hawk("Spongebob")
fish = Fish("Sigma")
rabbit.eat()