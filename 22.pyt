foods = []
prices = []
total = 0
while True:
  food = input("Enter a food to buy Q to quit=")
  if food == "q":
    break
  else:
    price = float(input(f"Enter the price of a {food}:$"))
    foods.append(food)
    prices.append(price)
print("----Your Cart----")
for food in foods:
  print(f"{food}",end="")
for price in prices:
  total += price
print()
print(f"Your total is ${total}")

