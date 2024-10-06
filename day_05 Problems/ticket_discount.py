# while True:

#     age = int(input("Enter your age: "))
#     day = input("Enter a day: ")

#     if age <18:
#         if day == 'wednesday':
#             print("The price of Ticket is $8 but In $2 discount you get $6 ")
#         else:
#             print("Your ticket Price is $8")

#     else:
#         if day == 'wednesday':
#             print("Your ticket Price is $12 but In $2 discount Ticket Price is: $10 ")
#         else:
#             print("Your ticket Price is $12")

#     if day == 'exit':
#         break


while True:
    age = int(input("Enter your age: "))
    day = input("Enter a day: ")

    price = 12 if age>18 else 8

    price = price-2 if day== 'wednesday' else price
    print(f"Your ticket price is ${price}")

    if age == 0:
        break

