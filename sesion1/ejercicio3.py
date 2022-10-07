'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Programador x
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))

print()

horasextras = float(input("Introduce tus horas de extras de trabajo: "))

print()

coste = float(input("Introduce lo que cobras por hora: "))

print()

paga = (horasextras + horas) * coste
print("Tu paga es", paga)