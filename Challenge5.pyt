class Dog:
  def speak(self):
    print("Woof!")
class Cat:
  def speak(self):
    print("Meow!")
class Robot:
  def speak(self):
    print("Beep! Boop!")
def make_it_speak(animal):
  animal.speak()
animals = [Dog(),Cat(),Robot()]
for a in animals:
  make_it_speak(a)