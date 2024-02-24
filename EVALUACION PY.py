## Importar librerias
import pickle 
import os

## Tema
class Biblioteca:
    def __init__(self): ##inicializar variables
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor): 
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += 1
        else:
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}

    def mostrar_libros(self):
        for titulo, info in self.libros.items():
            print(f"{titulo} - Autor: {info['autor']} - Cantidad: {info['cantidad']} - Disponible: {'Sí' if info['disponible'] else 'No'}")

    def prestar_libro(self, titulo, nombre_usuario):
        if titulo in self.libros and self.libros[titulo]['disponible']:
            if nombre_usuario in self.usuarios:
                self.usuarios[nombre_usuario]['libros_prestados'].append(titulo)
                self.libros[titulo]['disponible'] = False
                self.libros[titulo]['cantidad'] -= 1
                print(f"Libro '{titulo}' prestado a {nombre_usuario}.")
            else:
                print(f"Usuario '{nombre_usuario}' no registrado.")
        else:
            print(f"Libro '{titulo}' no disponible.")

    def registrar_usuario(self, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            self.usuarios[nombre_usuario] = {'libros_prestados': []}
            print(f"Usuario '{nombre_usuario}' registrado.")
        else:
            print(f"Usuario '{nombre_usuario}' ya registrado.")

    def guardar_datos(self):
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump({'libros': self.libros, 'usuarios': self.usuarios}, archivo)

    def cargar_datos(self):
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                datos_guardados = pickle.load(archivo)
                self.libros = datos_guardados.get('libros', {})
                self.usuarios = datos_guardados.get('usuarios', {})

    def listar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(usuario)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            libros_prestados = self.usuarios[nombre_usuario]['libros_prestados']
            if libros_prestados:
                print(f"Libros prestados a {nombre_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"{nombre_usuario} no tiene libros prestados.")
        else:
            print(f"Usuario '{nombre_usuario}' no registrado.")

    def devolver_libro(self, titulo, nombre_usuario):
        if nombre_usuario in self.usuarios and titulo in self.usuarios[nombre_usuario]['libros_prestados']:
            self.usuarios[nombre_usuario]['libros_prestados'].remove(titulo)
            self.libros[titulo]['disponible'] = True
            self.libros[titulo]['cantidad'] += 1
            print(f"Libro '{titulo}' devuelto por {nombre_usuario}.")
        else:
            print(f"El usuario '{nombre_usuario}' no tiene el libro '{titulo}' prestado.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.cargar_datos()

while True:
    print("\n=== Bienvenid@ al Menu del Sistema de gestion de Biblioteca ===")
    print("1. Agregar Libro")
    print("2. Mostrar Libros")
    print("3. Prestar Libro")
    print("4. Registrar Usuario")
    print("5. Guardar Datos")
    print("6. Cargar Datos")
    print("7. Listar Usuarios")
    print("8. Listar Libros de Usuario")
    print("9. Devolver Libro")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        biblioteca.agregar_libro(titulo, autor)

    elif opcion == '2':
        biblioteca.mostrar_libros()

    elif opcion == '3':
        titulo = input("Ingrese el título del libro: ")
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        biblioteca.prestar_libro(titulo, nombre_usuario)

    elif opcion == '4':
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        biblioteca.registrar_usuario(nombre_usuario)

    elif opcion == '5':
        biblioteca.guardar_datos()
        print("Datos guardados correctamente.")

    elif opcion == '6':
        biblioteca.cargar_datos()
        print("Datos cargados correctamente.")

    elif opcion == '7':
        biblioteca.listar_usuarios()

    elif opcion == '8':
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        biblioteca.listar_libros_usuario(nombre_usuario)

    elif opcion == '9':
        titulo = input("Ingrese el título del libro: ")
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        biblioteca.devolver_libro(titulo, nombre_usuario)

    elif opcion == '0':
        biblioteca.guardar_datos()
        print("Saliendo del programa. Datos guardados correctamente.")
        break

    else:
        print("Opción no válida. Inténtelo de nuevo.")