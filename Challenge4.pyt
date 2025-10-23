from abc import ABC ,abstractmethod
class Animal(ABC):
  @abstractmethod
  def speak(self):
    pass
  @abstractmethod
  def move(self):
    pass
class Dog(Animal):
  def speak(self):
    print("Woof!")
  def move(self):
    print("Runs on 4 legs")
class Cat(Animal):
  def speak(self):
    print("Meow!")
  def move(self):
    print("Walks gracefully")
class Bird(Animal):
  def speak(self):
    print("Chirp!")
  def move(self):
    print("Flies in the sky")
animals = [Dog(),Cat(),Bird()]
for animal in animals:
  animal.speak()
  animal.move()