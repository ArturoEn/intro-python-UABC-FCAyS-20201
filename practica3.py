class Estudiante:
  # Indicamos atributos para clase
  edad = 0
  carrera = "Desconocida"
  universidad = "Desconocida"
  genero = "Femenino"
  
  # Definimos una funcion para festejar
  def festejar(self):
    print ("Festejando")
  
  def estudiar(self, materia):
    print ("Estudiando" + materia)
  
  def llorar(self):
    print ("llorando...")
  
  def dormir(self):
    print ("Durmiendo...")
  
  # Ajustamos edad
  def cambiarEdad(self, edadAlumno):
    self.edad = edadAlumno
    print ("Nueva edad", edadAlumno)
  
# Generamos un nuevo Estudiante
miguel = Estudiante()
miguel.estudiar (" Logica para programacion")
# Imprimimos atributo del objeto
miguel.cambiarEdad(21)
  
