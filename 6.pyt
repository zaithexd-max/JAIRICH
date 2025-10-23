import random
import math
price1 = 3.14545
price2 = 4.5444
price3 = 4.4545
print(f"price1: {price1:.2f}")
age = int(input("Enter your age: "))
while age < 0:
    print("You can't have negative age.")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")
food = input("Enter the food you like (press q to leave): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter the food you like (press q to leave): ")
Num = int(input("Enter num between 1-10: "))
while Num < 1 or Num > 10:
    print(f"{Num} is not valid")
    Num = int(input("Enter num between 1-10: "))
random = random.randint(0,100)
if random < 50:
    print(f"Your number is {Num}")
elif random < 20:
    print(f"Nigga")
else:
    print(f"Sigma your number is {Num}")
 



