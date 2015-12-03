# -*- coding: latin1 -*-

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Eleve os Ã­mpares ao quadrado
print('quadrado pares nums')
print ([ x**2 for x in nums if x % 2 == 0])
print('quadrado impares range')
print ([ x**2 for x in range(1,12) if x % 2  ])
print ([ x**2 for x in nums if x % 2  ])

# usado como gerador
# Eleve os ímpares ao quadrado
gen = ( x**2 for x in nums if x % 2 )

# Mostra os resultados
for num in gen:
    print(num),