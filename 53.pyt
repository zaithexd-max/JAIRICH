class Employee:
  def __init__(self,name,position):
    self.name = name
    self.position = position
  def get_info(self):
    return f"Name: {self.name}\nPosition: {self.position}"
  
  @staticmethod
  def is_valid_position(position):
    valid_positions = ["Manager","Cashier","Cook"]
    return position in valid_positions
employee1 = Employee("Nigger","Manager")
employee2 = Employee("Nigga","Cook")
print(Employee.is_valid_position("Cook"))
print(f"{employee1.get_info()}")