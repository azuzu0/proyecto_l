import string
#Delta a Estrella
class CalculadoraResistencia:
    def __init__(self):
        self.valores = [] # Almacena todos los valores recibidos 
        self.denominador = 0 
        self.resistencias = [] # Almacenamos los resultados

    def agregar_valor(self, valor):
        self.valores.append(valor) # Cada valor que se haya recibido se agregara al vector "valores"
        self.denominador += valor # Aumentamos cada valor a esta variable. (Y nos da como resultado la suma de los valores)

    def calcular_resistencias(self):
        n = len(self.valores) # Obtenemos la longitud/cantidad de valores que se han almacenado
        for i in range(n): # Creamos un bucle con rango de la longitud almacenada (obtengo las posiciones)
            numerador = 1
            for j in range(n): # Aqui, hacemos lo mismo que el anterior for pero ignorando la interación actual del anterior for.
                if i != j: # Aqui verificamos que no se vaya a multiplicar el valor actual con sigo mismo.
                    numerador *= self.valores[j] # Multiplicamos las recistencia, el resultado lo almacenamos y volvemos a multiplicar otra resitencia
            resistencia = numerador / self.denominador # Realizamos el pertinente calculo.
            self.resistencias.append(resistencia)
        return self.resistencias

    def __str__(self):
        n = len(self.resistencias)
        resistencias_str = "Transformación Δ→Y: "
        for i in range(n):
            resistencia_str = f"\nR{i+1} = {self.resistencias[i]} Ω"
            resistencias_str += resistencia_str
        return resistencias_str
