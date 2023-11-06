# Proyecto integrados parte 4 - cohorte 50 - 2023
import os

# Función para convertir el mapa de laberinto en una matriz de caracteres
def string_to_matrix(map_string):
    return [list(row) for row in map_string.strip().split('\n')]

# Función para limpiar la pantalla y mostrar la matriz
def clear_screen_and_display(matrix):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in matrix:
        print(''.join(row))

# Función para el bucle principal del juego
def play_game(map_matrix, start_pos, end_pos):
    px, py = start_pos

    while (px, py) != end_pos:
        map_matrix[px][py] = 'P'
        clear_screen_and_display(map_matrix)
        map_matrix[px][py] = '.'

        key = input("Presiona una tecla de flecha (arriba, abajo, izquierda, derecha): ")
        if key == "arriba" and px > 0 and map_matrix[px - 1][py] != '#':
            px -= 1
        elif key == "abajo" and px < len(map_matrix) - 1 and map_matrix[px + 1][py] != '#':
            px += 1
        elif key == "izquierda" and py > 0 and map_matrix[px][py - 1] != '#':
            py -= 1
        elif key == "derecha" and py < len(map_matrix[0]) - 1 and map_matrix[px][py + 1] != '#':
            py += 1

# Mapa en forma de cadena
laberinto = """
..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################..
"""
# Convertir la cadena en una matriz de caracteres
map_matrix = string_to_matrix(laberinto)

# Posiciones inicial y final
start_position = (0, 0)
end_position = (len(map_matrix) - 1, len(map_matrix[0]) - 1)

# Jugar
play_game(map_matrix, start_position, end_position)