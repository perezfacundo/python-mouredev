
# 1. Declarar y asignar valores a las siguientes variables:
# - name: una cadena que contenga tu nombre.
# - age: un numero entero que represente tu edad
# - height: un numero flotante que represente tu altura.
# - Imprime cada variable en una linea separada.
print("\n# 1. Declarar y asignar valores a las siguientes variables:")
name = "Yair Corbalan"
age = 50
height = 1.7
print(f"Nombre: {name}. Edad: {age}. Altura: {height} mts.")

# 2. Convertir la variable edad de entero a cadena y concatenarla con un texto que diga cuantos años tienes.
print("\n# 2. Convertir la variable edad de entero a cadena y concatenarla con un texto que diga cuantos años tienes.")
strAge = str(age)
message = "Mi edad es "
print(strAge + message)

# 3. Declarar una variable booleana (is_student) que indique si eres estudiante o no. 
# - Usar True o False segun corresponda e imprimirla.
print("\n# 3. Declarar una variable booleana (is_student) que indique si eres estudiante o no.")
is_student = True
print(is_student)

# 4. Usar la funcion len() para calcular cuantos caracteres tiene tu nombre completo.
# - Luego almacenarlo en una variable.
print("\n# 4. Usar la funcion len() para calcular cuantos caracteres tiene tu nombre completo.")
print(f"Mi nombre '{name}' tiene {len(name)} caracteres.")

# 5. Declarar tres variables en una sola linea que representen tu nombre, apellido y ciudad de origen.
# - Imprimir estos valores
print("\n# 5. Declarar tres variables en una sola linea que representen tu nombre, apellido y ciudad de origen.")
firstname = "Fabricio"; lastname = "Losada"; origin_city = "Londres"
print(f"Mi nombre es {lastname}, {firstname}. Soy nacido en {origin_city}.")

# 6. Usar la funcion input para solicitar al usuario su color favorito y almacenarlo en una variable color.
# - Luego imprimir el valor ingresado.
print("\n# 6. Usar la funcion input para solicitar al usuario su color favorito y almacenarlo en una variable color.")
favorite_color = input("Ingrese su color favorito: ")
print(f"Mi color elegido es: {favorite_color}.")

# 7. Declarar una variable fruit e inicializarla con un valor.
# - Luego cambiar el valor de la fruta a otro diferente y volver a imprimirla.
print("\n# 7. Declarar una variable fruit e inicializarla con un valor.")
fruit = "Manzana"
fruit = "Mango"
print(fruit)

# 8. Convertir un numero decimal, almacenado en la variable price, a un numero entero y luego imprimirlo.
print("\n# 8. Convertir un numero decimal, almacenado en la variable price, a un numero entero y luego imprimirlo.")
float_price = 8.90
int_price = int(float_price)
print(f"El precio es de {int_price} USD.")

# 9. Declarar una variable llamada address_len.
# - Almacenar en ella la cantidad de caracteres de una direccion usando la funcion len().
# - Imprime el resultado.
print("\n# 9. Declarar una variable llamada address_len.")
address = "Zarate 5273, Villa Ballester, Ciudad de San Martin, Provincia de Buenos Aires"
address_len = len(address)
print(f"La direccion: '{address}', tiene {address_len} caracteres.")

# 10. Usar un tipo de dato forzado para declarar una variable phone, asegurandose de que siempre sera un numero.
# - Luego cambia su valor a un numero diferente y verificar el tipo de la variable con type().
print("# 10. Usar un tipo de dato forzado para declarar una variable phone, asegurandose de que siempre sera un numero.")
phone = int(input("Ingrese su numero de telefono: "))
print(type(phone))
phone = "abc"
print(type(phone))