class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse (self):
        print(f"Hola, soy {self.nombre}, me gusta el deporte y jugar con mis amigos. Tengo {self.edad}")
    
    def cumplir_años (self):
        self.edad += 1
        print(f"{self.nombre} cumple estos años este año: {self.edad}")


 
if __name__ == "__main__":
    Persona_1 = Persona ("Jorge", 16)
    Persona_2 = Persona ("Ema", 19)
    
    Persona_1.presentarse()
    Persona_2.presentarse()
    
    Persona_1.cumplir_años()
    Persona_2.cumplir_años()



        