# Configuración
archivo_original = r"Clase6_160326\testPMTsLG-1600-1600-20251015_19_26_ch1.txt"
archivo_salida = r"1000testPMTsLG-1600-1600-20251015_19_26_ch1.txt"
n_lineas = 1000  # Cambia esto a 50, 100, 1000, etc.

with open(archivo_original, "r") as origen:
    with open(archivo_salida, "w") as destino:
        for i in range(n_lineas):
            linea = origen.readline()
            if not linea: break  # Si el archivo tiene menos de N líneas, detente
            destino.write(linea)

print(f"Se han guardado las primeras {n_lineas} líneas en {archivo_salida}")