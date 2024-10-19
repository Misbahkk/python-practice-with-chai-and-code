x=99

# def num():
    
#     x=12
#     return x

# now check it with golabal keyword
def num():
    global x
    x=12
    return x



# print(x)
# print(num())
# print(x) #its value come after add golabal 12...



def check(num):
    def actull(n):
        return n ** num
    return actull


f = check(2)
g = check(3)
# when we call it only like this so its return object of  fuction in inner fucntionn
print(f) #<function check.<locals>.actull at 0x0000017B01E00FE0>
print(g) #<function check.<locals>.actull at 0x0000017B01E01080>

print(f(3))
print(g(3))