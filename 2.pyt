Temp = int(input("Enter Temperature: "));
Rain = input("Is it Rainning? Y/N: ");
print("Sigma")
if Rain == "Y":
  isRaining = True
elif Rain == "N":
  isRaining = False
if Temp > 34 or Temp < 0 or isRaining:
  print("The outdoor event is cancelled");
else:
  print("The outdoor event is still scheduled");
