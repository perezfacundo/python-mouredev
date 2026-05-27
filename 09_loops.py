# 1. Usa un bucle while para imprimir los números del 1 al 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Usa un bucle for para recorrer la lista [10, 20, 30, 40, 50] e imprime cada número.
decenas = [10, 20, 30, 40, 50]
for num in decenas:
    print(num)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
resultado = 1
while resultado <= 100:
    resultado += 1
print(resultado)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
cadena = "Python"
for char in cadena:
    print(char)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
i = 1
while i <= 50:
    if i % 7 == 0:
        break
    i += 1
print(f"El primer numero entre 1 y 50 divisible por 7 es: {i}")

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
person = { "name": "Brais", "age": 37, "country": "Galicia" }
for key in person:
    print(person[key])
print(person.keys())

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for num in range(10, 0, -1):
    print(num)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista [30, 10, 30, 20, 30, 40].
decenas = [30, 10, 30, 20, 30, 40]
veces = 0
for num in decenas:
    if num == 30:
        veces += 1
print(veces)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = ['Victor', 'Hugo', 'Julio', 'Alberto', 'Gabriel', 'Tomas', 'Matias', 'Pablo', 'Brais', 'Cesar']
for each in nombres:
    print(each)
    if each == 'Brais':
        break