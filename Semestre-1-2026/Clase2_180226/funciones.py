##Mas sobre python
##Clase2_180226
##Daniel Roberto Garcia Miranda
##Uso de funciones 

#Una funcion puede recibir un parametro y roducir un resultado (retornar un valor)
#Ej:
#esta funcion recibe un numero a y retorna su cuadrado
def funcion(a):
    return a*a

b = 5
print(funcion(b))

#Los metodos son funciones que se aplican a un objeto especifico
nombre = "daniel"
print(nombre)
NOMBRE = nombre.upper()
print(NOMBRE)

#Ejercicios
#Realizar funciones que:
#Determinen que un numero es primo

def primo(a):
    b = a//2 +1
    for i in range(2, b):
        if a%i == 0:
            return False
    return True

# a = int(input("Escriba un numero: "))
# hola = primo(a)
# if hola is True: print("El numero es primo")
# else: print("El numero no es primo")

#Funcion que imprima todos los primos entre un intervalo

def ImprimirPrimos(a,b):
    for i in range(a,b):
        x = primo(i)
        if x is True: print(i)

ImprimirPrimos(2, 1000)
