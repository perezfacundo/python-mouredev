# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
# ✅

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
# ✅
class Animal():
    def __init__(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def make_sound(self):
        if self.get_type == 'cat':
            print("miau")
        elif self.get_type == 'dog':
            print("guau")
        elif self.get_type == 'rat':
            print("pspsps")

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__speed = 0

    def __str__(self) -> str:
        return f"{self.__brand} - {self.__model}"

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book():
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Student():
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__califications = [3, 4, 5, 1]

    def add_calif(self, calif):
        self.__califications.append(calif)

    def get_higher_calif(self):
        res = 0
        for cal in self.__califications:
            if cal > res: res = cal
        return res

st = Student('Hugo', 'Balassone')
print(f"La nota mas alta es {st.get_higher_calif()}.")

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount():
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def deposit(self, quantity):
        self.__balance += quantity

    def retire(self, quantity):
        to_retire = 0
        if quantity >= self.__balance:
            to_retire = self.__balance
            self.__balance = 0
        else:
            self.__balance -= quantity
            to_retire = quantity
        return to_retire

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
class Point():
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_to(self, b2):
        import math
        dx = b2.get_x() - self.__x
        dy = b2.get_y() - self.__y
        return round(math.sqrt(dx ** 2 + dy ** 2), 2)

p1 = Point(10, 20)
p2 = Point(30, 60)
print(p1.distance_to(p2))

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee():
    def __init__(self, name, hourly_wage, hours_worked):
        self.__name = name
        self.__hourly_wage = hourly_wage
        self.__hours_worked = hours_worked

    def calc_liq(self):
        return self.__hourly_wage * self.__hours_worked

emp1 = Employee("Juan Perez", 52, 3500)
print(emp1.calc_liq())
emp2 = Employee("Walter Urquiza", 40, 3500)
print(emp2.calc_liq())

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store():
    def __init__(self, name):
        self.__name = name
        self.__inventory = []
    
    def add_car(self, car):
        self.__inventory.append(car)
    
    def add_list_cars(self, *cars):
        for each in cars:
            self.__inventory.append(each)
    
    def get_inventory(self):
        return self.__inventory

st = Store("Zarate 1550")
car1 = Car("Ferrari", "458 Spider")
car2 = Car("BMW", "320i")
car3 = Car("Nissan", "Silvia")
car4 = Car("Hyundai", "Tiburon")
st.add_list_cars(car1, car2, car3, car4)
lista = st.get_inventory()

for car in lista:
    print(car)
