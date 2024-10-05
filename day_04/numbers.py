# x="misbah"
# print(repr(x))

# print(str(x))
# print(x)  #print ans str givve the same results


# repr(): Gives a technical, precise representation (used for debugging). 
# It’s often more detailed and shows how you would recreate the object.

# str(): Gives a clean, easy-to-read format (used for displaying to humans). 
# It’s simpler and focuses on readability.

# print(): Simply prints the result to the console. 
# It uses str() internally to convert the object into a readable format.



# import datetime

# # crete a date time object
# new = datetime.datetime.now()

# print(repr(new))
# # give you the detailed , officila represntation (you could use the datetime object)



# # they both give you the simple and human readable version
# print(str(new))

# print(new)


# print(0o22) #this octal number reprasentation
# print(0xff) #this is hexa number reprasentation
# print(0b1000) #this is binary number reprasentation


# print(int('64',8))
# print(int('90',16))
# print(int('10000',2))



#--------------------------------------------------
#--------------------------------------------------
print((0.1+0.1+0.1)-0.3)
# OUTPUT - 5.551115123125783e-17 
# Because python give not this accurate result so we use libraruy for this type of oprations

from decimal import *
x =Decimal(0.1)+Decimal(0.1)+Decimal(0.1)
print(x)