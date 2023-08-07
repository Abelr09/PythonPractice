import random


def adivina_el_numero_computadora(x):
    print(
        f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo.! (●'◡'●)"
    )

    # definir limites [1, x]
    inferior = 1
    superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar una prediccion
        if inferior != superior:
            prediccion = random.randint(inferior, superior)
        else:
            prediccion = inferior  # podria ser tambier el limite superior

        # Obtener una respuesta del usuario
        respuesta = input(
            f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A).Si es muy baja. ingresa (B). Si es correcta, ingresa (C): "
        ).lower()

        # Pedimos al usuario que nos diga si la respuesta es Alta, Baja o Correcta
        if respuesta == "a":
            superior = prediccion - 1
        elif respuesta == "b":
            inferior = prediccion + 1

    print(
        f"¡Siii!! La computadora adivino tu numero correctamente: {prediccion} ╰(*°▽°*)╯"
    )


adivina_el_numero_computadora(10)
