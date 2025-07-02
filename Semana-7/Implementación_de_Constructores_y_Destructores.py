class Persona:
    """
    Esta clase representa a una persona y demuestra el uso básico
    de constructores y destructores.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Persona.

        Se llama automáticamente al crear un objeto Persona.
        Inicializa el atributo 'nombre' de la persona.
        """
        self.nombre = nombre
        print(f"Constructor: ¡Hola! Mi nombre es {self.nombre}. Acabo de nacer (creado).")

    def decir_hola(self):
        """
        Método simple para que la persona salude.
        """
        print(f"{self.nombre}: ¡Hola a todos!")

    def __del__(self):
        """
        Destructor de la clase Persona.

        Se llama automáticamente cuando el objeto 'Persona' está a punto de ser
        eliminado de la memoria (cuando ya no hay referencias a él).
        Simula que la persona se despide o desaparece.
        """
        print(f"Destructor: Adiós mundo, soy {self.nombre}. Estoy desapareciendo (destruido).")


# --- Demostración del uso de la clase Persona ---

print("--- Inicio del programa ---")

# 1. Creamos una instancia de la clase Persona
# Esto llama automáticamente al constructor __init__
persona1 = Persona("Ana")

# 2. Usamos el objeto
persona1.decir_hola()

# 3. Creamos otra instancia de la clase Persona
# El constructor __init__ también se llama para esta nueva persona
persona2 = Persona("Juan")
persona2.decir_hola()

# 4. Cuando el programa llega a este punto, si no hay más referencias a 'persona1',
# el destructor de 'persona1' podría llamarse (Python lo gestiona).
# Para forzar la demostración, podemos eliminar explícitamente la referencia:
del persona1
print("La referencia a 'persona1' ha sido eliminada.")

print("\n--- Fin del programa ---")
# Cuando el programa termina, el objeto 'persona2' que aún existe será destruido
# y su destructor (__del__) será llamado automáticamente.