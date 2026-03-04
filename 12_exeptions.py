#1
num1 = 10
num2 = 2
try:
    print(num1 / num2)
except:
    print("no se puede dividir por ese numero")

#2
text = 'Hola como estas?'
try:
    print(int(text))
except Exception as error:
    print(error)

#3
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")

#4

def operaciones(num1,num2):
    try:
        print(f"suma = {num1 + num2}")
        print(f"resta = {num1  - num2}")
        print(f"multiplicacion = {num1 * num2}")
        print(f"division = {num1 / num2}")
    except Exception as error:
        print("No se puede dividir por 0")
    else:
        print('La ejeucion continua')
    finally:
        print('La ejecucion finaliza')
    
operaciones(10,0)

#5
def ask_age():
    try:
        age = (input("Introduce tu edad: "))
        if age <= 0:
            raise ValueError("La edad debe ser un entero positivo.")
        return age
    except ValueError as e:
        print(f"Error: {e}")


#6
def list(list):
    try:
        num = int(input("Que indice de la lista quieres acceder: "))
        print(list[num])
    except:
        print("Error numero de la lista no encontrado")
lista = [1,2,3,4,5,6,7]
#list(lista)

#7
def cap_error(num, num1):
    try:
        if num >= 0 and num1 >= 0:
            return print((f"division = {num / num1}"))
        else:
            raise ValueError("Ambos valores deben ser números positivos.")
    except ZeroDivisionError as error:
        print("Error: No se puede dividir por cero.")
    except TypeError as error:
        print("Error: Ambos valores deben ser números.")

#8
class InsufficientFundsError(Exception):
    pass


def simulate_transaction(balance, withdrawal_amount):
    try:
        if withdrawal_amount > balance:
            raise InsufficientFundsError(
                "Saldo insuficiente para la transacciÃ³n.")
        balance -= withdrawal_amount
        print(f"TransacciÃ³n realizada correctamente. Nuevo saldo: {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        

#9
def list_Cade(list):
    try:
        print(int(list))
    except Exception as error:
        print("Error: No se puede convertir a entero.")
        
new_list= ['a', 'b', 'c']
list_Cade(new_list)

#10
def raiz(num):
    try:
        if num < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
             print(num ** 0.5)
    except:
        pass
