# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
from modules_to_13.calculator import sumar, restar, multiplicar, dividir
print(sumar(13, 45, 76))
print(restar(14, 234, 23))
print(dividir(1, 5))
print(dividir(8, 0))
print(multiplicar(10, 7))

# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
from modules_to_13.converter import convert_celsius_fahrenheit, convert_fahrenheit_celsius

print(convert_celsius_fahrenheit(20))
print(convert_fahrenheit_celsius(68))

# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
from modules_to_13.students import printStudents
printStudents()

# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
from modules_to_13.geometry import calcCircleArea, calcSquareArea
print(round(calcCircleArea(5), 2))
print(round(calcSquareArea(4), 2))

# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
print(sumar(10, 45, 3, 98, 10))
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".
from modules_to_13.Car import Car
c1 = Car("Ferrari", "430 Spider", 2005)
print(c1)
c2 = Car("Hyundai", "Tiburon", 2003)
print(c2)

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
# from modules_to_13.manageFiles import readlines, writelines
# readlines("archivo.txt", enum = True)
# writelines("archivo.txt", input("Ingresa por favor la linea a escribir en el archivo: "), last=True)

# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
from modules_to_13.statistics import calculateMedia, calculateMediana
print("Media: " + str(calculateMedia(12, 7, -3, 14, 7, 22, 0, 9, 15, 3)))
print("Mediana: " + str(calculateMediana(12, 7, -3, 14, 7, 22, 0, 9, 15, 3)))

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.
from modules_to_13.manageFiles import findWordInFile
print(findWordInFile("archivo2.txt", "software"))   # 6
print(findWordInFile("archivo2.txt", "prueba"))     # 5
print(findWordInFile("archivo2.txt", "una"))        # 5

# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
from modules_to_13.date import today, daysTo
print(today())
print(daysTo("30/09/2026"))