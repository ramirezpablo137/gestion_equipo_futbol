""" 󰳕 Desafío: Gestionar el Equipo de Fútbol Argentino 󰳕
Historia:
Tu tarea es gestionar el equipo titular el próximo partido. El equipo tiene una matriz de jugadores
organizada en 11 filas (representando a los titulares del próximo partido) y 5 columnas (Nombre,
Apellido, posición en la que juega, cantidad de goles en el torneo). Necesitamos que puedas:
1. Cargar los datos de los jugadores en la matriz (nombre, edad, goles, etc).
2. Mostrar la matriz con la información de todos los jugadores.
3. Modificar un jugador: Cambiar la información de un jugador seleccionando su fila y
columna.
Objetivos del programa:
1. Menú con las siguientes opciones:
○ 1. Pedir datos para cargar la matriz: Ingresar los datos de los jugadores (nombre,
edad, goles) para cada celda de la matriz.
○ 2. Mostrar matriz: Ver la matriz con la información de todos los jugadores.
○ 3. Modificar matriz: Mostrar la matriz, pedir la fila y columna a modificar, y luego
ingresar el nuevo dato.
○ 4. Salir: Finalizar el programa.
Requisitos técnicos:
● Usar matrices (arrays bidimensionales).
● Usar ciclos para recorrer la matriz.
● Usar funciones y separarlas en un archivo aparte, importando desde el main.
● Implementar un menú con opciones para interactuar con el usuario.
● Para la modificación, mostrar la matriz y pedir al usuario que ingrese la fila y columna a
modificar, luego el nuevo dato. """

def cargar_matriz(matriz):
    for i in range(len(matriz)):
        print(f"\nJugador #{i + 1}:")
        matriz[i][0] = input("Nombre: ")
        matriz[i][1] = input("Apellido: ")
        matriz[i][2] = input("Posición: ")
        matriz[i][3] = int(input("Cantidad de goles: "))
        matriz[i][4] = int(input("Edad: "))

def mostrar_matriz(matriz):
    if matriz == [[None] * len(matriz[0]) for _ in range(len(matriz))]:
        print("La matriz está vacía. Cargue los datos primero.")
        return
    print("\nMatriz de jugadores:")
    print("Fila | Nombre | Apellido | Posición | Goles | Edad")
    print("-" * 60)
    for i, fila in enumerate(matriz):
        print(f"{i + 1:>4} | " + " | ".join(f"{str(celda):<12}" for celda in fila))

def modificar_matriz(matriz):
    if matriz == [[None] * len(matriz[0]) for _ in range(len(matriz))]:
        print("La matriz está vacía. Cargue los datos primero.")
        return
    mostrar_matriz(matriz)
    try:
        fila = int(input("\nIngrese el número de fila del jugador a modificar (1-11): ")) - 1
        columna = int(input("Ingrese el número de columna a modificar (1-5): ")) - 1
        if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
            nuevo_valor = input("Ingrese el nuevo valor: ")
            matriz[fila][columna] = int(nuevo_valor) if columna in [3, 4] else nuevo_valor
            print("Dato modificado correctamente.")
        else:
            print("Fila o columna fuera de rango.")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")


