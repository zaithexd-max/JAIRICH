def message_decorator(func):
  def wrapper():
    print("Decorator is active")
    func()
  return wrapper
@message_decorator
def simple():
  print("Hello world")
simple()