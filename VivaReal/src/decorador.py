# -*- coding: latin1  -*-
#função decoradora
def exibeargs(func):
    #função que envolverá a outra
    def funcenv(*args):
        #exibindo os arqumentos da função
        print("Os argumentos da função %s são: %s" % (func.__name__,args))

        #retorna os resultados da função original
        return func(*args)

    #returna a função modificada
    return funcenv

#Aplicando decorador
@exibeargs
def multiply(*nums):
    m = 1
    for n in nums:
        m = m * n

    return m

print(multiply(4,2,3))