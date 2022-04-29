class Triangulo:
    def incializar(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.lista = [self.l1, self.l2, self.l3]
        print("ACABA DE INICIALIZAR UN TRIANGULO CON DIMENCIONES: ", self.lista)

    def printMaxNumber(self):

        print("el lado mas grande es de ", max(self.lista))

    def equilateridad(self):
        if self.l1 == self.l2 and self.l2 == self.l3:
            print(" es un triangulo equilatero ")

        else:
            print("no es un triangulo equilatero")


Triangulo1 = Triangulo()
Triangulo1.incializar(15, 3, 18)
Triangulo1.printMaxNumber()
Triangulo1.equilateridad()

Triangulo2 = Triangulo()
Triangulo2.incializar(15, 15, 15)
Triangulo2.printMaxNumber()
Triangulo2.equilateridad()
