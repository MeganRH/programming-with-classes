import time
import pyfiglet
title = pyfiglet.figlet_format("TIC-TAC-TOE")
print(title)

tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def dibujar_tablero(tablero):
    print(" %c | %c | %c " % (tablero[0], tablero[1], tablero[2]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[3], tablero[4], tablero[5]))
    print("---+---+---")
    print(" %c | %c | %c " % (tablero[6], tablero[7], tablero[8]))


def estado_del_juego(tablero):
    ## Revisar las lineas horizontales
    if (tablero[0] == tablero[1] == tablero[2] != ' '):
        estado_actual = "WINNER"
    elif (tablero[3] == tablero[4] == tablero[5] != ' '):
        estado_actual = "WINNER"
    elif (tablero[6] == tablero[7] == tablero[8] != ' '):
        estado_actual = "WINNER"

    ## Revisar las lineas verticales
    elif (tablero[0] == tablero[3] == tablero[6] != ' '):
        estado_actual = "WINNER"
    elif (tablero[1] == tablero[4] == tablero[7] != ' '):
        estado_actual = "WINNER"
    elif (tablero[2] == tablero[5] == tablero[6] != ' '):
        estado_actual = "WINNER"

    ## Revisar las lineas diagonales
    elif (tablero[0] == tablero[4] == tablero[8] != ' '):
        estado_actual = "WINNER"
    elif (tablero[6] == tablero[4] == tablero[2] != ' '):
        estado_actual = "WINNER"
    else:
        estado_actual = "Playing"

    return estado_actual

## Constantes iniciales


if __name__ == "__main__":
    jugador_actual = "X"
    estado_actual = "Playing"
    turno = 1

    print("LET'S PLAY")
    print("Here's the board")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Player X starts:")

    while(True):

        print("Player %s turn" % jugador_actual)
        poscion = int(input("Choose which position want to take(1-9):")) - 1

        if poscion >= 0 or poscion <= 9:

            if tablero[poscion] != " ":
                print(
                    "The position %s is already taken, please choose another" % str(poscion))
                continue
            else:
                tablero[poscion] = jugador_actual
                turno = turno + 1
        else:
            print("Invalid position")
            continue

        dibujar_tablero(tablero)

        estado_actual = estado_del_juego(tablero)

        if estado_actual == "Playing":

            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"
        else:
            print("PLAYER %s WINS" % jugador_actual)
            break

        if turno >= 9:
            print("Sorry NO more available boxes, IT'S A TIE!")
            break
#MEGANRIVEROCODE
