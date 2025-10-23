grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "F"}
def Showallgrade():
  for(x,y) in grades.items():
    print(f"{x}: {y}")

def AddaStudent():
  newStudent = input("Enter Student name: ")
  newStudentGrade = input("Enter Student grade: ")
  grades[newStudent] = newStudentGrade
  print(f"{newStudent} has been added with grade {newStudentGrade}")
def RemoveaStudent():
    print("Students:")
    for x in grades.keys():
        print(x)
    
    Remove = input("Choose one to remove: ")
    
    if Remove in grades:
        del grades[Remove]  # removes the student
        print(f"{Remove} has been removed.")
    else:
        print(f"{Remove} not found in the list.")

def LookupaStudent():
  Lookup = input("Pick someone to lookup: ")
  if Lookup in grades:
     print(f"{Lookup}'s grade is {grades[Lookup]}")
  else:
     print(f"{Lookup}'s is not found within the list")
islooking = True
def main():
  while islooking:
    print("Welcome to grade manager")
    print("1.Show all Grade")
    print("2.Add a Student")
    print("3.Remove a Student")
    print("4.Lookup Student")
    print("5.Exit")
    options = input("Choose an Option(1-5): ")
    if options == '1':
      Showallgrade()
    elif options == '2':
      AddaStudent()
    elif options == '3':
      RemoveaStudent()
    elif options == '4':
       LookupaStudent()
    elif options == '5':
       break
      
if __name__ == '__main__':
  main()