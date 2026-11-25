# game_logic.py - Tres en raya
# Aqui se traduce DF2 (validacion de la jugada) y DF3 (fin de la partida)
# Requisitos que cubre: RF-03, RF-04, RF-05, RF-06 y RF-07
# Jugador 1 = X y Jugador 2 = O
# El tablero son las variables c1 a c9 como en RAPTOR
# Una casilla libre guarda su propio numero ("1" a "9")

# ---------------------------------------------------------------
# DF2 - VALIDACION DE LA JUGADA (RF-03, RF-04 y RF-05)
# ---------------------------------------------------------------

# Estado de ejemplo (se asigna al inicio como en RAPTOR)
# Es un tablero casi ganado: si el jugador 1 elige la casilla 3, gana
# Otros estados para probar (cambiar c1 a c9 y turno):
#   Gana J2:  turno = 2 y tablero O O 3 / X X 6 / X 8 9 (elegir la 3)
#   Empate:   turno = 1 y tablero X O X / X O O / O X 9 (elegir la 9)
#   Continua: dejar este tablero y elegir otra casilla libre (ej. la 9)
c1 = "X"
c2 = "X"
c3 = "3"
c4 = "O"
c5 = "O"
c6 = "6"
c7 = "7"
c8 = "8"
c9 = "9"
turno = 1    # para probar al jugador 2 cambiar este 1 por un 2

# Se decide la marca segun el turno (RF-03)
if turno == 1:
    marca = "X"
else:
    marca = "O"

print("Tablero actual")
print(c1, "|", c2, "|", c3)
print(c4, "|", c5, "|", c6)
print(c7, "|", c8, "|", c9)

# Se repite mientras la jugada sea invalida (RF-04)
jugada_valida = False
while not jugada_valida:
    jugada = input("Turno del jugador " + str(turno) + " |" + marca
                   + "| Elige una casilla (1-9): ")

    # Validacion por formato: solo numeros enteros
    if not jugada.isdecimal():
        print("Error: Entrada invalida, ingresa un numero del 1 al 9")
    else:
        numero = int(jugada)

        # Validacion por rango: de 1 a 9
        if numero < 1 or numero > 9:
            print("Error: Entrada invalida, ingresa un numero del 1 al 9")
        else:
            # Validacion por las reglas: la casilla debe estar libre
            if numero == 1:
                contenido = c1
            elif numero == 2:
                contenido = c2
            elif numero == 3:
                contenido = c3
            elif numero == 4:
                contenido = c4
            elif numero == 5:
                contenido = c5
            elif numero == 6:
                contenido = c6
            elif numero == 7:
                contenido = c7
            elif numero == 8:
                contenido = c8
            else:
                contenido = c9

            if contenido != str(numero):
                print("Error: la casilla " + str(numero)
                      + " ya esta ocupada intenta de nuevo")
            else:
                jugada_valida = True

# Jugada valida: se guarda la marca en la casilla (RF-05)
if numero == 1:
    c1 = marca
elif numero == 2:
    c2 = marca
elif numero == 3:
    c3 = marca
elif numero == 4:
    c4 = marca
elif numero == 5:
    c5 = marca
elif numero == 6:
    c6 = marca
elif numero == 7:
    c7 = marca
elif numero == 8:
    c8 = marca
else:
    c9 = marca

print("Tablero actual")
print(c1, "|", c2, "|", c3)
print(c4, "|", c5, "|", c6)
print(c7, "|", c8, "|", c9)

# ---------------------------------------------------------------
# DF3 - FIN DE LA PARTIDA (RF-06 y RF-07)
# Hay 4 resultados: gana el jugador 1, gana el jugador 2,
# empate o la partida continua
# ---------------------------------------------------------------

# Aqui NO se vuelve a asignar el tablero: DF3 revisa el tablero que
# quedo despues de la jugada de DF2

# Se revisan las 8 lineas: 3 filas, 3 columnas y 2 diagonales (RF-06)
# ganador: 0 = nadie, 1 = jugador 1 (X), 2 = jugador 2 (O)
ganador = 0

# Filas
if c1 == c2 and c2 == c3:
    if c1 == "X":
        ganador = 1
    elif c1 == "O":
        ganador = 2
if c4 == c5 and c5 == c6:
    if c4 == "X":
        ganador = 1
    elif c4 == "O":
        ganador = 2
if c7 == c8 and c8 == c9:
    if c7 == "X":
        ganador = 1
    elif c7 == "O":
        ganador = 2

# Columnas
if c1 == c4 and c4 == c7:
    if c1 == "X":
        ganador = 1
    elif c1 == "O":
        ganador = 2
if c2 == c5 and c5 == c8:
    if c2 == "X":
        ganador = 1
    elif c2 == "O":
        ganador = 2
if c3 == c6 and c6 == c9:
    if c3 == "X":
        ganador = 1
    elif c3 == "O":
        ganador = 2

# Diagonales
if c1 == c5 and c5 == c9:
    if c1 == "X":
        ganador = 1
    elif c1 == "O":
        ganador = 2
if c3 == c5 and c5 == c7:
    if c3 == "X":
        ganador = 1
    elif c3 == "O":
        ganador = 2

# Se cuentan las casillas ocupadas para saber si el tablero esta lleno (RF-07)
ocupadas = 0
if c1 == "X" or c1 == "O":
    ocupadas = ocupadas + 1
if c2 == "X" or c2 == "O":
    ocupadas = ocupadas + 1
if c3 == "X" or c3 == "O":
    ocupadas = ocupadas + 1
if c4 == "X" or c4 == "O":
    ocupadas = ocupadas + 1
if c5 == "X" or c5 == "O":
    ocupadas = ocupadas + 1
if c6 == "X" or c6 == "O":
    ocupadas = ocupadas + 1
if c7 == "X" or c7 == "O":
    ocupadas = ocupadas + 1
if c8 == "X" or c8 == "O":
    ocupadas = ocupadas + 1
if c9 == "X" or c9 == "O":
    ocupadas = ocupadas + 1

# Resultado final: los 4 casos
if ganador == 1:
    print("Felicidades! El jugador 1 (X) ha Ganado la partida")
elif ganador == 2:
    print("Felicidades! El jugador 2 (O) ha Ganado la partida")
elif ocupadas == 9:
    print("El tablero esta lleno! Es un empate")
else:
    print("La partida continua")
