# Ya check kro ka hamre calculation ek dafa ho gai ha to vese agr duabra koi number ay sitution ia to run na ho voi utha ka deda
import time


def chache(func):
    chache_value={}
    print(chache_value)
    def wraper(*args):
        if args in chache_value:
            print("value is already in chache")
            return chache_value[args]
        result = func(*args)
        print("This is not in cache value")
        chache_value[args] = result
        return result
    return wraper



@chache
def long_funtion(a,b,c):
    time.sleep(4)
    return a+b+c


print(long_funtion(2,3,4))
print(long_funtion(2,3,4))
print(long_funtion(2,3,5))