import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print("--------Welcome--------")
print(f"Select a number between {lowest_num} to {highest_num}")
while is_running:
  guess = input("Enter your guess: ")
  if guess.isdigit():
    guess = int(guess)
    guesses += 1
    if guess > highest_num or guess < lowest_num:
      print("Invalid guess")
      print(f"Select a number between {lowest_num} to {highest_num}")
    elif guess < answer:
      print("Too Low")
    elif guess > answer:
      print("Too high")
    elif guess == answer:
      print("Correct")
      is_running = False
      if guesses < 5:
       print(f"You have guessed {guesses} Time Very pro")
      elif guesses >= 5:
        print(f"You have guessed {guesses} Time Omg so trash")
  else:
    print("Invalid guess")
    print(f"Select a number between {lowest_num} to {highest_num}")