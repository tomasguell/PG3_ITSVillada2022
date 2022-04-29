"""4) Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e
inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de
la clase Operación y llamarlos desde el mismo método __init__"""


class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.Ops()

    def Ops(self):
        print("suma, ", self.num1 + self.num2)
        print("resta, ", self.num1 - self.num2)
        print("multiplicacion, ", self.num1 * self.num2)
        print("division, ", self.num1 / self.num2)


numeros1 = Operaciones(100, 10)
