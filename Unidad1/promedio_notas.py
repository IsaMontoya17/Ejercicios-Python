def promedio():
    notas = []
    i = 1
    while True:
        nota = input(f"Ingrese 'salir' o la nota {i}: ")
        if nota.lower() == "salir":
            break
        notas.append(float(nota))
        i += 1
        
    if len(notas) == 0:
        print("No se ingresaron notas.")
    else:
        promedio = sum(notas) / len(notas)
        print("Su promedio es:", promedio)

promedio()
