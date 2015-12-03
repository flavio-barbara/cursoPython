# -*- coding: latin-1 -*-
def gen_pares():
    """
    Gera numeros pares infinitamente...
    """
    i = 0
    yield i
    while True:
        i += 2
        if (i >= 10):
            break;
        yield i

# Mostra cada numero e passa para o proximo
def geradorpar():
    for n in gen_pares():
        #print (n)
        #Parar o gerador
        if (n >= 10):
            break;
try:
    x = list(gen_pares())
    print(x)
except:
    print ("Divisao por zero!")
