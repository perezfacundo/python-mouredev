#1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, ". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name):
    return "Saludos terricola de nombre {}. Llévanos con tu líder.".format(name)

print(personalized_greeting("Facundo"))
#2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiply(num1, num2):
    return num1 * num2

print(multiply(2, 3))

#3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(num):
    return num % 2 == 0

print(is_even(10))

#4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(st):
    return st.upper()

print(convert_to_uppercase("hola que tal"))

#5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
# *args funciona como tupla
def arbitrary_sum(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(arbitrary_sum(1, 2, 3, 4, 5))
print(arbitrary_sum(10, 20, 30, 40, 50, 60))

#6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola,  ". Los argumentos deben ser pasados por clave.
# **kwargs funciona como diccionario (pares clave valor)
def generate_full_greeting(nombre, apellido):
    return "Buenas tardes sr {}, {}.".format(apellido, nombre)

print(generate_full_greeting(nombre="Victorino", apellido="Garcia"))

#7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponente):
    return base ** exponente

print(power(3,2))

#8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
#Correcion, Escribire una funcion que reciba una cantidad x de numeros 
def calculate_average(*args):
    res = 0
    for num in args:
        res += num
    return round(res / len(args), 2)

print(calculate_average(10, 10, 6))

#9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(chain):
    return len(chain)

print(count_characters("Alice in chains"))

#10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*args):
    for each in args:
        print(each.upper())

display_messages("w.a.s.p.", "metallica", "linkin park", "kiss", "queen", "hermetica", "rata blanca")