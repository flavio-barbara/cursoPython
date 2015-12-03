#-*- coding: latin1 -*-
#inteiro
var1 = 1

#ponto flutuante
var2 = 3.14

#Complexo
var3 = 4 / 3j

print ("Inteiro = ", var1)
print ("Ponto flutuante = ", var2)
print ("Complexo = ", var3)

#Convertendo real para inteiro
print ("int(var2) = ", int(var2))

#Convertendo inteiro para real
print ("float(var1) = ", float(var1))

#Operacoes com numeros complexos
print ("Parte real = ", var3.real)
print ("Parte imaginaria = ", var3.imag)
print ("Conjugado = ", var3.conjugate())