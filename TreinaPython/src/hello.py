# -*- coding: latin1 -*-
# def lista(ini, fim):
#     seq = []
#     for i in range(ini,fim+1):
#         seq = seq + [i]
#     return seq
#  
# def quadrado(elem):
#     return elem**2
#  
# ini = int(input("informe inicio: "))
# fim = int(input("informe fim: "))
# seq = lista(ini,fim)
# print(seq)
# quadr = list(map(quadrado,seq))
# print(quadr)
# vl = 0
# while vl < 99:
#  vl = input("entre com o valor: ")
#  vl = int(vl)3

#  if vl < 0 : print("congelando")
#  elif vl < 10 : print("frio")
#  elif vl < 20 : print("fresco")
#  else : print("quente")
# else : print("fim")
# for x in range(0,21,2):
#     print(x)
# dicionario = {1:'um', 2:'dois',3:'tres'}
# print(dicionario)
# dicionario[4]='quatro'
# dicionario['5']=55555
# dicionario[5]='5'
# print(dicionario)
# print(dicionario[1])
# dicionario[1]='cinco5'
# print(dicionario[1])
# print(dicionario[2])
# print(dicionario[3])
# print(dicionario[4])
# print(dicionario[5])
# print(dicionario['5'])
# print(dicionario.items())
# print(dicionario.keys())
# print(dicionario.values())
# del(dicionario['5'])
# print()
# print(dicionario.items())
# print(dicionario.keys())
# print(dicionario.values())
# for x in dicionario : 
#     print("chave: ", x) 
#     print("valor: ", dicionario[x])

# r1 = (range(25,50, 3))
# s1 = set(r1)
# s1b = set(range(25,50, 3))
# s2 = set(range(900,100,-200))
# s3 = set(range(100,1000,100))
# print('s1 = ',s1)
# print('s1b = ',s1b)
# print('s2 = ',s2)
# print('s3 = ',s3)
# print('----------------')
# print('uniao = ', s1.union(s1b))
# print('uniao = ', s1.intersection(s1b))
# print('uniao s2 = ', s2.union(s3))
# print('uniao s2 = ', s2.intersection(s3))
# print('isdisjoint = ', s2.isdisjoint(s1))

# valor4 = "string4"
# tupi = 23, 1200, "abc", valor4
# tup2 = 'xpto','flavio',123
# print(tupi)
# print(tup2)
# print('----------------')
# tupi, tup2 = tup2, tupi
# print(tupi)
# print(tup2)

# lista1 = [1,2,3]
# listab = ['a','b','c']
# #print(lista1)
# result = (listab + lista1) + [1000]
# result.append("fla")
# result.extend([9,-8,7,-6,1,1,1,1])
# result.insert(2,"inserido!")
# print(result)
# for item in result :
#     print(item)
# result.pop(4)
# print(result)
# result.sort()
# print(result)
# result.reverse()
# print(result)
# print(result.index(-8))
# lin = 0
# for i in result:
#     print(lin, i)
#     lin = lin+1


# palavra = "Flavio Barbara"
# palavra2 = """
# linha 1 = Flavio
# linha 2 = Barbara
# """
# print(palavra+"---conc"+" 1 ")
# print(palavra2)
# print(palavra[14::-1])
# print(palavra2[36::-1])
# print("tamanho: "+str(len(palavra)))
# print("tamanho: "+str(len(palavra2)))
# print("test concat: %s com %s" % (palavra, palavra2))

# i=40
# j=25
# print("i & j", bin(i & j))
# print("j | i", bin(j | i))
# print("j ^ i", bin(j ^ i))
# print("~ i", bin(~i))
# print("~ j", bin(~j))
# print("bin de 40 = ", bin(i))
# print("bin de 25 = ", bin(j))
# #deslocamentos bit a bit
# print("40 esq 1: ", bin(i << 1))
# print("40 esq 2: ", bin(i << 2))
# print("40 esq 3: ", bin(i << 3))
# print("40 esq 5: ", bin(i << 5))
# print("40 dir 1: ", bin(i >> 1))
# print("40 dir 2: ", bin(i >> 2))
# print("40 dir 3: ", bin(i >> 3))
# print("40 dir 5: ", bin(i >> 5))


# """
# mensagem a ser impressa no console
# """
# msg = "Flavio estÃ¡Ã©Ã­Ã³ÃºÃ½ aprendendo Python!  áéíóúý "
# print(msg)
# '''
# tipo da varivel
# '''
# tipo = type(msg)
# print(tipo)
# # mudando tipo dinamicamente
# msg = 123
# tipo = type(msg)
# print(tipo)
# '''
# variaveis numericas
# '''
# vInt = 23
# vFloat = 123.45
# vCplex = 3 + 4j
# #imprimindo variaveis
# print("inteiro: ", vInt)
# print("float: ", vFloat)
# print("Complex: ", vCplex)
# #convertendo tipos
# print("real pra inteiro: ", int(vFloat))
# print("inteiro pra real: ", float(vInt))
# #numeros complexos
# print("parte real: ", vCplex.real)
# print("parte imaginaria: ",vCplex.imag)
# print("conjugado: ",vCplex.conjugate())

#-*- coding: latin1 -*-
str = "Treinaweb"

#Interpolação
print("O  %s tamanho  %s de %s é %d" % (str, str, str, len(str)))
