# x=4
# y=x
# print(x,y)

# chai_dic = { 'lemon' : 'khati' , 'gengared' : 'karvi'}
# print(chai_dic['lemon']) 
# print(chai_dic.pop('lemon')) 
# print(chai_dic.popitem())
# print(chai_dic)



# # shallow copy
# import copy  
# list1 = [[1, 2, 3], [4, 5, 6]]  
# list2 = copy.copy(list1)  # Shallow copy  

# # list2[0][0] = 100  # Changing nested list element  
# list1[0][0] = 50  # Changing nested list element  
# print("Shallow copy " ,list1)  # Output: [[100, 2, 3], [4, 5, 6]]  
# print('Shallow copy  ',list2)  # Output: [[100, 2, 3], [4, 5, 6]]  


# # list3 = [[1, 2, 3], [4, 5, 6]]  
# list3 = [1, 2, 3]  
# list4 = copy.deepcopy(list3)  # Deep copy  

# # list3[0][0] = 100  # Changing nested list element  
# list4[0] = 100  # Changing nested list element  
# print("Deep copy  ",list3)  # Output: [[1, 2, 3], [4, 5, 6]]  
# print("Deep copy  ",list4)  # Output: [[100, 2, 3], [4, 5, 6]]  

# x= "hello".upper()
# print(x)

# def example(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# example(1, 2, 3, name="Alice", age=25)



# def decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper

# @decorator
# def greet():
#     print("Hello!")

# greet()


# lst = [1,2,3,4]
lst="misbah"
word = ""
for i in range(len(lst)-1,-1,-1):
    word += lst[i]
print(word)

dic = {x:x for x in range(10) if x%2 ==0}
print(dic)  # Output: {0: 0, 1: 1,