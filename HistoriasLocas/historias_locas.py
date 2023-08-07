# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con_______
# organizacion = "freecodecamp"
# print("Aprende a programar con  " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}")  # f-string

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo(plural): ")
madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verb1} problemas. ¡Aprende a {verb2} con tus amigos y alcanza tus {sustantivo_plural}"

print(madlib)
