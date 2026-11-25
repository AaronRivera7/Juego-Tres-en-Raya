# Menú del juego Tres en raya
# Autor: Aaron Rivera


def mostrar_menu() -> None:
    # Imprime las opciones disponibles del menú principal
    print("\n=== TRES EN RAYA  ===")
    print("1. Jugar")
    print("2. Salir")


def ejecutar_menu() -> None:
    # Ejecuta el ciclo del menú hasta que se elija la opción Salir.
    opcion = ""
    while opcion != "2":
        mostrar_menu()
        opcion = input("Selecciona una opción (1-2): ").strip()

        if opcion == "1":
            # La partida completa con turnos se agrega en la Fase 4
            print(
                "Modo de juego en desarrollo (Fase 4). "
                "Revisa game_logic.py para probar validación y fin de partida."
            )
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta pronto!")
        else:
            print("Opción inválida. Ingresa 1 para Jugar o 2 para Salir.")


if __name__ == "__main__":
    ejecutar_menu()
