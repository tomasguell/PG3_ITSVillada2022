"""6)Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con los
nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus
hijos."""


class Familia:
    def __init__(self, hijos):
        self.Padre = input("Ingrese el nombre del Padre")
        self.Madre = input("Ingrese el nombre de la Madre")
        self.Hijos = hijos

    def __str__(self):
        StringLista = "".join([str(item) for item in self.Hijos])
        return (
            "\nPadre: "
            + self.Padre
            + "\nMadre: "
            + self.Madre
            + "\nHijos: "
            + StringLista
        )


familia1 = Familia(["Facu", "Tomi"])
print(familia1)
familia2 = Familia(["Franco", "agus", "Guada"])

print(familia2)
