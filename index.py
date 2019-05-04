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

# Arrays

v = ["Hola", "Mundo", 4, 3.4, True, ["Otro", "Array"]]
v = v[0:3] # Toma el vector desde la posición cero a la posición 3
print(v[0])
v2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v3 = range(1,11) # Lo mismo que el anterior, no toma el ultimo valor
v4 = range(11)

# Recorrer vector
for x in v3:
    print(x)
    
# Eliminar elemento
v5 = ["Hola", "Carlos", 1]

v5.remove("Hola") # Elimina lo que diga hola
v5.pop() # Elimina la ultima pocición
v5.pop(1) # Elimina la posicion x, en este caso 1
v5.clear() # Elimina todo el vector

# Agregar Elementos
v5.append(5) # Agrega 5 en la ultima posición
v5.insert(2, "Donado") # Agrega donado en la posición 2

# Conoce la posición de un elemento
v5.index("Carlos") # Retorna la posisción de Carlos en el vector

print(len(v5)) # Retirna el numero de elementos del vector

v5.count("Carlos") # Cuenta el numero de registro que digan Carlos en el vector

# Ordenar un vector
a = [5, 2, 7, 0]
a.sort()

# Recorrer Saltando
for x in a[0:4:2]: # Recorre desde cero hasta cuatro saltando de dos en dos
    print(x)
    
for x in a[0::2]: # Recorre desde cero hasta el final saltando de dos en dos
    print(x)

res = 2 in a

a[-1] # Trae el ultimo elemento
a[-2] # Trae el penultimo elemento
    
# Matriz
m = [[2, 4], [4, 2]]

# Ejercicio sumatoria

print("Sumatoria de: ")
val = int(input())

vsum = range(val + 1)
suma = 0
for x in vsum:
    suma = suma + x
    
print(suma)

# Otra forma de sumatoria
print("la sumatoria es ", sum(range(val+1)))

# While - Mientras que

i = 1
while i<5:
    print(i)
    i = i + 1

# Procedimientos
def hola_mundo():
    print("Hola mundo")

# Funcionaes
def elevar_cuadrado(numero):
    return numero ** 2

def elevar_exponente(numero, exponente=2): # Aqui defino parametros por defecto
    return numero ** exponente

# Invocar funciones y metodos
hola_mundo()
elevar_cuadrado(5)
elevar_exponente(5)
elevar_exponente(5, 3)



















