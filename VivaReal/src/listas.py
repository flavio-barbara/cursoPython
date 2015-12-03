#-*- coding: latin1 -*-
lista = [1,2,3]

print(lista[0])
print(lista[1])
print(lista[2])
#concatenando listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista = lista1 + lista2
print(lista)
#Adicionando um elemento a lista concatenando listas
lista1 = lista1 + [4]
print("lista1 "+str(lista1))

#Adicionando um elemento a lista com o método append()
lista2.append(5)
print("lista2 "+str(lista2))
#extendendo listas
listaAux = [6,7,8]
lista.extend(listaAux)
print(lista)

#operacoes com listas
lista = [1,2,3]
i = 2
#Incluindo um item
lista.append(4)
#Incluindo uma lista
lista.extend([5,6,7])
#Incluindo um item na posição i
print("antes: "+str(lista))
lista.insert(i, 8)
print("incluindo 8 na posicao i=2 "+str(lista))
#Remove o item
lista.remove(8)
print("removendo item 8: "+str(lista))
#Remove o item da posição i
print(lista.pop(i))
print(lista.pop())
#Retorna o index do item
print("Indice do item '2' => ", lista.index(2))
lista.extend([7,6,1])
#Retorna o número de vezes que o item aparece
print("Numero de vezes de 6 => ", lista.count(6))
#Ordena os itens da lista
print(lista)
lista.sort()
print(lista)
#Inverte a ordem dos itens da lista
lista.reverse()
print(lista)
#listanta a lista
lista = ["Bernard Cornwell", "George Martin", "Anna Rice", "Jeff Lendsay"]
#loop para imprimir
for item in lista:
    print(item)
#imprimir ordem alfabet
print("-----------")
lista.sort()
for item in lista:
    print(item)
#imprimir ordem inversa
print("-----------")
lista.reverse()
for item in lista:
    print(item)
