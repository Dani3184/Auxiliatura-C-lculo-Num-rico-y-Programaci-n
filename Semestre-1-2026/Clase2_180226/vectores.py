#Clase2_180226
#Aux. Daniel Roberto Garcia Miranda
#Vectores
vector = [1, 2, 3, 4, 5, 6]

print(vector[4])
#Para hacer un vector de ceros
vec = 5*[0]
print(vec)
#Para hacer una matriz de ceros
filas = 3
columnas = 5
matriz = [[0] * columnas for _ in range(filas)]

def primo(a):
    b = a//2 +1
    for i in range(2, b):
        if a%i == 0:
            return False
    return True


#Ejercicios
#hacer una lista con numeros primos


def vectordePrimos(b):
    primos_vec = []
    for i in range(2,b):
        x = primo(i)
        if x is True: primos_vec.append(i)
    return primos_vec

print(vectordePrimos(100))
# print(vectordePrimos(1000))

for _ in vectordePrimos(1000): print(_)
