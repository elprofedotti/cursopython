class Alumno():
    
    def __str__(self):
        return "ALumno: {}, su nota es {}".format( self._nombre, self._nota )
    
    def setNota(self, nota):
        self._nota=nota

    def setNombre(self, nombre):
        self._nombre=nombre

    def getNota(self):
        print("Nota: ",self._nota)
        if self.estado()==True:
            print("Aprobado")
        else: print("Desaprobado")

    
    def getNombre(self):
        print("Nombre: ",self._nombre)
    
    def estado(self):
        if self._nota>6:
            return True
        else: return False

alumno = Alumno()
alumno.setNombre(input("Ingresa el nombre del alumno: "))
alumno.setNota(int(input ("Ingresa la nota: ")))
alumno.getNombre()
alumno.getNota()


