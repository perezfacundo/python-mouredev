# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).
num1 = 12; num2 = 0
try:
    res = num1 / num2
except:
    print("No es posible dividir por cero")

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.
def convertToInt(chain):
    try:
        return int(chain)
    except:
        return "Error al convertir la cadena de texto"
    
chain = "ocho"
print(convertToInt(chain))

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def leerArchivo(archivo, modo):
    with open(archivo, 'r') as archivo:
        
        if modo.upper() == 'COMPLETO':
            # Leer todo el archivo junto
            contenido = archivo.read()
            print(contenido)
        else:
            # Leer el archivo linea por linea
            for n, linea in enumerate(archivo):
                print("Jugador numero %s: %s" % (n, linea.strip()))

leerArchivo("archivo.txt", "renglon")

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.  

def operations(n1, n2):
    message = ""
    try: message += "Suma: %s + %s = %s \n" % (n1, n2, (n1 + n2))
    except: message += "Suma: %s + %s = Error" % (n1, n2)
    
    try: message += "Resta: %s - %s = %s \n" % (n1, n2, (n1 - n2))
    except: message += "Resta: %s - %s = Error" % (n1, n2)

    try: message += "Multiplicación: %s * %s = %s \n" % (n1, n2, (n1 * n2))
    except: message += "Multiplicación: %s - %s = Error" % (n1, n2)

    try: message += "División: %s / %s = %s \n" % (n1, n2, (n1 / n2))
    except: message += "División: %s / %s = Error" % (n1, n2)

    return message

print(operations(10, 0))

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.  
def getAge():
    number = 0
    number = int(input("Por favor, ingrese su edad: "))
    if number < 1:
        raise ValueError("El valor debe ser igual o mayor a 1")
    return number

try: 
    edad = getAge()
    print(edad)
except ValueError as ve: 
    print(ve)

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.  
def getElementByIndex(idx, lista):
    try: 
        return lista[idx]
    except Exception as e:
        return e

lista = [10, 3, 5, 1, 1, 8, 2, 4]
print(getElementByIndex(10, lista))

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.  


# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.  

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.  

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.




