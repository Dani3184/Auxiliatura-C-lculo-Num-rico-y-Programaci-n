import numpy as np

datos = np.loadtxt(f"testPMTsLG-1600-1600-20251015_19_26_ch1.txt")
print(datos)

carga = datos[:,0]
cargaN = carga*0.01952
Voltaje = datos[:,1]
VoltajeN = Voltaje*0.122
Tiempo= datos[:,2]
TiempoN= Tiempo*8
print(carga) 
print(Voltaje) 
print(Tiempo) 
import matplotlib.pyplot as plt
plt.hist(cargaN, bins=100)
plt.title("Histograma Carga vs Pico")
plt.ylabel("Carga pC")
plt.xlabel("Cuentas")
plt.grid(True)
plt.yscale("log")
plt.show()
plt.hist(VoltajeN, bins=100)
plt.yscale("log")
plt.show()
plt.hist(TiempoN, bins=100)
plt.show()
plt.scatter(cargaN,VoltajeN)
plt.show()