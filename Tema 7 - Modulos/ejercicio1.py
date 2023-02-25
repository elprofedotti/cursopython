import  calculadoraBasica as calc

print("A continuacion ingrese dos numeros para operar")
a = int(input("primer numero: "))
b = int(input("segundo numero: "))

def opciones():
    print("-----------------------------")
    print("Numeros ingresados {} - {}".format(a,b))
    print("-----------------------------")
    print("Que operacion desea que haga?")
    print(">>>")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("9 - Salir")

opciones()
opcion=input("Ingrese opcion: ")
while(opcion!="9"):
    if opcion=="1":
        print( "{} + {} = {}".format(a, b, calc.suma(a, b) ) )
    elif opcion=="2":
        print( "{} - {} = {}".format(a, b, calc.resta(a, b) ) )
    elif opcion=="3":
        print( "{} x {} = {}".format(a, b, calc.multiplicar(a, b) ) )
    elif opcion=="4":
        print( "{} % {} = {}".format(a, b, calc.dividir(a, b) ) )

    opciones()
    opcion=input("Ingrese opcion: ")
