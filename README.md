# Tres en Raya

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [B]

Juego por turnos para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

## Integrantes

- Aaron Rivera
- Emilio Castillo
- Andrés Ipiales

## Cómo ejecutarlo

```bash
python juego.py
python game_logic.py     


## Estructura del repositorio

| Archivo | Qué hace | Estado |

| `juego.py` | [Menú que se repite hasta elegir la opción "salir"] | [Iniciado] |
| `game_logic.py` | [Validá las jugadas en el tablero (DF2) y procesa los datos para dar a un ganador,perdedor o empate, finalizando así la partida (DF3)] | [ Iniciado] |
| `server.py` | [El Jugador 1 sera anfitrión y proporcionara el modo local y multijugador al cliente] | [Pendiente] |
| `client.py` | [Permite al Jugador 2 usar el modo local o multijugador en la Red Lan] | [Pendiente] |
| `diseno/` | Diagramas `.rap` de la Fase 2 | [Subido] |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú) | [`juego.py`, 12-28 ] | [En el menú se implemento while para que la consola solo saliera del bucle al momento de elegir "salir" ] |
| DF2 Validación de la jugada | [`game_logic.py`, 21-102] | [Se asigno una casillas predeterminadas del c1-c9 simulando una partida en curso al igual que en Raptor, logrando un ciclo de validacion con while not jugada_valida, .isdecimal en el rango 1-9 para validar la casilla libre ] |
| DF3 Fin de la partida | [`game_logic.py`, 104-186] | [Para que el programa determine si continuar la partida o finalizarla con el resultado obtenido, se valida las 8 posibles líneas ganadoras y conteo de casillas ocupadas] |

## Video explicativo

[Enlace al video] (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo
tradujimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia [MIT]. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos
citados en la sección «Créditos».

## Créditos

| Lenguaje Python 3 (solo biblioteca estándar, sin librerías externas) | Python Software Foundation, python.org | Para ejecutar `juego.py` y `game_logic.py` | PSF License |
| Código de terceros | Ninguno | — | — |
| Imágenes, sonidos u otros recursos visuales | Ninguno (interfaz de consola) | — | — |

### Uso de IA

<!-- Si no usaron IA, escriban: «No se usaron herramientas de IA». -->

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |

| [Gemini] | [Correciones al momento de redactar el código y organizar de forma correcta el README.MD ] | [Cambiamos información adicional y especificamos de una forma más práctica y precisa el repositorio] |
| [ Claude Anthropic] | [Nos ayudo a comprobar  la traducción y opciones al momento de pasar a código Python en el DF2 y DF3 sean identicos al Raptor de la fase 2 ] | [Comprobados salidas y entradas al momento de validar el menú, lógica y fin de la partida, tomando en cuenta siempre la fase 2 de nuestros Raptors] |
