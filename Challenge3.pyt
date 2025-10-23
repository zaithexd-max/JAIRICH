class Vehicle:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def info(self):
    print(f"Brand: {self.brand},Model: {self.model}")
class Car(Vehicle):
  def __init__(self,brand,model,year):
    self.year = year
    super().__init__(brand,model)
  def info(self):
    super().info()
    print(f"Year: {self.year}")
car = Car("Mini cooper","Sigma",2025)
car.info()

    