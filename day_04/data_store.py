# l1= [1,2,3]
# l2=l1
# print(l1)
# print(l2)
# l1[0]=44
# print(l1)
# print(l2)



# now change the refrence 
# n1= [2,3,4]
# n2=n1
# print(n1)
# print(n2)
# # beacuse we create a new refrence her 
# n1 = [2,3,4]
# n1[0] =22
# print("after change the data\n",n1)
# print(n2)



# h1=[1,2,3]
# # now we use slicing so this is not create a refrence same object
# # this create a copy of that object
# h2=h1[:]
# h1[0] = 88
# print(h1)
# print(h2)


m1=[1,2,3]
n2= m1
print(m1 == n2)
print(m1 is n2)

m1 = [1,2,3]
print(m1 == n2)
print(m1 is n2) #this output false because we create new referece