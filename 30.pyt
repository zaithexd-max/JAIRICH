def display_invoice(username,amount,due_date):
  print(f"Hello {username}")
  print(f"Your bill of ${amount:.2f} is due: {due_date}")
username = input("Enter your username: ")
amount = int(input("Enter amount: "))
due_date = input("Enter due_date: ")
display_invoice(username,amount,due_date)
