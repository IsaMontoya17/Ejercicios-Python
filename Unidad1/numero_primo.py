#Dado un número entero positivo, determinar si es primo o no.

def numPrimo():
    numero = int(input("Ingrese un número: "))
    es_primo = True
    if numero <= 1:
        es_primo = False
    else:
        for i in range(2, (numero // 2) + 1):
            if numero % i == 0:
                es_primo = False
                break   
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

if __name__ == "__main__":
    numPrimo()
