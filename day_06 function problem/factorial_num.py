num= 5
# for i in range(1,5):
#     num=num*i
#     print(num)


def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num* factorial(num-1)
    

print(factorial(num))