class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer (self):
        print(f"{self.nombre} está comiendo su comida davorita")

    def maullar (self):
        print(f"{self.nombre} dice: ¡Miau, miau!")

    def saltar (self):
        print(f"{self.nombre} está saltando en el árbol más alto")
    
    def presentarse (self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
        
        
if __name__ == "__main__":
    mi_gato = Gato("Paco", 3)
    mi_gato.presentarse()
    mi_gato.comer()
    mi_gato.maullar()
    mi_gato.saltar()