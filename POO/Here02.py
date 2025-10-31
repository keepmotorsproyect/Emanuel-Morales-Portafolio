class Figura:

    def __init__(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416
    def calcular_area(self):
        return self.pi * (self.radio ** 2)
    def calcular_perimetro(self):
        return 2 * self.pi * self.radio

class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 4, 3, 4, 5)

area_total = (
    circulo.calcular_area() +
    rectangulo.calcular_area() +
    triangulo.calcular_area()
)

print("Círculo:")
print("  Área =", (circulo.calcular_area(), 2))
print("  Perímetro =",(circulo.calcular_perimetro(), 2))
print()
print("Rectángulo:")
print("  Área =", (rectangulo.calcular_area(), 2))
print("  Perímetro =",(rectangulo.calcular_perimetro(), 2))
print()
print("Triángulo:")
print("  Área =", (triangulo.calcular_area(), 2))
print("  Perímetro =", (triangulo.calcular_perimetro(), 2))
print()
print("Área total de todas las figuras:",(area_total, 2))
