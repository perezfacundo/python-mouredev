# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
""" Modulo para realizar conversiones
    1. convert_celsius_fahrenheit() -> Convertir temperatura celsius a fahrenheit
    2. convert_fahrenheit_celsius() -> Convertir temperatura fahrenheit a celsius
"""

def convert_celsius_fahrenheit(temp):
    result = 0
    try:
        result = (temp * 1.8) + 32
    except Exception as e:
        result = "Error: %s" % e
    return result

def convert_fahrenheit_celsius(temp):
    result = 0
    try:
        result = ((temp - 32) * 5) / 9
    except Exception as e:
        result = "Error: %s" % e
    return result