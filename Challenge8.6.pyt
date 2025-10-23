is_logged_in = True
def login_required(func):
  def wrapper():
    if is_logged_in == True:
      func()
    else:
      print("Access denied,Please log in first")
  return wrapper
@login_required
def view_profile():
    print("Welcome to your profile page!")
view_profile()