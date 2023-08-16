# La programacion orientada a objetos nos permite simplificar los problemas que estamos trabajando,
# ya que nos permite representar y modelar cosas de la vida real
# Son elementos o instancias que se creana partir de clases
# Los objetos tienen atributos y codigos
# Tiene 4 pilares: Abstraccion, Encapsulamiento, Polimorfismo y Herencia

# pedro = Persona()
# print(type(pedro))


# paco = Persona()
# print(type(paco))


# print(pedro == paco)

# class Persona:
#     def __init__(self):
#         print("Estoy en el cisntructor")


# paco = Persona()


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # paco = Persona("Paco", 20)
    # print(paco.nombre)
    # print(paco.edad)
    # La variable self representa la instancia de la clase y atraves de ella se puede acceder
    # a las propiedades y funciones de la clase

    # Metodo cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")


# paco = Persona(nombre="paco", edad=20)
# paco.cumplir_anios()


# Herencia
class Empleado(Persona):
    def __init__(self, horas_totales, nombre, edad):
        super(Empleado, self).__init__(nombre, edad)
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")


paco = Empleado(nombre="Paco", edad=20, horas_totales=30)
paco.trabajar(horas_trabajadas=8)
paco.cumplir_anios()
