# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
print("\n1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.")
person = { "name": "Claudio", "age": 27, "country": "Ecuador" }
print(person)

# 2. Accede al valor de la clave name en el diccionario.
print("\n2. Accede al valor de la clave name en el diccionario.")
print(person["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
print("\n3. Añade una nueva clave job con el valor 'Programador' al diccionario del punto anterior. Imprime el diccionario actualizado.")
person["job"] = "Programador"
print(person["job"])

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
print("\n4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.")
person["age"] = 38
print(person)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
print("\n5. Elimina la clave country del diccionario e imprime el diccionario resultante.")
del person["country"]
print(person)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
print("\n6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).")
nums_dict = {}
for i in range(1, 6):
    nums_dict[i] = i
print(nums_dict)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
print("\n7. Verifica si la clave age está presente en el diccionario {'name': 'Brais', 'age': 37, 'country': 'Galicia'}.")
print("age" in person)

# 8. Imprime solo las claves del diccionario.
print("\n8. Imprime solo las claves del diccionario.")
print(person.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print("\n9. Convierte las claves del diccionario en una lista e imprime la lista resultante.")
person_keys = list(person.keys())
print(person_keys)

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
print("\n10. Crea un nuevo diccionario a partir de una lista de claves ['name', 'age', 'job'] usando fromkeys(), asignando a todas las claves el valor 'Desconocido'.")
new_person = person.fromkeys(person, "Desconocido")
print(new_person)

# Cuestionario 
print(person.get("age"))
print(person["age"])