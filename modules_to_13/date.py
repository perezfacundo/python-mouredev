# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
""" Modulo de utilidad de fechas y diferencia entre fechas """
from datetime import date, datetime

def today():
    return date.today().strftime("%d/%m/%Y")

def daysTo(another_date):
    res = 0
    today = datetime.now()
    ad = datetime.strptime(another_date, "%d/%m/%Y")
    res = ad - today
    return f"{res.days} days to {another_date}"