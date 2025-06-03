def value_count(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{k}:{v}' for k,v in kwargs.items())
        print(f"Function Nmae is: {func.__name__} and args : {args_value}\n kwargs {kwargs_value}")
        return result
    return wrapper


@value_count
def exmple(a,b,c,d=6):
    print(a+b+c+d)


exmple(1,2,c=3,d=5)