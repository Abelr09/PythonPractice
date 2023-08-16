# Diccionario

# lenguaje = {"nombre": "Abel", "Apellido": "aMARILLA"}
# print(lenguaje)

# a = 10
# b = 5
# c = 1
# b = 2

# if a < b:
#     print("A  es menor que b")
# elif a == b:
#     print("A es igual a b")
# else:
#     print("A es menor que b")

# if type(a) is bool:
#     print("A es verdadero")
# else:
#     print("A es falso")

# if a > b or b < c:
#     print("Las dos condiciones son verdaderas")

# For
# Itera letra por letra en el str
# for letra in "texto":
#     print(letra)

# Itera cada elemento de la lista con la condicion de que corte el ciclo en el elemento java
# lenguajes = ["python", "java", "golang"]
# for elemento in lenguajes:
#     print(elemento)
#     if elemento == "java":
#         break

# Se salta el ciclo
# lenguajes = ["python", "java", "golang"]
# for elemento in lenguajes:
#     if elemento == "java":
#         continue
#     print(elemento)

# for element in range(1, 5):
#     print(element)

# Ciclo While

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break

# Iterando sobre una lista

# lenguajes = ["Python", "java", "golang"]
# for elemento in lenguajes:
#     print(elemento)

# Combinando las funciones range y len
# lenguajes = ["Python", "java", "golang"]

# for index in range(len(lenguajes)):
#     print("Indice", index)
#     print("elemento", lenguajes[index])

# i = 0
# while i < len(lenguajes):
#     print(lenguajes[i])
#     i += 1

# iterando diccionarios
# lenguaje = {"Nombre": "Python", "creador": "Guido Van Rossum"}

# for llave in lenguaje:
#     print("Llave:", llave)
#     print("Valor:", lenguaje[llave])

# Usando las funciones keys, values e items
# for llave in lenguaje.keys():
#     print(llave)

# for valor in lenguaje.values():
#     print(valor)

# for llave, valor in lenguaje.items():
#     print(llave, valor)

# x = 0
# y = 0
# z = 50

# while x < z:
#     x = y * 15
#     print(x)
#     y += 2

# print("fin de instrucción while")

# Tabla de multiplicar del 4, del 0 al 10
# x = 4
# y = 0
# for y in range(11):
#     print(x, " x ", y, " = ", x * y)

# Funciones
# Bloque de codigo
# Contienen instrucciones relacionadas entre si
# Permiten organizar el codigo en partes pequeñas
# Permite organizacion y codigo legible
# Evita la repeticion de instrucciones y permite reutilizarlo

# APELLIDO = "Pinto"


# def funcion():
#     print("Mi primera funcion")
#     nombre = "Abel"
#     print(nombre, APELLIDO)


# funcion()

# Calcular el perimetro de un cuadrado:
# def perimetro_cuadrado(lado, unidades):
#     perimetro = lado * 4
#     print(f"El perimetro es {perimetro}{unidades}")


# perimetro_cuadrado(25, " metros")
# perimetro_cuadrado(lado=25, unidades="metros")


# return
# def calcular_cuadrado(lado):
#     perimetro = lado * 4
#     area = lado * lado
#     return area, perimetro


# resultado = calcular_cuadrado(lado=5)
# print(resultado)
# print(f"Area: {area}, Perimetro: {perimetro}")

# DocString


# def perimetro_cuadrado(lado):
# """Calcular el perimetro de un cuadrado

# Esta funcion recibe el valor de un lado de un cuadrado
# y a partir de este calcula y retorna su perimetro

# Args:
#     lado (int): medida del lado del cuadrado
# Returns:
#     perimetro (int): perimetro del cuadrado
# """

#     perimetro = lado * 4
#     return perimetro


# perimetro_cuadrado(lado=5)


# def mensaje(men):
#     y = ""
#     for x in men:
#         y = y + x
#         print(y)


# mensaje("Hola")

# Modulos ###

# import datetime #Esta libreria permite manipular fechas y horas

# hora_actual = datetime.datetime.now()
# print(hora_actual)

# import datetime as dt

# hora_actual = dt.datetime.now() #Con as le asignamos un alias
# print(hora_actual)

# from datetime import datetime #de esta manera se importan submodulos del modulo

# hora_actual = datetime.now()
# print(hora_actual)

# Creando mi propio modulo
# from cuadrado import area_cuadrado, perimetro_cuadrado

# lado = 5
# cuadrado = {
#     "lado": lado,
#     "area": area_cuadrado(lado),
#     "perimetro": perimetro_cuadrado(lado),
# }
# print(cuadrado)
# perimetro = perimetro_cuadrado(lado)
# print(perimetro)

# Paquetes
