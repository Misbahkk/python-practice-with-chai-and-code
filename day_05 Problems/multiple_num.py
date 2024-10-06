num = int(input("Enter a number for table: "))

for i in range(1,11):
    if i == 5:
        continue
    mul = num*i
    print(f"{num} X {i} = {mul}")
