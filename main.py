from estrella_delta import CalculadoraResistencia as CRED
from delta_estrella import CalculadoraResistencia as CRDE
import string

print("-"*30)
print("Bienvenido a Calculadora de Resitencias")
print("¿Qué quiere calcular?")
while True:
    try:
        opcion = int(input("Resitencias: Y→Δ Estrella-Delta (1) o Δ→Y Delta-Estrella (2): "))
        
        if opcion == 1: # Estrella-Delta
            calculadora = CRED()
            n = int(input("Ingrese la cantidad de resistencias que desea calcular: "))
            nombres_resistencias = [f"R{i}" for i in range(1, n+1)]
            for i in range(n):
                nombre_resistencia = nombres_resistencias[i]
                valor = float(input(f"Ingrese el valor de {nombre_resistencia} en ohmios: "))
                calculadora.agregar_valor(valor)
            resultados = calculadora.calcular_resistencias()
            print(calculadora)
            break
        elif opcion == 2: # Delta-Estrella
            calculadora = CRDE()
            n = int(input("Ingrese la cantidad de resistencias que desea calcular: "))
            nombres_resistencias = [f"R{x}" for x in string.ascii_lowercase[:n]]
            for i in range(n):
                nombre_resistencia = nombres_resistencias[i]
                valor = float(input(f"Ingrese el valor de {nombre_resistencia} en ohmios: "))
                calculadora.agregar_valor(valor)
            resultados = calculadora.calcular_resistencias()
            print(calculadora)
            break
        else:
            raise ValueError("El número ingresado no es valido")
    except ValueError as err:
        print("Error 158:",err)        
