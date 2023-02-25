""" En el calendario juliano, los años bisiestos son aquellos cuyas dos últimas cifras son divisibles por 4 (2012/ 4= 503), exceptuando los múltiplos de 100 (1700, 1800, 1900...) donde a su vez también se exceptúan aquellos divisibles por 400 (1600, 2000, 2400...) que sí serán bisiestos. """
def esBisiesto(anio):
    if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)): 
        return True

resultado=esBisiesto(int(input ("Ingresa el año, y te digo si es bisiesto: ")))
if (resultado):
    print("Es bisiesto")
else : print("No es bisiesto")


