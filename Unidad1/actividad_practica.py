#Actividad Práctica

#1. Escriba un algoritmo para calcular la factorial de un número. Recuerda que la factorial de un número n es el producto de todos los números enteros positivos desde 1 hasta n.

#2. Escriba un algoritmo para determinar si una palabra es un palíndromo. Un palíndromo es una palabra que se lee igual al revés que al derecho.

#3. Implementa un algoritmo que ordene una lista de números de menor a mayor. Puedes usar cualquier algoritmo de ordenación que prefieras.

# Ejercicio 1
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero = int(input("Ingrese un numero: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")

# Ejercicio 2
def palindromo(palabra):
    cont=0
    for i in range(len(palabra)):
        if palabra[i]==palabra[len(palabra)-i-1]:
            cont+=1
    if cont==len(palabra):
        print("La palabra es palindroma")
    else:
        print("La palabra no es palindroma")

palabra = input("Ingrese una palabra: ")
palindromo(palabra)

#Ejercicio 3
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista.sort() # con reverse=True como parametro ordena de forma descendente

print("Lista ordenada:", lista)