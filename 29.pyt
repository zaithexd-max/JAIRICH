import random
options = ("rock","paper","scissor")
ComputerAnswer = random.choice(options)
is_playing = True
print("--------Rock paper Scissor --------")
while is_playing:
  PlayerAnswer = input("Enter your move (all lowercase): ")
  print(f"Player = {PlayerAnswer}")
  print(f"Computer = {ComputerAnswer}")

  if(PlayerAnswer == "rock" and ComputerAnswer == "paper"):
    print("You lose")
  elif PlayerAnswer == "rock" and ComputerAnswer == "scissor":
    print("You Win")
  elif PlayerAnswer == ComputerAnswer:
    print("You tie")
  elif PlayerAnswer == "scissor" and ComputerAnswer == "rock":
    print("You lose")
  elif PlayerAnswer == "scissor" and ComputerAnswer == "paper":
    print("You Win")
  elif PlayerAnswer == "paper" and ComputerAnswer == "scissor":
    print("You lose")
  elif PlayerAnswer == "paper" and ComputerAnswer == "rock":
    print("You Win")
  else:
    print("Invalid move")

  



  