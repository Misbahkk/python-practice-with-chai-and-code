nums = [1,2,-3,4,-4,5,-6,7-8,-9]

positive_num = []
negative_num = []
for num in nums:
    if num< 0:
        negative_num.append(num)
    else:
        positive_num.append(num)


print(f"This is a Positive Nums: \n{positive_num}\n and length is {len(positive_num)}") 
print(f"This is a Negative Nums: \n{negative_num} and length is {len(negative_num)}") 