menu = {"Pizza": 3.00,
        "Popcorn":4.00,
        "Candy":2.00,
        "Nigger":1.00}
cart = []
total = 0
print("----Menu----")
for key,value in menu.items():
  print(f"{key:10}:${value:.2f}")
print("------------")
while True:
  food = input("Select and Item QtoQuit: ")
  if food == "q":
    break
  elif menu.get(food) is not None:
    cart.append(food)
for food in cart:
  total += menu.get(food) 
  print(food)
print()
print(f"Total is: {total:.2f}")
