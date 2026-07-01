# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
""" Modulo para resolver operaciones matematicas """

def sumar(*args):
    result = 0
    args_list = []
    for n in args:
        result += n
        args_list.append(str(n))
    
    return "Resultado: %s  = %s" % (" + ".join(args_list), result)

def restar(*args):
    array = []
    array_strs = []
    for n in args:
        array.append(int(n))
        array_strs.append(str(n))
    
    result = next(iter(array))
    i = 1
    while(i < len(array)):
        try:
            result -= array[i]
        except Exception as e:
            result = "Error: %s" % e
        
        if isinstance(result, str):
            return result
        i += 1
    
    return "Resultado: %s = %s" % (" + ".join(array_strs), result)

def dividir(n1, n2):
    result = 0
    try:
        result = n1 / n2
    except Exception as e:
        result = "Error: %s" % e
    
    return "Resultado: %s - %s = %s" % (n1, n2, result)

def multiplicar(n1, n2):
    result = 0
    try:
        result = n1 * n2
    except Exception as e:
        result = "Error: %s" % e
    
    return "Resultado: %s * %s = %s" % (n1, n2, result)