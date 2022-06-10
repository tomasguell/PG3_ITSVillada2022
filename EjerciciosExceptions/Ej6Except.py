import mysql.connector

texto = mysql.connector.connect(
    user="bdi", password="pepe1234", host="127.0.0.1", database="ejercicio2"
)
escribir = texto.cursor()
try:
    crearmedico = "insert into Empleados " "(dni, nombre, apellido)" "VALUES (%s, %s, %s)"
    cargardatosmedico = (46450514, "asd", "asd")
    escribir.execute(crearmedico, cargardatosmedico)
    texto.commit()
except mysql.connector.Error:
    print(" No se pudo ingresar ese dato, debido a que ya existe")
escribir.close()
texto.close()