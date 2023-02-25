class Alumno():
    _nombre=""
    _nota=0
    _estado=False
    def __str__(self):
        return "ALumno: {}, su nota es {}".format( self._nombre, self._nota )
    
    def setNota(self, nota):
        self._nota=nota
        if self._nota>6:
            self._estado=True

    def setNombre(self, nombre):
        self._nombre=nombre

    def getNota(self):
        #print("Nota: ",self._nota)
        """ if self.estado()==True:
            print("Aprobado")
        else: print("Desaprobado") """
        return self._nota

    
    def getNombre(self):
        #print("Nombre: ",self._nombre)
        return self._nombre
    
    def isEstado(self):
        return self._estado
    
    """ def estado(self):
        if self._nota>6:
            return True
        else: return False """

alumno = Alumno()
alumno.setNombre(input("Ingresa el nombre del alumno: "))
alumno.setNota(int(input ("Ingresa la nota: ")))
print("Nombre: {}".format(alumno.getNombre()))
print("Nota: {}".format(alumno.getNota()))
if alumno.isEstado():
    print("Esta APROBADO")
else: print("Esta DESAPROBADO")



