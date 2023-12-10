# Implemente un programa que solicite al usuario en nombre de una variable en camel case y muestre el nombre correspondiente en snake case

def snake_case():
    camel_case = input("Ingrese una variable en camelCase: ")
    snake_case=""
    
    for i in range (len(camel_case)):
        if camel_case[i].isupper():
            snake_case+= "_" + camel_case[i].lower()
        else:
            snake_case+=camel_case[i]
    
    print("La variable en snake case es: " , snake_case)
    
if __name__ == "__main__":
    snake_case()