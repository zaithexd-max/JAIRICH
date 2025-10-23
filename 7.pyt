principle = 0
rate = 0
time = 0

while True:
  principle = float(input("Enter principle: "))
  if principle <=0:
    print("Principle cant be less than or equal to 0")
  else:
    break
while True:
  rate = float(input("Enter rate: "))
  if rate <= 0:
    print("Rate cannot be less than or equal to 0")
  else:
    break
while True:
  time = int(input("Enter amount of year: "))
  if time <=0:
    print("Time cannot be less than or equal to 0")
  else:
    break
Total = principle*((1+(rate/100))**time)
print(f"Balance after {time} year is ${Total:.2f}")