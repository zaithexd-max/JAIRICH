class Student:
  class_year = 2024
  num_students = 0
  def __init__(self,name,age):
    self.name = name
    self.age = age
    Student.num_students += 1
student1 = Student("Spongebob",30)
student2 = Student("Patrick",35)
student2 = Student("Garry",4)
print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has a total of {Student.num_students}")