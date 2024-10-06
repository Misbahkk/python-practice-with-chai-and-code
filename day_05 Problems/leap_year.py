while True:

    year = int(input('Enter your year: '))

    if (year%4==0 and year%100!=0) or (year%400 ==0):
        print('This year is a leap year')
    else:
        print("This is not a leapyear ")
    
    if year==0:
        break