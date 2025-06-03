def sum_num(*args):
    print(*args)
    print(args)
    return sum(args)


# print(sum_num(1,2,3))
# print(sum_num(1,2,3,4,5))


def pair_kwargs(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} : {value}')
    print(kwargs)

# print(pair_kwargs(name="misbah",surnamw="yousaf")) 
# print(pair_kwargs(name="misbah",surnamw="yousaf",department= "CS")) 
# print(pair_kwargs(name="misbah",surnamw="yousaf",roll = "2k21/cse/56")) 


# -------------------------------------------------------------------------------
# Yeild

def even(limit):
    for i in range(2,limit+1,2):
        # return i  #// This return only 1 valuee and terminate the loop so that's why we use yield
        yield i # this stire the value in memory and also adress and geenrate the number
    
print(even(10))
for i in even(10):
    print(i)


