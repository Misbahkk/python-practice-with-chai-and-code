password = input("Enter your Password: ")

len_pass = len(password)

if len_pass <6:
    print("Your Paasoword is WEEK")

elif len_pass<10:
    print("Your Password is MEDIUM")
else:
    print("Your password is STRONG")
