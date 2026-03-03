#1
class Animal:
    def __init__(self,species):
        self.especies = species
    def make_sound(self):
        print("Sonido del animal generico")

my_animal = Animal("leon")
my_animal.make_sound()

#2
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        if self.species == "dog":
            print("Guau")
        elif self.species == "cat":
            print("Miau")
        else:
            print("Sonido animal genÃ©rico")

my_animal = Animal("dog")
my_animal.make_sound()

#3/4
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self._speed = 0
        
    def acecelerate(self):
        self._speed += 10
        
    def brake(self):
        if self._speed == 0:
            self._speed = 0
        else:
            self._speed - self._speed
        
    def get_speed(self):
        return(self._speed)
        
my_car = car("Bmw","240i")
my_car.acecelerate
print(my_car.brand, my_car.model, my_car._speed)

#5
class book:
    def __init__(self,title,author):
        self.title = title
        self._author = author
    def get_author(self):
        return self._author
    def title2(self,text):
        title_orther = text
        self.title = title_orther

my_libro = book("Casa","Jorge")
print(my_libro.get_author(), my_libro.title)
my_libro.title2("Luna")
print(my_libro.get_author(), my_libro.title)

my_list_estudents = (7,10,9)

#6
class estudiante:
    def __init__(self,nombre,apellido,notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas
    def nota_total(self):
        return sum(self.notas) / len(self.notas)

alumno = estudiante("carlos","perez",my_list_estudents)
print(alumno.nota_total())

#7
class BankAccoun:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def depositar(self,depositar):
        self.balance += depositar
    def retirar(self,retirar):
        if retirar <= self.balance:
            self.balance -= retirar
        else:
            print("Saldo insuficiente")
        
my_bank = BankAccoun("Marcos",100)
my_bank.retirar(10)
print(my_bank.balance)

#8
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5 
    
#9
class Employee:
    def __init__(self,name,hourly_wage,hourly_worked):
        self.name=name
        self.hourly_wage = hourly_wage
        self.hourly_worked = hourly_worked
    def pago_total(self):
        """horas_sema =self.hourly_worked / 4
        horas_dia = horas_sema / 5
        pago_dia = horas_dia * self.hourly_wage
        pago_sema = pago_dia * 5
        pago_total = pago_sema * 4
        return pago_total"""
        return self.hourly_wage * self.hourly_worked

empleado = Employee("Marcos",20,120)
print(empleado.pago_total())

#10
class Store:
    def __init__(self):
        self.inventory = []
    def agregate(self,producto):
        self.inventory.append(producto)
    def mostrar_productos(self):
        for producto in self.inventory:
            print(producto)

my_store  = Store()
my_store.agregate("teclado")
my_store.mostrar_productos()