rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter symbol: ")
for x in range(rows):
  for y in range(columns):
    print(symbol,end = "")
  print()