# 1. Almacenar las coordenadas geográficas fijas (latitud y longitud) de un monumento histórico. ¿Qué estructura usas?
print("\n1. Almacenar las coordenadas geográficas fijas (latitud y longitud) de un monumento histórico. ¿Qué estructura usas?")
coords = dict()
coords = {"lat": -123123, "lon": 234234}

# 2. Guardar una lista de compras del supermercado donde el orden importa y se pueden repetir productos. ¿Qué estructura usas?
print("\n2. Guardar una lista de compras del supermercado donde el orden importa y se pueden repetir productos. ¿Qué estructura usas?")
compras = list()
compras = ["Manzanas", "Manzanas", "Bananas", "Arroz", "Te en hebras"]

# 3. Registrar los números de identificación (DNI/ID) de los asistentes a un evento, asegurando que no haya duplicados. ¿Qué estructura usas?
print("\n3. Registrar los números de identificación (DNI/ID) de los asistentes a un evento, asegurando que no haya duplicados. ¿Qué estructura usas?")
asistentes = set()
import random

for i in range(0, 10):
    asistentes.add(random.randint(00000000, 50000000))
print(asistentes)

# 4. Guardar la información de un usuario (nombre, email, edad) para poder acceder a los datos mediante una clave. ¿Qué estructura usas?
print("\n4. Guardar la información de un usuario (nombre, email, edad) para poder acceder a los datos mediante una clave. ¿Qué estructura usas?")
user = {
    "nombre": "Francisco Varallo",
    "email": "fvarallo@google.com",
    "edad": 90
}

# 5. Almacenar el historial de páginas web visitadas en un navegador para poder volver atrás en el orden exacto. ¿Qué estructura usas?
print("\n5. Almacenar el historial de páginas web visitadas en un navegador para poder volver atrás en el orden exacto. ¿Qué estructura usas?")
historial = list()
historial.append("www.facebook.com")
historial.append("www.google.com")
historial.append("www.cadena3.com")
historial.append("www.millanel.com")
print(historial)

# 6. Definir los días de la semana (Lunes a Domingo) sabiendo que es una estructura constante que nunca debe modificarse. ¿Qué estructura usas?
print("\n6. Definir los días de la semana (Lunes a Domingo) sabiendo que es una estructura constante que nunca debe modificarse. ¿Qué estructura usas?")
semana_list = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
semana_tuple = tuple(semana_list)
print(semana_tuple)

# 7. Guardar el inventario de una tienda, asociando el nombre de cada producto con su cantidad disponible. ¿Qué estructura usas?
print("\n7. Guardar el inventario de una tienda, asociando el nombre de cada producto con su cantidad disponible. ¿Qué estructura usas?")
cantidades_almacen = {
    "Arroz": 12,
    "Polenta": 2,
    "Harina leudante": 20,
    "Coca Cola 500ml": 5,
    "Philip Morris BOX 12": 13
}

# 8. Recibir dos listas de amigos de dos usuarios diferentes y encontrar cuáles amigos tienen en común rápidamente. ¿Qué estructura usas?
print("\n8. Recibir dos listas de amigos de dos usuarios diferentes y encontrar cuáles amigos tienen en común rápidamente. ¿Qué estructura usas?")
qatar_list = ["Matias", "Tomas", "Pablo", "Ernesto", "Agustin"]
milla_list = ["Nicolas", "Braian", "Pablo", "Ernesto"]

qatar_set = set(qatar_list)
milla_set = set(milla_list)

common = qatar_set.intersection(milla_set)
print(common)

# 9. Almacenar las respuestas correctas de un examen de opción múltiple (A, B, C, A) manteniendo el orden de las preguntas. ¿Qué estructura usas?
print("\n9. Almacenar las respuestas correctas de un examen de opción múltiple (A, B, C, A) manteniendo el orden de las preguntas. ¿Qué estructura usas?")


# 10. Guardar los datos de configuración de una aplicación (puerto, host, debug) para consultarlos por su nombre. ¿Qué estructura usas?
print("\n10. Guardar los datos de configuración de una aplicación (puerto, host, debug) para consultarlos por su nombre. ¿Qué estructura usas?")

# 11. Registrar las patentes (placas) de los autos que ingresan a un estacionamiento para saber cuántos autos únicos entraron. ¿Qué estructura usas?
print("\n11. Registrar las patentes (placas) de los autos que ingresan a un estacionamiento para saber cuántos autos únicos entraron. ¿Qué estructura usas?")

# 12. Representar una fila de banco (espera) donde los clientes se atienden en el estricto orden en el que llegaron. ¿Qué estructura usas?
print("\n12. Representar una fila de banco (espera) donde los clientes se atienden en el estricto orden en el que llegaron. ¿Qué estructura usas?")

# 13. Almacenar un color en formato RGB (tres números enteros fijos entre 0 y 255) que no deben cambiar. ¿Qué estructura usas?
print("\n13. Almacenar un color en formato RGB (tres números enteros fijos entre 0 y 255) que no deben cambiar. ¿Qué estructura usas?")

# 14. Guardar un diccionario de traducción donde a cada palabra en inglés le corresponda su significado en español. ¿Qué estructura usas?
print("\n14. Guardar un diccionario de traducción donde a cada palabra en inglés le corresponda su significado en español. ¿Qué estructura usas?")

# 15. Almacenar las etiquetas (tags) de un artículo de blog, garantizando que el usuario no repita la misma etiqueta. ¿Qué estructura usas?
print("\n15. Almacenar las etiquetas (tags) de un artículo de blog, garantizando que el usuario no repita la misma etiqueta. ¿Qué estructura usas?")

# 16. Guardar las notas de un estudiante a lo largo del año para poder calcular su promedio al final. ¿Qué estructura usas?
print("\n16. Guardar las notas de un estudiante a lo largo del año para poder calcular su promedio al final. ¿Qué estructura usas?")

# 17. Guardar el resultado de una consulta que devuelve el nombre de un país y su capital como un par de datos inseparable. ¿Qué estructura usas?
print("\n17. Guardar el resultado de una consulta que devuelve el nombre de un país y su capital como un par de datos inseparable. ¿Qué estructura usas?")

# 18. Almacenar un catálogo de productos donde cada ID de producto se vincula a un objeto con sus detalles (precio, marca). ¿Qué estructura usas?
print("\n18. Almacenar un catálogo de productos donde cada ID de producto se vincula a un objeto con sus detalles (precio, marca). ¿Qué estructura usas?")

# 19. Guardar los números ganadores de la lotería de los últimos 10 años en el orden en que ocurrieron los sorteos. ¿Qué estructura usas?
print("\n19. Guardar los números ganadores de la lotería de los últimos 10 años en el orden en que ocurrieron los sorteos. ¿Qué estructura usas?")

# 20. Quitar todos los elementos duplicados de una colección de datos de manera eficiente y en una sola línea de código. ¿Qué estructura usas?
print("\n20. Quitar todos los elementos duplicados de una colección de datos de manera eficiente y en una sola línea de código. ¿Qué estructura usas?")