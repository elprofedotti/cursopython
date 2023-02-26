import sqlite3 as sq
import pprint as pp

def main():
    conn=sq.connect("miaplicacion.db")
    cursor=conn.cursor()
    #cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

    print("Cargue de alumnos")
    while True:
        
        id=input("id: ")
        nom=input("nombre: ")
        ape=input("apellido: ")
        crearAlumno(id,nom,ape, cursor)
        if input("Cargar otro? SI/NO:")=="SI":continue
        else:break
    
    conn.commit()
    cursor.execute("SELECT * FROM Alumnos")
    rows=cursor.fetchall()
    print("Los datos ingresados a la BD son:")
    pp.pp(rows)
    

    cursor.close()
    conn.close()

def crearAlumno(id,nom,ape, cursor):
    query=f"insert into Alumnos(id, Nombre, Apellido) values({id},'{nom}','{ape}')"

    cursor.execute(query)
    
if __name__ == "__main__": main()

