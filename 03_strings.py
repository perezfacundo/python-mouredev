# 1. Longitud de cadena: Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().
print("# 1. Longitud de cadena")
text = "Aprendiendo Python"
print(len(text))

# 2. Concatenación: Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola línea.
print("\n# 2. Concatenación")
resultado = "Hola" + "Python"
print(resultado)

# 3. Salto de línea: Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
print("\n# 3. Salto de línea")
resultado = "1era linea \n2da linea"
print(resultado)

# 4. F-strings: Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
print("\n# 4. F-strings")
first_name = "Facundo"
last_name = "Perez"
age = 27
resultado = f"Mi nombre es {last_name} {first_name}. Tengo {age} años de edad."
print(resultado)

# 5. Desempaquetado: Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelos uno por uno.
print("\n# 5. Desempaquetado")
language = "Python"
letra1, letra2, letra3, letra4, letra5, letra6 = language
print(letra1, letra2, letra3, letra4, letra5, letra6)

# 6. Slicing (Rebanado): Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.
print("\n# 6. Slicing (Rebanado)")
word = "Programacion"
print(word[3:7])

# 7. Inversión: Invierte la cadena "Python" usando slicing y muestra el resultado.
print("\n# 7. Inversión")
print(word[::-1])

# 8. Mayúsculas: Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprímela.
print("\n# 8. Mayúsculas")
phrase = "aprendiendo python"
print(phrase.upper())

# 9. Conteo: Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".
print("\n# 9. Conteo")
print(phrase.count("n"))

# 10. Validación: Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.
print("\n# 10. Validación")
cod_area = "3521"
print(type(cod_area) == int)