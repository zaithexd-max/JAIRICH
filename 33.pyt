def display_name(*args):
  for arg in args:
    print(arg,end="")
display_name("Napat","Tararatsatien","The sigma")
print()
def display_info(**kwargs):
  for key in kwargs.keys():
    print(key)
display_info(name = "Jai",age = "18")
def shipping_label(*args,**kwargs):
  for arg in args:
    print(arg,end = " ")
  print()
  print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('apt')}{kwargs.get('Sigma')}{kwargs.get('Coloured')}")
shipping_label("Dr.","Spongebob","Squarepant",
               street="123 Fake st",
               apt="100",
               Sigma="Yes",
               Coloured="Yes")
