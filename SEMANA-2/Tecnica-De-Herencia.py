# Clase Padre (o Superclase)
class Forma:
    def __init__(self, x, y):
        self.x = x  # Posición en el eje X
        self.y = y  # Posición en el eje Y
        print(f"Se creó una Forma en ({self.x}, {self.y}).")

    def mover(self, nuevo_x, nuevo_y):
        """
        Método que todas las formas pueden hacer: moverse.
        """
        self.x = nuevo_x
        self.y = nuevo_y
        print(f"La forma se movió a ({self.x}, {self.y}).")

# Clase Hija (o Subclase) que HEREDA de Forma
class Circulo(Forma):
    def __init__(self, x, y, radio):
        # Llama al constructor de la clase padre (Forma)
        super().__init__(x, y)
        self.radio = radio
        print(f"  ...y es un Círculo con radio {self.radio}.")

    def calcular_area(self):
        """
        Método específico de la clase Círculo.
        """
        import math
        return math.pi * (self.radio ** 2)

    def describir(self):
        """
        Método para describir el círculo, combinando propiedades heredadas y propias.
        """
        return f"Círculo en ({self.x}, {self.y}) con radio {self.radio}"

# --- Usando la Herencia ---

print("--- Creando una forma genérica ---")
mi_forma_generica = Forma(10, 20)
mi_forma_generica.mover(30, 40)

print("\n--- Creando un Círculo (que hereda de Forma) ---")
mi_circulo = Circulo(50, 60, 10)

# El círculo HEREDA 'x' y 'y' de Forma
print(f"\nPosición del círculo: ({mi_circulo.x}, {mi_circulo.y})")

# El círculo HEREDA el método 'mover' de Forma
mi_circulo.mover(70, 80)

# El círculo usa su método 'calcular_area' específico
area = mi_circulo.calcular_area()
print(f"Área del círculo: {area:.2f}")

# El círculo usa su método 'describir'
print(mi_circulo.describir())