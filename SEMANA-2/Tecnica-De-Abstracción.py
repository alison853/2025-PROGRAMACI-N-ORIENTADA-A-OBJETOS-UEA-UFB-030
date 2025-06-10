class Bombilla:
    def __init__(self):
        self._esta_encendida = False # Detalle interno que no necesitas ver

    def encender(self):
        """
        Abstracción: Simplemente enciende la luz.
        Oculta todo el funcionamiento eléctrico.
        """
        self._esta_encendida = True
        print("La bombilla está ENCENDIDA.")

    def apagar(self):
        """ Bienvenidos
        Abstracción: Simplemente apaga la luz.
        Oculta cómo se interrumpe el circuito.
        """
        self._esta_encendida = False
        print("La bombilla está APAGADA.")

# --- Uso de la Bombilla ---
mi_bombilla = Bombilla()

print("--- Interacción simple ---")
mi_bombilla.encender()
mi_bombilla.apagar()
mi_bombilla.encender()