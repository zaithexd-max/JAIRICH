class BankAccount:
  balance = 0
  def __init__(self,balance):
    self._balance = balance
  @property
  def balance(self):
    return self._balance   
  @balance.setter 
  def balance(self, value):
    if value > 0:
      self._balance = value
    else:
      print("Invalid input")
  def deposit(self, amount):
       self._balance += amount
  def withdraw(self, amount):
    if amount > self._balance:
      print("Invalid input")
    else:
      self.balance -= amount
  @property
  def status(self):
    return f"{self._balance:.2f}$"   
account = BankAccount(100)
print(f"Initial balance: {account.balance}")
account.deposit(50)
print(f"After deposit: {account.balance}")
account.withdraw(100)  # This should raise an error if balance is only 150
print(f"Status: {account.status}")
    