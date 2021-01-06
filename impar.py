"""Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

Solución
"""
numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: ") )
print("Muy bien!! Finalizo el programa")

