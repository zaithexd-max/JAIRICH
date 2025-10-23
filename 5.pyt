Username = input("Enter Username: ");
Check1 = Username.count(" ");
Check2 = len(Username);
Check3 = Username.isdigit();
if Check2 > 12:
  print("Username cannot contain more than 12 Characters")
elif Check1 > 0:
  print("Cannot have space")
elif Check3:
  print("Cannot have number in a username")
else:
  print("Succesful")
