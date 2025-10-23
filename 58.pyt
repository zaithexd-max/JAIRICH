try:
  number = int(input("Enter a number: "))
  print(1/number)
except ZeroDivisionError:
  print("You cant divide by Zero idiot")
except ValueError:
  print("Enter only number please!")
except Exception:
  print("Something went wrong!")
finally:
  print("Do some cleanup here")