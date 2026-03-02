#1
new_set = {1,2,3,4,5}
print(new_set)

#2
new_set.add(6)
print(new_set)

#3
new_set.add(5)
print(new_set)

#4
print(3 in new_set)

#5
new_set.remove(4)
print(new_set)

#6
new_set.clear()
print(len(new_set))

#7
new_other_set = {"manzana", "naranja", "platano"}
new_list = list(new_other_set)
print(new_list[0])

#8
print({1,2,3}.union({4,5,6}))

#9
new_set2 = {1,2,3,4}
print(new_set2.difference({3,4,5,6}))

#10
del new_set
print(new_set)