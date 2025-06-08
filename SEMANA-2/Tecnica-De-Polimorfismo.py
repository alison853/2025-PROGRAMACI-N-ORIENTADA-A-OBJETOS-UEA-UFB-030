class BotonAceptar:
    def pulsar(self):
        print("Acción: Guardar datos.")

class BotonCancelar:
    def pulsar(self):
        print("Acción: Descartar cambios.")

class BotonAyuda:
    def pulsar(self):
        print("Acción: Abrir manual de ayuda.")

# --- Usando el Polimorfismo ---

mis_botones = [
    BotonAceptar(),
    BotonCancelar(),
    BotonAyuda()
]

print("--- Pulsando diferentes botones ---")

for boton in mis_botones:
    boton.pulsar() # El mismo comando, diferentes resultados