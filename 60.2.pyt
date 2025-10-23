import json
unemployee = {
  "name":"Porpiang",
  "age": 15,
  "job": "Eat"
}
file_path = "C:/Users/User/Desktop/output.json"
try:
  with open(file = file_path, mode ="w") as file:
      json.dump(unemployee,file,indent= 4)
      print(f"Json file {file_path} was created")
except FileExistsError:
  print("It already existed you fucking nigger")