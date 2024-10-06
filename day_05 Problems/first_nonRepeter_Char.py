string = input("Enter a string: ")

# teeter
word=''

for char in range(len(string)): # t e e t e r
    is_unique = True
    for check in range(len(string)):  #e
            #r              e
        if char!=check and string[char] == string[check]:
            is_unique=False
            break

        
    if is_unique:
       print(string[char])
       break



            

# short trick

for char in range(len(string)):
    if string.count(string[char]) == 1:
        print(string[char])
        break