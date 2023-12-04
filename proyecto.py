from readchar import readkey, key
from typing import List, Tuple

print("==========================================")
print("Bienvenido al Juego de laberinto")
print("============================================")

nombre=input("Ingresa tu nombre de usuario por favor: ")

print(f"Bienvenido al Juego {nombre} Que disfrutes")


print("======================================")
print("Lector de teclas por teclado")
print("======================================")
print("Presiona la tecla (↑ para salir):")

while True:
    k=readkey()

    if k==key.UP :
        break
    print(f"Tecla presionada: {k}")

print("fin")
import os
def borrar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')
#funcion para borrar terminal
numero=0

while numero <=50 :
    borrar_terminal()
    
    print(f"Presiona ( n ) para imprimir un nuevo numero, limite (50) Número: {numero}")
    entrada = readkey()

    if entrada == "n" :
            numero += 1
