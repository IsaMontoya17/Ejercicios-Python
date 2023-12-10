# formula: peso en kg/(altura en m)^2

def IMC():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en m: "))
    
    imc = peso/altura**2
    
    if imc < 18.5:
        resultado = " esta bajo de peso"
    elif 18.5 <= imc < 25:
        resultado = "esta normal"
    else:
        resultado = "tiene sobrepeso"
    
    print(f"Su IMC es {imc:.1f}, usted {resultado}")
    
IMC()