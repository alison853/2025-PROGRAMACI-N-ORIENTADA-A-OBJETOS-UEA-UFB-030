class ClimaDia:
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura

    def obtener_temperatura(self):
        return self.__temperatura

    def __str__(self):
        return f"{self.__dia}: {self.__temperatura}°C"


class SemanaClimatica:
    def __init__(self):
        self.__dias = []

    def agregar_dia(self, clima_dia):
        self.__dias.append(clima_dia)

    def calcular_promedio(self):
        total = sum(d.obtener_temperatura() for d in self.__dias)
        return total / len(self.__dias)

    def mostrar_temperaturas(self):
        for dia in self.__dias:
            print(dia)


# Programa principal
def main():
    semana = SemanaClimatica()
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in nombres_dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        semana.agregar_dia(ClimaDia(dia, temp))

    print("\nTemperaturas ingresadas:")
    semana.mostrar_temperaturas()

    promedio = semana.calcular_promedio()
    print(f"\nPromedio semanal de temperatura: {promedio:.2f}°C")


# Llamada al programa
main()
