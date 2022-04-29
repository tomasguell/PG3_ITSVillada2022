"""2) Implementar una clase llamada Alumno que tenga 
como atributos su nombre y su nota. Definir los
métodos para inicializar sus atributos, imprimirlos 
y mostrar un mensaje si está regular 
(nota mayor o igual a Definir dos objetos de la clase Alumno."""

class Alumno:
    def inicializador(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(self.nombre, " Nota ", self.nota)

    def regularidad(self):
        if self.nota >= 6:
            print("el alumno ", self.nombre, " esta aprobado ")    
        else:
            print("el alumno ", self.nombre, " esta desaprobado ")           




persona1 = Alumno()
persona1.inicializador("Tomas", 8)
persona1.imprimir()
persona1.regularidad()   


persona2 = Alumno()
persona2.inicializador("Facundo", 4)
persona2.imprimir()    
persona2.regularidad()        