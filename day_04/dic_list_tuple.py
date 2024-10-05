# dictionary

# student_roll = {'Misbah':'56/CSE/2k24','Maadeha':'52/CSE/2k24','Laiba':'50/CSE/2k24'}

# for key, vaalue in student_roll.items():
#     print(f"Student Name: {key}, Roll Number: {vaalue}")


# nested dic 
# student_detail = {
#     'chai_dic': {'lemon' : 'khati' , 'gengared' : 'karvi'},
#     'chai_dic1': {'lemon' : 'khati' , 'geng':'tea'},
# }

# print(student_detail['chai_dic']['lemon'])



squre_num = {x:x**2 for x in range(6)}
print(squre_num)

key =["Misbah","Maaadeha","Laiba"]
values = "Student"
create_dic = dict.fromkeys(key,key)
print(create_dic)