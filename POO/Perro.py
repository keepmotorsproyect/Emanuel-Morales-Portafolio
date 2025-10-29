class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer (self):
        print(f"{self.nombre} está comiendo su comida davorita")

    def ladrar (self):
        print(f"{self.nombre} dice: ¡Guau, guau!")

    def presentarse (self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
        
if __name__ == "__main__":
    mi_perro = Perro("Pancho", 4)
    mi_perro.presentarse()
    mi_perro.comer()
    mi_perro.ladrar()