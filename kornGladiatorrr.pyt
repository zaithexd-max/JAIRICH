food = []
price = []
total = 0
while True:
  food_item = input("Enter a food to buy Q to quit=")
  if food_item.lower() == "q":
    break
  else:
    food.append(food_item)
    price_item = float(input(f"Enter the price of a {food_item}:$"))
    price.append(price_item)