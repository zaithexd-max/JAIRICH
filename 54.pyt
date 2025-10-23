class Student:
  count = 0
  TotalGpa = 0
  def __init__(self,name,gpa):
    self.name = name
    self.gpa = gpa
    Student.count += 1
    Student.TotalGpa += gpa

  def get_info(self):
    return f"{self.name} = {self.gpa}"
  @classmethod #Related to class attribute/data
  def get_count(cls):
    return f"Total number of students: {cls.count}"
  @classmethod
  def get_average_gpa(cls):
    return f"{cls.TotalGpa/cls.count}"
student1 = Student("Jai",3.5)
student2 = Student("Porpiang",3.2)
student3 = Student("Sigma",4.0)
print(Student.get_count())
print(Student.get_average_gpa())