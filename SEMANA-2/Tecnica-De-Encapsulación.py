class BombillaSegura:
    def __init__(self):
        self.__estado_encendida = False # Este dato está PROTEGIDO

    def encender(self):
        """Método seguro para encender."""
        self.__estado_encendida = True
        print("Luz ENCENDIDA.")

    def apagar(self):
        """Método seguro para apagar."""
        self.__estado_encendida = False
        print("Luz APAGADA.")

# --- Usando la Bombilla ---
mi_luz = BombillaSegura()

mi_luz.encender()
mi_luz.apagar()

# No puedes hacer esto directamente: mi_luz.__estado_encendida = True
# Intentarías modificar el interior sin permiso.
