# -*- coding: latin1  -*-
#fun��o decoradora
def exibeargs(func):
    #fun��o que envolver� a outra
    def funcenv(*args):
        #exibindo os arqumentos da fun��o
        print("Os argumentos da fun��o %s s�o: %s" % (func.__name__,args))

        #retorna os resultados da fun��o original
        return func(*args)

    #returna a fun��o modificada
    return funcenv

#Aplicando decorador
@exibeargs
def multiply(*nums):
    m = 1
    for n in nums:
        m = m * n

    return m

print(multiply(4,2,3))