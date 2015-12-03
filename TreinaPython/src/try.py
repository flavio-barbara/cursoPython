# -*- coding: latin1 -*-
import traceback

list = []
for i in range(3):
    while 1:
        try:
            list.append(int(input("Digite um valor: ")))
            break;
        except:
            trace = traceback.format_exc()

            print("Ocorreu o erro:", trace)

            #Cria um arquivo de log de erro
            open('trace.log', 'a').write(trace)
print(list)

# -*- coding: latin1 -*-

try:
    print(1/0)
except ZeroDivisionError:
    print("Erro ao tentar dividir por zero")

temp = open('trace.log', "r")

for linha in temp:
    print(linha)

temp.close()
