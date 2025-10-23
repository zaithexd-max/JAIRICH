def main():
  balance = 0
  def show_balance():
    print(f"You have ${balance}")
  def deposit():
    deposit = float(input("How much do you deposit: "))
    if deposit < 0:
      print("Cant deposit less than 0")
      return 0
    else:
      return deposit
  def withdraw():
    withdraw = float(input("How much do you withdraw: "))
    if withdraw > balance:
      print("You dont have enough money")
      return 0
    elif withdraw < 0:
      print("You cannot enter 0 or less than")
      return 0
    else:
      print(f"You have ${balance}")
      return withdraw
  is_running = True
  while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        show_balance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw()
    elif choice == 4:
        is_running = False
    else:
        print("That's invalid choice")
  print("Thank you have a nice day")

if __name__ == '__main__':
  main()
