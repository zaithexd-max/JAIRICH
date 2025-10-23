#Mode:
# w = writing a new file / overwrite a file
# x = Error if replicate more than two file
# a = to append the file
txt_data = "I Like pizza"
file_path = "C:/Users/User/Desktop/output.txt"
try:
  with open(file = file_path, mode ="w") as file:
      file.write(txt_data)
      print(f"txt file {file_path} was created")
except FileExistsError:
  print("It already existed you fucking nigger")