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

from funciones import cargar_matriz, mostrar_matriz, modificar_matriz

def menu():
    """Muestra el menú de opciones y devuelve la opción seleccionada."""
    print("\nMenú de opciones:")
    print("1. Cargar datos de los jugadores")
    print("2. Mostrar matriz de jugadores")
    print("3. Modificar datos de un jugador")
    print("4. Salir")
    return int(input("Seleccione una opción: "))

def main():
    
    matriz = [[None] * 5 for _ in range(11)]
    
    while True:
        opcion = menu()
        match opcion:
            case 1:
                cargar_matriz(matriz)
            case 2:
                mostrar_matriz(matriz)
            case 3:
                modificar_matriz(matriz)
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

