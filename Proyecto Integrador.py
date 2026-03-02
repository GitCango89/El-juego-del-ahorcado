# Proyecto Integrador Final
# Nombre: David Cango
# Tema: Impacto de las nuevas tecnologías en la sociedad
# Fecha: (01 de marzo de 2026)

import random

# Diccionario con tecnologías y su impacto

tecnologias = {
    "inteligencia artificial": "Puede mejorar la productividad y automatizar procesos.",
    "robotica": "Optimiza trabajos industriales pero puede reemplazar empleos.",
    "blockchain": "Aumenta la seguridad en transacciones digitales.",
    "realidad virtual": "Transforma la educación y el entretenimiento.",
    "ciberseguridad": "Protege la información en la era digital."
}

# Función principal del juego
def jugar_ahorcado():
    palabra = random.choice(list(tecnologias.keys()))
    letras_adivinadas = []
    intentos = 6

    print("=== JUEGO DEL AHORCADO ===")
    print("Tema: Tecnologías del Futuro\n")

    while intentos > 0:
        progreso = ""

        for letra in palabra:
            if letra in letras_adivinadas:
                progreso += letra + " "
            elif letra == " ":
                progreso += "  "
            else:
                progreso += "_ "

        print("\nPalabra:", progreso)

        if "_" not in progreso:
            print("\n¡Felicidades! Adivinaste la tecnología.")
            print("Impacto en la sociedad:")
            print(tecnologias[palabra])
            return

        letra_usuario = input("Ingresa una letra: ").lower()

        if letra_usuario in palabra:
            letras_adivinadas.append(letra_usuario)
        else:
            intentos -= 1
            print("Incorrecto. Intentos restantes:", intentos)

    print("\nPerdiste. La palabra era:", palabra)
    print("Reflexión:")
    print(tecnologias[palabra])


# Llamado de la función principal
jugar_ahorcado()
