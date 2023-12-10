def main():

    menu = {
    "burrito": 4.50,
    "hamburguesa": 6.00,
    "pizza": 8.50,
    "ensalada": 5.25,
    "tacos": 3.75,
    "sopa": 4.00,
    "pasta": 7.50,
    "hot dog": 3.25,
    "pollo asado": 9.00,
    "sandwich": 5.50
    }

    total=0

    while True:
        try:
            item = input("Ingrese un articulo de su pedido: ")
        except EOFError:
            break
        item = item.lower()
        if item in menu:
            precio_articulo = menu[item]
            total += precio_articulo
            print(f"Precio de {item}: ${precio_articulo:.2f}")
        elif item == "control-d":
            print(f"El total de su pedido es ${total:.2f}") #las f significan la cantidad de decimales
            break
        else:
            print("Articulo inválido")
            

if __name__=="__main__":
    main()