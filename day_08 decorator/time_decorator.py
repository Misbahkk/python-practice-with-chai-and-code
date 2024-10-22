import time



# alwyas create a decorator funtion in function
def timer(func):
    def wraper(*args,**kwargs):
        start = time.time()
        print(f"The satrt time is: {start}")
        result =func(*args,**kwargs)
        end = time.time()
        print(f"The end time is: {end}")
        print(f"{func.__name__} execute time is {end-start}")
        return result
    
    return wraper


# now we create a decorator of timer fucntion
@timer
def example_funtion(n):
    time.sleep(n)


example_funtion(3)