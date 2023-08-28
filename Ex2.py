class Forma:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Retangulo(Forma):
    def calcular_area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def calcular_area(self):
        return 0.5 * self.largura * self.altura
