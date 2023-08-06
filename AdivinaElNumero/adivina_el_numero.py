import random


def adivina_el_numero(x):
    print("(*/ω＼*)============================(*/ω＼*)")
    print("       ¡¡Bienvenido(a) al Juego!!")
    print("^_^ ================================ ^_^")
    print("Tu meta es adivinar el numero generado por el juego!")

    numero_aleatorio = random.randint(1, x)  # Numero aleatorio entre 1 y x.

    prediccion = 0

    # Repetimos una secuencia de numeros repetidas veces hasta que el usuario acierte
    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))  # f-string

        if prediccion < numero_aleatorio:
            print("Intenta de nuevo. Este numero es muy pequeño. (╯°□°）╯")
        elif prediccion > numero_aleatorio:
            print("Intenta de nuevo. Este numero es muy grande.(╯°□°）╯")
    print(
        f"¡Felicitaciones! adivinaste el numero {numero_aleatorio} correctamente. ╰(*°▽°*)╯"
    )


adivina_el_numero(10)
