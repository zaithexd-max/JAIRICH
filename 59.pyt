import os
file_path = "C:/Users/User/Desktop/test"
if os.path.exists(file_path):
  print(f"{file_path} exist")
  if os.path.isfile(file_path ):
    print("That is a file")
  elif os.path.isdir(file_path):
    print("That is a directory")
else:
  print("That location doesnt exist")