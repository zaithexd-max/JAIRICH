import csv
file_path = "C:/Users/User/Desktop/input.csv"
try:
  with open(file_path,"r") as file:
    content = csv.reader(file)
    for line in content:
      if line:
       print(line[0])
except FileNotFoundError:
  print("File not found")
except PermissionError:
  print("You dont have permission to read that file")
except Exception as e:
    print("An error occurred:", e)