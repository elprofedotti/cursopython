import sqlite3 as sq

def main():
    id=input("Ingrese id a eliminar: ")
    
    eliminarUsuario(id)                  

def main3():
    id=input("id: ")
    user=input("usuario: ")
    psw=input("contraseña: ")
    crearUsuario(id,user,psw)

def main2():
    usuario=input("Ingrese usuario: ")
    pas=input("Ingrese pass: ")

    if verifCred(usuario,pas):
        print("Login correcto")
    else:
        print("Login INcorrecto")


def verifCred(usuario,pas):
    conn=sq.connect("miaplicacion.db")
    cursor=conn.cursor()
    
    query=f"select id from users where username='{usuario}' and password='{pas}'"

    rows=cursor.execute(query)
    data=rows.fetchone()

    cursor.close()
    conn.close()

    if data==None:
        return False

    return True

def crearUsuario(id,usuario,pas):
    conn=sq.connect("miaplicacion.db")
    cursor=conn.cursor()
    
    query=f"insert into users(id, username, password) values({id},'{usuario}','{pas}')"

    rows=cursor.execute(query)
    #print(type(rows))
    conn.commit()
    print("Los datos ingresados a la BD son:")
    print(rows)

    
    cursor.close()
    conn.close()


def eliminarUsuario(id):
    conn=sq.connect("miaplicacion.db")
    cursor=conn.cursor()
    
    query=f"delete from users where id={id}"

    rows=cursor.execute(query)
    #print(type(rows))
    conn.commit()
    print("usuario eliminado")
    
    
    cursor.close()
    conn.close()

if __name__ == "__main__": main()