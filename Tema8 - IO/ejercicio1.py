archivo = open('miArchivo.txt', 'w')
archivo.write((input("Escribe lo que quieras que conteng ael archivo recien creado: ")+"\n"))
archivo.close()

archivo = open('miArchivo.txt', 'a')
archivo.write((input("Escribe lo que quieras que conteng ael archivo recien creado: ")+"\n"))
archivo.close()

archivo=open('miArchivo.txt','r')
print(archivo.read())
archivo.close()
