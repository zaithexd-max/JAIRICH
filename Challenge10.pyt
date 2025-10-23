import time
import threading
def print_num():
  for i in range(0,5):
    print(i,end="")
    time.sleep(1)
def print_letter():
  for c in ["A","B","C","D","E"]:
    print(c)
    time.sleep(1)
Move1 = threading.Thread(target=print_num)
Move1.start()
Move2 = threading.Thread(target=print_letter)
Move2.start()
Move1.join()
Move2.join()
print("Finished")