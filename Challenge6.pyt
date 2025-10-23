class Counter:
  total_count = 0
  def __init__(self):
    Counter.total_count += 1
  @classmethod
  def get_total_count(cls):
    return Counter.total_count
  @classmethod
  def reset_count(cls):
    Counter.total_count = 0
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
print(Counter.get_total_count())
print(Counter.reset_count())
counter4 = Counter()
counter5 = Counter()
print(Counter.get_total_count())