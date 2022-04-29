"""5) (HERENCIA) Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como
responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo
sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado"""


class Persona(object):
    def __init__(self):
        self.nombre = input("ingrese el nombre")
        self.edad = input("Ingrese la edad")
        print(
            "ACABA DE INICIALIZAR UNA PERSONA DE NOMBRE: ",
            self.nombre,
            "CON LA EDAD DE: ",
            self.edad,
        )


class Empleado(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.sueldo = float(input("ingrese su sueldo"))
        print(
            "ACABA DE INICIALIZAR UN EMPLEADO DE NOMBRE: ",
            self.nombre,
            "CON LA EDAD DE: ",
            self.edad,
            "Y EL SUELDO DE",
            self.sueldo,
        )
        self.Impuestos()

    def Impuestos(self):
        if self.sueldo > 3000:
            print("debe pagar sus impuestos")

        else:
            print("no debe pagar impuestos")


empleado1 = Empleado()
