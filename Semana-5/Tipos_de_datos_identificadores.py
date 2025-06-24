# Este programa calcula el área de un rectángulo

def calcular_area_rectangulo():
    # Voy a pedirle al usuario que me dé las medidas del rectángulo
    print("¡Hola! Vamos a calcular el área de un rectángulo.")

    # Pido la base y la convierto a número con decimales (float)
    base_rectangulo_str = input("Por favor, ingresa la longitud de la base (en cm): ")
    # Intento convertir a float, por si acaso el usuario pone algo que no es número
    try:
        base_rectangulo = float(base_rectangulo_str)
    except ValueError:
        print("¡Oops! Parece que no ingresaste un número válido para la base. Intenta de nuevo.")
        return # Salgo de la función si hay un error

    # Pido la altura y también la convierto a número con decimales
    altura_rectangulo_str = input("Ahora, ingresa la altura (en cm): ")
    try:
        altura_rectangulo = float(altura_rectangulo_str)
    except ValueError:
        print("¡Oops! Parece que no ingresaste un número válido para la altura. Intenta de nuevo.")
        return # Salgo de la función si hay un error

    # Verifico que las medidas sean positivas, porque no existen áreas con lados negativos
    if base_rectangulo > 0 and altura_rectangulo > 0:
        # Aquí es donde hago la magia: multiplico base por altura
        area_calculada = base_rectangulo * altura_rectangulo

        # Muestro el resultado usando un tipo de dato string (texto)
        print(f"El área de tu rectángulo es: {area_calculada} cm²")

        # Aquí uso un tipo de dato booleano para indicar si el cálculo fue exitoso
        calculo_exitoso = True
        print(f"¿El cálculo fue exitoso? {calculo_exitoso}")
    else:
        # Si las medidas no son positivas, le aviso al usuario
        print("Las medidas deben ser números positivos. ¡Intenta de nuevo!")
        calculo_exitoso = False
        print(f"¿El cálculo fue exitoso? {calculo_exitoso}")

# Llamo a la función para que el programa se ejecute
calcular_area_rectangulo()