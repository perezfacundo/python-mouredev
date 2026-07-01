# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
" Modulo de Estudiantes "
"   1. Lista de estudiantes"
"   2. Funcion para imprimir todos los nombres"

STUDENTS = ['Mafalda', 'Felipe', 'Libertad', 'Manolito', 'Susanita', 'Paul', 'John', 'Ringo', 'George']

def printStudents():
    for st in STUDENTS:
        print(st)