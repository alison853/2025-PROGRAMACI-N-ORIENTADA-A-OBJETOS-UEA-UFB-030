# Archivo: EjemplosMundoReal_POO/biblioteca.py

class Libro:
    """
    Representa un libro en la biblioteca.
    Atributos:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        isbn (str): El ISBN único del libro.
        disponible (bool): True si el libro está disponible para préstamo, False en caso contrario.
    """

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Por defecto, un libro nuevo está disponible

    def __str__(self):
        """Devuelve una representación legible del objeto Libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"


class Usuario:
    """
    Representa un usuario de la biblioteca.
    Atributos:
        nombre (str): El nombre del usuario.
        id_usuario (str): Un ID único para el usuario.
        libros_prestados (list): Una lista de objetos Libro que el usuario tiene prestados.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Inicialmente, el usuario no tiene libros prestados

    def __str__(self):
        """Devuelve una representación legible del objeto Usuario."""
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    """
    Gestiona la colección de libros y los usuarios, así como los préstamos.
    Atributos:
        catalogo (list): Una lista de objetos Libro disponibles en la biblioteca.
        usuarios (list): Una lista de objetos Usuario registrados en la biblioteca.
    """

    def __init__(self):
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        """Añade un libro al catálogo de la biblioteca."""
        self.catalogo.append(libro)
        print(f"'{libro.titulo}' ha sido añadido a la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' ha sido registrado.")

    def prestar_libro(self, libro_isbn, id_usuario):
        """
        Intenta prestar un libro a un usuario.
        Verifica si el libro está disponible y si el usuario existe.
        """
        libro_encontrado = None
        for libro in self.catalogo:
            if libro.isbn == libro_isbn:
                libro_encontrado = libro
                break

        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_encontrado = usuario
                break

        if not libro_encontrado:
            print(f"Error: Libro con ISBN {libro_isbn} no encontrado.")
            return False
        if not usuario_encontrado:
            print(f"Error: Usuario con ID {id_usuario} no encontrado.")
            return False

        if libro_encontrado.disponible:
            libro_encontrado.disponible = False
            usuario_encontrado.libros_prestados.append(libro_encontrado)
            print(f"'{libro_encontrado.titulo}' prestado a {usuario_encontrado.nombre}.")
            return True
        else:
            print(f"'{libro_encontrado.titulo}' no está disponible actualmente.")
            return False

    def devolver_libro(self, libro_isbn, id_usuario):
        """
        Permite a un usuario devolver un libro.
        Actualiza el estado del libro y lo remueve de la lista de prestados del usuario.
        """
        libro_encontrado = None
        for libro in self.catalogo:
            if libro.isbn == libro_isbn:
                libro_encontrado = libro
                break

        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_encontrado = usuario
                break

        if not libro_encontrado or not usuario_encontrado:
            print("Error: Libro o usuario no encontrado.")
            return False

        if libro_encontrado in usuario_encontrado.libros_prestados:
            libro_encontrado.disponible = True
            usuario_encontrado.libros_prestados.remove(libro_encontrado)
            print(f"'{libro_encontrado.titulo}' ha sido devuelto por {usuario_encontrado.nombre}.")
            return True
        else:
            print(f"Error: El libro '{libro_encontrado.titulo}' no fue prestado a {usuario_encontrado.nombre}.")
            return False

    def mostrar_catalogo(self):
        """Muestra todos los libros en el catálogo de la biblioteca."""
        print("\n--- Catálogo de la Biblioteca ---")
        if not self.catalogo:
            print("El catálogo está vacío.")
            return
        for libro in self.catalogo:
            print(libro)
        print("--------------------------------")

    def mostrar_libros_usuario(self, id_usuario):
        """Muestra los libros que un usuario tiene prestados."""
        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_encontrado = usuario
                break

        if not usuario_encontrado:
            print(f"Error: Usuario con ID {id_usuario} no encontrado.")
            return

        print(f"\n--- Libros prestados a {usuario_encontrado.nombre} ---")
        if not usuario_encontrado.libros_prestados:
            print(f"{usuario_encontrado.nombre} no tiene libros prestados.")
            return
        for libro in usuario_encontrado.libros_prestados:
            print(libro)
        print("------------------------------------------")


# --- Demostración del Sistema de Biblioteca ---
if __name__ == "__main__":
    mi_biblioteca = Biblioteca()

    # Creación de objetos Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0307474728")
    libro2 = Libro("1984", "George Orwell", "978-0451524935")
    libro3 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "978-0618260274")

    # Creación de objetos Usuario
    usuario1 = Usuario("Ana García", "U001")
    usuario2 = Usuario("Luis Pérez", "U002")

    # Interacción con la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)

    mi_biblioteca.registrar_usuario(usuario1)
    mi_biblioteca.registrar_usuario(usuario2)

    mi_biblioteca.mostrar_catalogo()

    # Préstamos
    mi_biblioteca.prestar_libro("978-0307474728", "U001")  # Ana presta Cien Años
    mi_biblioteca.prestar_libro("978-0451524935", "U002")  # Luis presta 1984
    mi_biblioteca.prestar_libro("978-0307474728", "U002")  # Luis intenta prestar Cien Años (no disponible)

    mi_biblioteca.mostrar_catalogo()  # Ver el estado de los libros
    mi_biblioteca.mostrar_libros_usuario("U001")
    mi_biblioteca.mostrar_libros_usuario("U002")

    # Devolución
    mi_biblioteca.devolver_libro("978-0307474728", "U001")  # Ana devuelve Cien Años

    mi_biblioteca.mostrar_catalogo()  # Ver el estado de los libros nuevamente
    mi_biblioteca.mostrar_libros_usuario("U001")