# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
# Comentario de linea
"""
Comentario de parrafo
"""
a = 5
A = 7

# Hola Mundo
print("Hola Mundo")

# Variables
x = 4
y = "Texto"
z = 4.5
a = True
b = False
c = 4+5j
print(x, y, z, a, b, c)
print(x+' '+y+' '+z+' '+a+' '+b+' '+c)  #  Va a mandar error, la concatenación con + solo aplica a string

# Conocer el tipo de datos de una variable
print(type(b))

# Conversiones de tipos de datos

# Enteros
x = int("2")
print(x)
x = int(2.8)  # Solo toma parte entera
print(x)

# Float
x = float(2)  # Pasa a 2.0
print(x)
x = float("2.8")
print(x)

# String
x = str(2)  # Pasa a 2.0
print(x)
x = str(2.8)
print(x)

# Manejo de cadenas de texto y algunos metodos
cad = "Hello World"
print(cad[0])
print(cad[2])
print(cad[0:4])  # Retorna Hell porque no toma el ultimo valor
print(len(cad))  # Longitud de la cadena
print(cad.lower())  # Pasa todo a minusculas
print(cad.upper())  # Pasa todo a mayusculas
print(cad.replace('l', 'Y'))  # Reemplaza la letra l por la letra Y
print(cad.split(" "))

cad = "     Hello World   "
print(cad)
cad = cad.strip()  # Quita espacios adelante y atras
print(cad)
print(cad[0])

# Operaciones
import math
# Operaciones Aritmeticas
a = 2
b = 3
c = a + b
c = a - b
c = a * b
c = a / b
c = a // b  # Trae la parte entera de la division
c = a % b  # mod - Trae el reciduo
c = a ** b  # Exponente
c = math.sqrt(a)
print(c)


# Captura pos consola
print("Digite el nombre:")
nombre = input()
print("Hola "+nombre+"!")


print("Digite numero uno:")
n1 = input()
print("Digite numero dos:")
n2 = input()
print(n1+n2)  # Los input son string por lo tanto concatena
n1 = float(n1)
n2 = float(n2)
print(n1+n2)

# Condiciones (Los if no abren y cierran, se diferencia por la identación)
a = 2
b = 5
if a == b:
    print('Son iguales')
elif a > b:
    print(a, 'Es mayor que', b)
else:
    print(b, 'Es mayor que', a)


if b > a:
    if b > 1:
        print(b, 'Es mayor que 1 y es mayor que', a)


if b > a and b > 1:
    print(b, 'Es mayor que 1 y es mayor que', a)


print("Digite Edad:")
edad = int(input())
"""
if (edad >= 18):
    print("Es mayor de edad")
else:
    print("Es menor de edad")    
"""

# Si de linea con sino
print("Es mayor de edad") if (edad >= 18) else print("Es menor de edad")

# Si de linea sin sino
if (edad >= 18): print("Es mayor de edad")






























