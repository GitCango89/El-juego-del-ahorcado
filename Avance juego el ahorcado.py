# Juego del Ahorcado - Avance de desarrollo
# Autor: David Sebastián Cango Zhunaula
# Materia: Lógica de programación
# Este programa permite adivinar una palabra letra por letra

palabra = "uide"  # palabra secreta
letras_adivinadas = []
intentos = 6

print("BIENVENIDOS AL JUEGO DEL AHORCADO")

# Bucle principal del juego
while intentos > 0:

    # Mostrar progreso actual
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "

    print("\nPalabra:", progreso)

    # Verificar si ya ganó
    if "_" not in progreso:
        print("¡Ganaste! Adivinaste la palabra")
        break

    # Pedir letra al usuario
    intento = input("Ingresa una letra: ").lower()

    # Condicional para verificar la letra
    if intento in palabra:
        print("Letra correcta")
        letras_adivinadas.append(intento)
    else:
        print("Letra incorrecta")
        intentos -= 1
        print("Intentos restantes:", intentos)

# Resultado final si pierde
if intentos == 0:
    print("Perdiste. La palabra era:", palabra)
