#Numeros Primos

def primo(N):
    a = 0
    if N == 0 or N == 1 or N == 2 or N == 4: return False
    for i in range(2, N//2):
        if N%i == 0:
            a = a +1    
            break      
    if a > 0:     
        # print(N, "no es primo")
        return False
    else:
        # print(N, "es primo")
        return True

a = int(input("Introduce un numero: "))
primo(a)

for i in range(a):
    if primo(i): print(i)
