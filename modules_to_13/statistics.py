# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

"Modulo para calcular estadistica"
"   1. calculateMedia(): simplemente el promedio de un conjunto de numeros. "
"   2. calculateMediana(): El valor que esta en el centro del conjunto de datos, partiendolo en 2 mitades. "

def calculateMedia(*args):
    res = 0
    for num in args:
        res += num
    return res / len(args)

def calculateMediana(*args):
    import math

    res = 0
    nums_list = list()
    # ordenar el conjunto de numeros
    for num in sorted(args):
        nums_list.append(num)
    
    if not len(nums_list) % 2 == 0: # si no es par:
        return math.ceil(len(nums_list) / 2)
    else:
        i = int(len(nums_list) / 2) - 1
        return calculateMedia(nums_list[i], nums_list[i+1])
    