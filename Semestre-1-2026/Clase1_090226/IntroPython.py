##Clase 09 02 2026
#Aux. Daniel Garcia
##Introducción a python
import math as mt
#imprimir texto, funcion print
# print("Hola mundo")
# print("Hola ", "mundo")
# print("Hello")
# print(" world!", end="")
# print("Hello", end="")
# print(" world!")
# print("555", "0123", "Hola", sep="-")


#INPUT
# a = input("dame tu nombre: ")
# Edad = int(input("Tu edad es ?"))
# print("Tu nombre es: ",  a)
# print("Tu nombre es: " +  a)
# print("Tu edad es: ",  Edad)

#variables
# a = 5 #(int)
# pi = 3.14 #(float)
# nombre = "Daniel" #(string)
# verda = True #(booleano)

# print(type(a))
# print(type(pi))
# print(type(nombre))
# print(type(verda))

# #convertir tipos
# number = 12
# numero = str(number)
# print(number, numero[1])

# Operaciones con string
# Concatenar
# a = "hola"
# b = "Mundo"
# c = a + b
# print(c)

# #tamano
# longitud = len(a)
# print(longitud)

# #Acceso a caracteres, es como acceder a las posiciones de un vector
# ultima = a[3]
# print(ultima)
# palabra = "radar"
# print(palabra[0])
# print(palabra[-1])

# #Operaciones con numeros
# a = 5
# b = 2

# c = a*b #Multiplicacion
# d = a**b #Potenciacion
# e = a+b #Suma o resta
# f = a/b # division
# h = a//b #resltado entero
# g = a%b #Da el resto de la división
# print(a,b,c,d,e,f,g, sep="-")
#Redondeo e impresion
# c = 4.124124
# d = 1.2151532
# e = 1e-19
# pi = mt.pi
# print(round(c, 2))
# print(f"Resultado: A = {c:.2f}, B = {d:.5f}, C = {e:.20f}")
# print(f"%.2f"% c)
# print(f" Los primeros 42 digitos de pi son: {pi:.42f}")
# print(round(6.6))
# print(f"{0.1:.40}")

#Libreria Math

#Condicionales
# #funcion if:
# Numero = int(input("Ingrese un numero del 1 al 99: "))
# if Numero > 50:
#     print("El numero es muy grande")
# elif Numero < 32:
#     print("El numero es muy pequeno")
# else: print("El numero es perfecto")
# # Podemos hacer condiciones logicas con and o or

# edad = int(input("Introduzca su edad: "))
# carrera= input("Introduzca su carrera: ")
# if edad > 18 and carrera.lower() == "fisica":
#     print("Puede pasar")
# else: print("No puede pasar")

#Bucles con for
for i in range(0,10):
    print(i)

i = 0
for x in range(10):
    i += x #+= signifia i = i + x
print(i)


#bucles con while
x = 10
while (x < 100):
    print(x)
    x += 10
Encencido = True
Velocidad = 12
while(Encencido == True):
    print(Velocidad)
    if Velocidad > 15: Encencido = False
    Velocidad += 1
print("Se apago el ventilador")

while True:
    print("Esto se ejecutará al menos una vez")
    respuesta = input("¿Quieres repetir? (s/n): ")
    
    if respuesta.lower() != 's':
        break 
    if respuesta.lower() != 'n': print("esa no es una opcion")
    