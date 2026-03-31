# for i in range(0,10):
#     print(i)

# suma = 0
# # for i in range(20):
# #     suma = suma + i
# # print(suma)

# while suma < 200:
#     suma+=5
#     print(suma)
# print(suma) 

x = 25
contador = 0
for i in range(1,x):
    if i%2 == 0:
        print(i)
        contador+=1

print(contador)

numero = 251361
contador = 0
for i in range(2,numero//2):
    if numero%i == 0:
        contador +=1
# print(contador)
if contador > 0: print("no es primo")
else: print("es primo")