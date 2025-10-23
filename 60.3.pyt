import csv
unemployed = [["Name","Age","Job"],
              ["Colored",10,"CsMajor"],
              ["Mr.Griddy",50,"Blow"],
              ["NeckHurt",40,"Hand"]]
file_path = "C:/Users/User/Desktop/output.csv"
try:
  with open(file = file_path, mode ="w") as file:
      writer = csv.writer(file)
      for x in unemployed:
        writer.writerow(x)
      print(f"csv file {file_path} was created")
except FileExistsError:
  print("It already existed you fucking nigger")