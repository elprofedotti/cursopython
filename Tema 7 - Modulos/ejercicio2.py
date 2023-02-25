#modulo time
import time


if int(time.strftime('%H')) >= 16:
    print ("Hora de ir pa casita!!!")
        
else:
    print ("Quedan {} horas y {} minutos pa  ir a casita!!!".format(18- int(time.strftime('%H')), 59-int(time.strftime('%M'))))
	
