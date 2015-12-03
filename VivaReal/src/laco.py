#-*- coding: latin1 -*-
#Soma de 0 a 99
s = 0
x = 1

while x < 100:
    s = s + x
    x = x + 1

print("A soma e' = " + str(s) + " no loop")

#Soma de 0 a 10
s = 0
for x in range(111,10,-1):
    s = s + x

print("A soma é %d" %s)

#imprimindo lista
lista = {"George R.R. Martin", "A Guerra dos Tronos", "Volume 1", "Saga de fogo e gelo"}
print("Itens da lista:")
for item in lista:
    print(item)
    
# print dicionario
print("____________")
orcamento = {"asa": 1200, "combustivel": 200, "motor": 4500}

for chave in orcamento:
    print("Chave: ", chave, " Valor: "+str(orcamento[chave]))
    
print("____________")
orcamento = {"asa": 1200, "combustível": 200, "motor": 4500}

for chave in orcamento:
    print("O valor da chave %s  é %d" % (chave, orcamento[chave]))