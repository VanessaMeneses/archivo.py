# Archivo principal del proyecto integrador 2023 cohorte 50.
# Videojuego de texto 
# Creamos la variable nombre para que el ususario puede registrarse y en seguida damos un mensaje de bienvenida.
'''nombre = str(input('Ingrese el nombre de usuario: '))
print(f'Hola {nombre} bienvenid@ a esta maravillosa experiencia!')'''

 #if __(main) == '__(main)__':


#Proyecto integrador parte 2- cohorte 50.
# se inicia el juego de texto presionando una tecla cualquiera entendiendo que si se presiona UP es salida directa del juego
'''import readchar
import keyboard 
while True:
    Tecla = readchar.readchar()
    print(f'tecla presionada: {Tecla}')
    if keyboard.is_pressed('up'):
            print('tecla de salida presionada. sale de juego')
            break'''
        
'''proyecto integrador parte 3'''
import os

numero = 0

while numero <= 50:
    # Leer la tecla 'n' del teclado
    entrada = input("Presiona la tecla 'n' para avanzar: ")

    if entrada == 'n':
        numero += 1
        # Borrar la terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Número actual: {numero}')
    else:
        print('Debes presionar la tecla "n" para avanzar.')

print('Llegaste a 50. ¡Terminado!')
