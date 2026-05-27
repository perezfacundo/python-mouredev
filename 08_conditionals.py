# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
print("\n1. Escribe un programa que verifique si un número es positivo, negativo o cero.")
num = -1
if num > 0:
    print("Positivo")
else:
    print("Negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad (18 años o más) o menor de edad.
print("\n2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad (18 años o más) o menor de edad.")
edad = int(input("Por favor ingresa tu edad: "))
print("Eres mayor de edad") if edad >= 18 else print("No eres mayor de edad")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
print("\n3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.")
cadena = str(input("Ingresa una cadena de texto y te dire si esta vacia: ")).replace(" ", "")
print("Esta vacia") if cadena is "" else print("No esta vacia")

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
print("\n4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.")
print("Ingresa dos numeros para compararlos")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
if num1 > num2:
    print(f"El {num1} es mayor que el {num2}.")
elif num2 > num1:
    print(f"El {num2} es mayor que el {num1}.")
else:
    print(f"Los numeros {num1} y {num2} son iguales.")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
print("\n5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.")
num = int(input("Ingresa un numero para saber si es divisible por 3 y por 5: "))
res = (num % 3 == 0) and (num % 5 == 0)
if res:
    print("Es divisible")
else:
    print("No es divisible")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
print("\n6. Solicita al usuario que ingrese un número y verifica si es par o impar.")
num = int(input("Ingresa un numero para saber si es par o no: "))
res = num % 2 == 0
if res:
    print("El numero es par")
else:
    print("El numero no es par")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad (mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
print("\n7. Escribe un programa que determine si una persona puede votar en función de su edad (mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.")
edad = 15
if edad >= 18:
    print("La persona tiene edad para votar")
else:
    if edad >= 16:
        print("La persona es menor, pero puede votar con permiso.")
    else:
        print("La persona es menor. No puede votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
print("\n8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.")
user = "fpq"
password = "kjdr42!"
input_password = "23fewf"
if password == input_password:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
print("\n9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).")
number = 10
if number <= 10 and number >= 20:
    print("El numero esta entre 10 y 20, incluidos.")
else:
    print("El numero no esta entre 10 y 20, incluidos.")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color (rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
print("\n10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color (rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.")
color = "rojo"
if color == "rojo":
    print("Debe detenerse")
elif color == "amarillo":
    print("Debe reducir la velocidad")
elif color == "verde":
    print("Puede avanzar")
else:
    print("El color no corresponde a un semaforo.")