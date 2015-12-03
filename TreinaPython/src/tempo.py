# -*- coding: latin-1 -*-
import time
#import datetime
from datetime import datetime

def dorme ():
    for i in range(1):
        # sleep() espera durante o nÃºmero de segundos
        # especificados como parÃ¢metro
        time.sleep(1)
        print (datetime.today())
        return 1

# localtime() Retorna a data e hora local no formato struct_time
print (time.localtime())
dorme()

# asctime() retorna a data e hora como string
print (time.asctime())
dorme()

# time() retorna o tempo do sistema em segundos
ts1 = time.time()
dorme()

# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print (ts1, 'gmtime ->', tt1)
dorme()


# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)

# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print (ts2, 'mktime ->', tt2)
dorme()


# clock() retorma o tempo desde quando o programa
# iniciou, em segundos
print ('O programa levou', time.clock(), 'segundos ate agora...')
# Contando os segundos...


# datetime() recebe como parâmetros:
# ano, mês, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime(2020, 12, 31, 23, 59)

# Objetos date e time podem ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()

# Quanto tempo falta para 31/12/2020
dd = dt - dt.today()


print ('Data:', data)
print ('Hora:', hora)
print ('Quanto tempo falta para 31/12/2020:', str(dd))
print(dt.today())
