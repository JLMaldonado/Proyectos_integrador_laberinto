print("==========================================")
print("Bienvenido al Juego de laberinto")
print("============================================")

nombre=input("Ingresa tu nombre de usuario por favor: ")

print(f"Bienvenido al Juego {nombre} Que disfrutes")

from readchar import readkey, key

import keyboard
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