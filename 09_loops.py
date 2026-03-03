#1
num = 0 
while num < 11:
    print(num)
    num +=1
    
#2
new_list = [10,20,30,40,50]
for elemnt in new_list:
    print(elemnt)
    
#3
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
    print(sum)
    
#4
word = 'python'
for letter in word:
    print(letter)
    
#5
num_1 = 0
while num_1 < 51:
    num_1 += 1
    if (num_1 % 7) == 0:
        print("este numero es divisible por 7 ", num_1)
        break
    
    print(num_1)

#6
dic = {"name": "Brais", "age": 37, "country": "Galicia"}
for elements in dic:
    print(dic.keys())
    

#7
num_par = 0 
while num_par < 21:
    num_par +=1
    if (num_par % 2)==0:
        print(num_par)
        
#8
new_list = [30,10,30,20,30,40]
for elements in  new_list:
    print(new_list.count(30))
    

#9
for numeros in range(10,0,-1):
    print(numeros)
    
#10
new_list = ("Marcos","Julian","Brais","kadk","dsada")
for i in new_list:
    print(i)
    if i == "Brais":
        break