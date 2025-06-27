# --- Clase Base: Animal ---
class Animal:
    def __init__(self, nombre):
        # Encapsulación: El nombre es un atributo "privado"
        # Esto significa que no lo modificas directamente, usas métodos.
        self.__nombre = nombre

    def get_nombre(self):
        """Obtiene el nombre del animal."""
        return self.__nombre

    def hacer_sonido(self):
        """Método que todo animal debe tener."""
        return "Hace un sonido genérico."

    def describir(self):
        """Método general para describir el animal."""
        return f"Soy un animal llamado {self.get_nombre()}."

# --- Clase Derivada: Perro ---
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Herencia: Llamamos al constructor de la clase Animal
        super().__init__(nombre)
        self.raza = raza # Atributo específico de Perro

    # Polimorfismo: Sobreescribimos el método hacer_sonido
    def hacer_sonido(self):
        """El perro hace un sonido específico."""
        return "¡Guau! ¡Guau!"

    # Polimorfismo: Sobreescribimos el método describir
    def describir(self):
        """Descripción más detallada para un perro."""
        return f"Soy un perro llamado {self.get_nombre()}, de raza {self.raza}."

# --- Clase Derivada: Gato ---
class Gato(Animal):
    def __init__(self, nombre, color):
        # Herencia: Llamamos al constructor de la clase Animal
        super().__init__(nombre)
        self.color = color # Atributo específico de Gato

    # Polimorfismo: Sobreescribimos el método hacer_sonido
    def hacer_sonido(self):
        """El gato hace un sonido específico."""
        return "¡Miau! ¡Miau!"

    # Polimorfismo: Sobreescribimos el método describir
    def describir(self):
        """Descripción más detallada para un gato."""
        return f"Soy un gato llamado {self.get_nombre()}, de color {self.color}."

# --- ¡Hora de jugar con nuestros animales! ---

print("--- Demostración de Herencia y Encapsulación ---")

# Creamos un animal genérico
mi_animal = Animal("Bicho")
print(mi_animal.describir())
print(f"¿Cuál es el nombre de mi animal genérico? {mi_animal.get_nombre()}")
print(mi_animal.hacer_sonido())

print("\n--- Demostración de Perro (Hereda de Animal) ---")

# Creamos un perro
mi_perro = Perro("Fido", "Labrador")
print(mi_perro.describir())           # Usa su propia descripción
print(mi_perro.hacer_sonido())        # Usa su propio sonido
print(f"La raza de Fido es: {mi_perro.raza}")
# Podemos ver su nombre gracias al método heredado de Animal
print(f"El nombre de mi perro es: {mi_perro.get_nombre()}")

print("\n--- Demostración de Gato (Hereda de Animal) ---")

# Creamos un gato
mi_gato = Gato("Luna", "Blanco")
print(mi_gato.describir())            # Usa su propia descripción
print(mi_gato.hacer_sonido())         # Usa su propio sonido
print(f"El color de Luna es: {mi_gato.color}")
print(f"El nombre de mi gato es: {mi_gato.get_nombre()}")

print("\n--- Demostración de Polimorfismo ---")

# Metemos varios animales en una lista, ¡de diferentes tipos!
animales_en_granja = [mi_animal, mi_perro, mi_gato]

# Ahora, vamos a hacer que todos hagan su sonido y se describan
# Cada animal usará su propia versión de los métodos, ¡eso es polimorfismo!
for animal in animales_en_granja:
    print(animal.describir())
    print(animal.hacer_sonido())
    print("-" * 10)