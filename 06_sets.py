# 1. Crea un set con los números del 1 al 5 e imprímelo.
print("\n1- Crea un set con los números del 1 al 5 e imprímelo.")
nums_set = set(range(1, 6, 1)) # {1, 2, 3, 4, 5}
print(nums_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
print("\n2- Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.")
nums_set.add(6)
print(nums_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
print("\n3- Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?")
nums_set.add(5) # No muestra error, pero tampoco se añade.
print(nums_set)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print("\n4- Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.")
print(3 in nums_set)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
print("\n5- Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.")
nums_set.remove(4)
print(nums_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
print("\n6- Usa el método clear() para vaciar un set y luego imprime su longitud.")
nums_set.clear()
print(len(nums_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
print('\n7- Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.')
fruits_set = set()
fruits_set = {"manzana", "naranja", "platano"}
fruits_list = list(fruits_set)
print(fruits_list)

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
print("\n8- Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.")
first_set = set(range(1, 4))
sec_set = set(range(4, 7))
third_set = first_set.union(sec_set)
print(third_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
print("\n9- Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.")
first_set = set(range(1, 5))
sec_set = set(range(3, 7))
diff_set = first_set.difference(sec_set).union(sec_set.difference(first_set)) # 1 y 2, 5 y 6
print(diff_set)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
print("\n10- Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.")
my_set = set()
del my_set
try:
    print(my_set)
except:
    print("NameError: name 'my_set' is not defined")