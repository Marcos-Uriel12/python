#1
new_dic = {"name":"Marcos","age":21,"country":"Argentina"}
print(new_dic)

#2
print(new_dic["name"])

#3
new_dic["job"] = "Programador"
print(new_dic)

#4
new_dic["age"] = 38
print(new_dic)

#5
del new_dic["country"]
print(new_dic)

#6
new_other_dic = {1:1,2:2*2,3:3*3,4:4*4,5:5*5}
print(new_other_dic)

#7
print("age" in new_dic)

#8
print(new_dic.keys())

#9
new_list = list(new_dic.keys())
print(new_list)

#10
new_list2 = ["name","age","job"]
new_dic_fro= dict.fromkeys(new_list2)
print(new_dic_fro)