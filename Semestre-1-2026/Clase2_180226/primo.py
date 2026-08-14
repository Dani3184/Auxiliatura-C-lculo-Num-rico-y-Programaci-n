def primos(a):
    for i in range(2,a//2):
        resto = a % i
        print(i, resto)  
        if resto == 0: 
            print("no es primo")
            return False
            break
        return True
primos(42)

sum()
for x in range(4,0.1):
    print(x)