class Empleado:
    def __init__(self, nombre,salario,porcentaje):
        self._nombre = nombre
        self._salario = salario
        self.porcentaje = porcentaje    
    
    def presentar(self):
        print(f"Hola soy {self._nombre} y mi salario es de {self._salario}")

    def salario_final(self):
        print(f"Mi salario final es de {self._salario*self.porcentaje}")


if __name__ == "__main__":
    empleado= Empleado("Miguel", 1423500, (19/100))

    empleado.presentar()
    empleado.salario_final()