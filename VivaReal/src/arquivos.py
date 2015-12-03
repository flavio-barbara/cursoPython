# -*- coding: latin1 -*-

#Criando um objeto do tipo file
temp = open("temp.txt", "w")

#Escrevendo no arquivo
for i in range(100):
    temp.write('%i Dolares valem %f Reais\n' % (i, i * 3.10))

#fechando arquivo
temp.close();

#Abrindo o arquivo para leitura
temp = open("temp.txt", "r")

for linha in temp:
    print(linha)

temp.close()