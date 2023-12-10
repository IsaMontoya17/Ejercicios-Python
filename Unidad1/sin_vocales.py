#Implementa un programa que solicite al usuario una cadena de texto y luego muestre esa cadena pero sin las vocales

def vocales():
    cadena = input("Ingrese una cadena de texto: ")
    resultado = abreviacion(cadena)
    print("La cadena de texto abreviada es: " + "".join(resultado))
    
def abreviacion(pal):
    pal = pal.lower()
    salida = []
    for i in range(len(pal)): #len es como en .lenght en java
        if pal[i] not in ["a","e","i","o","u"," "]:
            salida.append(pal[i])
    return salida

if __name__=="__main__":
    vocales()