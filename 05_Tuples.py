#1 
new_tuple = (10,20,30,40,50)
print(new_tuple)

#2
tupple_1 = (100,200,300,400,500)
print(tupple_1[1])

#3
#tupple_2 = (1,2,3)
#tupple_2[1] = 10 

#4
tupple_3 = (1,2,3,3,4,5,3)
print(tupple_3.count(3))

#5 
tupple_4 = ("java","Python","Javascript","Python")
print(tupple_4.index("Python"))

#6
tupple_5 = (1,2,3,4)
tupple_6 = (5,6,7,8)
print(tupple_5 + tupple_6)

#7
subtuple = new_tuple[2:4]
print(subtuple)

#8 
tuple_convert = ("rojo","azul","verde")
list_tuple = list(tuple_convert)
list_tuple[1] = "amarillo"
tuple_convert2 = tuple(list_tuple)
print(tuple_convert2)
print(type(tuple_convert2))

#9
#del new_tuple
#print(new_tuple)

#10 
tuple_7 = (100)
print(tuple_7)