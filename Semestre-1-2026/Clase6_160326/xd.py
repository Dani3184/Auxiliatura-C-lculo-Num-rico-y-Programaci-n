import Daniel

vec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Daniel.promedio(vec)
import random
import numpy as np
import matplotlib.pyplot as plt

# pedir cotas
a=float(input("Ingrese la cota inferior a: "))
b=float(input("Ingrese la cota superior b: "))
n=707
nbin=50
semilla=7
random.seed(semilla)
misnum=np.empty(n)

for i in range(n):
    misnum[i]=a+(b-a)*random.random()
dx=(b-a)/nbin
histo=np.zeros(nbin)
for j in range(n):
    x=misnum[j]
    posicion=(x-a)/dx
    i=int(posicion)
    if i>=nbin:
        i=nbin-1
    histo[i]+=1
xgraf=[]
ygraf=[]
for i in range(nbin): 
    xgraf.append(a+i*dx)
    ygraf.append(0)
    xgraf.append(a+i*dx)
    ygraf.append(histo[i])
    xgraf.append(a+(i+1)*dx)
    ygraf.append(histo[i])
    xgraf.append(a+(i+1)*dx)
    ygraf.append(0)

plt.plot(xgraf,ygraf)
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.title("Histograma")
plt.show()