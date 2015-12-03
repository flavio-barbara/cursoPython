#-*- coding: latin1 -*-
def quadrado(elemento):
    return elemento**2

sequencia = [1,2,3,4,5,6]
resultado = list(map(quadrado, sequencia))

print(resultado)
print("----------------------")

def cambio(componente):
    print(componente[0] + ' R$ '+ str(componente[1]))
    print(componente[0]+ ' US$ '+ str(componente[1]*3.7))
    print('\n')

orcamento = {'asa': 1200, 'combustivel':200, 'motor': 4500}

list(map(cambio, orcamento.items()))
