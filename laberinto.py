
from readchar import readkey, key
from typing import List, Tuple
import os 

print("==========================================")
print("Bienvenido al Juego de laberinto")
print("============================================")

nombre=input("Ingresa tu nombre de usuario por favor: ")

print(f"Bienvenido al Juego {nombre} Que disfrutes")
# Función para convertir el laberinto en cadena en una matriz de caracteres
def convertir_laberinto(laberinto_str: str) -> List[List[str]]:
    lineas = laberinto_str.strip().split("\n")
    laberinto = [list(linea) for linea in lineas]
    return laberinto

# Función para limpiar la pantalla y mostrar el mapa
def mostrar_laberinto(laberinto: List[List[str]]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla en Windows 
    for fila in laberinto:
        print("".join(fila))

# Función para el bucle principal del juego
def main_loop(laberinto: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
    px, py = inicio  # Coordenadas del jugador
    laberinto[px][py] = 'P'  # Posición inicial del jugador

    while (px, py) != final:
        mostrar_laberinto(laberinto)
        tecla = readkey() if os.name == 'nt' else input()
        if final == (19,27):
            print(f"----------------------------------------------------")
            print(f"--------------!!Ganaste!! {nombre} ------------------")
            print(f"----------------------------------------------------")
        # Calcula la nueva posición tentativa del jugador
        nueva_px, nueva_py = px, py

        if tecla == 'w':
            nueva_px -= 1
        elif tecla == 's':
            nueva_px += 1
        elif tecla == 'a':
            nueva_py -= 1
        elif tecla == 'd':
            nueva_py += 1
        elif tecla == "m":
            break  

        # Verifica si la nueva posición es válida
        if 0 <= nueva_px < len(laberinto) and 0 <= nueva_py < len(laberinto[0]) and laberinto[nueva_px][nueva_py] != '#':
            laberinto[nueva_px][nueva_py] = 'P'
            laberinto[px][py] = '.'
            px, py = nueva_px, nueva_py

# Mapa del laberinto como cadena (reemplaza con tu propio laberinto generado)
laberinto_str = """
      ############################
         #  #        #     #  #
#  #######  #######  ####  #  #
#              #        #  #  #
#  #######  #######  #  #  #  #
#     #     #  #     #  #     #
#  ####  #  #  #  #######  ####
#  #     #           #  #     #
#  ####  ####  #######  #  #  #
#     #  #        #        #  #
#  #######  #######  #######  #
#  #                 #        #
#  #######  ####  #######  ####
#     #        #  #           #
##########  #######  #  #  ####
#  #  #           #  #  #     #
#  #  ####  ####  #############
#           #           #     #
#  ####  ##########  #  #  ####
#     #     #        #       
############################  


"""

# Coordenadas de inicio y final
inicio = (0, 0)
final = (19,27)
if final == (5, 1):
    print("ganaste")
# Convierte el laberinto en una matriz de caracteres
laberinto = convertir_laberinto(laberinto_str)

# Inicia el bucle principal del juego
main_loop(laberinto, inicio, final)
