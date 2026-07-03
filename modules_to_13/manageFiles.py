# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

" Modulo de lectura y escritura de archivos "

def readlines(path, enum = True):
    with open(path, 'r') as file:
        if not enum:
            print(file.read())
        else:
            for n, line in enumerate(file):
                print(f"{n}: {line.strip()}")

def writelines(path, newLine, last = False):
    mode = 'w'
    if last: mode = 'a'

    with open(path, mode, encoding='utf-8') as file:
        file.write(newLine + "\n")

def findWordInFile(path, word):
    res = 0
    with open(path, "r") as file:
        for line in file:
            if word in line:
                res += line.lower().count(word)
    return f"times to {word} in {path}: {res}"
    