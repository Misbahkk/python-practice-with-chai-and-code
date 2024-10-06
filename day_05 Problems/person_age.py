
while True:

    age = int(input("enter your Age: "))

    if age<13:
        print("you are a kid")
    elif 19>=age >=13:
        print("you are a teenager")
    elif 59>= age >= 20:
        print("you are an adult")
    elif age>=60:
        print("you are a senior")
    else:
        print("invalid input")

    if age == 0:
        break