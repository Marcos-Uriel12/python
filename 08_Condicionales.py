#1 
num = 0
if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")
    
#2
#edad = input("Ingrese su edad: ")
edad = 18
if int(edad) >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
#3
text = ""
if not text:
    print("Cadena vacica")
else:
    print("la cadena tiene texto")

#4
num_1 = 5 #int(input("Primer numero: "))
num_2 = 3 #int(input("Segundo numero: "))    
if num_1 > num_2:
    print("El numero mayor es: ",num_1)
elif num_1 < num_2:
    print("El numero mayo es: ",num_2)
else:
    print("Los numeros son iguales")
    
#5
num = 15
if (num % 3) == 0 and (num % 5) == 0:
    print("numero divisible")
else:
    print("este numero no es divisible")

#6
num_par = 50 #int(input("Ingrese el numero: "))
if (num_par % 2 ) == 0:
    print("Numero par")
else:
    print("Numero impar")

#7
edad_2 = 20
if edad_2 > 18:
    print("Puede votar")
elif edad_2 >15:
    print("puede votar con permiso especial")
else:
    print("no puede votar menor de edad")

#8 
contraseña = "hola123"
contraseña_rev="hola123" #input("Ingrese la contraseña: ")
if contraseña == contraseña_rev:
    print("contraseña exitosa")
else:
    print("contraseña invalida")

#9
numero_1=15
if numero_1 > 10 and numero_1 < 20:
    print("numero entre 10 y 20")
else:
    print("numero por fuera de 10 y 20")
    
#10
sema=input("ingrese el color del semaforo(rojo,verde,amarillo): ")
if sema == "rojo":
    print("parar")
elif sema == "amarillo":
    print("paso de color")
elif sema == "verde":
    print("avanzar")
else:
    print("color erroneo")

    
    
    
    