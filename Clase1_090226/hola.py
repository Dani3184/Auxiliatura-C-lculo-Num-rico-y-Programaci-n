# # print("hola")
# # print("hola", "mundo", sep="-")

# nombre = input("Escribe tu nombre")
# print(nombre)
# print("nombre")

# # tamano = len(nombre)
# tamano = len("hola")
# print(tamano)
# a =  1
# print("hola", a,  "mundo")

a = 2
b =7
c = b/a
d = b//a
e = b%a
print(c,d,e,sep="---")


c = 1.25136137613
print(round(c,4))
print(f"hola mundo {c:.6f}")

import math as mt
pi = mt.pi
print(pi)

xd = 0.1
print(f"hola juan {xd:.30f} hdoagdkgs")


numero = int(input("ingrese un numero"))
if numero > 100:
    print("el numero es muy grande")
elif numero < 50:
    print("el numero es muy pequeno")
else: print("el numero es perfecto")

if numero < 100 and numero > 50:
    print("es perfecto") 
else: print("numero equivocado")