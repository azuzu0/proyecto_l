import string
# Estrella a Delta
class CalculadoraResistencia:
    def __init__(self):
        self.valores = [] # Almacena todos los valores recibidos 
        self.resistencias = [] # Almacenamos los resultados

    def agregar_valor(self, valor):
        self.valores.append(valor) # Cada valor que se haya recibido se agregara al vector "valores"

    def calcular_resistencias(self):
        valores = self.valores
        rt =[self.valores[0] * self.valores[1], self.valores[1] * self.valores[2], self.valores[2] * self.valores[0] ]
        suma = sum(rt)
        for value in valores:
            resistencias = suma / value
            self.resistencias.append(resistencias)
        return self.resistencias

    def __str__(self):
        n = len(self.resistencias)
        resistencias_str = "Transformación Y→Δ: "
        for i in range(n):
            resistencia_str = f"\nR{string.ascii_lowercase[i]} = {self.resistencias[i]} Ω"
            resistencias_str += resistencia_str
        return resistencias_str
