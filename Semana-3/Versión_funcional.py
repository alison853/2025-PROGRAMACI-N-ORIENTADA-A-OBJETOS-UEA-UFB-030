# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de los 7 días de la semana:")
    for i in range(7):
        temp = float(input(f"Día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamada al programa
main()
