import json
file_path = "C:/Users/User/Desktop/input.json"
try:
  with open(file_path,"r") as file:
    content = json.load(file)
    print(content["name"])
except FileNotFoundError:
  print("File not found")
except PermissionError:
  print("You dont have permission to read that file")