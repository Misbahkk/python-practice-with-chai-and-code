# num=5
# fact=1
# while num>=1:    
#     fact = fact*num

#     num-=1
# print(fact)


# while True:
#     num = int(input("Enter a Number: "))
#     if num >0 and num <11:
#         break

# print("You enter a number between 1 to 10")



# ----------------------------------------------
# check is  prime

num = int(input("enter a number: "))

is_prime = True

if num >1:
    for i in range(2,num):
        if(num%2) == 0:
            is_prime=False
            break

print(is_prime)