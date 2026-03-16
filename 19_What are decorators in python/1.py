import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) 
        end = time.time()
        print(f"{func.__name__} ran in time: {end-start}")
        # return result
    return wrapper

@timer # jab bhi call ho ga timer se ho kar hi guzray ga
def example_func(n):
    time.sleep(n)

example_func(4)

# can do this but no need to do this use decorator
# wrapper = timer(example_func) 
# wrapper(3)