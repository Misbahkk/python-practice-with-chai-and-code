string = input("Enter your String for reverseinng: ")

# print(string[::-1])
reverse_string =''
# for char in range(len(string)):
#     reverse_string +=string[-char-1]
#     # print(string[-char-1])
# print(reverse_string)


for char in string:
    reverse_string = char+reverse_string

print(reverse_string)