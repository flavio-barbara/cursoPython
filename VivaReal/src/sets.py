#-*- coding: latin1 -*-
# Conjuntos de 8, 9, 10dados
import listas
s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))
# Exibe os dados
print("s1 = ", s1)
print("s2 = ", s2)
print("s3 = ", s3)
#Uniao
s1s2 = s1.union(s2)

print("Uniao de s1 e s2", s1s2)

# Diferenca
print("Diferenca com s3", s1s2.difference(s3))

# Interseção
print("Interseccao com s3", s1s2.intersection(s3))

# Testa se um set inclui outro
if s1.issuperset([1,2]):
    print("s1 inclui 1 e 2")

#Testa se não existe elementos em comum
if s1.isdisjoint(s2):
    print("s1 e s2 nao tem elementos em comum")

#conversoes lista-set
lista = list(s1) + list(s2) + list(s3)
lista.sort()
print("listas:" + str(lista))
s = set(lista)
print(s)
    