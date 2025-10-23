import time 
def timing_decorator(func):

  def wrapper(*args, **kwargs):
    start_time = time.time()  
    result = func(*args, **kwargs)  
    end_time = time.time() 
    duration = end_time - start_time  
    print(f"Function '{func.__name__}' executed in {duration:.3f} seconds")
    return result            
  return wrapper  

@timing_decorator
def some_function(param):
       
  for i in range(1000000): 
            pass
  print(f"Function did something with {param}")
  
some_function("example")
    
