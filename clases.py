from readchar import readkey, key
from typing import List, Tuple
import os 
import random
class Juego:
    def __init__(self, laberinto_str: str, inicio: Tuple[int, int], final: Tuple[int, int], nombre: str):
        self.laberinto = self.convertir_laberinto(laberinto_str)
        self.inicio = inicio
        self.final = final
        self.nombre = nombre

    # Función para convertir el laberinto en cadena en una matriz de caracteres
    def convertir_laberinto(self, laberinto_str: str) -> List[List[str]]:
        lineas = laberinto_str.strip().split("\n")
        laberinto = [list(linea) for linea in lineas]
        return laberinto

    # Función para limpiar la pantalla y mostrar el mapa
    def mostrar_laberinto(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla en Windows 
        for fila in self.laberinto:
            print("".join(fila))

    # Función para el bucle principal del juego
    def main_loop(self):
        px, py = self.inicio  # Coordenadas del jugador
        self.laberinto[px][py] = 'P'  # Posición inicial del jugador

        while (px, py) != self.final:
            
            self.mostrar_laberinto()
            print("==========================================")
            print(f"========= Juego de laberinto --- Jugador {self.nombre}--- ==============")
            print("==========================================")
            print("--Presiona w (arriba) , s (abajo) , d (derecha), a (izquierda)-- ")
            tecla = readkey() if os.name == 'nt' else input()
            if self.final == (19,27):
                print(f"----------------------------------------------------")
                print(f"--------------!!Ganaste!! {self.nombre} ---------------------")
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
            if 0 <= nueva_px < len(self.laberinto) and 0 <= nueva_py < len(self.laberinto[0]) and self.laberinto[nueva_px][nueva_py] != '#':
                self.laberinto[nueva_px][nueva_py] = 'P'
                self.laberinto[px][py] = '.'
                px, py = nueva_px, nueva_py
if __name__ == "__main__":
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


"""  # Replace with the actual laberinto string
    inicio = (0, 0)  # Replace with the actual starting position
    final = (19, 27)  # Replace with the actual ending position
    nombre = "..."  # Replace with the actual player name

    juego = Juego(laberinto_str, inicio, final, nombre)
    juego.main_loop()
class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas: str, nombre: str):
        self.path_a_mapas = path_a_mapas
        self.nombre = nombre
        self.laberinto, self.inicio, self.final = self.leer_mapa()

    def leer_mapa(self):
        archivos = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = f"{self.path_a_mapas}/{nombre_archivo}"
        with open(path_completo, "r") as archivo:
            lineas = archivo.readlines()
            inicio = tuple(map(int, lineas[0].strip().split()))
            final = tuple(map(int, lineas[1].strip().split()))
            laberinto = [list(linea.strip()) for linea in lineas[2:]]
            return laberinto, inicio, final

if __name__ == "__main__":
    path_a_mapas = "map1.txt"  # Replace with the actual path to the map files
    nombre = "map1.txt"  # Replace with the actual player name

    juego = JuegoArchivo(path_a_mapas, nombre)
    juego.main_loop()