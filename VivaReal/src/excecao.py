# -*- coding: latin1 -*-
try:
    print(1/0)
except ZeroDivisionError:
    print("Erro ao tentar dividir por zero")
    

lista = []
for i in range(3):
    while 1:
        try:
            lista.append(int(input("Digite um valor: ")))
            break;
        except:
            print("Digite apenas números")
print(lista)

import traceback
lista = []
for i in range(3):
    while 1:
        try:
            lista.append(int(input("Digite um valor: ")))
            break;
        except:
            trace = traceback.format_exc()
            print("Ocorreu o erro:", trace)
            #Cria um arquivo de log de erro
            logerr = open('trace.log', 'a')
            logerr.write(trace)
print(lista)
logerr.close()