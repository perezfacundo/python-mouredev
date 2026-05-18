# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
print("\n# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.")
decenas = tuple(range(10, 60, 10))
print(decenas)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
print("\n# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.")
centenas = tuple(range(100, 600, 100))
print(centenas[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
print("\n# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.")
nums = tuple(range(1, 4, 1))
try:
    nums[0] = 1 # Método "__setitem__" no definido en el tipo "tuple[int, ...]"
except:
    print("Una tupla no puede modificarse")

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
print("\n# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).")
reps_nums = tuple() # Se espera 1 argumento posicional
reps_nums = (1, 2, 3, 3, 4, 5, 3)
print(f"Cuantas veces aparece el n 3 en la tupla {reps_nums} ? Respuesta: {reps_nums.count(3)}")

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
print("\n# 5. Encuentra el índice de la primera aparición de la cadena 'Python' en la tupla ('Java', 'Python', 'JavaScript', 'Python').")
languages = tuple()
languages = ('Java', 'Python', 'JavaScript', 'Python')
print(languages.index("Python")) # 1

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
print("\n# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.")
first_tup = tuple(range(1, 4, 1))
second_tup = tuple(range(4, 7, 1))
third_tuple = first_tup + second_tup
print(third_tuple)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
print("\n# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).")
sub_decenas = tuple()
sub_decenas = decenas[1:3]
print(sub_decenas)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
print("\n# 8. Convierte la tupla ('rojo', 'verde', 'azul') en una lista, cambia el segundo elemento a 'amarillo' y vuelve a convertirla en una tupla. Imprime la tupla resultante.")
colors_tup = tuple()
colors_tup = ('rojo', 'verde', 'azul')
colors_list = list(colors_tup)
print(colors_list)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
print("\n# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.")
my_tuple = tuple()
del my_tuple
try:
    print(my_tuple)
except:
    print('"my_tuple" está sin consolidar')

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
print("\n# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.")
last_tuple = (100,)
print(last_tuple[2])