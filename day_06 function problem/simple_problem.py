# retrun a squee a number

def squre(num):
    return num**2
    
# print(squre(5))


def sum(num1,num2):
    return num1+num2

num1 = 5
num2=7
# print(sum(num1,num2))


def mul(num1,num2):
    return num1*num2
num2='misbah '
print(mul(num1,num2))


import math
def circle(r):
    area = math.pi*(r**2)
    cercum = 2*math.pi*r
    return area,cercum


r= 7
a,c = circle(r)
print(f"Area of circle is : {a:.2f} \n Circumfarance of circle is {c:.2f}")