import os
import random

class Juego:
    def _init_(self, mapa):
        self.mapa = mapa

    def obtener_mapa(self):
        return self.mapa

class JuegoArchivo(Juego):
    def _init_(self, path_a_mapas):
        # Obtener la lista de archivos en el directorio
        archivos = os.listdir(path_a_mapas)
        
        # Elegir un archivo aleatorio
        nombre_archivo = random.choice(archivos)
        
        # Componer el path completo
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        
        # Llamar al constructor de la clase base con el mapa leído
        super()._init_(self.leer_mapa(path_completo))

    def leer_mapa(self, path):
        # Abrir el archivo en modo lectura
        with open(path, 'r') as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()
            
            # Concatenar las líneas en una cadena
            cadena_mapa = ''.join(lineas)
            
            # Eliminar caracteres en blanco residuales y retornar
            return cadena_mapa.strip()