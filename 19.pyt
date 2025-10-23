import time;
my_Time = int(input("Enter the time in second:"))
for x in reversed(range(0,my_Time+1)):
  seconds = x%60
  minutes = int(x/60)%60
  hours = int(x/3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
print("TIME UP")