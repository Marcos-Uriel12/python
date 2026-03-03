#1 
def personalized_greeting(nombre = "Desconocido"):
    print("Hola",nombre)
    
personalized_greeting()

#2
def multiply(num_1, num_2):
    mul = num_1 * num_2
    return mul

print(multiply(5,2))

#3
def is_even(num):
    if (num % 2) ==0:
        return True
    else:
        return False

print(is_even(5))

#4
def convert_to_uppercase(text):
    return text.upper()
print(convert_to_uppercase("hola como estsas"))

#5
def arbitrary_sum(*numbers):
    return sum(numbers)
print(arbitrary_sum(5,5,5))

#6
def generate_full_greeting(name,surname):
    return(f"Hola {name} {surname}")
print(generate_full_greeting(name="Marcos", surname="Machuca"))

#7
def power(base,exp):
    return base ** exp
print(power(5,2))

#8
def calculate_average(n1,n2,n3):
    cal=(n1+n2+n3) /3
    return cal
print(calculate_average(7,7,7))

#9
def count_characters(texto):
    return len(texto)
count_characters("Hola me llamo marcos")

#10
def display_messages(*textos):
    for message in textos:
        print(message.upper())
display_messages("hola","mamam")