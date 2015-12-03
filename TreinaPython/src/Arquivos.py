# -*- coding: latin1 -*-

#Criando um objeto do tipo file
temp = open("/home/flavio/python3/curso/temp.txt", "w")

#Escrevendo no arquivo
for i in range(100):
    temp.write('%i Dolares valem %f reais\n' % (i, i * 1.70))

#fechando arquivo
temp.close();
print(temp.name)

#Abrindo o arquivo para leitura
temp = open(temp.name, "r")

for linha in temp:
    print(linha)

temp.close()