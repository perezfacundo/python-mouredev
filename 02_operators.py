# 1. Realiza las siguientes operaciones aritméticas:
# - Suma: 15 + 25
# - Resta: 50 - 22
# - Multiplicación: 8 * 7
# - División: 100 / 20
print("\n# 1. Realiza las siguientes operaciones aritméticas")
print(f"Suma: 15 + 25 = {15 + 25}")
print(f"Resta: 50 - 22 = {50 - 22}")
print(f"Multiplicacion: 8 * 7 = {8 * 7}")
print(f"Division: 100 / 20 = {100 / 20}")

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable "remainder". Luego imprímelo.
print("\n# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable 'remainder'. Luego imprímelo.")
remainder = 37 % 5
print(remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase " es mi número favorito". Imprime el resultado.
print("\n# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase 'es mi número favorito'. Imprime el resultado.")
num = 7
str_num = str(num)
phrase = "es mi numero favorito"
print(f"El {str_num} {phrase}.")

# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
print("\n# 4. Repite la palabra 'Python' 10 veces usando el operador de multiplicación para cadenas y luego imprímela.")
cadena = "Python" * 10
print(cadena)

# 5. Crea dos variables: "a" y "b" con los valores 12 y 8 respectivamente.
# Compara si "a" es mayor que "b" y almacena el resultado en una variable booleana "resultado". Imprime el valor de "resultado".
print("\n# 5. Crea dos variables: 'a' y 'b' con los valores 12 y 8 respectivamente.")
a = 12; b = 8
resultado = a > b
print(f"Es a mayor que b ?: {resultado}")

# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y < y explica cuál tiene mayor orden alfabético.
print("\n# 6. Compara dos cadenas de texto ('apple' y 'banana') usando los operadores > y < y explica cuál tiene mayor orden alfabético.")
word1 = 'apple'; word2 = 'banana'
print(f"Alfabéticamente, está apple antes que banana ?: {word1 < word2}")

# 7. Realiza una comparación lógica usando "and" para verificar si el número 10 es mayor que 5 y menor que 20. 
# Imprime el resultado.
print("\n# 7. Realiza una comparación lógica usando 'and' para verificar si el número 10 es mayor que 5 y menor que 20. ")
resultado = 10 > 5 and 10 < 20
print(f"Es el numero 10, mayor que 5 y menor que 20?: {resultado}.")

print("\n# 8. Usa el operador 'or' para verificar si el número 7 es menor que 3 o mayor que 5.")
# 8. Usa el operador "or" para verificar si el número 7 es menor que 3 o mayor que 5.
# Imprime el resultado.
resultado = 7 < 3 or 7 > 5
print(f"Es el numero 7 menor que 3, o mayor que 5?: {resultado}.")

# 9. Aplica el operador "not" para invertir el resultado de la comparación 15 > 20. 
# ¿Cuál es el resultado?
print("\n# 9. Aplica el operador 'not' para invertir el resultado de la comparación 15 > 20.")
resultado = 15 > 20
print(f"Es el 15 mayor que el 20?: {resultado}. Resultado invertido: {not resultado}.")

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. 
# Imprime el resultado.
print("\n# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. ")
resultado = ((((5 * 3) + 2) > 10) and (((5 * 3) + 2) < 20))
print(f"Es el numero resultante de la expresion '((5 * 3) + 2)' mayor que 10 y menor que 20?: {resultado}.")