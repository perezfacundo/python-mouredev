# 1. Crea una lista con los números del 1 al 5 e imprímela.
print("# 1. Crea una lista con los números del 1 al 5 e imprímela.")
numeros = list(range(1, 6))
print(numeros)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
print("\n# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].")
decenas = list(range(10, 50, 10))
print(decenas[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
print("\n# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.")
numeros.append(6)
print(numeros)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
print("\n# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].")
decenas.insert(1, 15)
print(decenas)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
print("\n# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].")
decenas.remove(30)
print(decenas)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5].
# Almacénalo en una variable. Imprime la variable y la lista.
print("\n# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5].")
print(numeros)
numeros.pop()
print(str(numeros) + " _ <-")

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
print("\n# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.")
centenas = list(range(100, 600, 100))
print(centenas)
centenas = centenas[::-1]
print(centenas)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
print("\n# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.")
numeros = [3, 1, 4, 2, 5]
numeros.sort()
print(numeros)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6].
# Almacena el resultado en una nueva lista. Imprime la lista resultante.
print("# 9. Concatena las listas [1, 2, 3] y [4, 5, 6].")
primeros = list(range(1, 4, 1))
ultimos = list(range(4, 7, 1))
todo = primeros + ultimos
print(todo)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50].
# Que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
print("# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50].")
decenas = list(range(10, 60, 10))
sub_decenas = decenas[0:2]
print(sub_decenas)

# 11.
my_list = [1, 2, 3, 4]
print(my_list[1:4])