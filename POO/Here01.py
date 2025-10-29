class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def comer(self):
        print(f"{self.nombre} está comiendo su comida favorita.")

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def caminar(self):
        print(f"{self.nombre} está caminando silenciosamente.")

perro = Perro("Pancho", 4)
gato = Gato("Paco", 3)

perro.presentar()
perro.comer()

gato.presentar()
gato.caminar()
