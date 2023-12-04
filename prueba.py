class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
    def es_posicion_valida(self, posicion):
        return (posicion[0] >= 0 and posicion[0] < len(self.mapa) and
                posicion[1] >= 0 and posicion[1] < len(self.mapa[0]))
    def es_posicion_final(self, posicion):
        return posicion == self.posicion_final
    def obtener_vecinos(self, posicion):
        vecinos = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            vecino = (posicion[0] + dx, posicion[1] + dy)
            if self.es_posicion_valida(vecino) and self.mapa[vecino[0]][vecino[1]] != '#':
                vecinos.append(vecino)
        return vecinos
    def buscar_camino(self):
        visitados = set()
        frontera = [self.posicion_inicial]
        while frontera:
            posicion = frontera.pop(0)
            if posicion not in visitados:
                visitados.add(posicion)
                if self.es_posicion_final(posicion):
                    return True
                for vecino in self.obtener_vecinos(posicion):
                    frontera.append(vecino)
        return False
    def __str__(self):
        mapa_str = ''
        for fila in self.mapa:
            mapa_str += ''.join(fila) + '\n'
        return mapa_str
def main():
    mapa = [['#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#']]
    posicion_inicial = (1, 1)
    posicion_final = (3, 3)
    juego = Juego(mapa, posicion_inicial, posicion_final)

import os
import random
class JuegoArchivo(Juego):
    def __init__(self):
        path_a_mapas = "path/to/maps"
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = f"{path_a_mapas}/{nombre_archivo}"
        with open(path_completo, "r") as f:
            mapa_str = f.read()
        mapa_str = mapa_str.strip()
        mapa = []
        for fila in mapa_str.split("\n"):
            mapa.append(list(fila))
        posicion_inicial = tuple(map(int, mapa_str.split("\n")[0].split(" ")))
        posicion_final = tuple(map(int, mapa_str.split("\n")[1].split(" ")))
        super().__init__(mapa, posicion_inicial, posicion_final)
import os
import random

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.mapa = self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        lista_archivos = os.listdir(self.path_a_mapas)
        if not lista_archivos:
            raise Exception("No se encontraron archivos de mapas en el directorio especificado.")

        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo_mapa:
            mapa_data = archivo_mapa.read()
        
        return self.procesar_mapa(mapa_data)

    def procesar_mapa(self, mapa_data):
        lineas_mapa = mapa_data.strip().split('\n')
        
        # La primera línea debe contener las dimensiones del mapa y las coordenadas de inicio y fin.
        dimensiones, inicio, fin = lineas_mapa[0].split(',')
        dimensiones = tuple(map(int, dimensiones.split()))
        inicio = tuple(map(int, inicio.split()))
        fin = tuple(map(int, fin.split()))

        # Las líneas restantes contienen el mapa en sí.
        mapa = '\n'.join(lineas_mapa[1:])
        
        return dimensiones, inicio, fin, mapa
jugar=JuegoArchivo(Juego)       