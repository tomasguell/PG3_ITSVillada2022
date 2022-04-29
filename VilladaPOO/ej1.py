class Persona:
    def inicializador(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre)


persona1 = Persona()
persona1.inicializador("Tomas")
persona1.imprimir()


persona2 = Persona()
persona2.inicializador("Facundo")
persona2.imprimir()
