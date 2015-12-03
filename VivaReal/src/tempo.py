# -*- coding: latin-1 -*-
import time

# localtime() Retorna a data e hora local no formato struct_time
print (time.localtime(), "struct")

# asctime() retorna a data e hora como string
print (time.asctime(),"string")

# time() retorna o tempo do sistema em segundos
ts1 = time.time()
print(ts1,"segundos")

# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print (ts1, '->', tt1)

# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)

# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print (ts2, '->', tt2)

# clock() retorma o tempo desde quando o programa
# iniciou, em segundos
print ('O programa levou', time.clock(), 'segundos ate agora...')
# Contando os segundos...
for i in range(5):
    # sleep() espera durante o nÃºmero de segundos
    # especificados como parÃ¢metro
    time.sleep(1)
    print (i + 1, 'segundo(s)',time.time())

print("--------------------------------------")

#import datetime
from datetime import datetime

# datetime() recebe como parâmetros:
# ano, mês, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime(2020, 12, 31, 23, 59, 59)

# Objetos date e time podem ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()

# Quanto tempo falta para 31/12/2020
dd = dt - dt.today()

print ('Data:', data)
print ('Hora:', hora)
print ('Quanto tempo falta para 31/12/2020:', str(dd).replace('days', 'dias'))
print(dt.day)
print(dt.hour)