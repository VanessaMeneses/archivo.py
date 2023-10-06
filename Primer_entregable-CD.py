'''# -*- coding: utf-8 -*-
# Variables
# Asignación de variables
# para asignar un valor a una variable, solo debemos usar el operador "="

nombre = "Ariel"   # 
edad = 23
fuma = False

# estatura en metros
estatura = 1.8

print("nombre", nombre)
print("edad", edad)
print("fuma", fuma)
print("estatura", estatura, "m")

x = 123
print(type(x))

x = 3.123
print(type("asdfasd"))

print("nombre", type(nombre))
print("edad", type(edad))
print("fuma", type(fuma))
print("estatura", type(estatura))

# Enteros int
# Los enteros siguen las mismas reglas que en las matemáticas

numero_1 = 112
numero_2 = 23

# suma
print(numero_1 + numero_2)

# resta
print(numero_1 - numero_2)

# multiplicación
print(numero_1 * numero_2)

# división puede resultar en un numero con decimales
print(numero_1 / numero_2)

# división entera resultar en un numero entero sin decimales
# es el cociente de una división
print(numero_1 // numero_2)

# modulo o resto de una division
print(numero_1 % numero_2)

# número al cuadrado
print(numero_1 ** 2)

# Conversion de valores

# convertir entero a flotante
print (float(3))

# convertir entero a string
print (str(3))

# convertir entero a boolean
print (bool(3))

print (int(3.2))

# funciones para realizar operaciones

print (round(3.14162021,2))

# String
# asignar
nombre = "soy un nombre 234 $%^$%"

# imprimir
print(nombre)

dir()

## Asignación en memoria

x = "1"

#x -> lugar de memoria -> 1
#y -> lugar de memoria -> 3

print(hex(id(x)))

y = "1"
print(hex(id(y)))'''

####____________
'''En Python, tanto los enteros (integers) como los flotantes (floats) tienen límites que están determinados 
por las limitaciones de la representación numérica en la computadora en la que se ejecuta el programa. 
Estos límites dependen de la arquitectura de la máquina y de la versión de Python que estás utilizando.'''
#Puedes usar las funciones sys.maxsize y sys.float_info para obtener información sobre los límites de enteros 
# y flotantes en tu sistema específico:
# import sys

# print("Límite de enteros:", sys.maxsize)
# print("Información de flotantes:", sys.float_info)
# Esto proporcionará información más detallada sobre los límites en tu sistema particular.





