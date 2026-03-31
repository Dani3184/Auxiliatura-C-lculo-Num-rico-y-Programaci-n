##Soluciones de practicas
#Aux. Daniel Roberto Garcia Miranda
##Ejercicios 1 elipse
#Podemos hacer por separado una funcion que determine si dos puntos x e y estan dentro la elipse de parametros h, k, a y b
import matplotlib.pyplot as plt
import numpy as np

def Elipse(h,k,a,b,x,y):
    #Calculamos:
    dx = (b**2)*(x-h)**2
    dy = (a**2)*(y-k)**2
    if dx + dy <= (a**2)*(b**2):
        return True
    else: return False

#definimos los parametros de la elipse
a = 2
b = 3
h = 1
k = 5
#el punto
x = int(input("Introduzca x: "))
y = int(input("Introduzca y: "))

if Elipse(a,b,h,k,x,y): print("El punto esta dentro la elipse")
else: print("El punto esta fuera de la elipse")

#Grafico
# 1. Dibujar la elipse (forma ultra simple)
t = np.linspace(0, 7, 100) 
plt.plot(h + a*np.cos(t), k + b*np.sin(t))

# 2. Dibujar el punto
color = 'green' if Elipse(h,k,a,b,x,y) else 'red'
plt.scatter(x, y, c=color)

# 3. Mostrar
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.show()