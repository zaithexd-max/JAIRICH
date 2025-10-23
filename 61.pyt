file_path = "C:/Users/User/Desktop/input.txt"
try:
  with open(file_path,"r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
  print("File not found")
except PermissionError:
  print("You dont have permission to read that file")