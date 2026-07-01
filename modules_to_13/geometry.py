# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
"Modulo de geometria"
"   1. calcCircleArea(): Calcular area de un circulo"
"   2. calcSquareArea(): Calcular area de un cuadrado"

def calcCircleArea(radio):
    from math import pi
    return pi * (radio ** 2)

def calcSquareArea(lado):
    return lado ** 2