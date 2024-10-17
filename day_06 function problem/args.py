def sum_num(*args):
    print(*args)
    print(args)
    return sum(args)


print(sum_num(1,2,3))
print(sum_num(1,2,3,4,5))